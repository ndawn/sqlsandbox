#!/usr/bin/env python3

from datetime import datetime

from models import *
from session import engine, session


def main():
    Base.metadata.create_all(engine)

    session.query(ItemParameter).delete()
    session.query(CategoryParameter).delete()
    session.query(OrderedItem).delete()
    session.query(Order).delete()
    session.query(Item).delete()
    session.query(Category).delete()
    session.query(User).delete()
    session.commit()

    users = [
        User(name='Maksim'),
        User(name='Andrey'),
    ]
    session.add_all(users)

    categories = [
        Category(name='test_category_a'),
        Category(name='test_category_b'),
        Category(name='test_category_c'),
        Category(name='test_category_d'),
        Category(name='test_category_e'),
        Category(name='test_category_f'),
        Category(name='test_category_g'),
        Category(name='test_category_h'),
    ]
    session.add_all(categories)

    category_parameters = [
        CategoryParameter(name='test_category_parameter_a', category=categories[0]),
        CategoryParameter(name='test_category_parameter_b', category=categories[0]),
        CategoryParameter(name='test_category_parameter_c', category=categories[1]),
        CategoryParameter(name='test_category_parameter_d', category=categories[1]),
        CategoryParameter(name='test_category_parameter_e', category=categories[2]),
        CategoryParameter(name='test_category_parameter_f', category=categories[2]),
        CategoryParameter(name='test_category_parameter_g', category=categories[3]),
        CategoryParameter(name='test_category_parameter_h', category=categories[3]),
        CategoryParameter(name='test_category_parameter_i', category=categories[4]),
        CategoryParameter(name='test_category_parameter_j', category=categories[4]),
        CategoryParameter(name='test_category_parameter_k', category=categories[5]),
        CategoryParameter(name='test_category_parameter_l', category=categories[5]),
        CategoryParameter(name='test_category_parameter_m', category=categories[6]),
        CategoryParameter(name='test_category_parameter_n', category=categories[6]),
        CategoryParameter(name='test_category_parameter_o', category=categories[7]),
        CategoryParameter(name='test_category_parameter_p', category=categories[7]),
    ]
    session.add_all(category_parameters)

    items = [
        Item(name='test_item_a', category=categories[0], price=6.0),
        Item(name='test_item_b', category=categories[0], price=3.7),
        Item(name='test_item_c', category=categories[1], price=7.8),
        Item(name='test_item_d', category=categories[1], price=7.1),
        Item(name='test_item_e', category=categories[2], price=2.8),
        Item(name='test_item_f', category=categories[2], price=1.4),
        Item(name='test_item_g', category=categories[3], price=5.0),
        Item(name='test_item_h', category=categories[3], price=5.1),
        Item(name='test_item_i', category=categories[4], price=4.5),
        Item(name='test_item_j', category=categories[4], price=6.3),
        Item(name='test_item_k', category=categories[5], price=6.6),
        Item(name='test_item_l', category=categories[5], price=6.3),
        Item(name='test_item_m', category=categories[6], price=8.9),
        Item(name='test_item_n', category=categories[6], price=1.9),
        Item(name='test_item_o', category=categories[7], price=2.8),
        Item(name='test_item_p', category=categories[7], price=3.3),
    ]
    session.add_all(items)

    item_parameters = [
        ItemParameter(value='test_item_parameter_a', parameter=category_parameters[0], item=items[0]),
        ItemParameter(value='test_item_parameter_b', parameter=category_parameters[0], item=items[1]),
        ItemParameter(value='test_item_parameter_c', parameter=category_parameters[1], item=items[2]),
        ItemParameter(value='test_item_parameter_d', parameter=category_parameters[1], item=items[3]),
        ItemParameter(value='test_item_parameter_e', parameter=category_parameters[2], item=items[4]),
        ItemParameter(value='test_item_parameter_f', parameter=category_parameters[2], item=items[5]),
        ItemParameter(value='test_item_parameter_g', parameter=category_parameters[3], item=items[6]),
        ItemParameter(value='test_item_parameter_h', parameter=category_parameters[3], item=items[7]),
        ItemParameter(value='test_item_parameter_i', parameter=category_parameters[4], item=items[8]),
        ItemParameter(value='test_item_parameter_j', parameter=category_parameters[4], item=items[9]),
        ItemParameter(value='test_item_parameter_k', parameter=category_parameters[5], item=items[10]),
        ItemParameter(value='test_item_parameter_l', parameter=category_parameters[5], item=items[11]),
        ItemParameter(value='test_item_parameter_m', parameter=category_parameters[6], item=items[12]),
        ItemParameter(value='test_item_parameter_n', parameter=category_parameters[6], item=items[13]),
        ItemParameter(value='test_item_parameter_o', parameter=category_parameters[7], item=items[14]),
        ItemParameter(value='test_item_parameter_p', parameter=category_parameters[7], item=items[15]),
        ItemParameter(value='test_item_parameter_q', parameter=category_parameters[8], item=items[0]),
        ItemParameter(value='test_item_parameter_r', parameter=category_parameters[8], item=items[1]),
        ItemParameter(value='test_item_parameter_s', parameter=category_parameters[9], item=items[2]),
        ItemParameter(value='test_item_parameter_t', parameter=category_parameters[9], item=items[3]),
        ItemParameter(value='test_item_parameter_u', parameter=category_parameters[10], item=items[4]),
        ItemParameter(value='test_item_parameter_v', parameter=category_parameters[10], item=items[5]),
        ItemParameter(value='test_item_parameter_w', parameter=category_parameters[11], item=items[6]),
        ItemParameter(value='test_item_parameter_x', parameter=category_parameters[11], item=items[7]),
        ItemParameter(value='test_item_parameter_y', parameter=category_parameters[12], item=items[8]),
        ItemParameter(value='test_item_parameter_z', parameter=category_parameters[12], item=items[9]),
        ItemParameter(value='test_item_parameter_0', parameter=category_parameters[13], item=items[10]),
        ItemParameter(value='test_item_parameter_1', parameter=category_parameters[13], item=items[11]),
        ItemParameter(value='test_item_parameter_2', parameter=category_parameters[14], item=items[12]),
        ItemParameter(value='test_item_parameter_3', parameter=category_parameters[14], item=items[13]),
        ItemParameter(value='test_item_parameter_4', parameter=category_parameters[15], item=items[14]),
        ItemParameter(value='test_item_parameter_5', parameter=category_parameters[15], item=items[15]),
    ]
    session.add_all(item_parameters)

    orders = [
        Order(user=users[0], created_at=datetime(2022, 4, 19)),
        Order(user=users[0], created_at=datetime(2022, 4, 20)),
        Order(user=users[1], created_at=datetime(2022, 4, 17)),
        Order(user=users[1], created_at=datetime(2022, 4, 18)),
    ]
    session.add_all(orders)

    ordered_items = [
        OrderedItem(order=orders[0], item=items[0], price=items[0].price, quantity=1),
        OrderedItem(order=orders[0], item=items[1], price=items[1].price, quantity=3),
        OrderedItem(order=orders[0], item=items[2], price=items[2].price, quantity=2),
        OrderedItem(order=orders[0], item=items[3], price=items[3].price, quantity=1),
        OrderedItem(order=orders[1], item=items[4], price=items[4].price, quantity=2),
        OrderedItem(order=orders[1], item=items[5], price=items[5].price, quantity=1),
        OrderedItem(order=orders[1], item=items[6], price=items[6].price, quantity=1),
        OrderedItem(order=orders[1], item=items[7], price=items[7].price, quantity=10),
        OrderedItem(order=orders[2], item=items[8], price=items[8].price, quantity=2),
        OrderedItem(order=orders[2], item=items[9], price=items[9].price, quantity=2),
        OrderedItem(order=orders[2], item=items[10], price=items[10].price, quantity=3),
        OrderedItem(order=orders[2], item=items[11], price=items[11].price, quantity=1),
        OrderedItem(order=orders[3], item=items[12], price=items[12].price, quantity=1),
        OrderedItem(order=orders[3], item=items[13], price=items[13].price, quantity=4),
        OrderedItem(order=orders[3], item=items[14], price=items[14].price, quantity=1),
        OrderedItem(order=orders[3], item=items[15], price=items[15].price, quantity=2),
    ]
    session.add_all(ordered_items)

    session.commit()


if __name__ == '__main__':
    main()
