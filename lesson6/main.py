# Напишіть програму на Python для перевірки дійсності паролів, які вводять користувачі.
# Перевірка:

# Принаймні 1 літера між [az] і 1 літера між [AZ].
# Принаймні 1 число між [0-9].
# Принаймні 1 символ із [$#@].
# Мінімальна довжина 6 символів.
# Максимальна довжина 16 символів.

# ask_password = input("Створіть пароль :")


# a = 16
# b = float(20)

# if a < b:
#     print("a менше ніж б")
#     if type(a) == float:
#             print("а є float")
#             if type(a) != type(b):
#                 print("Оперуйте однаковими типами даних")
#     elif type(a) == int:
#             print("а є int")
#             if type(a) != type(b):
#                 print("Оперуйте однаковими типами даних")
# elif a > b:
#     print("a більше ніж б")
#     if type(a) == float:
#             print("а є float")
#             if type(a) != type(b):
#                 print("Оперуйте однаковими типами даних")
#     elif type(a) == int:
#             print("а є int")
#             if type(a) != type(b):
#                 print("Оперуйте однаковими типами даних")
# elif a == b:
#     print("а рівне б")
#     if type(a) == float:
#             print("а є float")
#             if type(a) != type(b):
#                 print("Оперуйте однаковими типами даних")
#     elif type(a) == int:
#             print("а є int")
#             if type(a) != type(b):
#                 print("Оперуйте однаковими типами даних")


# name = 'Zahar'
# if len(name) > 10:
#     print("Довжина слова більше ніж 10")
#     if "h" in name:
#         print(f"Буква h є в змінній name, і вона знаходиться на {name.index('h')} індексі")
# elif len(name) < 10:
#     print("Довжина менше")
#     if "h" in name:
#         print(f"Буква h є в змінній name, і вона знаходиться на {name.index('h')} індексі")



# boxers = {
#     'category': {
#         '90+': {
#             'id_1': {
#                 'name': 'Volodymyr Klitchko',
#                 'characteristics': {
#                     'year': 1970,
#                     'height': 180,
#                     'weight': 200,
#                     'hand len': 70,
#                 }   
#             },
#             'id_2': {
#                 'name': 'Anthony Joshua',
#                 'characteristics': {
#                     'year': 1974,
#                     'height': 200,
#                     'weight': 250,
#                     'hand len': 75,
#                 }
#             }
#         }
#     }
# }



# Якщо боксер молодший то ми виводимо, що в нього більше амбіцій але ймовірно менше досвіду
# Якщо боксер легший тоді ми виводимо що він швидший але сила удару менша
# Якщо боксер є вищий то ми виводимо що довжина рук більша
# Якщо нижчий то виводимо що цьому боксеру буде складніше підібратись до опонента


# if boxers['category']['90+']['id_1']['characteristics']['year'] < boxers['category']['90+']['id_2']['characteristics']['year']:
#     boxer_name_id1 = boxers['category']['90+']['id_1']['name']
#     boxer_name_id2 = boxers['category']['90+']['id_2']['name']
#     print(f'{boxer_name_id2} більше амбіцій але ймовірно менше досвіду ніж в {boxer_name_id1}') #Done

# elif boxers['category']['90+']['id_1']['characteristics']['year'] > boxers['category']['90+']['id_2']['characteristics']['year']:
#      boxer_name_id1 = boxers['category']['90+']['id_1']['name']
#      boxer_name_id2 = boxers['category']['90+']['id_2']['name']
#      print(f'{boxer_name_id2} менше амбіцій але ймовірно більше досвіду ніж в {boxer_name_id1}')

# elif boxers['category']['90+']['id_1']['characteristics']['year'] == boxers['category']['90+']['id_2']['characteristics']['year']:
#      boxer_name_id1 = boxers['category']['90+']['id_1']['name']
#      boxer_name_id2 = boxers['category']['90+']['id_2']['name']
#      print(f'{boxer_name_id2} по віку рівний боксеру {boxer_name_id1}')



