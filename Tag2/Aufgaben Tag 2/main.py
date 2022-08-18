from spiel import Spiel


def starte_spiel(monster1, monster2):

    das_spiel = Spiel(0)

    # Solange beide Monster am Leben sind
    while monster1.ist_am_leben and monster2.ist_am_leben and das_spiel.gib_runden_anzahl() <= 7 and das_spiel.gib_runden_anzahl() >= 0: #der Kampf

        x = int(input("Spieler 1: Hier den Index der Attacke angeben"))

        monster1.angriff(monster1.attackenliste[x], monster2)
        print(f"{monster1.name} greift {monster2.name} mit {monster1.attackenliste[x].name} an!")
        print(f"Es wurde {monster1.attackenliste[x].schaden} verursacht und {monster2.name} hat noch {monster1.lebenspunkte} Leben!")
      
        if monster1.lebenspunkte <= 0 or monster2.lebenspunkte <= 0:
            das_spiel.beende_spiel()
            break

        y = int(input("Spieler 2: Hier den Index der Attacke angeben"))

        monster2.angriff(monster2.attackenliste[y], monster1)
        print(f"{monster2.name} greift {monster1.name} mit {monster2.attackenliste[y].name} an!")
        print(f"Es wurde {monster2.attackenliste[y].schaden} verursacht und {monster1.name} hat noch {monster1.lebenspunkte} Leben!")
        if monster1.lebenspunkte <= 0 or monster2.lebenspunkte <= 0:
            das_spiel.beende_spiel()
            break

        das_spiel.erhoehe_rundenzahl()






