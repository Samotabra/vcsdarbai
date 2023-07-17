import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Variantas 1: Automobilių pardavimų analizė
# Projekto tema: Automobilių pardavimų analizė pagal marke, modelį ir regioną
# Aprašymas: Šiame projekte naudosite "pandas", "numpy" ir "matplotlib" ar  "Seaborn" bibliotekas taip pat būtina
# naudoti Git, siekdami atlikti išsamią automobilių pardavimų analizę pagal marke, modelį ir regioną. Projekto metu
# atlikite šiuos veiksmus:
#     1.	Duomenų surinkimas: Surinkite automobilių pardavimo duomenis iš skirtingų šaltinių, tokių kaip internetinės
#     svetainės, automobilių pardavimo platformos ar oficialūs gamintojų duomenys.
#     2.	Duomenų valymas ir transformacija: Naudodami "pandas" biblioteką, valysite ir transformuosime surinktus
#     duomenis. Tai gali apimti trūkstamų reikšmių užpildymą, netikslumų šalinimą ir duomenų formatavimą.
#     3.	Duomenų analizė: Išanalizuosime automobilių pardavimo duomenis, naudodami skirtingus statistinius metodus
#     ir "numpy" funkcijas. Galime atlikti įvairias analizes, tokią kaip pardavimų skaičiaus kitimas pagal metus,
#     vidutinės kainos pasiskirstymas, populiariausių automobilių modelių sąrašas ir pan.
#     4.	Vizualizacija: Naudojant "matplotlib","Seaborn", sukurkite grafikus, diagramas ir interaktyvius elementus,
#     kad galėtumėte vizualiai pateikti rezultatus ir įžvalgas iš atliktos analizės. Galite sukurti linijinius grafikus
#     ar geografines žemėlapių vizualizacijas, rodančias pardavimus pagal regioną.
#     5.	Rezultatų pristatymas: Baigus analizę ir vizualizaciją, suformuokite baigiamasias išvadas ir jas
#     pristatykite pranešimo arba ataskaitos formatu.


#csv_file_path = 'C:/Users\Tomas\Desktop\VilniausCodingSchool\atsiskaitymas\elauto_pardavimai.csv'
#df = pd.read_csv("C:/Users/Tomas/Desktop/VilniausCodingSchool/atsiskaitymas/elektra1.csv", encoding="utf-8")

df = pd.read_csv('auto_electra_selling.csv', encoding="utf-8") #imam
# sep=';', sep=',', sep='\t'

#print(df)
print(df.to_string())   #imam

# sausis_suma = df['Sausis'].sum()   #imam viska
# print("Sausi viso:", sausis_suma)
#
# vasaris_suma = df['Vasaris'].sum()
# print("Vasari viso:", vasaris_suma)
#
# kovas_suma = df['Kovas'].sum()
# print("Kova viso:", kovas_suma)
#
# pirmas_ketvirtis = sausis_suma + vasaris_suma + kovas_suma
# print("Pirmas ketvirtis:", pirmas_ketvirtis)
#
# # antras ketv.
# balandis_suma = df['Balandis'].sum()
# print("Balandi viso:", balandis_suma)
#
# geguze_suma = df['Geguze'].sum()
# print("Geguze viso:", geguze_suma)
#
# birzelis_suma = df['Birzelis'].sum()
# print("Birzeli viso:", birzelis_suma)
#
# antras_ketvirtis = balandis_suma + geguze_suma + birzelis_suma
# print("Antras ketvirtis:", antras_ketvirtis)
#
# #trecias.ketv.
# liepa_suma = df['Liepa'].sum()
# print("Liepa viso:", liepa_suma)
#
# rugpjutis_suma = df['Rugpjutis'].sum()
# print("Rugpjuti viso:", rugpjutis_suma)
#
# rugsejis_suma = df['Rugsejis'].sum()
# print("Rugseji viso:", rugsejis_suma)
#
# trecias_ketvirtis = liepa_suma + rugpjutis_suma + rugsejis_suma
# print("Trecias ketvirtis:", trecias_ketvirtis)
#
# #ketvirtas ketv.
# spalis_suma = df['Spalis'].sum()
# print("Spali viso:", spalis_suma)
#
# lapkritis_suma = df['Lapkritis'].sum()
# print("Lapkriti viso:", lapkritis_suma)
#
# gruodis_suma = df['Gruodis'].sum()
# print("Gruodi viso:", gruodis_suma)
#
# ketvirtas_ketvirtis = spalis_suma + lapkritis_suma + gruodis_suma
# print("Ketvirtas ketvirtis:", ketvirtas_ketvirtis)
#
# ketvirciu_suma = pirmas_ketvirtis + antras_ketvirtis + trecias_ketvirtis + ketvirtas_ketvirtis
# print('Viso per metus:', ketvirciu_suma)
#
# ketvirciai = ['Pirmas ketvirtis', 'Antras ketvirtis', 'Trečias ketvirtis', 'Ketvirtas ketvirtis']
# viso = [pirmas_ketvirtis, antras_ketvirtis, trecias_ketvirtis, ketvirtas_ketvirtis]
#
# plt.plot(ketvirciai, viso, marker='o', color='orange') #imam
# plt.xlabel('')
# plt.ylabel('Kiekis vnt.')
# plt.title('Elektromobiliu pardavimai ketvirciais per 2022 m.')
# plt.show()

