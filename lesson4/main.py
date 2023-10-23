# a = [1,2,3,4]
# a.append(5)
# a.insert(0,1)
# y = a.pop(-1)
# a.remove()
# print(a[::-1])

# b = (1,2,2,2,2,2,2,2,2,3,True,4, True, 5)
# print(b.index(4)) # 4
# print(b.count(2)) 

# b = ('Zahar', 'Ivan', 'Nazar')
# b = list(b)

# b.pop(1)
# # b.remove('Ivan')

# print(b)
# b = tuple(b)
# print(b)

# b = ('Zahar', 'Ivan', 'Nazar')
# c = tuple([i for i in b if i != 'Ivan'])
# print(c)

# a: list[int] = [1,2,3,4,5]
# b = []

# for element in a:
#     b.append(element)

# b = [element for element in a if element % 2 == 0]

# print(b)

# a = [i for i in range(1,101,10)]
# print(a)


# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)

# my_set = {1,2,3,4,5,5,5, True, 'Hello', (1,2,3,4,5)} # unordered, can not have dublicates
# print(type(my_set))

# print(my_set)


# a = {1,2,3, (1,2,3)}

# a.add('dkjfbndkjfdfdf')
# print(a)














# mytuple = ("banana", "apple", "cherry", 3, "melon")
# print(mytuple)


# myset = {1,2,3,4,'hello'}
# print(myset)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# a = set(mytuple)
# print(type(a))
# print(a)


# myset = {1,2,3,4,'hello'}
# a = tuple(myset)
# print(type(a))
# print(a)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# a = set(mytuple)
# print(type(a))
# print(a)
# b = tuple(a)
# print(b)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# a = mytuple[2]
# print(a)


# myset = {1,2,3,4,'hello'}
# myset.add(8)
# print(myset)
# myset.remove(4)
# print(myset)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# i = 3
# if i in mytuple:
#     print("є")
# else:
#     print("німа")


# myset = {1,2,3,4,'hello'}
# i = 99
# if i in myset:
#     print("є")
# else:
#     print("німа")


# set1 = {1,2,3,4,5}
# set2 = {6,7,8,9,10}
# a = set1.union(set2)
# print(a)


# x = {1,4,7,9}
# y = {2,4,5,7,8}
# z = x.intersection(y)
# print(z)


# x = {1,4,6,9}
# y = {2,4,5,7,8,9}
# z = x.difference(y)
# print(z)


# x = {1,4,7,9}
# y = {2,4,5,7,8}
# z = x.symmetric_difference(y)
# print(z)


# x = {1,4,7,9}
# y = {2,4,5,7,8}
# z = x.issubset(y)
# print(z)


# mytuple = (("banana", "apple", "cherry", 3, "melon"),(5,7),(9,9))
# print(mytuple)


# x = frozenset({1,4,7,9})
# y = frozenset({2,4,5,7,8})
# a = {x,y}
# print(a)


# x = {1,4,7,9}
# x.clear()
# print(x)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# a = len(mytuple)
# print(a)


# x = {1,4,7,9}
# a = len(x)
# print(a)


# a: list[int] = set([i for i in range (1, 51)])
# b = []

# for element in a:
#     b.append(element)

# b = [element for element in a if element % 2 != 0]

# print(b)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# if not mytuple:
#     print("є пустим")
# else:
#     print("не є")


# myset = {1,2,3,4,'hello'}
# if not myset:
#     print("є")
# else:
#     print("не є")


# mytuple = ([1,2,3],{4,5,6})
# print(mytuple)


# mytuple = ()
# list1 = [1,2,3]
# set1 = {4,5,6}
# mytuple = (list1,set1)
# print(mytuple)


# myset = {1,2,3,4,5,6,7, False, 'Hello', (8,9,10,'hi')}
# print(myset)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# f = mytuple[0]
# l = mytuple[-1]
# print("F:",f)
# print("L",l)


# mytuple = ("banana", "apple", "cherry", 3, "melon")
# mytuple2 = (1,2,3,4,4,5)
# a = mytuple + mytuple2
# print(a)


# x = {1,4,7,9}
# y = {2,4,5,7,8}
# z = x.issubset(y)
# print(z)
















# my_school = {
#     "adress": "K.N.Olgy",
#     "number": 31,
#     "capacity": 800
# }

# question = int(input("Скільки додати учнів до вашої школи?: "))
# my_school["capacity"] += question

# if my_school["capacity"] > 850:
#     print("В нашій школі недостатньо місць")
#     my_school["school_need"] = "Потребуємо додаткових місць"
#     print(f'Зменшіть кількість на {my_school["capacity"] - 800} або добудуйте додаткові корпуси')


# print(my_school)


# data = {}

# name = str(input('Як вас звати ?: '))
# lastname = str(input('Яке ваше прізвище ?: '))
# age = str(input('Скільки вам років ?: '))

# data['name'] = name

# print(data)


# if else elif



# a = 12
# b = 20

# if a < b and a > 12:
#     print('Наша змінна a є меншою ніж змінна b')    
# elif a > b and a < 100:
#     print('Наша змінна a є більшою ніж змінна b')
# elif a == b:
#     print('Наша змінна a є рівна b')
# else:
#     print("HA HA")


# a = 1
# b = 3

# # if a == 1 or b == 2:
# #     print('hello')


# print('hello') if a == 1 or b == 2













# dict = {0:634, 6:634}
# dict.update({2:30})
# print(dict)


# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# dict4 = {}
# for i in (dict1, dict2, dict3): dict4.update(i)
# print(dict4)


# dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(sup):
#   if sup in dict:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present(7)


# valera=int(input("Input a number "))
# petro = dict()

# for i in range(1,valera+1):
#     petro[i]=i*i

# print(petro)


# dictor=dict()
# for sup in range(1,16):
#     dictor[sup]=sup**2
# print(dictor)


# dict1 = {'b': 100, 'c': 200}
# dict2 = {'s': 300, 'y': 200}
# dictor = dict1.copy()
# dictor.update(dict2)
# print(dictor)


# my_dictionary  = {'hello':13654,'hi':-54,'bye':247}
# result=1
# for key in my_dictionary:    
#     result=result * my_dictionary[key]

# print(result)


# dictionary = {'a':1,'b':2,'c':3,'d':4}
# if 'a' in dictionary: 
#     del dictionary['c']
# print(dictionary)


# models = ['M5', 'E63', 'RS7']
# car = ['BMW','Mercedes','Audi']
# mix = dict(zip(models, car))
# print(mix)


# dictionary = {}

# if not bool(dictionary):
#     print("Dictionary is empty")

	
