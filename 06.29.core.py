import numpy as np
import matplotlib.pyplot as plt
#
# # sukuriame np array (Masyva)
#
# # arr = np.array([1, 2, 3])
# # arr2 = np.array([4, 5, 6])
# # result = arr + arr2
# #
# # print(result)
#
# #kelimas kvadratu
#arr = np.array([1, 2, 3, 4, 5])
# #result = np.square(arr)
#
# #indeksavimas
# #value = arr[1]
# #print(value)
#
# # array slicing
# # sliced_arr = arr[1:4]
# # print(sliced_arr)
#
# # sliced_arr = arr[:3] #rodo pirmas tris reiksmes
# # print(sliced_arr)
#
# # sliced_arr = arr[3:] #reiksmes po 3 (4 ir 5)
# # print(sliced_arr)
#
# matrica = np.array([[1,2,3], [4,5,6], [7,8,9]])
# matrica2 = np.array([[10,11,12], [13,14,15], [16,17,18]])
#
# daugyba = np.dot(matrica, matrica2)
# print(daugyba)
# #daugyba [0,0] = (1*10) + (2*13) + (3*16) = 84
#
# random_numbers = np.random.randint(0,10, size=5)
# print(random_numbers)

# numbers = np.linspace(0,1,5)
# print(numbers)
#
# sequence = np.arange(10)
# print(sequence)

# x = np.linspace(0,10,100)
# y = np.sin(x)
#
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sinusine funkcija')
# plt.show()

# x = np.random.rand(100)
# y = np.random.rand(100)
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Random points')
# plt.show()

#data = np.random.randn(1000)

# plt.hist(data, bins=20)
# plt.xlabel('Values')
# plt.ylabel('Freguency')
# plt.title('Histogram')
# plt.show()

# masyvas = np.array([1, 2, 3, 4, 5])
# daugiau_uz_du = masyvas[masyvas > 2]
# print(daugiau_uz_du)

# masyvas = np.array([1, 2, 3, 4, 5])
# daugiau_uz_du = np.where(masyvas > 2)
# print(daugiau_uz_du)

# arr1 = np.array([True,False,True])
# arr2 = np.array([False,True,True])
# result = np.logical_and(arr1, arr2)
# print(result)

# arr = np.array([1, 2, 3, 4, 5, 6])
# change_arr = np.reshape(arr, (2, 3))  # i dvi dalis po 3 skaicius
# print(change_arr)

# arr = np.array([1, 2, 3, 4, 5, 6])
# splitting = np.split(arr, 3)  # padalino i tris dalis
# print(splitting)

# arr = np.array([4, 3, 2, 1, 6, 5])
# sorting = np.sort(arr)

# arr = np.array([4, 3, 2, 1, 6, 5, 4, 2, 1, 5, 10, 15])
# unique = np.unique(arr)
# print(unique)
#.................................................................
# #duomenu sarasas su akciju kainu reiksmemis
# akcijos = np.array([100, 110, 120, 115, 105, 95, 105, 100])
#
# #apskaiciuojame dienos pelna ir nuostoli
# dienos_pelnas = akcijos[1:] - akcijos[:-1]
# dienos_nuostolis = akcijos[:-1] - akcijos[1:]
#
# #randame diena su didziausia ir maziausia akciju kaina
# didziausia_reiksme = np.max(akcijos)
# didziausia_reiksme_indeksas = np.argmax(akcijos)
# maziausia_reiksme = np.min(akcijos)
# maziausios_reiksmes_indeksas = np.argmin(akcijos)
#
# # apskaiciuoti akciju kainos svyravimus
# kainos_svyravimas = np.ptp(akcijos)
#
# print(f'Dienos pelnas: {dienos_pelnas}')
# print(f'Dienos nuostolis: {dienos_nuostolis}')
# print(f'Didziausia akciju kaina: {didziausia_reiksme}, diena: {didziausia_reiksme_indeksas +1}')
# print(f'maziausia akciju kaina: {maziausia_reiksme}, diena: {maziausios_reiksmes_indeksas +1}')
#
# print(f'Akciju kainos svyravimas: {kainos_svyravimas}')

