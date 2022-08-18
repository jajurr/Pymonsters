import messages
from attacke import Attacke
from charakter import Charakter
from main import starte_spiel



messages.print_header()

monster1 = Charakter("benni", 100, "feuer")

m1_attacke1 = Attacke("schlag", "feuer", 20)
m1_attacke2 = Attacke("kinnhaken", "wasser", 25)
m1_attacke3 = Attacke("steinwurf", "natur", 30)
m1_heilung = Attacke("regeneration", "natur", -20)

monster1.fuege_attacke_hinzu(m1_attacke1)
monster1.fuege_attacke_hinzu(m1_attacke2)
monster1.fuege_attacke_hinzu(m1_attacke3)
monster1.fuege_attacke_hinzu(m1_heilung)



monster2 = Charakter("Yannick", 100, "wasser")

m2_attacke1 = Attacke("feuerball", "feuer", 20)
m2_attacke2 = Attacke("ohrfeige", "natur", 25)
m2_attacke3 = Attacke("karatekick", "wasser", 30)
m2_heilung = Attacke("mittagsschlaf", "natur", -20)

monster2.fuege_attacke_hinzu(m2_attacke1)
monster2.fuege_attacke_hinzu(m2_attacke2)
monster2.fuege_attacke_hinzu(m2_attacke3)
monster2.fuege_attacke_hinzu(m2_heilung)

starte_spiel(monster1, monster2)



