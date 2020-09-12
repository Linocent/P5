from API import SelectProduct, FillDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BDD import Categorie, Store, Products

select_product = SelectProduct()
filldb = FillDB()


class Menu:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://Timothee:RedBull/75019@localhost/openfoodfact')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.conn = self.engine.connect()

    def show(self):

        compt = 1
        Dict_cat = {
            '1': "charcuteries",
            '2': "citronnades",
            '3': "boissons-gazeuses",
            '4': "purees-de-pommes-de-terre",
            '5': "chips-de-pommes-de-terre",
            '6': "fromages-de-france",
            '7': "yaourts-aux-fruits",
            '8': "pates-a-tartiner",
            '9': "biscuits-sables",
            '10': "pizzas",
            '11': "hamburgers"
        }

        filldb.fill_cat(Dict_cat)
        filldb.fill_product(Dict_cat, select_product)

        while compt == 1:
            choice = input("Sélection de l'action:\n"
                           "1: Choix d'une catégorie\n"
                           "2: Voir les substitues\n"
                           "3: Effacer données (en cours de dev)\n"
                           "0: fermeture\n")
            if choice == '1':
                choice = input("liste des catégories:\n"
                                '1: Charcuteries\n'
                                '2: Citronade\n'
                                '3: Boissons gazeuses\n'
                                '4: Purée PDT\n'
                                '5: Chips\n'
                                '6: Fromages\n'
                                '7: Yaourt\n'
                                '8: Pâte à tartiner\n'
                                '9: Biscuits sablés\n'
                                '10: Pizzas\n'
                                '11: Hamburger\n'
                                )
                select_product.extract(choice, Dict_cat[choice])

                """result = self.session.query(Products).from_statement(
                    f"SELECT products_name FROM products WHERE categorie_id={choice}")
                print("This is result: ", result)
                for row in result:
                    print("Product: ", row['products'])"""

            if choice == '2':
                pass
            if choice == '0':
                print('Au revoir.')
                compt = 0
            if choice == '3':
                with self.engine.connect() as connection:
                    connection.execute("DROP TABLE Substitue",
                                       "DROP TABLE products",
                                       "DROP TABLE categorie")


Menu = Menu()