# if boxers['category']['90+']['id_1']['characteristics']['weight'] > boxers['category']['90+']['id_2']['characteristics']['weight']:
#         print(f'{boxer_name_id2} швидший але сила удару менша ніж {boxer_name_id1} ')  #Done

# elif boxers['category']['90+']['id_1']['characteristics']['weight'] < boxers['category']['90+']['id_2']['characteristics']['weight']:
#         print(f'{boxer_name_id2} повільніший але сила удару більша ніж {boxer_name_id1} ') 

# elif boxers['category']['90+']['id_1']['characteristics']['weight'] == boxers['category']['90+']['id_2']['characteristics']['weight']:
#         print(f'{boxer_name_id2} по вазі рівний боксеру {boxer_name_id1} ') 



# if boxers['category']['90+']['id_1']['characteristics']['hand len'] > boxers['category']['90+']['id_2']['characteristics']['hand len']:
#         print(f'в {boxer_name_id2} довжина рук менша ніж в {boxer_name_id1} ') #Undone #Done

# elif boxers['category']['90+']['id_1']['characteristics']['hand len'] < boxers['category']['90+']['id_2']['characteristics']['hand len']:
#         print(f'в {boxer_name_id2} довжина рук більша ніж в {boxer_name_id1} ')

# elif boxers['category']['90+']['id_1']['characteristics']['hand len'] == boxers['category']['90+']['id_2']['characteristics']['hand len']:
#         print(f'в {boxer_name_id2} довжина рук одинакова з {boxer_name_id1} ')



# if boxers['category']['90+']['id_1']['characteristics']['height'] < boxers['category']['90+']['id_2']['characteristics']['height']:
#         print(f' {boxer_name_id2} буде легше підібратись до {boxer_name_id1} ')  #Undone #Done

# elif boxers['category']['90+']['id_1']['characteristics']['height'] > boxers['category']['90+']['id_2']['characteristics']['height']:
#         print(f' {boxer_name_id2} буде складніше підібратись до {boxer_name_id1} ')

# elif boxers['category']['90+']['id_1']['characteristics']['height'] == boxers['category']['90+']['id_2']['characteristics']['height']:
#         print(f' {boxer_name_id2} рівний по росту {boxer_name_id1} ')
          




# for num in range(1500, 2701):
#        if num % 7 == 0 and num % 5 == 0: 
#               print(num)


# a = input("Введіть слово в нижньому регістрі: ") 
# d = a.upper() 
# print("змінене слово:", d)



# 1. Написати програму, яка приймаєвід вас інпутом інормацію про спортсмена(рік, вага, ріст, розмах рук)
# 2. Цю інформацію ми зберігаємо в словник, а потім ми скоротивши наші умовні оператори до 25 рядків робимо всі умови
# 3. Ваша програма повинна питати, інпут, а коли ви введете всі дані, вона питає чи бажаєте ввести ше одного спортсмена і якшо
# 4. Щоб зупинити введення нажимаєте букву 'q'



# a = input('Write number')
# print(a)
# if a == 'q':
#     print('ПРограма завершилась')

# my_dict = {
#     'name': a,

# }

# a = '100'
# b = '100'

# if type(a) == type(b):
#     print('вони однакового типу даних')
#     if b.isdigit():
#         print('б є цифрою в стрінзі')



# a = 'hello'
# b = '100'


# print(a.isdigit())
# print(b.isdigit())



# a = [1,2,3,4,3,2] #13 #15
# if sum(a) < 15:
#     print(f'сума є менша від 15,сума є меншою на {15-sum(a)}')
# elif sum(a) > 15:
#     print(f'сума є більша від 15, сума є більшою на {sum(a)-15}')
# elif sum(a) == 15:
#     print(f'сума дорівнює 15')
    


#   5. Напишіть функцію, яка долучає квадрат кожного числа в цьому списку до нового списку
#   x = [2,3,4,5,6,7,8]
#   a = []
 
