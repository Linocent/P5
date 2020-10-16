"""This files creates the table Substitute, Categorie, Products and Store."""

from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import SmallInteger, VARCHAR, CHAR
from sqlalchemy.dialects.mysql import TINYINT, TINYTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://Timothee:RedBull/75019@localhost/openfoodfact')


class Substitue(Base):
    __tablename__ = 'substitue'
    products_ID = Column('products_to_substitute', ForeignKey('products.id'))
    substitue_ID = Column('products_substitute', ForeignKey('products.id'))
    id = Column('id', TINYINT, primary_key=True, autoincrement=True)
    mysql_engine = 'InnoDB'

    def __repr__(self):
        return f"Substitue: {self.products_ID, self.substitue_ID}"


class Categorie(Base):
    __tablename__ = 'categorie'
    id = Column(TINYINT, primary_key=True)
    name = Column('categorie_Name', VARCHAR(50))
    mysql_engine = 'InnoDB'
    mysql_charset = 'utf8'
    products = relationship(
        'Products', back_populates='categorie')

    def __repr__(self):
        return f"Categorie: {self.id, self.name}"


class Products(Base):
    __tablename__ = "products"
    id = Column(SmallInteger, autoincrement=True, primary_key=True)
    name = Column("product_name", VARCHAR(255))
    name_nut = Column("nutriscore", CHAR(10))
    name_url = Column("url_product", TINYTEXT)
    store_name = Column("store_name", VARCHAR(255))
    mysql_engine = 'InnoDB'
    mysql_charset = 'utf8'
    categorie_id = Column(TINYINT, ForeignKey("categorie.id"))
    categorie = relationship("Categorie", back_populates="products")
    store_id = Column(SmallInteger, ForeignKey("store.id"))
    store = relationship("Store", back_populates="products")

    def __repr__(self):
        return f"Products: {self.id,self.name, self.name_nut, self.name_url, self.store_name}"


class Store(Base):
    __tablename__ = 'store'
    id = Column(SmallInteger, autoincrement=True, primary_key=True)
    name_store = Column('name_stores', VARCHAR(255))
    mysql_engine = 'InnoDB'
    mysql_charset = 'utf8'
    products = relationship(
        "Products", back_populates="store")

    def __repr__(self):
        return f"Store: {self.id, self.name_store}"


Base.metadata.create_all(engine)
