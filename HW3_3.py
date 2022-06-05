# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами

user_name = input('Print your name: ')
user_city = input('Print tour city: ')
user_age = int(input('Print your age: '))
print(f'Hi, my name is {user_name}, i am from {user_city} and i am {user_age} years old')
print("Hi, my name is {}, i am from {} and i am {} years old".format(user_name, user_city, user_age))
print("Hi, my name is %s, i am from %s and i am %d years old" % (user_name, user_city, user_age))
