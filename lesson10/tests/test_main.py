from app.main import *

def test_func_func():
    a = 'hello world'
    assert func(a) == 'HELLO WORLD'


def test_function_square():
    assert square(10) == str(100)


def test_calc_sum_calc():
    assert calc(10, 10, '+') == 20


def test_calc_min_calc():
    assert calc(10, 10, '-') == 0


def test_calc_mult_calc():
    assert calc(10, 10, '*') == 100


def test_calc_div_calc():
    assert calc(10, 10, '//') == 1


def test_calc_mistake_calc():
    assert calc(10, 10, '5') == 'mistake'


def test_function_square():
    assert square(10) == str(100)


def test_func_sum_of_digits():
    assert sum_of_digits(56)


# def test_function_is_prime():
#     assert is_primes(10) == False


def test_func_tion_factorial():
    assert factorial(0) == 1


def test_func_tion__reverse_string():
    a = 'car'
    assert reverse_string(a) == 'rac'


# def test_func_tions_first_n_primes():
#     assert first_n_primes(2) == 3


def test_func_tions_first_n_primess():
    assert is_prime(3) == True 


def test_func_tionss_multiply_list_elements():
    assert multiply_list_elements(list_) == 1 * 2 * 3 * 4 * 5


def test_func_tionss_max_of_three():
    assert max_of_three(9, 5, 7) == 9


def test_func_tionss_min_of_three():
    assert min_of_three(9, 5, 7) == 5


def test_func_tionss_length_of_string():
    assert length_of_string(a) == 3


def test_func_tionss_tuple():
    assert tuple([10, 20, 'v']) == (10, 20, 'v')


def test_func_tionsss_vowel_count():
    assert vowel_count(c) == 1


def test_func_tionssss_consonant_count():
    assert consonant_count(d) == 1


def test_func_tionssss1_title_case():
    assert title_case(e) == 'Auto'


def test_func_tionssss2_sum_of_squares():
    assert sum_of_squares(3) == 14


def test_func_square_of_sums_square_of_sums():
    assert square_of_sums(3) == 36


def test_func_tionssss_convert_to_binary():
    assert convert_to_binary(5) == '101'


def test_func_tionssss_convert_to_octal():
    assert convert_to_octal(2) == '2'


def test_func_tionssss_convert_to_hex():
    assert convert_to_hex(4) == '4'


def test_func_tionssss_char_count():
    assert char_count('car', 'a') == 1


def test_func_tionssss_replace_vowels():
    assert replace_vowels('car', 'd') == 'cdr'


def test_func_tionssss_sum_of_list():
    k = [1, 2, 3, 4, 5, 6, 7]
    assert sum_of_list(k) == 28


def test_func_tionssss_average_of_list():
    assert average_of_list(t) == 3


def test_func_tionssss_longest_string():
    assert longest_string(k) == 'auto'


def test_func_tionssss_shortest_string():
    assert shortest_string(s) == 'car'


def test_func_tionssss_is_substring():
    assert is_substring('car', 'car') == True


def test_func_tionssss_greet():
    assert greet('world') == "Hello, world!"


def test_func_tionssss_is_anagram():
    assert is_anagram('car', 'auto') == False


def test_func_tionssss_starts_with_vowel():
    assert starts_with_vowel('state') == False


def test_func_tionssss_sum_of_odds():
    assert sum_of_odds(2) == 1


def test_func_tionssss_sum_of_evens():
    assert sum_of_evens(2) == 2


def test_func_tionssss_count_occurrences():
    assert count_occurrences('car') == {'a': 1, 'c': 1, 'r': 1}


def test_func_tionssss_list_to_tuple():
    assert list_to_tuple(h) == (1, 2, 3, 4, 5)


def test_func_tionssss_tuple_to_list():
    assert tuple_to_list(h) == [1, 2, 3, 4, 5]


def test_func_tionssss_dict_keys():
    assert dict_keys(my_dict) == ['car', 'auto']


def test_func_tionssss_dict_values():
    assert dict_values(my_dictionary) == [1, 2]


def test_func_tionssss_merge_dicts():
    assert merge_dicts(my_dictionary1, my_dictionary2) == {
        'car': 1, 'auto': 2, 'dodge': 3, 'BMW': 4}


def test_func_tionssss_filter_odds():
    assert filter_odds(n) == [1, 3, 5]


def test_func_tionss_filter_evens():
    assert filter_evens(n) == [2, 4]
