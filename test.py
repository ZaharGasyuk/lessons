# import numpy
# a = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# print(numpy.mean(a))


# def s():
#     print('hello world')
# s()
    

# def s(a):
#     print(a)
# s('hello')


# def s(a,b):
#     print(a+b)
# s(10,29)


# def func(a):
#     print(len(a))
# func('hello')


# def func(a,b):
#     return a*b
# print(func(10,20))


# def func():
#     a = int(input('Введіть перше число: '))
#     b = int(input('Введіть друге число: '))
#     return a + b
# print(func())


# a = [1,2,3,4,5]
# def func(my_list):
#     for i in my_list:
#         print(i, end=' ')
# func(a)

# a = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# def middle(my_list):
#     return sum(my_list)/len(my_list)


# def middle1(my_list):
#     y = 0
#     for i in my_list:
#         y += i
#     result = y/len(my_list)
#     return result
# print(middle1(a))
    

# a = [77, 78, 85, 86, 86, 86,            87,             89, 89, 88, 94, 99, 103]


# a = [99,86,89,89,88,111,86,103,89,94,78,77,85,86,87]

# import numpy


# a = [99,86,89,89,88,111,86,     103,        89,94,78,77,85,86,87]

# def function(my_list):
#     my_list.sort()
#     result = len(my_list)//2
#     return float(my_list[result])
# print(function(a))

# print(numpy.median(a))










# 3
# a = 'abcd'
# def func(my_str):
#     for i in my_str:
#         c = str(i[::-1])
#         print(c, end = ' ')
# func(a)


# a= input("Введіть щось: ")
# c = a[::-1]
# print(c)




# 4
# a=input("Введіть щось: ")
# c = a[::-1]
# print(c)
# if a == c:
#     print("Є паліндромом")
# else:
#     print("Не є")
# a = 10

# 5
# def func(a, b):
#     while b:
#        a, b = b, a % b
#         return a
# c = func(50, 175)
# print(f"НСД чисел 87 і 76 є {c}"


# def func():
#     a = int(input('Введіть вік: '))
#     b = input('Введіть ім\'я: ')
#     return f'Привіт {b} вам через {100-a} буде 100 років'
# print(func())
                  

# def func():
#     a = int(input('Введіть число: '))
#     for i in range(1,a+1):
#         if a % i == 0:
#             print(i)
# func()


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# def func(list1, list2):
#     return set([i for i in list1 for z in list2 if i == z])

# print(func(a, b))



# def func():
#     import random
#     a = random.randint(1, 10)

#     ask = int(input('Write your number: '))
#     if ask == a:
#         print('Ви вгадали ')
#     else:
#         print('Ви не вгадали ')


# func()



# def func(length):
#     import string   
#     import random
#     our_password = string.ascii_letters + string.punctuation + string.digits    
#     return "".join(random.choice(our_password) for i in range(length))


# print(func(20))


# def func():
#     import random
#     a = random.randint(1, 100)

#     ask = input('Чи ви вгадали число? ')
#     if ask == 'так':
#         print('Гарно, молодці!')
#     elif ask == 'ні':
#         ask1 = input('Число завелике чи замаленьке ?': )
#         if ask1 == "завелике":
#             pass
#         else: 
#             pass



# def spin_words(sentence):
#     sentence = sentence.split()
#     result = sentence[0], sentence[1][::-1], sentence[2][::-1]
#     return " ".join(result)



# print(spin_words("Hey fellow warriors"))

def spin_words(sentence):
    return sentence[::-1]


spin_words("Hello my name is Zahar")
