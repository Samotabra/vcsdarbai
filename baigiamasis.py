import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
   Siame darbe apzvelgiamos populiariausios 2022 metais Valstybineje imoneje "Regitra" iregistruotos M1 klases 
elektromobiliu markes. 
   Pateikiami duomenys apima dvi kategorijas ("Tik elektra varomos transporto priemones" ir "Is isores ikraunami hibridai
("plug-in")"), dvi savybes ("Naudota" ir "Nauja") bei 30 elektromobiliu markiu"""

# Pateikiami visi turimi duomenys

df = pd.read_csv('auto_electra_selling.csv', encoding="utf-8")

print(df.to_string())

# Sumuojamos kiekvieno men. ir ketvircio registracijos

# sausis_suma = df['Sausis'].sum()
# print("Sausi viso:", sausis_suma)

# vasaris_suma = df['Vasaris'].sum()
# print("Vasari viso:", vasaris_suma)

# kovas_suma = df['Kovas'].sum()
# print("Kova viso:", kovas_suma)

# pirmas_ketvirtis = sausis_suma + vasaris_suma + kovas_suma
# print("Pirmas ketvirtis:", pirmas_ketvirtis)

# # antras ketv.
# balandis_suma = df['Balandis'].sum()
# print("Balandi viso:", balandis_suma)

# geguze_suma = df['Geguze'].sum()
# print("Geguze viso:", geguze_suma)

# birzelis_suma = df['Birzelis'].sum()
# print("Birzeli viso:", birzelis_suma)

# antras_ketvirtis = balandis_suma + geguze_suma + birzelis_suma
# print("Antras ketvirtis:", antras_ketvirtis)

# #trecias.ketv.
# liepa_suma = df['Liepa'].sum()
# print("Liepa viso:", liepa_suma)

# rugpjutis_suma = df['Rugpjutis'].sum()
# print("Rugpjuti viso:", rugpjutis_suma)
#
# rugsejis_suma = df['Rugsejis'].sum()
# print("Rugseji viso:", rugsejis_suma)

# trecias_ketvirtis = liepa_suma + rugpjutis_suma + rugsejis_suma
# print("Trecias ketvirtis:", trecias_ketvirtis)

# #ketvirtas ketv.
# spalis_suma = df['Spalis'].sum()
# print("Spali viso:", spalis_suma)

# lapkritis_suma = df['Lapkritis'].sum()
# print("Lapkriti viso:", lapkritis_suma)

# gruodis_suma = df['Gruodis'].sum()
# print("Gruodi viso:", gruodis_suma)

# ketvirtas_ketvirtis = spalis_suma + lapkritis_suma + gruodis_suma
# print("Ketvirtas ketvirtis:", ketvirtas_ketvirtis)

# ketvirciu_suma = pirmas_ketvirtis + antras_ketvirtis + trecias_ketvirtis + ketvirtas_ketvirtis
# print('Viso per metus:', ketvirciu_suma)

# ketvirciai = ['Pirmas ketvirtis', 'Antras ketvirtis', 'Trečias ketvirtis', 'Ketvirtas ketvirtis']
# viso = [pirmas_ketvirtis, antras_ketvirtis, trecias_ketvirtis, ketvirtas_ketvirtis]

# plt.plot(ketvirciai, viso, marker='o', color='orange')
# plt.xlabel('')
# plt.ylabel('Kiekis vnt.')
# plt.title('Elektromobiliu pardavimai ketvirciais per 2022 m.')
# plt.show()

# Rusiavimas pagal mazejancia registracija

# df = df.sort_values(by=['IS_VISO'], ascending=[False])
# print(df.to_string())

# Suminis reistraciju palyginimas pagal elektromobiliu marke:

# group_sum = df.groupby('Marke') ['IS_VISO'].sum()
# print(group_sum)
#
# group_sum.plot(kind='bar', figsize=(8, 4))
#
# plt.title('Elektromobiliu pardavimai Lietuvoje pagal markes 2022')
# plt.xlabel('MARKE')
# plt.ylabel('KIEKIS VNT.')
#
# plt.show()

# Suminis reistraciju palyginimas pagal savybe:

# group_sum = df.groupby('Savybe') ['IS_VISO'].sum()
# print(group_sum)
#
# group_sum.plot(kind='bar', figsize=(8, 4))
#
# plt.title('Elektromobiliu pardavimai Lietuvoje pagal savybes 2022')
# plt.xlabel('SAVYBE')
# plt.ylabel('KIEKIS VNT.')
# plt.show()


# Registraciju rusiavimas pagal elektromobiliu markes,  apimant kategorijas, savybes:

# df = df.sort_values(by=['Marke'])
# print(df.to_string())

# Kiekvienos lektromobiliu markes rusiavimas apimant visus men.:

# df = df.sort_values(by=['IS_VISO'])
# print(df.to_string())

# df.plot(kind='bar', figsize=(8, 4))
#
# plt.title('Elektromobiliu pardavimai Lietuvoje menesiais 2022')
# plt.xlabel('MARKE')
# plt.ylabel('KIEKIS VNT.')
# plt.show()

# Didziausiu registraciju grupavimas pagal elektromobiliu markes:

# group_max = df.groupby('Marke')['IS_VISO'].max()
# print(group_max)

# Maziausiu registraciju grupavimas pagal elektromobiliu markes:

# group_min = df.groupby('Marke')['IS_VISO'].min()
# print(group_min)

"""Is ataskaitos galime pastebeti, kad nauju ir naudotu elektromobiliu registracija per 2022 metus islaike panasius 
kiekius. Nauju elektromobiliu rinkoje dominuoja is isores ikraunami hibridai, kuriu nei vienas nebuvo registruotas 
naudotas. Tik elektra varomu transporto priemoniu registre lyderiavo naudoti Tesla modeliai"""