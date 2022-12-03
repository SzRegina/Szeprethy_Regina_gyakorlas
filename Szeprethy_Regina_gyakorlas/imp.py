"""5. feladat
Adott az alábbi 2 lista Az egyikben személyek nevét tároljuk, a másikban azonos pozíción ugyanezek személyek nemét:

szemelyek = ["Ákos", "Béla", "Éva", "Zoli", "Judit"]

nemek = ["férfi", "férfi", "nő", "férfi", "nő"]

Írd ki az utolsó férfi nevét!

A rendelkezésre álló idő 10 perc.

A kódról és a program futásáról is képernyőképet kérek feltölteni. """

#1
szemelyek = ["Ákos", "Béla", "Éva", "Zoli", "Judit"]
nemek = ["férfi", "férfi", "nő", "férfi", "nő"]

print(str(szemelyek[3]) + " " + str(nemek[3]))

#2 nemek listán megyek végig, és az utolsó férfit keresem
szemelyek = ["Ákos", "Béla", "Éva", "Zoli", "Judit"]
nemek = ["férfi", "férfi", "nő", "férfi", "nő"]

"""i= 0
last_man = ""
while (i <len(nemek)):
    if (nemek[i]) == "férfi"):
        last_man = szemelyek[i]
    i += 1
print(f"{last_man}")

# nemek listán hátulról
i = len(nemek) - 1
while(i >= 0) and nemek[i] == "nő"):
    i-=1
if i>=0:
    print(szemelyek[i])
else:
    print("Nincs férfi")"""


#3 utolsó férfi index
"""i = 0
utolso_f_index = 0
while (i< len(nemek)):
    if (nemek[i]=="férfi"):
        utolso_f_index = i
    i+=1
if utolso_f_index >= 0:
    print(utolso_f_index)

#Patricia

i =-1
print(i>-len(nemek) and nemek[-1])
while nemek[i] != "férfi":
    i-=1
print(szemelyek[i]) """

""""
******

Készíts egy sorozat nevű tömböt a következő elemekkel: -3, 5, 11, -2, 4
Készíts egy metódust, ami kiírja a tömb elemeit egymás mellé, 
a metódus paraméterében kapott szeparátor felhasználásával! Az utolsó elem után ne legyen szeparátor!
pl: separator:  #    à -3# 5# 11# -2# 4

************

Változtasd meg a tömb elemeit a következő módon:
A tömb első eleméhez adj egy véletlenszámot a [5; 12] intervallumból!
Az utolsó elem értékét kérd be, ez páratlan hárommal osztható kéjegyű szám legyen! 
Ha nem ilyen számot adnak meg, akkor addig folytassa a program a bekérést, 
amíg megfelelő nem lesz a bekért szám! A bekéréshez készíts külön függvényt!
Használd a 2. feladat kiíró metódusát paraméter nélkül, ekkor szóközzel írja ki a tömb elemeit, egymás mellé!
Add meg az első kétjegyű szám helyét és  értékét a tömbből!
Számold meg, hogy hány prímszám van a tömbben! Ehhez készíts külön függvényt, 
ami eldönti, hogy a paraméterében kapott szám prímszám-e? """

sorozat = [-3, 5, 11, -2, 4]
import random

def masodik():
    szeparator = ","
    i = 0
    szoveg = ""
    while (i < len(sorozat)):
        if i == 4:
            szoveg += str(sorozat[i])
        else:
            szoveg += str(sorozat[i])+szeparator
        i += 1
    print(szoveg)
def random_szam():
    random_szam = random.randrange(5, 12)
    sorozat2 = [(-3 + int(random_szam)), 5, 11, -2, 4]
    print(sorozat2)

def random2():
    sorozat3 = [-3, 5, 11, -2, 4]
    x = 0
    while ( 10>= x <100 and x % 2 == 0):
        x = int(input("Adj meg egy páratlan, hárommal osztható számot! "))
    sorozat3[len(sorozat3) -1] = x









