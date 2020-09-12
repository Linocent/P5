import requests as rq
from BDD import Categorie, Store, Products
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SelectProduct:

    def __init__(self):

        self.product_list = []
        self.prod_name = []
        self.prod_url = []
        self.prod_nutri = []
        self.prod_stores = []

    def extract(self, dict_cat_key, dict_cat_value):

        product = rq.get('https://fr.openfoodfacts.org/categorie/'+dict_cat_value+'/1.json')
        prod_key = dict_cat_key
        if product.status_code == rq.codes.ok:
            dict = product.json()
            # print("this is dict: ", dict)
            for prod in dict.get('products'):
                self.prod_name = prod.get('product_name_fr')
                self.prod_url = prod.get('url')
                self.prod_nutri = prod.get('nutrition_grades')
                print(type(self.prod_nutri))
                self.prod_stores = prod.get('stores', 'None')
                print("This is store: ", type(self.prod_stores))
                # store = self.prod_stores.split(',')
                # print(self.prod_stores.type)
                self.product_list.append([self.prod_name, self.prod_nutri, self.prod_url, self.prod_stores, prod_key])
                select_product.split_store(self.prod_stores)
                print(self.product_list)
                self.product_list.remove([self.prod_name, self.prod_nutri, self.prod_url, self.prod_stores, prod_key])

    def split_store(self, list_store):
        store = list_store[3][0].split(',')
        print(store)
        return store
        """for k in range(len(mylist)):
            print(get_list_magasins(mylist[k]))"""


class FillDB:

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://Timothee:RedBull/75019@localhost/openfoodfact')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.conn = self.engine.connect()

    def fill_cat(self, dictcat):

        if self.session.query(Categorie.id).count() == 0:
            for key, value in dictcat.items():
                new_cat = Categorie(id=key,
                                    name=value)
                self.session.add(new_cat)
                self.session.commit()

    def fill_product(self, dictcat, select_product):

        if self.session.query(Products.id).count() == 0:
            for key in dictcat.keys():
                select_product.extract(key, dictcat[key])
                for prod in select_product.product_list:
                    newproduct = Products(name=prod[0],
                                          name_nut=prod[1],
                                          name_url=prod[2],
                                          categorie_id=prod[4])
                    """newstore = Store(name_store=prod[3],
                                     product_key=)"""
                    self.session.add(newproduct)
                    self.session.commit()
                    select_product.product_list.remove(prod)


select_product = SelectProduct()
filldb = FillDB()

