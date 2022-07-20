#4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

#def printBin (N):
#    if N==0:
#       return 0
#    #for i in N :  
#    print (N%2,end = "")
#    printBin (N//2)
#printBin (7)  
N = int(input('Введите число N = '))
binarynumber=""
if (N!=0):
    while (N>=1):
        if (N %2==0):
            binarynumber=binarynumber+"0"
            N=N/2
        else:
            binarynumber=binarynumber+"1"
            N=(N-1)/2
else:
    binarynumber="0"
n= binarynumber[::-1]
print(n)
    
