from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class RepresentativeModel:
    def __repr__(self):
        return f'{self.__class__.__name__}(id={getattr(self, "id", None)})'


class User(RepresentativeModel, Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(16), unique=True)
    orders = relationship('Order')


class Order(RepresentativeModel, Base):
    __tablename__ = 'orders'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')
    items = relationship('OrderedItem', back_populates='order')
    created_at = Column('created_at', DateTime, default=datetime.utcnow())


class Category(RepresentativeModel, Base):
    __tablename__ = 'categories'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(32), unique=True)
    parameters = relationship('CategoryParameter', back_populates='category')
    items = relationship('Item', back_populates='category')


class CategoryParameter(RepresentativeModel, Base):
    __tablename__ = 'category_parameters'

    id = Column('id', Integer, primary_key=True)
    category_id = Column('category_id', ForeignKey('categories.id'))
    category = relationship('Category', back_populates='parameters')
    name = Column('name', String(32))


class ItemParameter(RepresentativeModel, Base):
    __tablename__ = 'item_parameters'

    id = Column('id', Integer, primary_key=True)
    parameter_id = Column('parameter_id', ForeignKey('category_parameters.id'))
    parameter = relationship('CategoryParameter')
    item_id = Column('item_id', ForeignKey('items.id'))
    item = relationship('Item', back_populates='parameters')
    value = Column('value', String(32))


class Item(RepresentativeModel, Base):
    __tablename__ = 'items'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(32))
    category_id = Column('category_id', ForeignKey('categories.id'))
    category = relationship('Category')
    parameters = relationship('ItemParameter')
    price = Column('price', Float(2))


class OrderedItem(RepresentativeModel, Base):
    __tablename__ = 'ordered_items'

    order_id = Column('order_id', ForeignKey('orders.id'), primary_key=True)
    item_id = Column('item_id', ForeignKey('items.id'), primary_key=True)
    price = Column('price', Float(2))
    quantity = Column('quantity', Integer, default=1)
    order = relationship('Order', back_populates='items')
    item = relationship('Item')

    def __repr__(self):
        return f'OrderedItem(order_id={self.order_id}, item_id={self.item_id})'
