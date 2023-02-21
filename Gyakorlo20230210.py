#1.
"""
szam1 = int(input("Add meg az első számot:"))
szam2 = int(input("Add meg a második számot:"))
szam3 = int(input("Add meg a harmadik számot:"))

if szam1 < szam2 and szam1 < szam3:
    print("A legkisebb szám a(z): ",szam1)
if szam2 < szam1 and szam2 < szam3:
    print("A legkisebb szám a(z): ",szam2)
if szam3 < szam1 and szam3 < szam2:
    print("A legkisebb szám a(z): ",szam3)
"""
#2.
"""
szam4 = int(input("Add meg az első számot:"))
szam5 = int(input("Add meg a második számot:"))
szam6 = int(input("Add meg a harmadik számot:"))

if szam4 != szam5 and szam4 != szam6 and szam5 != szam6:
    print("Az értékek nem egyeznek meg")
else:
    print("Az értékek megegyeznek")
"""
#3.
"""
x = int(input("Add meg a pontszámot:"))

if x < 50:
    print("Az érdemjegyed elégtelen")
if 50 <= x < 60:
    print("Az érdemjegy elégséges")
if 60<=x<70:
    print("Az érdemjegy közepes")
if 70<=x<85:
    print("Az érdemjegy jó")
if x>=85:
    print("Az érdemjegy kiváló")
"""
#4.
"""
szam7 = int(input("Add meg a számot:"))

if szam7 % 3 == 0 and szam7 % 5 == 0:
    print("A szám osztható 3-mal vagy 5-tel")
else:
    print("A szám nem osztható 3-mal vagy 5-tel")
"""
#5.
"""
szam8 = int(input("Add meg az első számot:"))
szam9 = int(input("Add meg a második számot:"))
szam10 = int(input("Add meg a harmadik számot:"))

if szam8 + szam9 == szam10 or szam8 + szam10 == szam9 or szam10 + szam9 == szam8:
    print("Két szám összege egyenlő a harmadikkal.")
else:
    print("Két szám összege nem egyezik meg.")
"""
#6.
"""
szam11 = int(input("Add meg az első számot:"))
szam12 = int(input("Add meg a második számot:"))
szam13 = int(input("Add meg a harmadik számot:"))

van_benne = False

if szam11 % 2 == 0 and szam12 % 2 == 0 and szam13 % 2 == 0:
    print("Minden szám páros.")
else:
    print("Nem minden szám páros")
"""
#7.
"""
szam14 = int(input("Kérem adjon meg egy egész, pozitív számot:"))
x = 1
while szam14 > x >0:
    x+=1
    if x % 3 == 0:
        print(x)
"""
#8.
"""
A = float(input("Adj meg egy valós számot:"))
K = int(input("Adj meg egy egész számot:"))

hatvany = A**K
print(hatvany)
"""
#26.
"""
lista1 = [5,8,6,7,2]
copylist = lista1.copy()
print(copylist)
"""
#27.
"""
lista = [5,6,3,2,7]
lista.sort()
lista.reverse()
print("A csökkenő számok elemi:")

for x in lista:
    print(x)
"""
#10.
"""
szamok = int(input("Add meg a 20-nál nem nagyobb számot!"))
print(szamok*"*" + "START")
"""
#21.
"""
parameter = input("Add meg a szót:")
print(len(parameter)*"*")
"""

