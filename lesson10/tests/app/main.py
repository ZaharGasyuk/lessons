def func(text):
    return text.upper()


def square(b):
    return str(b*b)


def calc(number1, number2, symbol):
    if symbol == '+':
        result = number1 + number2
    elif symbol == '-':
        result = number1 - number2
    elif symbol == '*':
        result = number1 * number2
    elif symbol == '//':
        result = number1 // number2
    else:
        return 'mistake'
    return result


def square(b):
    return str(b*b)


def sum_of_digits(n):
    return sum(int(i) for i in str(n))


# def is_primes(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def reverse_string(s):
    return s[::-1]


def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if primes(num):
            primes.append(num)
        num += 1
    return primes


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


list_ = (1, 2, 3, 4, 5)


def multiply_list_elements(lst):
    result = 1
    for elem in lst:
        result *= elem
    return result


a = (9)
b = (5)
c = (7)


def max_of_three(a, b, c):
    return max(a, b, c)


a = (9)
b = (5)
c = (7)


def min_of_three(a, b, c):
    return min(a, b, c)


a = ('car', 2, 3)


def length_of_string(s):
    return len(s)


b = {10, 20, 'v', 20}


def unique_elements(lst):
    return list(set(lst))


c = ('car')


def vowel_count(s):
    return sum(1 for char in s if char in "aeiouAEIOU")


d = ('auto')


def consonant_count(s):
    return sum(1 for char in s if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")


e = ('auto')


def title_case(s):
    return s.title()


def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))


def square_of_sums(n):
    return sum(range(1, n+1))**2


def convert_to_binary(n):
    return bin(n)[2:]


def convert_to_octal(n):
    return oct(n)[2:]


def convert_to_hex(n):
    return hex(n)[2:]


def char_count(s, char):
    return s.count(char)


def replace_vowels(s, char):
    for vowel in "aeiouAEIOU":
        s = s.replace(vowel, char)
    return s


def sum_of_list(lst):
    return sum(lst)


t = (1, 2, 3, 4, 5)


def average_of_list(lst):
    return sum(lst) / len(lst) if lst else 0


k = ('car', 'auto')


def longest_string(strings):
    return max(strings, key=len, default="")


s = ('car', 'auto')


def shortest_string(strings):
    return min(strings, key=len, default="")


def is_substring(sub, s):
    return sub in s


def greet(name):
    return f"Hello, {name}!"


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def starts_with_vowel(s):
    return s[0].lower() in "aeiou" if s else False


def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)


def sum_of_evens(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)


def count_occurrences(lst):
    return {i: lst.count(i) for i in set(lst)}


h = (1, 2, 3, 4, 5)


def list_to_tuple(lst):
    return tuple(lst)


h = [1, 2, 3, 4, 5]


def tuple_to_list(tpl):
    return list(tpl)


my_dict = {'car': 1, 'auto': 2}


def dict_keys(dct):
    return list(dct.keys())


my_dictionary = {'car': 1, 'auto': 2}


def dict_values(dct):
    return list(dct.values())


my_dictionary1 = {'car': 1, 'auto': 2}
my_dictionary2 = {'dodge': 3, 'BMW': 4}


def merge_dicts(dct1, dct2):
    merged = dct1.copy()
    merged.update(dct2)
    return merged


n = (1, 2, 3, 4, 5)


def filter_odds(lst):
    return [i for i in lst if i % 2 != 0]


n = (1, 2, 3, 4, 5)


def filter_evens(lst):
    return [i for i in lst if i % 2 == 0]
