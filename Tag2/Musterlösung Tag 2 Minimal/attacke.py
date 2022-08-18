
class Attacke:

    # Der Konstruktor der Klasse Attacke soll 2 Parameter entgegennehmen
    # Den namen der Attacke
    # den schaden der Attacke
    def __init__(self, name, schaden):
        self.name = name
        self.schaden = schaden

    def gib_name(self):
        return self.name

    def gib_schaden(self):
        return self.schaden




