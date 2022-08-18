class Spiel:

    # Der Konstruktor nimmt einen Parameter entgegen. Das ist die RundenAnzahl.
    def __init__(self, runden_anzahl):
        self.runden_anzahl = runden_anzahl

    # Diese Methode erhöht die Rundenanzahl um 1.
    def erhoehe_rundenzahl(self):
        self.runden_anzahl += 1

    # Setzt die Rundenanzahl auf -1.
    def beende_spiel(self):
        self.runden_anzahl = -1

    # Setzt die Rundenanzahl auf 1.
    def starte_spiel(self):
        self.runden_anzahl = 1

    # gibt die aktuelle Rundenanzahl zurück.
    def gib_runden_anzahl(self):
        return self.runden_anzahl
