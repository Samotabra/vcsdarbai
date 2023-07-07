# # 1. Parašykite funkciją, kuri priima tekstą ir grąžina žodžius, kurie pasikartoja daugiau nei vieną kartą. Papildoma
# # sąlyga žodžius turi grąžinti sąraše.
#
# # def pasikartojantys_zodziai(tekstas):
# #     zodziai = tekstas.split()
# #     sarasas = []
# #
# #     for zodis in set(zodziai):
# #         if zodziai.count(zodis) > 1:
# #             sarasas.append(zodis)
# #
# #     return sarasas
# #
# # tekstas1 = "Labas rytas, Laba diena, Labas vakaras"
# # print(pasikartojantys_zodziai(tekstas1))
#
# # 1.1 2 var. (ivesti teksta vartotojui)
#
# def pasikartojantys_zodziai():
#     tekstas = input('Iveskite teksta: ')
#     zodziai = tekstas.split()
#     sarasas = []
#
#     for zodis in set(zodziai):
#         if zodziai.count(zodis) > 1:
#             sarasas.append(zodis)
#
#     return sarasas
#
# print(pasikartojantys_zodziai())
#
# # 2. 2.Parašykite funkciją, kuri nuskaito tekstiniame faile esančius žodžius ir grąžina juos surikiuotus pagal abėcėlę.
# # tekstas:"Data science is a fantastic career with a tonne of potential for future growth. Already, there is a lot of
# # demand, competitive pay, and several benefits.
# #     Companies are actively looking for data scientists that can glean valuable information from massive amounts of
# #     data."
#
# def surikiuoti_zodziai(failo_pavadinimas):
#     with open(failo_pavadinimas, 'r', encoding="utf8") as file:
#         content = file.read()
#         text = content.split()
#         sorting = sorted(text)
#
#     return sorting
#
# failas = "tekstinis_failas.txt"
# print(surikiuoti_zodziai(failas))
#
# # .....................................
#
# # 3. Padaryti TO DO list aplikacija
#
# def menu():
#     print('1. Add task')
#     print('2. View tasks')
#     print('3. Mark task as completed')
#     print('4. Remove task')
#     print('5. Exit')
#
# def add_task(todo_list):
#     task = input('Enter task description: ')
#     todo_list.append({'task': task, 'completed': False})
#     print('Task added successfully!')
#
# def view_task(todo_list):
#     if not todo_list:
#         print('your todo list is empty')
#     else:
#         print('Your todo list: ')
#         for index, task in enumerate(todo_list, start=1):
#             status = '✓' if task['completed'] else ' '
#             print(f"{index}. [{status} {task['task']}")
#
# def mark_completed(todo_list):
#     view_task(todo_list)
#     task_number = int(input('Enter a number of the task you want to mark as completed: ')) - 1
#     if 0 <= task_number < len(todo_list):
#         todo_list[task_number]['completed'] = True
#         print('Task marked as completed!')
#     else:
#         print('Invalid task number')
#
# def remove_task(todo_list):
#     view_task(todo_list)
#     task_number = int(input('Enter a number of the task you want to remove: ')) - 1
#     if 0 <= task_number < len(todo_list):
#         removed_task = todo_list.pop(task_number)
#         print(f"Your task '{remove_task['task']}' was remove!")
#     else:
#         print('Invalid task number')
#
# def main():
#     todo_list = []
#     while True:
#         menu()
#         choise = input('Enter your choise (1-5): ')
#         if choise == "1":
#             task = add_task(todo_list)
#
#         elif choise == "2":
#             view_task(todo_list)
#
#         elif choise == "3":
#             mark_completed(todo_list)
#
#         elif choise == "4":
#             remove_task(todo_list)
#
#         elif choise == "5":
#             print('Exiting todo list app. Good bye!')
#             break
#
#         else:
#             print('Wrong input!')
#
# if __name__ == '__main__':
#     main()

# 4. Ivesti duomenis apie studentus

import pandas as pd

# def studento_duomenu_ivedimas():
#     student_data = pd.DataFrame(columns=['name', 'age', 'grade'])
#     while True:
#         student_name = input("Iveskite studento varda(or 'quit' to exit):")
#         if student_name.lower() == 'quit':
#             break
#         student_age = int(input("Iveskite studento amziu"))
#         student_grade = int(input("Iveskite studento pazymi"))
#
#         student_data = pd.concat([student_data, pd.DataFrame({'name': [student_name], 'age': [student_age], 'grade': [student_grade]
# })])
#
#     print('\nStudent list\n')
#     print(student_data)
#     avg_age = student_data['age'].astype(int).mean()
#     avg_grade = student_data['grade'].astype(int).mean()
#     print('\n Aerage age: ', avg_age)
#     print('\n Aerage grade: ', avg_grade)
#
#     sorted_data = student_data.sort_values(by='grade', ascending=False)
#     print('\n Student list sorted by grade:\n')
#     print(sorted_data)
#
#  studento_duomenu_ivedimas()

# 5. password generating

# import string
# import random
#
# def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
#     chars = ''
#     if include_uppercase:
#         chars += string.ascii_uppercase
#     if include_lowercase:
#         chars += string.ascii_lowercase
#     if include_numbers:
#         chars += string.digits
#     if include_special_chars:
#         chars += string.punctuation
#
#     if not chars:
#         print('Error: No character type selected for the password')
#         return None
#     password = ''.join(random.choice(chars) for _ in range(length))
#     return password
#
# def main():
#     print('Welcome to the PASSWORD GENERATOR!')
#     length = int(input('Enter the length of password: '))
#     include_uppercase = input('Include uppercase letters?(y/n): ').lower() == 'y'
#     include_lowercase = input('Include lowercase letters?(y/n): ').lower() == 'y'
#     include_numbers = input('Include numbers?(y/n): ').lower() == 'y'
#     include_special_chars = input('Include special chars?(y/n): ').lower() == 'y'
#
#     password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
#     if password:
#         print('Generate_password', password)
#
# if __name__ == "__main__":
#     main()







