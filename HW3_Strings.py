import re
password = input('Enter your password: ')
print(password)
if len(password) < 5:
    print(f'Incorrect password, length should be more then 5 symbols')
if '@' not in password and '#' not in password and '%' not in password and '&' not in password:
    print(f'Incorrect password, it should be at least one of this symbols: @, #, %, &')
if not re.search('[0-9]', password):
    print(f'Incorrect password, it should be numbers 0-9')
if not re.search('[a-z]', password):
    print(f'Incorrect password, it should be letters in lower register a-z')
if not re.search('[A-Z]', password):
    print(f'Incorrect password, it should be letters in upper register A-Z')
