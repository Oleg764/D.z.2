# 3. Задать список из n чисел последовательности (1+1/n)^n
# и вывести на экран их сумму

n = int(input('Введите число  n : '))
numbers = []
for i in range(1, n+1):
    input_value =  (1+1/n) **n                                     
    numbers.append(input_value)
sum = 0
for i in numbers:
    sum += i
print (numbers)
print('Сумма всех чисел последовательности:', sum)







