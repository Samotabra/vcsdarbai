# Darbas su failais naudojant open funkcija;

# file = open("tekstas.txt", "a", encoding="utf8")
# file.write("Tekstas naujame faile, kuriame isbandome open funkcija ir daugiau")
# file.close()

# with open("tekstas1.txt", "w", encoding="utf8") as file:
#     file.write("Tekstas antrajame faile\n")
#     file.write("Antra eilute\n")
#     file.write("Trecia eilute\n")


# filename = input("Iveskite failo pavadinima-> ")
#
# try:
#     with open(filename, "r", encoding="utf8") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileNotFoundError:
#     print("File not fount!")
# except:
#     print("Something went wrong!")

#filename = input("Iveskite naujo failo pavadinima-> ")

# try:
#     with open(filename, "w", encoding="utf8") as file:
#         file.write("Pavyzdiniai duomenys: \n")
#         file.write("Vardas: Mantas\n")
#         file.write("Pavarde: Markus\n")
#         print("Duomenys sekmingai irasyti")
# except:
#     print("ivyko klaida irasant duomenis i faila!")







