from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import aliased, joinedload

from models import *
from session import Session


def get_most_recent_orders(session: Session) -> List[Order]:
    order_right = aliased(Order)

    query = (
        session.query(Order)
        .outerjoin(
            order_right,
            (
                (Order.user_id == order_right.user_id)
                & (Order.created_at < order_right.created_at)
            ),
        )
        .filter(order_right.created_at.is_(None))
        .order_by(desc(Order.created_at))
    )

    return query.subquery()


def get_last_order(session: Session, user_id: int) -> Order:
    most_recent_orders = get_most_recent_orders(session)

    query = (
        session.query(Order)
        .join(most_recent_orders, Order.id == most_recent_orders.c.id)
        .join(User)
        .options(joinedload(Order.items).joinedload(OrderedItem.item))
        .filter(User.id == user_id)
    )

    return query.first()


def main():
    session = Session()

    last_order = get_last_order(session, 3)

    print(
        f'Last order (ID: {last_order.id} | '
        f'User ID: {last_order.user.id} | '
        f'Created at: {last_order.created_at.isoformat()}) '
        f'contents:'
    )
    print(
        '\n'.join(
            [
                f'Item ID: {ordered_item.item.id} | '
                f'Item name: {ordered_item.item.name} | '
                f'Ordered price: {ordered_item.price} | '
                f'Ordered quantity: {ordered_item.quantity} | '
                f'Overall price: {round(ordered_item.price * ordered_item.quantity, 2)}'
                for ordered_item in last_order.items
            ]
        )
    )


if __name__ == '__main__':
    main()
