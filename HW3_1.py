# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

numbers = 'one two three'
print(numbers.replace(' ', '-'))

numbers = 'one two three'
new_numbers = numbers.split(' ')
print('-'.join(new_numbers))
