"""
# Problem 1
calc = input('Введите пример (H: 5+2 )>>> ')
if int(calc[-1]) == 0:
    print('Деление на ноль невозможно!!!')
else:
    print(eval(calc))


# Problem 2
a = 0
b = 2
c = 5
a1 = a
a, b, c = a1 + b, c - a1, a + b + c
print(a, b, c)


# Problem 3
kvadrat = int(input('Введите сторону квадрата >>> '))
print(f'Информация о квадрате:\nПериметр:{kvadrat * 4}\nПлощадь:{kvadrat ** 2}')


# Problem 4
sequence_0 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70', 0)
sequence_1 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, '70')
sequence_2 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70', 0.0)
sequence_3 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70')
all = [sequence_0, sequence_1, sequence_2, sequence_3]
for j in all:
    count = 0
    for i in j:
        if i in j[j.index(i) + 1:]:
            print('Последовательность не уникальна.')
            break
        else:
            count += 1
    if count == len(j):
        print('Последовательность уникальна.')



# Problem 6
user_num = input('Your number >>> ')
if user_num[0] > user_num[1] and user_num[1] > user_num[2] and user_num[2] > user_num[3]:
    print('Right number!!!')
else:
    print('Wrong number!!!')

"""











