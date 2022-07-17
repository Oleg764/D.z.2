#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


a=[]

N = int(input('Введите  число N  = '))
    
def get_factorial_list(N):
    f = 1
    fact = []
    for i in range(1, N+1):
        f =f* i
        fact.append(f)
    return fact

print(get_factorial_list(N))