# x = [2,3,4,5,6,7,8]
# a = []

# for i in x:
#     a.append(i*i)
# print(a)

# import math 

# a = [4, 9, 16, 25, 36, 49, 64]
# s = []
# for i in a:
#     s.append(int(math.sqrt(i))) 
# print(s)



# a = ['1', '4', '6', '3', 1000]

# g = [] #суму усіх цифр в стрінзі


# for i in a:
#     if i.isdigit():
#         i = int(i)
#         g.append(i)

# g = sum(g)

# print(g)











# import sys
# print("Версія Python:")
# print(sys.version)


# import datetime
# current_datetime = datetime.datetime.now()
# print("Поточна дата та час:", current_datetime)


# first_name = input("Введіть ім'я: ")
# last_name = input("Введіть прізвище: ")
# full_name_reversed = last_name + " " + first_name
# print("Зворотній порядок імені та прізвища:", full_name_reversed)


# input_string = input("Введіть послідовність чисел, розділених комами: ")
# number_list = input_string.split(',')
# number_list = [int(num.strip()) for num in number_list]
# number_tuple = tuple(number_list)
# print("Список чисел:", number_list)
# print("Кортеж чисел:", number_tuple)


# color_list = ["Red", "Green", "White", "Black"]
# print("Перший колір:", color_list[0])
# print("Останній колір:", color_list[-1])


n = int(input("Введіть ціле число n: "))
nn = n * 2
nnn = n * 3
result = n + nn + nnn
print("Результат обчислення {} + {} + {} = {}".format(n, nn, nnn, result))


# import calendar
# year = int(input("Введіть рік (наприклад, 1941): "))
# month = int(input("Введіть місяць (1-12): "))
# cal = calendar.month(year, month)
# print("Календар на {} рік і {} місяць:".format(year, calendar.month_name[month]))
# print(cal)


# from datetime import date
# f_date = date(2023, 9, 6)
# l_date = date(2008, 9, 27)
# delta = l_date - f_date
# print(delta.days)


# number = float(input("Введіть число: "))
# difference = number - 17
# if difference > 17:
#     result = abs(difference) * 2
# else:
#     result = abs(difference)
# print("Результат:", result)


# number = int(input("Введіть число: "))
# if (100 <= number <= 1000) or (200 <= number <= 2000):
#     print("Число знаходиться в межах 100 до 1000 або 200 до 2000.")
# else:
#     print("Число не знаходиться в заданих межах.")


# num1 = float(input("Введіть перше число: "))
# num2 = float(input("Введіть друге число: "))
# num3 = float(input("Введіть третє число: "))

# sum_of_numbers = num1 + num2 + num3
# if num1 == num2 == num3:
#     result = sum_of_numbers * 3
# else:
#     result = sum_of_numbers
# print("Результат:", result)


# number = int(input("Введіть ціле число: "))

# if number % 2 == 0:
#     print("Число {} є парним.".format(number))
# else:
#     print("Число {} є непарним.".format(number))


# numbers = [1, 4, 9, 6, 3, 4, 7, 2]
# count_of_4 = numbers.count(4)
# print("Число 4 зустрічається в списку {} разів.".format(count_of_4))


# a = input("Введіть букву: ")

# if a.lower() in 'aeiouаеіоу':
#     print("Ця буква є голосною.")
# else:
#     print("Ця буква є приголосною.")


# Значення = [10, 20, 30, 40, 50]

# Чек = int(input("Введіть значення для перевірки: "))
# if Чек in Значення:
#     print("Значення {} міститься в групі значень.".format(Чек))
# else:
#     print("Значення {} не міститься в групі значень.".format(Чек))


# my_list = ["То", "є", "список"]

# result_string = " ".join(my_list)
# print("Результат:", result_string)
# print(type(my_list))


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527 ]

for x in numbers:
    if x == 237:
        break;
    elif x % 2 == 0:
        print(x)