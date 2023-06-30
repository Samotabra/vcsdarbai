import pandas as pd
from matplotlib import pyplot as plt

# Suskirstykite klientus pagal šalį.
# Atrinkite užsakymus, kurių suma viršija 1000 eurų
# Išfiltruokite užsakymus, kurie buvo pristatyti nuo 2003/9/30 iki 2005/03/15 .
# Išfiltruokite užsakymus, kurių statusas 'Disputed';
# Sukurkite skritulinę diagramą, kurioje būtų pavaizduota klientų skaičiaus pasiskirstymas pagal šalis

#df = pd.read_csv('sales_data_sample.csv', encoding="ISO-8859-1")
# print(df.head(5))

# 1.Suskirstykite klientus pagal šalį.

# group_country = df.groupby('COUNTRY')
# print(group_country)
#
# plt.figure(figsize=(12, 6))
# group_country.size().plot(kind='bar')
# plt.title('salys pagal uzsakyma')
# plt.xlabel('salis')
# plt.ylabel('klientai')
# plt.show()

#2. Atrinkite užsakymus, kurių suma viršija 1000 eurų

# group_by_order = df[df['SALES'] > 1000]
# print(group_by_order)

# df['total'] = df['QUANTITYORDERED'] * df['PRICEEACH']
# group_by_order = df[df['total'] > 5000][['CUSTOMERNAME', 'total']]
# df.to_csv('sales_data_sample.csv', index=False)
# print(group_by_order)

# 3. Išfiltruokite užsakymus, kurie buvo pristatyti nuo 2003/9/30 iki 2005/03/15 .

# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'], format='%d/%m/%Y %H:%M', errors='coerce') #format datos eiliskumas
# datu_filtravimas = df[(df['ORDERDATE'] >= '9/9/2003') & (df['ORDERDATE'] <= '3/3/2005')]
# print(datu_filtravimas)

# kitas budas datos format:
# df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
# start_date = '2003-09-30'
# end_date = '2005-03-15'
# order_date = df[df['ORDERDATE'].between(start_date, end_date)]

#4. Išfiltruokite užsakymus, kurių statusas 'Disputed'

# disputed = df[df['STATUS']=='Disputed']
# print(disputed)

#5(1).Sukurkite skritulinę diagramą, kurioje būtų pavaizduota klientų skaičiaus pasiskirstymas pagal šalis

# group_country = df['COUNTRY'].value_counts().nlargest(5)
#
# plt.bar(group_country.index, group_country.values)
#
# plt.title('salys pagal uzsakyma')
# plt.xlabel('salis')
# plt.ylabel('klientai')
# plt.xticks(rotation=90)
# plt.show()
#__________________________________________________________________________

