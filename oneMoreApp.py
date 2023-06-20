#
#
# class Knyga:
#     def __init__(self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.puslapiai = puslapiai
#         # parasyti metoda ar knyga turi >300 psl.
#     def virs_300_psl(self):
#             if self.puslapiai > 300:
#                 return True
#             else:
#                 return False
# Knyga1 = Knyga("Haris Poteris", "Rasytoja", 600)
# Knyga2 = Knyga("Karlsonas kuris gyvena ant stogo", "Rasytoja2", 250)
#
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())


# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         # parasyti metoda kuris padidins atlyginima tam tikru procentu
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#
#     def visa_informacija(self):
#         print(f"informacija apie darbuotoja: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")
#
#
# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1000)
# Darbuotojas2 = Darbuotojas("Petras", "Petraitis", 1200)
#
# Darbuotojas1.padidinti_atlyginima(10)
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} gavo Naujas atlyginimas: {Darbuotojas1.atlyginimas}")
#
# Darbuotojas1.pakeisti_pavarde("Kazlauskas")
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} pasikeite pavarde!")
#
# Darbuotojas1.visa_informacija()
#
# Darbuotojas2.padidinti_atlyginima(10)
# print(f"{Darbuotojas2.vardas} {Darbuotojas2.pavarde} gavo Naujas atlyginimas: {Darbuotojas2.atlyginimas}")


# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#         # atnaujinti kaina
#
#     def atnaujinti_kaina(self, nauja_kaina):
#             self.kaina = nauja_kaina
#             print(f"{self.pavadinimas} nauja kaina {nauja_kaina}")
#
# Preke1 = Preke ("Pienas", 5, 50)
# Preke2 = Preke ("Duona", 2, 60)
#
# Preke1.atnaujinti_kaina(2.50)

# reikia pranesti pirkejui, kad sandelyje nera tiek prekiu

# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#         # atnaujinti kaina
#
#     def atnaujinti_kaina(self, nauja_kaina):
#             self.kaina = nauja_kaina
#             print(f"{self.pavadinimas} nauja kaina {nauja_kaina}")
#
#     def sandelio_likutis(self, kiekis):
#         if pardavimo_kiekis <= self.kiekis:
#             self.kiekis -= pardavimo_kiekis
#             print(f"Parduota{self.pavadinimas} {pardavimo_kiekis}")
#         else:
#             print(f"Nepakanka prekiu: {self.pavadinimas}")
#
#     def sandelio_papildymas(self, padidintas_likutis):
#             self.kiekis += padidintas_likutis
#             print(f"Padidintas kiekis {self.pavadinimas} {padidintas_likutis}")
#
#
#
# #sukuriamas objektas
# Preke1 = Preke ("Pienas", 5, 50)
# Preke2 = Preke ("Duona", 2, 60)
#
# Preke1.atnaujinti_kaina(2.50)
# Preke1. sandelio_likutis(15)
# Preke2.sandelio_likutis(8)
# Preke1. sandelio_papildymas(20)
# Preke1. sandelio_papildymas(15)
# print(Sandelio likutis, Preke1.kiekis)   YRA KLAIDU

#Blogo kurimas.

# class Blog:
#     def __init__(self):
#         self.posts = []
#     def create_post(self, pavadinimas, aprasymas):
#         post = {
#         "pavadinimas": pavadinimas,
#         "aprasymas": aprasymas
#         }
#
#         self.posts.append(post)
#         print(f"Irasas sekmingai sukurtas")
#
#
#     def display_all_posts(self):
#         if not self.posts:
#             print("no blog post found")
#         else:
#             print("Blog posts:")
#             for post in self.posts:
#                 print(f"pavadinimas: {post['pavadinimas']}")
#                 print(f"aprasymas: {post['aprasymas']}")
#                 print("-------")
#
#     def update_post(self, title, new_description):
#         for post in self.posts:
#             if post["title"] == title:
#                post["description"] = new_description
#                print("Blog post updated")
#                break
#         else:
#             print("Blog post not found")
#
#     del delete_post(self, title):
#         for post in self.posts:
#             if post["title"] == title:
#                 self.post.remove(post)
#                 print("Post was removed")
#                 break
#         else:
#             print("Post was not found")
#
#
#
# post1 = Blog()
#
# post1.create_post("duomenu analitikos studentai uzkariavo pasauli", "karta gyveno analitikai, kurie ismoks programuoti")
# post1.create_post("Mokslininkai isrado nauja metoda", "Kaip greiciau ismokti duomenu analize")
# post1.create_post("Kulinarijos sedevrai", "Tukstantis ir vienas receptas")
# post1.display_all_posts()
# post1.update_post("Teksto pakeitimai", "Pakartotinas keitimas")
# post1.display_all_posts()
# post1.delete_post("duomenu analitikos studentai uzkariavo pasauli")
# post1.display_all_posts()
#CRUD create, read, update, delete.

# Dictionary (Zodynas)
# zmogus = {
#     "vardas": "Jonas",
#     "amzius": 27
#     "miestas": "Vilnius"
# }
# print("Mano vardas: ", zmogus['vardas'])
#
# zmogus["lytis"] = "Vyras"
# #pridedame nauja elementa i savo zodyna
# print("As esu", zmogus["Lytis"])
#
# #keiciame reiksmes
# zmogus["amzius] = 20
# print("Atsiprasau man yra: ", zmogus['amzius'])
#
# # triname reiksmes
#
# del zmogus["miestas"]
#
# print  NEBAIGTA


# Tuple
# kordinates = (10,50)
# print(kordinates[1])
#
# kordinates1 = (54, 42,12)
#
# sujungtos_kordinates = kordinates + kordinates1
# print(sujungtos_kordinates)

# 2023-06-15

# TicTacToe








