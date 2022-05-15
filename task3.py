from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import aliased, joinedload

from models import *
from session import Session


def get_category_with_item_parameters(session: Session, category_id: int) -> Category:
    query = (
        session.query(Category)
        .options(joinedload(Category.items).joinedload(Item.parameters).joinedload(ItemParameter.parameter))
        .filter(Category.id == category_id)
    )

    return query.first()


def main():
    session = Session()

    category = get_category_with_item_parameters(session, 9)

    print(
        f'Category (ID: {category.id} | '
        f'Name: {category.name} | '
        f'contents:'
    )
    print(
        '\n\n'.join(
            [
                f'Item ID: {item.id} | '
                f'Item name: {item.name} | '
                f'Item price: {item.price}\n'
                'Parameters:\n'
                + '\n'.join(
                    [
                        f'    Name: {parameter.parameter.name} | '
                        f'Value: {parameter.value}'
                        for parameter in item.parameters
                    ]
                )
                for item in category.items
            ]
        )
    )


if __name__ == '__main__':
    main()
