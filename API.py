"""This file extract data from OpenFoodFact, fill the
DataBase and empty the Database. """
import requests as rq
from BDD import Categorie, Store, Products, Substitue
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SelectProduct:
    """Extract data from OpenFoodFact."""

    def __init__(self):

        self.product_list = []
        self.prod_name = []
        self.prod_url = []
        self.prod_nutri = []
        self.prod_stores = []

    def extract(self, dict_cat_key, dict_cat_value):
        """Extract data from OpenFoodFact."""
        product = rq.get('https://fr.openfoodfacts.org/categorie/'
                         +dict_cat_value+'/1.json')
        prod_key = dict_cat_key
        if product.status_code == rq.codes.ok:
            dict = product.json()
            for prod in dict.get('products'):
                self.prod_name = prod.get('product_name_fr')
                self.prod_url = prod.get('url')
                self.prod_nutri = prod.get('nutrition_grades')
                self.prod_stores = prod.get('stores', 'nothing')
                self.product_list.append([self.prod_name, self.prod_nutri,
                                          self.prod_url, self.prod_stores,
                                          prod_key])
                print(self.product_list)
        else:
            print("Can't connect.")

    def split_store(self, list_store):
        """Split a list of some store. Unused here,
        but I want to use it later."""
        store = list_store
        if "," in list_store:
            store = list_store.split(",")
        else:
            pass
        return store


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


select_product = SelectProduct()
