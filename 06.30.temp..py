import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# temperaturos
#
# temperaturos = np.array(
#     [20, 22, 23, 19, 25, 21, 20, 18, 24, 26, 22, 21, 20, 25, 23, 21, 19, 20, 22, 24, 26, 21, 23, 25, 26, 22, 20, 21])
#
# # apskaiciuojame vid. temperatura
#
# vidutine_temperatura = np.mean(temperaturos)
# print(vidutine_temperatura)
#
# # apskaiciuojam didziausia temperat.
# didziausia_temp = np.max(temperaturos)
#
# # apskaiciuojam maziausia temperat.
# maziausia_temp = np.min(temperaturos)
#
# slekcio_verte = 23
#
# # randame dienas, kai temp. virsijo slenkstine verte
#
# virsijo_slenkstine_temp = temperaturos[temperaturos > slekcio_verte]
# print(f'Dienos, kai temperatura virsijo slenkstine verte: {virsijo_slenkstine_temp}')


# df = pd.DataFrame({'Temperatura': temperaturos})
#
# slenkstis = 23
#
# filtruojame_df = df[df['Temperatura'] > slenkstis]
#
# plt.plot(df.index, df['Temperatura'], label='Temperatūra')
# plt.scatter(filtruojame_df.index, filtruojame_df["Temperatura"], color='red', label='Viršijo slenksti')
# plt.axhline(y=slenkstis, color='gray', linestyle='--', label='Slenkscio verte')
# plt.xlabel('Dienos')
# plt.ylabel('Temperatūros')
# plt.title('Kasdienine temperatura')
# plt.legend()
# plt.show()
#...............................................................................

# Apsirašykite duomenų rinkinį su pirkinių krepšelio prekių ir jų kainų informacija.
# Naudodami NumPy ir Matplotlib:
# Apskaičiuokite bendrą pirkinių krepšelio sumą. Raskite brangiausią ir pigiausią prekę.
# Sudarykite pie diagramą, kurioje rodomi skirtingų prekių dalis bendroje sumoje.



# prekes = np.array(['Obuolys', 'Pienas', 'Sviestas', 'Bananai'])
# kiekis = np.array([3, 2, 4, 5])
# kainos = np.array([1, 1.5, 2.7, 1.5])
# suma = np.dot(kainos, kiekis)
# #suma = kiekis * kainos
#
# print(suma)
#
# brangiausia_preke = prekes[np.argmax(kainos)]
# print(f'Brangiausia prekė: {brangiausia_preke}')
#
# pigiausia_preke = prekes[np.argmin(kainos)]
# print(f'Pigiausia prekė: {pigiausia_preke}')
#
# fig, ax=plt.subplots()
# ax.pie(kiekis * kainos, labels=prekes, autopct='%1.1f%%', startangle=90)
# ax.axis('equal')
#
# plt.title('Prekiu krepselis')
# plt.show()

# Aprašykite duomenų rinkinį, kuriame yra metiniai pardavimų duomenys.
#
# Naudodami NumPy ir Matplotlib:
#     1.Apskaičiuokite metinį pardavimų sumažėjimą procentais kiekvieniems metams.
#     2.Sukurkite linijinę diagramą, kurioje rodomi metiniai pardavimų pokyčiai.
#     3.Naudojant NumPy funkcijas, apskaičiuokite tendencijos liniją, kuri prognozuotų ateities pardavimų pokyčius.
#     4.Atvaizduokite tendencijos liniją kartu su esamais duomenimis.

metai = np.array([2018, 2019, 2020, 2021, 2022])
pardavimai = np.array([50000, 33000, 37000, 29000, 41000])

pardavimu_pokytis = (pardavimai[1:] - pardavimai[:-1]) / pardavimai[:-1] * 100
print(pardavimu_pokytis)

plt.plot(metai[1:], pardavimu_pokytis, marker='o', color='pink')
plt.xlabel('Metai')
plt.ylabel('Pardavimu pokytis')
plt.title('Metiniai pardavimu pokyciai')

tendencija = np.polyfit(metai[1:], pardavimu_pokytis, 1)
prognoze = np.polyval(tendencija, metai[1:])

# Atvaizduojame tendencijos liniją kartu su esamais duomenimis

plt.plot(metai[1:], prognoze, color='red', label='prognoze')
plt.legend()

plt.show()




