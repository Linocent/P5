import requests as rq



def test():
    r = rq.get('https://fr.openfoodfacts.org/categorie/popcorn/1.json')
    if r.status_code == rq.codes.ok:
        """requeste = rq.request('GET', 'https://fr.openfoodfacts.org/categories')
        print(requeste)"""
        print(r.json())
    # categorie = rq.loads(r.text)
    # print(categorie.keys())

test()