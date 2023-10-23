
def calculator():

    ask_name = str(input("Як вас звати?: "))
    number1 = int(input(f"{ask_name} Введіть будь ласка перше число: "))
    number2 = int(input(f"{ask_name} Введіть будь ласка друге число: "))
    symbol = input(f"{ask_name} Введіть будь ласка операцію: *,//,-,+: ")

    if symbol == "+":
        result = number1 + number2
    elif symbol == "-":
        result = number1 - number2
    elif symbol == "*":
        result = number1 * number2
    elif symbol == "//" or symbol == "/" :
        if number2 != 0:
            result = number1 / number2
        else:
            result = 'Помилка, ділити на 0 не можна'
    return result 

print(calculator())