#...................................................
#ketvirciai = df.groupby(['Pirmas ketvirtis', 'Antras ketvirtis', 'Trecias ketvirtis', 'Ketvirtas ketvirtis']).sum()
#print(ketvirciai)

#...................................................
# #kitas variantas
# pirmas_ketvirtis = df[['Sausis', 'Vasaris', 'Kovas']].sum()
# print("Sausi viso:", pirmas_ketvirtis['Sausis'])
# print("Vasari viso:", pirmas_ketvirtis['Vasaris'])
# print("Kova viso:", pirmas_ketvirtis['Kovas'])

# df['Pirmas ketvirtis'] = df[['Sausis', 'Vasaris', 'Kovas']].sum(axis=1)
# print(df)

# stulpeliai = df.columns
# print(stulpeliai)

# grouped = df.groupby(['Savybe'])   # mayby
# print(grouped)

# group_average = df.groupby('').mean()
# print(group_average)
#..................................
# df = df.sort_values(by=['IS_VISO'], ascending=[False])   #imam, issrusiuota pagal pardavimo kiekius mazejanciai
# print(df.to_string())
#....................................
# group_average_all = df.groupby('Marke')['IS_VISO'].mean()  #imam, bet ar reikia? visu pardavimu vidurkis pagal markes
# print(group_average_all)
#
# group_average_all.plot(kind='bar', figsize=(8, 4))     # corect
#
# plt.title('Elektromobiliu pardavimu vidurkis pagal markes Lietuvoje 2022')       # corect
# plt.xlabel('MARKE')
# plt.ylabel('KIEKIS VNT.')
#
# plt.show()
#............................

group_sum = df.groupby('Marke') ['IS_VISO'].sum() #corect imam
#print(group_sum)

# df = df.sort_values(by=['Marke'])   #imam, pardavimai pagal marke, kategorija, savybe
# print(df.to_string())
#.........................................................
# df = df.sort_values(by=['IS_VISO'])   #imam, pardavimai pagal markes kiekviena men.
# print(df.to_string())
#
# df.plot(kind='bar', figsize=(8, 4))     # corect
#
# plt.title('Elektromobiliu pardavimai Lietuvoje menesiais 2022')       # corect
# plt.xlabel('MARKE')
# plt.ylabel('KIEKIS VNT.')
# plt.show()

# group_sum.plot(kind='bar', figsize=(8, 4))     # corect  imam
#
# plt.title('Elektromobiliu pardavimai Lietuvoje pagal markes 2022')       # corect
# plt.xlabel('MARKE')
# plt.ylabel('KIEKIS VNT.')
#
# plt.show()
#....................................

# group_sum = df.groupby('Savybe') ['IS_VISO'].sum() #corect imam
# print(group_sum)
#
# group_sum.plot(kind='bar', figsize=(8, 4))     # corect
#
# plt.title('Elektromobiliu pardavimai Lietuvoje pagal savybes 2022')       # corect
# plt.xlabel('SAVYBE')
# plt.ylabel('KIEKIS VNT.')
# plt.show()

# group_sum = df.plot(x='Savybe', y='IS_VISO', kind='bar')  #???
#
# for i, v in enumerate(df['IS_VISO']):
#     group_sum.text(i, v + 10, str(v), ha='center')
# plt.show()
#....................................



# group_category = df.groupby('Kategorija')['IS_VISO'].mean()  #??? per mazi kiekiai ne
# print(group_category)


# group_size = df.groupby(['Marke', 'Kovas']).size()   # corect ne
# print(group_size)

# group_max = df.groupby('Marke')['IS_VISO'].max()   # mayby imam
# print(group_max)
#
# group_min = df.groupby('Marke')['IS_VISO'].min()   # mayby imam
# print(group_min)




# group_category.plot(kind='bar', figsize=(8, 4))     # ???
# #
# plt.title('Elektromobiliu pardavimai Lietuvoje 2022 pagal kategorijas')       # ??? per mazi kiekiai ne
# plt.xlabel('Kategorija')
# plt.ylabel('KIEKIS VNT.')
#
# plt.show()
#....................................


