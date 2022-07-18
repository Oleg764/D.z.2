N = int(input('Введите число  n : '))
numbers =[]
for i in range(-N, N+1):
    N= -N +1    
    numbers.append(i)

print (numbers)
int_list = []
for element in input('Введите 2 номера позиций через пробел  : ').split():
    int_list.append(int(element))

composition_elem =numbers[int_list [0]]*numbers[int_list [1]]
print ('Произведение элементов = ',composition_elem)
