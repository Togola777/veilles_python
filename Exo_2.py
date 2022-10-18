# codinging: utf-8

# définition de class local

class P:
    ""
    def __init__(self, name = "Lapinou", type_animal = "lapin", age = 7):
        ""
        self._name = name
        self._type_animal = type_animal
        self._age = age

    def affiche(self):
        print("Votre animal est:", self._name, "de type ", self._type_animal, "d'âge ", self._age)


##########___________main_________#################

print("Veillez entrer les informations relative à l'anilmal (nom, type et age):")
nom = input("Nom:")
type = input("Type: ")
age = input("Âge: ")
a_1 = P(nom, type, age)
a_1.affiche()