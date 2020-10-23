from model import Categorie, Store, Products, Substitue
from api import select_product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataBase:
    """Manage the DataBase (fill and empty it)."""

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://Timothee:RedBull/'
                                    '75019@localhost/openfoodfact')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.conn = self.engine.connect()

    def fill_cat(self, dictcat):
        """Fill the table categorie."""

        if self.session.query(Categorie.id).count() == 0:
            for key, value in dictcat.items():
                print(f"Downloading categorie: {value}")
                new_cat = Categorie(id=key,
                                    name=value)
                self.session.add(new_cat)
                self.session.commit()
        else:
            pass

    def fill_product(self, dictcat):
        """Fill the table products and store."""

        if self.session.query(Products.id).count() == 0:
            for key in dictcat.keys():
                select_product.extract(key, dictcat[key])
                for prod in select_product.product_list:
                    print(f"Downloading products: {prod}")
                    if prod[0] and prod[1] != 'NULL' or '':
                        newstore = Store(name_store=prod[3])
                        self.session.add(newstore)
                        self.session.commit()

                        store = self.session.query(Store.id).count()
                        newproduct = Products(name=prod[0],
                                              name_nut=prod[1],
                                              name_url=prod[2],
                                              store_name=prod[3],
                                              categorie_id=prod[4],
                                              store_id=store)
                        self.session.add(newproduct)
                        self.session.commit()
                        select_product.product_list.remove(prod)
                    else:
                        pass
        else:
            pass

    def fill_sub(self, id_s, id_p):
        """Fill the table substitute."""

        newsub = Substitue(products_ID=id_p,
                           substitue_ID=id_s)
        self.session.add(newsub)
        self.session.commit()

    def empty_db(self):
        """Empty the DataBase."""
        self.session.query(Substitue).delete()
        self.session.query(Products).delete()
        self.session.query(Store).delete()
        self.session.query(Categorie).delete()
        self.session.commit()