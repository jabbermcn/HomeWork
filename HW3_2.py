# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

st = input('Enter 3 numbers separated by commas: ')
st_split = st.split(',')
print(st_split)
print(f'Number of values: {len(st_split)}')
avg_sum = 0
for i in st_split:
    avg_sum += int(i)
print(f'Average: {round(avg_sum / len(st_split), 3)}')
