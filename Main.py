# !/usr/bin/python3
# -*- coding: Utf-8 -*-

"""Select a categorie and a product to find a substitute,
save them and consult them.

Script python
files: database.py, api.py, show.py, main.py."""
from show import Menu
from database import DataBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = DataBase()
menu = Menu()


class Main:
    """It's the structure of the project. It's the menu."""

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://Timothee:RedBull/'
                                    '75019@localhost/openfoodfact')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.conn = self.engine.connect()
        self.verif = 0

    def main(self):

        compt = 1
        dict_cat = {
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

        db.fill_cat(dict_cat)
        db.fill_product(dict_cat)

        while compt != 0:
            choice = input("Choose an action:\n"
                           "1: Choose a categorie\n"
                           "2: See substitutes\n"
                           "3: Empty data\n"
                           "0: Close\n")
            if choice == '1':
                select = input("Select the categorie:\n"
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
                               '11: Hamburger\n')
                menu.selection(select)
                menu.sub(select)
                compt = 0
            if choice == '2':
                menu.show_substitue()
                compt = 0
            if choice == '0':
                print('Goodbye.')
                compt = 0
            if choice == '3':
                db.empty_db()


Main = Main()
if __name__ == "__main__":
    Main.main()
