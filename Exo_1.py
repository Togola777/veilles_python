# codiging utf - 8

# définition de class
class Table:
    "Class définissant la table d'une entreprise"
    def __init__(self, ref, mat_table, poids_table, haut_table, long_table, larg_table, prix_vente, _prix_fab,_nbre_tab_stcok):
        "Méthode constructeur"
        self.ref = ref
        self.mat_table = mat_table
        self.poids_table =poids_table
        self.haut_table =haut_table
        self.long_table =long_table
        self.larg_table = larg_table
        self.prix_vente = prix_vente
        self._prix_fab = _prix_fab
        self._nbre_tab_stock = _nbre_tab_stcok

    def get_prix_fab(self):
        "Méthode accesseur de _prix_fab"
        return self._prix_fab

    def get_nbre_tab_stock(self):
        "Méthode accesseur de nbre_tab_stock"
        return self._nbre_tab_stock

    def set_prix_fab(self, prix_fab):
        ""
        self._prix_fab = prix_fab

    def set_nbre_tab_stock(self, nbre_tab_stock):
        ""
        self._nbre_tab_stock = nbre_tab_stock

    def affichage(self):
        " Methode permettant d'afficher les information d'une talbe"
        print("Table référencée par ", self.ref, " à matière ", self.mat_table, "de longueur ", self.long_table, "et largeur ", self.larg_table, "a une hauteur de ", self.haut_table, "et un poids de ", self.poids_table, "pour une prix de vente:", self.prix_vente)

    def cal_gain(self):
        ""
        print("Le gain par rapport au stock est: ", (self._nbre_tab_stock*self.prix_vente))


###########_______________programme principal_________________#####################
t_1 = Table(7, "bois", 40, 90, 72, 50,10000, 400, 25)
t_1.set_prix_fab(5000)
t_1.set_nbre_tab_stock(17)
t_1.affichage()
print("Le prix de fabrication est: ", t_1.get_prix_fab())
print("Le nombre de stock est: ", t_1.get_nbre_tab_stock())
t_1.cal_gain()