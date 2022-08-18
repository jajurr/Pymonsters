# Aufgabe 1
# Hallo Welt
# printe "hallo Welt" auf die Konsole
# printe beliebige Worte auf die Konsole
# printe eine Zahl
print("Hallo,Welt")

# Aufgabe 2
# Rechenbesipsiele mit Basisoperatoren
# printe das Ergebnis einer Addition / Subtraktion / Multiplikation / Division / Modulo
# auf die Konsole

print(8 + 10)
print(8 - 10)
print(8 * 10)
print(8 / 10)
print(8 % 10)
# Aufgabe 3
# Benutze Variablen
# weise den Variablen variable1 und variable2 Werte zu und printe das Ergbenis.
# Nutze dazu die Zahlen aus Aufgabe 2.
# als nächstes erstelle eine Variable, die das Wort "hallo" beinhaltet.
# printe die erstellte Variable.
# erstelle eine Variable x mit dem inhalt "1" (Mit Anführungszeichen) und eine
# Variable y mit dem Inhalt "2".
# Was passiert wenn du (x + y) printest?

x = 4
y = 8
print(x + y)

a = "Hallo1"
print(a)
b = "Welt"
print(a + b)
# Aufgabe 4
# Fallunterscheidung if
# Nutze die Zuweisung der Variablen aus Aufgabe 3 und prüfe ob variable1 größer als, gleich oder kleiner die varibale2 ist
# printe in beiden Fällen einen Hinweis auf die Konsole. (z.B. variable1 ist größer als variable2)

print(x < y)
print(x > y)
print(x == y)

# Aufgabe 5
# input-Funktion
# Frage den Nutzer mit der input-Funktion nach einem Passowrt ab. Das Passwort lautet "Pymon".
# Gibt der NUtzer dies korrekt ein, soll ihm dies per print-Befehl mitgeteilt werden. Ist es falsch, ebenfalls.

passworteingabe = input("Wie lautet das Passwort?")
passwort = "Pymon"
if (passwort == passworteingabe):
    print("richtig")
else:
    print("falsch")

    # Aufgabe 6
    # while-Funktion
    # Ein Pymon besitzt 100 Lebenspunkte, es bekommt jede Runde 5 Lebenspunkte abgezogen. Wenn das Pymon keine
    # Lebenspunkte mehr besitzt, gebe aus "Das Pymon muss wieder aufgeladen werden".
    # Lass dein Programm die Runden zählen, die dein Pymon durchgehalten hat und gib das
    # Ergebnis am Ende auf der Konsole aus

    lebenspunkte = 100
    runde = 0
    while (lebenspunkte != 0):
        lebenspunkte = lebenspunkte - 5
        runde = runde + 1

    if (lebenspunkte == 0):
        print("Das Pymon ist tot")
        print("Dein Pymon hat" + str(runde) + "Runden ausgehalten")

# Aufgabe 7
# Listen, for-Schleife
# Erstelle eine Liste mit coolen Namen von Attackend
# Lass dir alle Elemente der Liste auf die Konsole ausgeben.
# Lass dir nur das erste oder nur das zweite Element deiner Liste printen
# Lass dir die Anzahl der Elemente deiner Liste auf die Konsole ausgeben
# Füge einen Attackennamen nachträglich hinzu.
# Überschreibe den Attackennamen an der 1. Stelle deiner Liste.
# Entferne einen Attackennamen aus deiner Liste.

attacken = ["Dampfhammer", "Tackle", "Blubber"]
for y in attacken:
    print(y)

print(attacken[0])
print(attacken[1])

zaehler = 0
for x in attacken:
    zaehler += 1
print(zaehler)
#print(len(attacken))

attacken.append("Feuerball")

attacken[0] = "Käsebrot"

del attacken[1]


# Aufgabe 8
# Klassen, Attribute
# Attackenklasse erstellen
# Die Attacke soll einen Namen haben und einen Schadenswert als Attribute haben.
# Greife auf die erstellte Attacke zu und frage den Namen ab.
# Ändere den Namen deiner Attacke, indem du auf ihn zugreifst.
# Erstelle 4 Attacken und füge sie einer Liste hinzu.
# Greife auf die Liste zu und gebe jeden Namen der Attacke gefolgt von
# einem Doppelpunkt und dem Schadenswert auf der Konsole aus.
# Beispiel: Attacke1 : 100
# Greife auf die Liste zu und führe für jede Attacke in deren Name der Buchstabe "a"
# vorkommt einen beliebigen Printbefehl aus.
class Attacke:
    def __init__(self, name, schaden):
        self.name = name
        self.schaden = schaden


tackle = Attacke("Tackle", 20)
blubber = Attacke("Blubber", 20)
doppler = Attacke("Doppler", 0)
faust = Attacke("Faustschlag", 40)

liste = [tackle, blubber, doppler, faust]
for attacke in liste:
    print(f"{attacke.name} : {attacke.schaden}")

#print(attacke.name + ":" + str(attacke.schaden))
#print(liste[0].name + ":" + liste[0].schaden....)


# Aufgabe 9
# Methoden
# definiere eine Methode print_hallo(), die bei Aufruf 2x "Hallo Welt" auf die Konsole ausgibt.
# Definiere eine Methode berechne(x,y), die zwei Zahlen entgegennimmt, sie addiert und dann auf der Konsole ausgibt.
# Definiere eine Methode print_oder_berechne(x,y), die zwei Zahlen entgegennimmt, wenn die erste Zahl größer als 10 ist,
# führe deine print_hallo() Methode aus, ansonsten führe die Methode berechne(x,y) mit
# den beiden übergebenen Zahlen aus.
# Definiert eine Methode, der ihr ein Objekt der Klasse "Attacke" übergebt und die automatisch den Namen
# der Attacke auf die Konsole schreibt
def print_hallo():
    print("Hallo Welt")
    print("Hallo Welt")


def berechne(x, y):
    print(x + y)


def print_oder_berechne(x, y):
    if x > 10:
        print_hallo()
    else:
        berechne(x, y)


def eineMethode(Attacke):
    print(Attacke.name)


# Aufgabe 10
# macht euch Gedanken, wie ein Game Loop funktionieren könnte.
# Ausgangspunkt ist ein Rundenbasiertes Spiel, bei dem beide Spieler abwechselnd an der Reihe sind
# Wie beendet ihr den Game Loop?
# Was sind die Bedingungen für das Beenden?
