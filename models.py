from datetime import datetime
from typing import List

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class RepresentativeModel:
    def __repr__(self):
        return f'{self.__class__.__name__}(id={getattr(self, "id", None)})'


class User(RepresentativeModel, Base):
    __tablename__ = 'users'

    id: int = Column('id', Integer, primary_key=True)
    name: str = Column('name', String(16), unique=True)
    orders: List['Order'] = relationship('Order')


class Order(RepresentativeModel, Base):
    __tablename__ = 'orders'

    id: int = Column('id', Integer, primary_key=True)
    user_id: int = Column('user_id', ForeignKey('users.id'))
    user: 'User' = relationship('User', back_populates='orders')
    items: List['Item'] = relationship('OrderedItem', back_populates='order')
    created_at: datetime = Column('created_at', DateTime, default=datetime.utcnow())


class Category(RepresentativeModel, Base):
    __tablename__ = 'categories'

    id: int = Column('id', Integer, primary_key=True)
    name: str = Column('name', String(32), unique=True)
    parameters: List['CategoryParameter'] = relationship('CategoryParameter', back_populates='category')
    items: List['Item'] = relationship('Item', back_populates='category')


class CategoryParameter(RepresentativeModel, Base):
    __tablename__ = 'category_parameters'

    id: int = Column('id', Integer, primary_key=True)
    category_id: int = Column('category_id', ForeignKey('categories.id'))
    category: 'Category' = relationship('Category', back_populates='parameters')
    name: str = Column('name', String(32))


class ItemParameter(RepresentativeModel, Base):
    __tablename__ = 'item_parameters'

    id: int = Column('id', Integer, primary_key=True)
    parameter_id: int = Column('parameter_id', ForeignKey('category_parameters.id'))
    parameter: 'CategoryParameter' = relationship('CategoryParameter')
    item_id: int = Column('item_id', ForeignKey('items.id'))
    item: 'Item' = relationship('Item', back_populates='parameters')
    value: str = Column('value', String(32))


class Item(RepresentativeModel, Base):
    __tablename__ = 'items'

    id: int = Column('id', Integer, primary_key=True)
    name: str = Column('name', String(32))
    category_id: int = Column('category_id', ForeignKey('categories.id'))
    category: 'Category' = relationship('Category')
    parameters: List['ItemParameter'] = relationship('ItemParameter')
    price: float = Column('price', Float(2))


class OrderedItem(RepresentativeModel, Base):
    __tablename__ = 'ordered_items'

    order_id: int = Column('order_id', ForeignKey('orders.id'), primary_key=True)
    item_id: int = Column('item_id', ForeignKey('items.id'), primary_key=True)
    price: float = Column('price', Float(2))
    quantity: int = Column('quantity', Integer, default=1)
    order: 'Order' = relationship('Order', back_populates='items')
    item: 'Item' = relationship('Item')

    def __repr__(self):
        return f'OrderedItem(order_id={self.order_id}, item_id={self.item_id})'
