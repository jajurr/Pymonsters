import messages
from attacke import Attacke
from charakter import Charakter
from main import starte_spiel



messages.print_header()

monster1 = Charakter("benni", 100)

m1_attacke1 = Attacke("schlag", 20)
m1_attacke2 = Attacke("kinnhaken", 25)
m1_attacke3 = Attacke("steinwurf", 30)
m1_heilung = Attacke("regeneration", -20)

monster1.fuege_attacke_hinzu(m1_attacke1)
monster1.fuege_attacke_hinzu(m1_attacke2)
monster1.fuege_attacke_hinzu(m1_attacke3)
monster1.fuege_attacke_hinzu(m1_heilung)



monster2 = Charakter("Yannick", 100)

m2_attacke1 = Attacke("feuerball", 20)
m2_attacke2 = Attacke("ohrfeige", 25)
m2_attacke3 = Attacke("karatekick", 30)
m2_heilung = Attacke("mittagsschlaf", -20)

monster2.fuege_attacke_hinzu(m2_attacke1)
monster2.fuege_attacke_hinzu(m2_attacke2)
monster2.fuege_attacke_hinzu(m2_attacke3)
monster2.fuege_attacke_hinzu(m2_heilung)

starte_spiel(monster1, monster2)



