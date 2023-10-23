
# def calculator():
#     import pyttsx3
#     import speech_recognition

#     r = speech_recognition.Recognizer()

#     name = 'Zahar'

#     with speech_recognition.Microphone() as source:
#         print("Скажіть перше число: ")
#         number1 = r.listen(source) # в цій змінній зберігаємо те що ви сказали
#         text_number1 = r.recognize_google(number1) # а в цю змінну переводимо те що ви сказали в текст
#         print(text_number1)

#     with speech_recognition.Microphone() as source:
#         print("Скажіть друге число: ")
#         number2 = r.listen(source)
#         text_number2 = r.recognize_google(number2)
#         print(text_number2)

#     with speech_recognition.Microphone() as source:
#         print("Скажіть символ: ")
#         symbol = r.listen(source)
#         text_symbol = r.recognize_google(symbol)
#         print(text_symbol)

#     engine = pyttsx3.init()

#     if text_symbol == 'hi':
#         result = int(text_number1) - int(text_number2)
#         engine.say(f"{name}, Your result is : {result}")
#         engine.runAndWait()


#     if text_symbol == 'Plus':
#         result = int(text_number1) + int(text_number2)
#         engine.say(f"{name}, Your result is : {result}")
#         engine.runAndWait()


#     if text_symbol == 'hello':
#         result = int(text_number1) * int(text_number2)
#         engine.say(f"{name}, Your result is : {result}")
#         engine.runAndWait()


#     if text_symbol == 'bus':
#         result = int(text_number1) // int(text_number2)
#         engine.say(f"{name}, Your result is : {result}")
#         engine.runAndWait()

# calculator()


# name = 'Zahar'
# age = 15

# print("Hello, my name is", name)
# print("Hello, my name is {}".format(name))
# print(f"Hello, my name is {name}")


