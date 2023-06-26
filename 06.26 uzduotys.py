import pandas as pd
from matplotlib import pyplot as plt

#employees.csv
# * Apskaičiuoti vidurkį, sumą, minimumą, maksimumą ir kitus statistinius rodiklius stulpeliuose arba grupėse
#naudojant mean(), sum(), min(), max() ir kitas funkcijas.

df = pd.read_csv('employees.csv')
print(df.head(10))


group_sizes = df.groupby('FIRST_NAME').size()
# print(group_sizes)

group_average = df.groupby('FIRST_NAME')['EMPLOYEE_ID'].mean()
# print(group_average)

group_max = df.groupby('FIRST_NAME')['EMPLOYEE_ID'].max()
# print(group_max)



