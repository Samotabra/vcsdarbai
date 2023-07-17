# import pandas as pd
# import psycopg2
#
#
# # #Užduotys:
# # #1. Užduotis:
# #     # [+] Sukurkite klasę "Automobilis" su savybėmis "marke" ir "metai".
# #
# # class Automobilis:
# #      def __init__(self, marke, metai):
# #           self.marke = marke
# #           self.metai = metai
# #           self.isvesta = False
# #
# # # [+] Sukurkite metodą "informacija", kuris išveda automobilio informaciją.
# #
# #      def isvedam_informacija(self):
# #           if not self.isvesta:
# #                print("Info isvesta")
# #                self.isvesta = True
# #           else:
# #                print("Info jau pateikta")
# #
# # #[+] Sukurkite vaikinę klasę "ElektrinisAutomobilis", kuri paveldi klasę "Automobilis" ir papildomai turi savybę
# # # "baterijos_talpa" ir metodą "baterijos talpa informacija", kuris išveda informaciją apie automobilio baterijos talpą.
# #
# # class ElektrinisAutomobilis:
# #      def __init__(self, baterijostalpa):
# #           self.baterijostalpa = baterijostalpa
# #
# #      def baterijos_talpa_info(self, procentai):
# #           baterija = self.baterijostalpa * procentai / 100
# #           self.baterijostalpa = baterija
# #
# # # 2. Užduotis:
# # #      [+] Naudodami pandas, nuskaitykite CSV failą "duomenys.csv" ir įrašykite duomenis į PostgreSQL duomenų bazės
# # #      "students" lentelę.
# # #      [+] Papildoma sąlyga: Įrašykite duomenis į "students" lentelę tik tuomet, jei amžius yra didesnis nei 20.
#
# # data = pd.read_csv('duomenys.csv')
# # filtered_data = data[data['amzius'] > 20]
#
# # Manto pvz.
# data = pd.read_csv('duomenys.csv', encoding="utf8")
# filtered_data = data[data['amzius'] > 20]
# db_params = {
#     'host': 'localhost',
#     'port': 5432,
#     'database': 'students',
#     'user': 'postgres',
#     'password': 'a1b2r3a4'
# }
# # creating table
# def create_table():
#     connection = psycopg2.connect(**db_params)
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS students (
#         id SERIAL PRIMARY KEY,
#         vardas VARCHAR(50),
#         pavarde VARCHAR(50),
#         amzius VARCHAR(10)
#         )
#         """
#     cursor = connection.cursor()
#     cursor.execute(create_table_query)
#     connection.commit()
#     cursor.close()
#     connection.close()
#     create_table()
# # inserting data into database -> student table
# def insert_data():
#     connection = psycopg2.connect(**db_params)  # connect to db
#     cursor = connection.cursor()
# # for eina per kiekviena dokumento eilute ir filtruoja rezultatus pagal musu parasyta salyga
#     for _, row in filtered_data.iterrows():
#         insert_data_into_table = f"""
#         INSERT INTO students.public.students (vardas, pavarde, amzius)
#         VALUES ('{row['vardas']}','{row['pavarde']}','{row['amzius']}')
#         """
#         cursor.execute(insert_data_into_table)
#         connection.commit()
#         cursor.close()
#         connection.close()
# insert_data()
#
#
#
# # 3. Užduotis:
# #      [+] Išskirkite produktų pavadinimus iš {https://www.rde.lt/categories/lt/1599/sort/5/filter/0_0_0_0/page/1/
# #      Dvira%C4%8Diai.html} puslapio naudodami Beautiful Soup ir išsaugokite juos į Pandas DataFrame stulpelį.
# # 4. Užduotis:
# #     [+] Išskirkite informaciją apie produktų kainas ir jų kategorijas iš pigu.lt puslapio naudodami Beautiful Soup ir
# #     išsaugokite juos į Pandas DataFrame.
# #     [+]  Remdamiesi gautais duomenimis sukurkite stulpelinę diagramą, kurioje bus pavaizduotos produktų kainos pagal
# #     kategorijas mažėjančia tvarka.
#
