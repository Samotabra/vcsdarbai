
# komentuoja viena eilute
"""
Multi-komentavimas

"""

# vardas = "Modestas"
# amzius = 25
#
# arVartotojasAktyvus = False
#
# produktoKaina = 3.99

# miestai = ["Vilniuje", "Kaunas", "Klaipeda"]

# print("Mano vardas " + vardas + " As gyvenu " + miestai[0] + " mano amzius " + str(amzius))
# print(miestai[-2])

# miestai[1] = "Siauliai"
# miestai.append("Panevezys")
# miestai.insert(1, "Anyksciai")
# miestai.pop()
# del miestai[2]

# print(miestai)

# print(miestai[0])

# print(type(miestai))
# print(amzius)


# zodis = "Kaunas"


# skaiciuSarasas = [1,3,53,123,1245,12312]
# skaicius = int(input("Iveskite skaiciu: "))


# if skaicius > 0:
    # print("Skaicius yra teigiamas")
# elif skaicius < 0:
    # print("Skaicius yra neigiamas")
# else:
    # print("Skaicius yra nulis")

# print(len(miestai))

# if len(skaiciuSarasas) > 0:
    # print("Skaiciu sarasas pilnas")
# else:
    # print("Skaiciu sarasas tuscias")

# print("Mano vardas " + "Tomas" + " As gyvenu " + miestai[0] + " mano amzius " + str(amzius))
# miestai[1] = "Siauliai"


# print(type(produktoKaina))
# print(amzius)

# miestai.insert(1, "Anyksciai")
# miestai.pop()
# del miestai[2]
# print(miestai)

# if amzius == 18:
    # print("Pilnametis")

# elif amzius == 24:
    # print("Daugiau nei 18")
# elif amzius > 24:
    # print("Daugiau nei 25")
# else:
    # print("Nepilnametis")

"""
Priskirimo operatoriai
= Priskirimas
+= Prideda ir priskiria
-= Atima ir priskiria
*=
/=
%=

Matematiniai operatoriai
+
-
*
/
%
** kelimas laipsniu
// sveikoji dalyba

Palyginimo operatoriai
== lygu
!= nelygu
>
<
>=
<=

Loginiai operatoriai
and
OR
not

Narystes operatoriai

in
not in

Tapatumo (identity) operatoriai

is
is not
"""


# ivertinimas = [1,2,3,4,5,6,7,8,9,10]
# islaikymoRiba = 5
# ivertinimas = int(input("iveskit ivertinima: "))
# if ivertinimas >= islaikymoRiba:
    # print("Egzaminas islaikytas")
# else:
    # print("Egzaminas neislaikytas")

"""2. patikrinkite ar skaicius yra lyginis"""
# Skaiciai = 7
# if Skaiciai % 2 == 0:
    # print("Lyginis skaicius")
# else:
    # print("Nelyginis skaicius")

"""3. Patikrinkite, ar sarase yra bent du skaiciai"""

# sarasas = [1,2,3,4,5,6,7,8,9,10]

    # if len(sarasas) >= 2:
        # print("yra 2 skaiciai")
    # else:
        # print("nera 2 skaiciu")

        # for i in range(0, 10):
            # print(i)

# vardai = ["Jonas", "Saulius", "Lina", "Marius", "Rugile"]
    # key    value
# for vardas in vardai:
    # print(vardai)

    # skaiciai = [10, 20, 30, 40, 50, 23]
    # atrinkti = []

    # for skaicius in skaiciai:
        # if skaicius > 25:
            # atrinkti.append(skaicius)

        # print("Atrinkti skaiciai: ", atrinkti)

# skaiciai = [10, 10, 20, 44, 50, 50, 23, 23, 2, 45, 44, 11, 21]

# unikalios_reiksmes = []

# for skaicius in skaiciai:
    # if skaicius not in unikalios_reiksmes:
       # unikalios_reiksmes.append(skaicius)

        #print("Unikalios reiksmes: ", unikalios_reiksmes) pavyko

# def suma(a, b):
    # return a + b

# rezultatas = suma(2, 5)
#print("Suma: ", rezultatas)

# def pasisveikinimas(vardas="Anonimas"):
    # print("Labas,", vardas)

# pasisveikinimas("Modestas") pavyko

# def sujungti_sarasus(sarasas1, sarasas2):
    # sujungtas_sarasas = sarasas1 + sarasas2
    # return sujungtas_sarasas

# rezultatas = sujungti_sarasus([1, 2, 3],[4, 5, 6])
# print("Sujungtas sarasas: ", rezultatas)   pavyko

# 1.Parašykite funkciją ar_lyginis, kuri priima vieną skaičių kaip
# argumentą ir patikrina, ar skaičius yra lyginis. Jei skaičius yra lyginis, tada funkcija turi grąžinti True,
# o jei nelyginis - False.

# def ar_lyginis(skaicius):

    # if skaicius % 2 == 0:
        # return True
    # else:
        #return False
# print (ar_lyginis(9))

# 2. Parašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo;

# def didziausias_skaicius(sarasas):
    # didziausias = sarasas[0]
    # for skaicius in sarasas:
        # if skaicius > didziausias:
            # didziausias = skaicius
    # return didziausias
# skaiciusarasas = [1, 2, 7, 80, 50, 54, 6, 10]
# rezultatas = didziausias_skaicius(skaiciusarasas)
# print(rezultatas)  pavyko


# 3. Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina naują sąrašą,
# kuriame yra tik unikalios reikšmės iš pradinio sąrašo.

# def unikalios_reiksmes(sarasas):
    # tuscias_sarasas = []
    # for reiksme in sarasas:
        # if reiksme not in tuscias_sarasas:
            # tuscias_sarasas.append(reiksme)

    # return tuscias_sarasas
# naujas_sarasas = [1, 1, 5, 6, 6, 6, 84, 95, 32, 32, 15]
# print(unikalios_reiksmes(naujas_sarasas))

# 1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.


# def suma_nelyginiu(sarasas):
#     suma = 0
#     for nelyginis_skaicius in sarasas:
#         if nelyginis_skaicius % 2 != 0:
#             suma += nelyginis_skaicius
#     return suma
# pradinis_sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rezultatas = suma_nelyginiu(pradinis_sarasas)
# print(rezultatas)

# 2.Raskite didžiausią skaičių iš Jūsų sukurto skaičių sąrašo.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina didžiausią skaičių.
# pradinis_sarasas = [5,9, ]

# 3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius.

# def pirminis_skaicius (skaicius):
#     if skaicius < 2:
#         return False
#     for daliklis in range (2, skaicius):
#         if skaicius % daliklis == 0:
#             return False
#     return True
# skaicius = 1
# if pirminis_skaicius(skaicius):
#     print(f"skaicius {skaicius} yra pirminis skaicius")
# else:
#     print(f"skaicius {skaicius} yra ne pirminis skaicius")

# 23-06-13 Objektinis programavimas.

# skaicius = 1
# while skaicius <= 5:
#     print(skaicius)
#     skaicius += 1

# skaicius = int(input("iveskite_skaiciu: "))
# while skaicius >= 0:
#     if skaicius % 2 == 0:
#         print(skaicius)
#     skaicius -= 1

