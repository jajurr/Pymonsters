class Spiel:

    def __init__(self, runden_anzahl):
        self.runden_anzahl = runden_anzahl

    def erhoehe_rundenzahl(self):
        self.runden_anzahl += 1

    def gib_finale_auswertung(self):
        pass

    def beende_spiel(self):
        self.runden_ablauf = -1

    def gib_spielstatus(self):
        pass

    def starte_spiel(self):
        self.runden_ablauf = 1

    def gib_runden_anzahl(self):
        return self.runden_anzahl
