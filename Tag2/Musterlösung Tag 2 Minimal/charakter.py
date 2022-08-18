class Charakter:

    # Der Konstruktor der Klasse Charackter soll folgende Parameter entgegen nehmen:
    # - Namen
    # - Lebenspunkte
    # Füge diese Parameter dem Kopf des Konstruktor hinzu und initialisiere sie.
    # Mache dir über weitere Feldvariablen Gedanken, die du im Laufe der
    # restlichen Programmierung benötigen könntest.
    def __init__(self, name, lebenspunkte):
        self.ist_am_leben = True  # Wann muss diese Variable verändert werden? Namen nicht verändern!
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.attackenliste = []
        


    # Tipp:
    # Baue dir zum Testen print Befehle in deine Methoden, damit du siehst, was passiert.

    # Attacken sollen in einer Liste gespeichert werden.
    # diese liste muss unbeding "attackenliste" (ohne "") heißen.
    # Wo wäre es sinnvoll diese Liste zu erzeugen?
    # Vergiss nicht: Die Attackenliste ist Teil deines Charakters!
    #
    # Die folgende Methode soll ein Objekt der Klasse Attacke
    # der Attackenliste hinzufügen.
    #
    # Zusatzaufgabe:
    # Achte darauf, dass die Attackenliste nicht mehr als 4
    # Attacken speichert.
    # Was soll passieren, wenn man mehr als 4 Attacken hinzufügen möchte?
    def fuege_attacke_hinzu(self, attacke):
        self.attackenliste.append(attacke)



    # Eine Attacke aus der Attackenliste soll verlernt werden.
    # Die Methode nimmt ein Objekt der Klasse Attacke entgegen.
    #
    # Zusatzaufgabe: Kopiere die Methode und forme sie so um, dass du auch eine
    # Zahl eingeben kannst, die eine Attacke aus der Liste entfernt
    def verlerne_attacke(self):
        self.attackenliste.remove(attackenname)



    # Diese Methode soll aufgerufen werden, wenn ein Angriff stattfindet.
    # Du musst einen Schadenswert übergeben und in der Methode sollen
    # die neuen Lebenspunkte berechnet werden
    # Was soll passieren, wenn die Lebenspunkte unter 0 fallen? Schaue dir deine Feldvariablen erneut an!
    #
    # Zusatzaufgabe:
    # Wie würdest du eine Heilung programmieren?
    # Was passiert, wenn Heilung über die maximalen Lebenspunkte hinaus geht?
    def veraendere_lebenspunkte(self, wert):
        self.lebenspunkte = self.lebenspunkte - int(wert)




    # Die Methode angriff nimmt ein Objekt der Klasse Attacke und ein Objekt der Klasse Charakter entgegen
    # Das Objekt der Klasse Charakter ist das Ziel, das von der Attacke getroffen werden soll.
    # Stelle sicher, dass die übergebene Attacke in der Attackenliste des Angreifers ist.
    # Was soll passieren, wenn das nicht der Fall ist?
    # Der Schadenswert deiner Attacke soll nun von den Lebenspunkten des Ziels abgezogen werden.
    # Welche Methoden, die du bereits geschrieben hast können dir dabei helfen?
    #
    # Zusatzaufgabe:
    # Was passiert, wenn du eine Attacke mit einer negativen Zahl erstellst?
    # Wie kannst du dich selbst und nicht den Gegner heilen?
    def angriff(self, attacke, ziel):
        if attacke in self.attackenliste:
          ziel.veraendere_lebenspunkte(attacke.schaden)


