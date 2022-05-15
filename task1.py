from sqlalchemy import Numeric, desc, func
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
        .options(joinedload(Order.user))
        .filter(order_right.created_at.is_(None))
        .order_by(desc(Order.created_at))
    )

    return query.all()


def get_most_expensive_orders(session: Session) -> List[Order]:
    order_sums = (
        session.query(
            Order,
            func.round(func.cast(func.sum(OrderedItem.price * OrderedItem.quantity), Numeric), 2).label('order_sum'),
        )
        .join(OrderedItem)
        .group_by(Order.id)
    ).cte('order_sums')

    order_sums_right = aliased(order_sums)

    query = (
        session.query(User, order_sums.c.id, order_sums.c.created_at)
        .outerjoin(
            order_sums_right,
            (
                (order_sums.c.user_id == order_sums_right.c.user_id)
                & (order_sums.c.order_sum < order_sums_right.c.order_sum)
            ),
        )
        .join(User, User.id == order_sums.c.user_id)
        .filter(order_sums_right.c.order_sum.is_(None))
        .order_by(desc(order_sums.c.order_sum))
    )

    return [
        Order(
            id=item.id,
            user=item.User,
            user_id=item.User.id,
            created_at=item.created_at,
        )
        for item in query
    ]


def pretty_print_orders(header: str, orders: List[Order]) -> None:
    print(header)
    print(
        '\n'.join(
            [
                f'ID: {order.id} | User ID: {order.user_id} | Created at: {order.created_at.isoformat()}'
                for order in orders
            ]
        )
    )


def main():
    session = Session()

    most_recent_orders = get_most_recent_orders(session)
    most_expensive_orders = get_most_expensive_orders(session)

    pretty_print_orders('Most recent orders:', most_recent_orders)
    print()
    pretty_print_orders('Most expensive orders:', most_expensive_orders)


if __name__ == '__main__':
    main()
