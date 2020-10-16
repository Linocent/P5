"""File which show and manage the query from the menu in Main.py"""
from API import SelectProduct, DataBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BDD import Products, Substitue

select_product = SelectProduct()
db = DataBase()


class Menu:
    """Manage query of the menu."""

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://Timothee:RedBull/75019@localhost/openfoodfact')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.conn = self.engine.connect()
        self.id = dict()
        self.d = list()
        self.verif = 0

    def selection(self, cat):
        """Find all product in categorie selected."""

        result = self.session.query(Products).filter_by(categorie_id=cat).all()
        idp = self.session.query(Products.id).filter_by(categorie_id=cat).all()

        for id_product in idp:
            id_product = str(id_product).replace(',', '').replace('(', '').replace(')', '')
            self.d.append(id_product)

        for prod in result:
            print(prod)

        while self.verif == 0:
            prod = input("Enter the number of product:\n")
            if prod in self.d:
                product = self.session.query(Products).get(f"{prod}")
                self.id.update({"p_id": prod})
                print(f"{product} ")
                self.verif = 1
            else:
                pass

    def sub(self, cat):
        """Find substitute and save him."""
        select = input(f"Do you want to have substitue?\n"
                       f"o: Oui\n"
                       f"n : Non\n")
        if select == "o":
            substitue = self.session.query(Products).filter_by(categorie_id=cat).\
                order_by(Products.name_nut).first()
            print(substitue)
            save = input(f"Do you want to save the substitue?\n"
                         f"o: Oui\n"
                         f"n : Non\n")
            id_sub = self.session.query(Products.id).filter_by(categorie_id=cat).\
                order_by(Products.name_nut).first()
            id_sub2 = str(id_sub).replace(',', '').replace('(', '').replace(')', '')
            self.id.update({"id_sub": id_sub2})
            if save == "o":
                db.fill_sub(self.id['id_sub'], self.id['p_id'])
            else:
                pass
        else:
            pass

    def show_substitue(self):
        """Show substitutes."""
        products = self.session.query(Products).join(Substitue,
                                                     Substitue.products_ID == Products.id)
        substitue = self.session.query(Products).join(Substitue,
                                                      Substitue.substitue_ID == Products.id)
        for prod in products:
            print(prod)
            for sub in substitue:
                print(f"The substitute: {sub}")
