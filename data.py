import pandas as pd
from matplotlib import pyplot as plt

# vienmate duomenu struktura, kuri saugo vienos eilutes duomenis su indeksais
# data = pd.Series([10, 20, 30, 40, 50])
# print(data)


# Dvimate duomenu struktura, kuri saugo duomenis lenteles pavidalu su stulpeliu ir eiluciu indeksais

# data = {
#         'Name': ['Mantas','Deividas','Migle', 'Ausrine'],
#         'Age': [29, 27, 24, 45],
#         'City': ['Marijampole', 'Vilnius', 'Kaunas', 'Vilnius']
#         }

------------------------------------------------------------------------
# df = pd.DataFrame(data)               # df - data frame (lentele)
# print(df)

# Atvaizduojame pirmas 4 eilutes DataFrame

# print(df.head(3))

# selected_columns = df[['Name', 'City']]
# print(selected_columns)

# prideti nauja stulpeli

# df['Salary'] = [1600, 1400, 1300, 1200]
# print(df)

# grupuokime duomenis pagal miesta ir gaukime vidutini atlyginima

# average_salary_by_city = df.groupby('City')['Salary'].mean()
# # print(average_salary_by_city)
# mean() naudojama apskaiciuoti vidurki
# average_age = df['Age'].mean()
# print(f"Average age: {average_age}")

# filtered_data = df[df['Age'] > 25][['Name', 'Age']]
# print(filtered_data)

# df = pd.read_csv('employees.csv')
# # print(df.head(5))
#
# # grupuoti pagal 'first_name' stulpeli ir suskaiciuoti jo dydi
#
# group_sizes = df.groupby('FIRST_NAME').size()
# print(group_sizes)

# group_average = df.groupby('FIRST_NAME')['SALARY'].mean()
# # print(group_average)
#
# group_stats = df.groupby('FIRST_NAME')['SALARY'].describe()
# # print(group_stats)
#
# group_max = df.groupby('FIRST_NAME')['SALARY'].max()
# # print(group_max)
#
# group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', 'max']})
# print(group_agg)

# atvaizduojama linijine diagrama
# group_agg.plot(kind='bar', figsize=(8, 4))
# # pridedamos diagramos antrastes
# plt.title('Suvestines statistika pagal vardus ir ju atlyginimus')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')

# atvaizduojama diagrama
# plt.show()
------------------------------------------------------------------------




