# #Užduotys:
# #1. Užduotis:
#     # [+] Sukurkite klasę "Automobilis" su savybėmis "marke" ir "metai".
#
# class Automobilis:
#      def __init__(self, marke, metai):
#           self.marke = marke
#           self.metai = metai
#           self.isvesta = False
#
# # [+] Sukurkite metodą "informacija", kuris išveda automobilio informaciją.
#
#      def isvedam_informacija(self):
#           if not self.isvesta:
#                print("Info isvesta")
#                self.isvesta = True
#           else:
#                print("Info jau pateikta")
#
# #[+] Sukurkite vaikinę klasę "ElektrinisAutomobilis", kuri paveldi klasę "Automobilis" ir papildomai turi savybę
# # "baterijos_talpa" ir metodą "baterijos talpa informacija", kuris išveda informaciją apie automobilio baterijos talpą.
#
# class ElektrinisAutomobilis:
#      def __init__(self, baterijostalpa):
#           self.baterijostalpa = baterijostalpa
#
#      def baterijos_talpa_info(self, procentai):
#           baterija = self.baterijostalpa * procentai / 100
#           self.baterijostalpa = baterija
#
# # 2. Užduotis:
# #      [+] Naudodami pandas, nuskaitykite CSV failą "duomenys.csv" ir įrašykite duomenis į PostgreSQL duomenų bazės
# #      "students" lentelę.
# #      [+] Papildoma sąlyga: Įrašykite duomenis į "students" lentelę tik tuomet, jei amžius yra didesnis nei 20.
#
# import pandas as pd
#
# df = pd.read_csv('duomenys.csv')
# print(df.head(10))