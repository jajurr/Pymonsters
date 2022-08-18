import messages
from spiel import Spiel
from attacke import Attacke



def starte_spiel(monster1, monster2):

    das_spiel = Spiel(0)

    while monster1.gib_ist_am_leben() and monster2.gib_ist_am_leben() and das_spiel.gib_runden_anzahl() <= 7 and das_spiel.gib_runden_anzahl() >= 0: #der Kampf

        x = int(input("Spieler 1: Hier den Index der Attacke angeben"))

        monster1.angriff(monster1.gib_attackenliste()[x], monster2)

        if monster1.gib_lebenspunkte() <= 0 or monster2.gib_lebenspunkte() <= 0:
            das_spiel.beende_spiel()
            break

        y = int(input("Spieler 2: Hier den Index der Attacke angeben"))

        monster2.angriff(monster2.gib_attackenliste()[y], monster1)

        if monster1.gib_lebenspunkte() <= 0 or monster2.gib_lebenspunkte() <= 0:
            das_spiel.beende_spiel()
            break

        das_spiel.erhoehe_rundenzahl()






