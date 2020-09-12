import requests as rq
from Show import Menu

Menu.show()



def test():
    r = rq.get('https://fr.openfoodfacts.org/categories.json')
    if r.status_code == rq.codes.ok:
        print(r.json())
    # categorie = rq.loads(r.text)
    # print(categorie.keys())


def oeuf():
    oeuf = rq.get('https://fr.openfoodfacts.org/categorie/oeufs.json')
    if oeuf.status_code == rq.codes.ok:
        # print(r.json())
        dict = oeuf.json()
        for prod in dict.get('products'):
            prod_name = prod.get('product_name_fr')
            prod_url = prod.get('url')
            prod_nutri = prod.get('nutrition_grades')
            prod_stores = prod.get('stores')
            # print(prod_name)
            # print(prod_nutri)
            # print(prod_url)
            # print(prod_stores)
            prod_list = {}
            oeuf_list = [prod_name, prod_nutri, prod_url, prod_stores]
            print(oeuf_list)


def citronade():
    citron = rq.get('https://fr.openfoodfacts.org/categorie/citronnades.json')
    if citron.status_code == rq.codes.ok:
        # print(r.json())
        dict = citron.json()
        for prod in dict.get('products'):
            prod_name = prod.get('product_name_fr')
            prod_url = prod.get('url')
            prod_nutri = prod.get('nutrition_grades')
            prod_stores = prod.get('stores')
            # print(prod_name)
            # print(prod_nutri)
            # print(prod_url)
            # print(prod_stores)
            prod_list = {}
            citron_list = [prod_name, prod_nutri, prod_url, prod_stores]
            print(citron_list)


def oeuf2():  # Inutilisé
    cat_list = ['https://fr.openfoodfacts.org/categorie/oeufs.json',
                'https://fr.openfoodfacts.org/categorie/citronnades.json',
                'https://fr.openfoodfacts.org/categorie/boissons-gazeuses.json',
                'https://fr.openfoodfacts.org/categorie/purees-de-pommes-de-terre.json',
                'https://fr.openfoodfacts.org/categorie/chips-de-pommes-de-terre.json',
                'https://fr.openfoodfacts.org/categorie/fromages-de-france.json',
                'https://fr.openfoodfacts.org/categorie/yaourts-aux-fruits.json',
                'https://fr.openfoodfacts.org/categorie/pates-a-tartiner.json',
                'https://fr.openfoodfacts.org/categorie/biscuits-sables.json',
                'https://fr.openfoodfacts.org/categorie/pizzas.json',
                'https://fr.openfoodfacts.org/categorie/hamburgers.json'
                ]
    for k in range(len(cat_list) - 1):
        r = rq.get(cat_list[k])
        dict = r.json()
        for prod in dict.get('products'):
            prod_name = prod.get('product_name_fr')
            prod_url = prod.get('url')
            prod_nutri = prod.get('nutrition_grades')
            prod_stores = prod.get('stores')
            # print(prod_name)
            # print(prod_nutri)
            # print(prod_url)
            # print(prod_stores)
            prod_list = {}
            prod_list = [prod_name, prod_nutri, prod_url, prod_stores]
            print(prod_list)
