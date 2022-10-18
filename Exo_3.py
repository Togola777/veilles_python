# codiging:utf-8

class Persone:
    ""
    def __init__(self, nom = "Kassim", prenom = "N'diaye", cin = "18M"):
        ""
        self.nom = nom
        self.prenom = prenom
        self.cin = cin

    def ToString(self):
        ""
        print("nom:", self.nom, "   prénom:", self.prenom, "    cin:", self.cin)


class Vaccine(Persone):
    ""
    def __init__(self, nom = "Kassim", prenom = "N'diaye", cin = "18M", code_vac = 259, date_vac = "28/07/2022"):
        ""
        Persone.__init__(self, nom = "Kassim", prenom = "N'diaye", cin = "18M")
        self._code_vac = code_vac
        self._date_vac = date_vac

    def get_code_vac(self):
        return self._code_vac

    def get_date_vac(self):
        return self._date_vac

    def set_code_vac(self, code_vac):
        self._code_vac = code_vac

    def set_date_vac(self, date_vac):
        self._date_vac = date_vac

    def ToString(self):
        ""
        Persone.ToString(self)
        print("A été vacciner au date ", self._date_vac, "et a pour code vaccination:", self._code_vac)


class vaccin:
    def recopie(self, v):
        self.code_vacc = v.code_vacc
        self.nom_vac = v.nom_vac
        self.dur_dose = v.dur_dose
    def __init__(self):
        self.code_vacc = 4525
        self.nom_vac = "coqcitose"
        self.dur_dose = 3

    def ToString(self):
        print("Nom du vaccin: ", self.nom_vac, "code du vaccin: ", self.code_vacc, "Durré de dose:", self.dur_dose)

############_________main________##############
v1 = Vaccine()
v1.set_date_vac("14/12/2021")
v1.get_code_vac()
v1.ToString()
vc = vaccin()
vc2 = vaccin()
vc2.recopie(vc)
print("Information de vc:")
vc.ToString()
print("Information de vc2:")
vc2.ToString()
