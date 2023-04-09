
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# user_num = int(input('Print a 3digits number: '))
# decs = user_num // 10
# sots = user_num // 100

# third_digit = user_num - (decs * 10)
# second_digit = decs - (sots * 10)

# sum_digit = sots + second_digit + third_digit
# print('The sum of digits in your number is: ', sum_digit)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# sum_cranes = int(input('Print sum of cranes: '))
# # Понятия не имею, как решать уравнения в python, предварительно решила уравнение на бумаге взяв значение суммы из
# # первого примера: 6 = 2x + (2x * 2) из чего выяснила, что количество журавликов, которое делает Петя или Серёжа,
# # всегда будет меньше суммы в шесть раз.

# cranes_peter = sum_cranes // 6
# cranes_serge = sum_cranes // 6
# cranes_kate = (cranes_peter + cranes_serge) * 2
# print(f'Peter is made {cranes_peter} cranes, Serge is made {cranes_serge} cranes, Kate is made {cranes_kate} cranes.')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

# user_num = int(input('Print num, of your ticket: '))

# digit1 = user_num // 100000
# digit2 = (user_num // 10000) - ((user_num // 100000) * 10)
# digit3 = (user_num // 1000) - ((user_num // 10000) * 10)
# digit4 = (user_num // 100) - ((user_num // 1000) * 10)
# digit5 = (user_num // 10) - ((user_num // 100) * 10)
# digit6 = user_num - ((user_num // 10)* 10)

# sum123 = digit1 + digit2 + digit3
# sum456 = digit4 + digit5 + digit6

# if sum123 == sum456:
#     print('Youve got a lucky ticket!')
# else:
#     print('Youve got an unlucky ticket!')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input('Print a length of chocolate: '))
# m = int(input('Print a width of chocolate: '))
# k = int(input('Print a sum of pieces you want to get: '))

# if n * m // 2 and k // 2:
#     print('The chocolate can be divided!')
# else: 
#     print("The chocolate can't be divided!")