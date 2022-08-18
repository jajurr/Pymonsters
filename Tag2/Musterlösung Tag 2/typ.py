 # Mögliche Typen: normal, wasser, feuer, natur

class Typ:
    def __init__(self, typ):
        self.ueberpruefe_zulaessige_typen(typ)
        self.__typ = typ
        self.__schwaeche = self.berechne_schwaeche()
        self.__staerke = self.berechne_staerke()

    def gib_typ(self):
        return self.__typ

    def berechne_multiplikator(self, anderer_typ):
        if self.__typ == anderer_typ:
            return 0.75
        elif anderer_typ == self.__schwaeche:
            return 1.25
        elif anderer_typ == self.__staerke:
            return 0.75
        else:
            return 1


    def berechne_schwaeche(self):
        if self.__typ == "normal":
            return "keine"
        elif self.__typ == "wasser":
            return "natur"
        elif self.__typ == "feuer":
            return "wasser"
        elif self.__typ == "natur":
            return "feuer"
        else:
            return print("Falscher Typ eingegeben")


    def berechne_staerke(self):
        if self.__typ == "normal":
            return "keine"
        elif self.__typ == "wasser":
            return "feuer"
        elif self.__typ == "feuer":
            return "natur"
        elif self.__typ == "natur":
            return "wasser"
        else:
            return print("Falscher Typ eingegeben")


    def ueberpruefe_zulaessige_typen(self, typ):
        if typ == "wasser" or typ == "normal" or typ == "feuer" or typ == "natur":
            pass
        else:
            print("Fehlermeldung, ungültiger Typ")
