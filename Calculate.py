#
#
#
# # import colorama
#
# class Calculator:
#     def __init__(self):
#         self.result = 5
#
#     def sudetis(self, skaicius):
#         self.result += skaicius
#
#     def atimtis(self, skaicius):
#         self.result -= skaicius
#
#     def daugyba(self, skaicius):
#         self.result *= skaicius
#
#     def dalyba(self, skaicius):
#         if skaicius != 0:
#             self.result /= skaicius
#         else:
#             print("Dalyba is nulio negalima")
#
#
#     def isvalyti(self):
#         self.rezult = 0
#
#         # kadangi nera print, get - gauna reiksme, set - nustato reiksme
#
#     def get_result(self):
#         return self.result
#
#
# Skaiciuoklis = Calculator()
# while True:
#     print("Pasirinkite norima veiksma_> ")
#     print("1. Sudetis")
#     print("2. Atimtis")
#     print("3. Daugyba")
#     print("4. Dalyba")
#     print("5. Isvalyti")
#     pasirinkimas = input("Iveskite pasirinkimo numeri_> ")
#
#     if pasirinkimas == "1":
#         skaicius = int(input("Iveskite skaiciu_> "))
#         Skaiciuoklis.sudetis(skaicius)
#
#
#
#     elif pasirinkimas == "2":
#         skaicius = int(input("Iveskite skaiciu_> "))
#         Skaiciuoklis.atimtis(skaicius)
#
#     elif pasirinkimas == "3":
#         skaicius = int(input("Iveskite skaiciu_> "))
#         Skaiciuoklis.daugyba(skaicius)
#
#     elif pasirinkimas == "4":
#         skaicius = float(input("Iveskite skaiciu_> "))
#         Skaiciuoklis.dalyba(skaicius)
#
#     elif pasirinkimas == "5":
#         skaicius = int(input("Iveskite skaiciu --_> "))
#         Skaiciuoklis.isvalyti()
#
#     else:
#         print("Neteisingas pasirinkimas, bandykite dar karta")
#
#
#     print("result: ", Skaiciuoklis.get_result())
#     print()


#06-16  ..........................................

# metodo perrasymas

# class Animal:
#     def make_sound(self, name):
#         self.name = name
#         print("The animal makes a sound")
#
#
# class Dog(Animal):
#     def make_sound(self):
#         print("The dog barks")
#
#
# dog = Dog()
# dog.make_sound()
#......................................................

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#
#
#     def start_engine(self):
#         print("Engine started!")
#
#     def stop_engine(self):
#         print("Engine stopped!")
#
#
# class Car(Vehicle):
#
#     def drive(self):
#         print("Car ir driving!")
#
# car = Car("Toyota")
# print(car.brand)
# car.start_engine()
# car.drive()
# car.stop_engine()

#..............................................................................

#sukurti Tevine klase zmogus ...
# class Zmogus:
#     def __init__ (self, name, age):     #isvardinam savybes
#         self.name = name                #aprasome savybes
#         self.age = age
#
#     def display_info(self):                         #metodas rodyti info apie zmogu
#         print(f"zmogaus vardas yra {self.name}")
#         print(f"zmogaus amzius yra {self.age}")
#
# class Darbuotojas (Zmogus):                      #sukuriame vaikine klase (inheritance)
#     def __init__ (self, name, age, salary):      #isvardiname kokias savybes tures darbuotojas
#         super().__init__(name, age)              #nurodome, kurias savybes tures is Zmogus klases
#         self.salary = salary                     #aprasome papildoma darbuotojo savybe
#
#     def display_info(self):
#         super().display_info()                   #panaudosiu Tevines klases metoda, print vardas, amzius
#         print(f"darbuotojo atlyginimas yra {self.salary}")
#
# zmogus = Zmogus("Antanukas", 12)                 #sukuriame Tevines klases objekta
# darbuotojas = Darbuotojas("Jonukas", 25, 2000)   #sukuriame vaikines klases objekta
#
# zmogus.display_info()
# print()
# darbuotojas.display_info()

#.........................................................................

#sukurti pirkiniu krepselio funkcionaluma: turim produkta ir krepseli

# class Product:
#     def __init__ (self, title, price):
#         self.title = title
#         self.price = price
#
#     def display_info(self):
#         print(f"produkto pavadinimas yra {self.title}")
#         print(f"produkto kaina {self.price} $")
#
# class ShoppingCart(Product):
#     def __init__ (self):
#         super().__init__(title=None, price=None)
#         self.product = []
#
#     def add_product(self, product):
#         self.product.append(product)
#         print(f" produktas {product.title} pridetas i krepseli ")
#
#     def remove_product(self, product):
#         if product in self.product:
#             self.product.remove(product)
#             print(f" produktas {product.title} pasalintas is krepselio ")
#         else:
#             print(f"produktas {product.title} nerastas")
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.product:
#             total_price += product.price
#         return total_price
#
# class DiscountedProduct(Product):
#     def __init__ (self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage = discount_percentage
#
#     def calculate_discount_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100)
#         discounted_price = self.price - discount_amount
#         return discounted_price
#
#     def display_info(self):
#         super().display_info()
#         print(f"nuolaida {self.discount_percentage} %")
#         print(f"galutine kaina {self.calculate_discount_price()} $")
#
# produktas = Product("Pienas", 2.99)
# produktas1 = DiscountedProduct("Obuolys", 2.99, 15)
# produktas2 = Product("Sviestas", 4.99)
#
# shoppingcart = ShoppingCart()
# shoppingcart.add_product(produktas)
# shoppingcart.add_product(produktas1)
# shoppingcart.add_product(produktas2)
# print()
# for product in shoppingcart.product:
#     product.display_info()
#     print()
#
# total_price = shoppingcart.calculate_total_price()
# print(f"Bendra kaina {total_price} $")
# print()
#
# shoppingcart.remove_product(produktas)
#
# total_price = shoppingcart.calculate_total_price()
# print(f"Nauja bendra kaina {total_price} $")
# print()


#.............................................................................

# import random
# import time
# studentai = ["Rugile", "Egidijus", "Deividas", "Tomas", "Migle", "SauliusS", "SauliusA", "Ausrine", "Mantas", "Vaidas",
#              "Jurate", "Modestas"]
# random_student = random.choice(studentai)
# time.sleep(3)
# print("Atsitiktinai parinktas studentas: ", random_student)

#................................................................................

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#     def set_name(self, name):
#         self.name = name
#
#
#     def get_age(self):
#         return self.age
#     def set_age(self, age):
#         if age >= 0:
#            self.age = age
#         else:
#             print("Amzius negali buti neigiamas")
#
# person = Person("Jonas", 15)
#
# print("name", person.get_name())
# print("age", person.get_age())
#
#
# person.set_name("Petras")
# person.set_age(-12)
#
# print("new name", person.get_name())
# print("new age", person.get_age())



