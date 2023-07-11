import pandas as pd


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

df = pd.read_csv("elektra1.csv", sep=';', encoding="utf-8")
# sep=';', sep=',', sep='\t'
print(df)

# selected_columns = df[['Elektromobilio kategorija', 'IŠ VISO']]
# print(selected_columns)


