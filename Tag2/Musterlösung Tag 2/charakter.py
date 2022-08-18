from typ import Typ


class Charakter():


    def __init__(self, name, lebenspunkte, typ):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.max_leben = lebenspunkte
        self.attackenliste = []     #Liste mit max. 4 Attacken
        self.ist_am_leben = True
        self.typ = Typ(typ)


    # Getter Methoden:
    def gib_name(self):
        return self.name

    def gib_lebenspunkte(self):
        return self.lebenspunkte

    def __gib_typ(self):
        return self.typ

    def gib_typ_name(self):
        return self.typ.gib_typ()

    def gib_attackenliste(self):
        return self.attackenliste

    def gib_ist_am_leben(self):
        return self.ist_am_leben


    # Verändernde Methoden:
    def veraendere_lebenspunkte(self, wert):
        self.lebenspunkte = self.lebenspunkte - int(wert)
        if self.lebenspunkte > self.max_leben:
            self.lebenspunkte = self.max_leben
        if self.lebenspunkte <= 0:
            self.lebenspunkte = 0
            self.ist_am_leben = False
            self.print_ist_besiegt()


        # brauchen wir das wirklich?
        else:
            self.ist_am_leben = True

    def fuege_attacke_hinzu(self, attacke):
        if len(self.attackenliste) < 5:
            self.attackenliste.append(attacke)
        else:
            print(f"Du hast zu viele Attacken!")
            print(f"Mit der Methode: .verlerneAttacke(attackenname) oder .verlerneAttackeByIndex(Index), kannst du Attacken entfernen")

    def verlerne_attacke(self, attackenname):
        self.attackenliste.remove(attackenname)

    def verlerne_attacke_by_index(self, index):
        self.attackenliste.remove(self.attackenliste[index])


    # Sondierende Methoden:
    def berechne_multiplikator(self, typ_eingehende_attacke):
        return self.typ.berechne_multiplikator(typ_eingehende_attacke)


    # Print Methoden:
    def print_effektivitaet(self, multiplikator):
        if multiplikator > 1:
            print("Die Attacke hat erhöhten Schaden verursacht!")
        elif multiplikator < 1:
            print("die Attacke hat verringerten Schaden verursacht!")

    def print_heilung(self, attackenname):
        print(f"{self.gib_name()} heilt sich selbst mit {attackenname}!")
        print(f"{self.gib_name()} hat nun {self.gib_lebenspunkte()}!")

    def print_angriff(self, zielname, attacke):
        print(f"{self.gib_name()} greift {zielname} mit {attacke.gib_name()} ({attacke.gib_typ_string()}) an!")

    def print_uebrige_lebenspunkte(self, ziellebenspunkte):
        print(f"Es sind {ziellebenspunkte} Leben übrig")

    def print_ist_besiegt(self):
        print(f"{self.gib_name()} ist besiegt!")


    # Angriff
    def angriff(self, attacke, ziel):
        if attacke in self.attackenliste:
            # Schaden über 0: Attacke wird auf Ziel angewendet
            if attacke.gib_schaden() >= 0:
                self.print_angriff(ziel.gib_name(), attacke)
                multiplikator = ziel.berechne_multiplikator(attacke.gib_typ_string())
                ziel.veraendere_lebenspunkte(attacke.gib_schaden()*multiplikator)

                if ziel.gib_ist_am_leben:
                    self.print_uebrige_lebenspunkte(ziel.gib_lebenspunkte())
                    self.print_effektivitaet(multiplikator)

            # Schaden unter 0: Attacke wird auf sich selbst angewendet
            else:
                self.veraendere_lebenspunkte(attacke.gib_schaden())
                self.print_heilung(attacke.gib_name())




