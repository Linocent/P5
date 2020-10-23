"""This file extract data from OpenFoodFact, fill the
DataBase and empty the Database. """
import requests as rq


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
                         + dict_cat_value+'/1.json')
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


select_product = SelectProduct()
