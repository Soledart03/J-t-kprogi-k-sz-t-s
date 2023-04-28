class Adat():
    def __init__(self,sor):
        egy = sor.rstrip("\n").split(";")
        self.nev = egy[0]
        self.hegy = egy[1]
        self.magassag = int(egy[2])
        
f = open("hegyek.txt", encoding = "utf-8")
be = f.readlines()
hegyek = []
for x in be[1:]:
    egysor = Adat(x)
    hegyek.append(egysor)

#teszt
"""  
for x in hegyek:
    print(x.nev)
"""
#3

hegyek_szama = len(hegyek)
print(f"3. feladat: Hegycsúcsok száma : {hegyek_szama}")

#4

magassagok = []
for x in hegyek:
    magassagok.append(x.magassag)

ossz_magassagok = sum(magassagok)
atlag = ossz_magassagok / hegyek_szama

print("4.feladat: Hegycsúcsok átlagos magassága: {:.2f}".format(atlag),"m")

#5

legmagasabb = max(magassagok)
print("5.feladat: A legmagasabb hegycsúcs adatai: ")
for x in hegyek:
    if x.magassag == legmagasabb:
        print(f"Név: {x.nev}")
        print(f"Hegység: {x.hegy}")
        print(f"Magasság: {x.magassag}")
#6


borzsony = []
for x in hegyek:
    if x.hegy == "Börzsöny":
        borzsony.append(x.magassag)
beker = int(input("6.feladat: Kérem a magasságot: "))

van = False

for x in borzsony:
    if x > beker:
        van = True
if van:
    print(f"Van {beker}m-nél magasabb hegycsúcs a Börzsönyben!")
else:
    print(f"Nincs {beker}m-nél magasabb hegycsúcs a Börzsönyben!")
    
#7
    
mag = []
db = 0
for x in hegyek:
    if x.magassag > 500:
        db +=1
print(f"7.feladat: 500m-nél magasabb hegycsúcsok száma: {db}")



#8: feladat: Készítünk egy magassagok.txt fájlt, amiben a m-ek lesznek
"""
ki = open("magassagok.txt", "w")

for x in magassagok:
    ki.write(str(x) + "\n")
    
ki.close()

print("A kiíratás befejeződött! ")
"""

#9 feladat

ki = open("otszaz.txt", "w")

for x in hegyek:
    if x.magassag > 500:
        ki.write(x.hegy + "\n")
ki.close()

print("A kiíratás befejeződött! ")















