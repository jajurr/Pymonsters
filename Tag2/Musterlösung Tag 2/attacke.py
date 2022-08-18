from typ import Typ

class Attacke():
    def __init__(self, name, typ, schaden):
        self.attackentyp = Typ(typ)
        self.name = name
        self.schaden = schaden

    def gib_name(self):
        return self.name

    def gib_schaden(self):
        return self.schaden

    def gib_typ_string(self):
        return self.attackentyp.gib_typ()



