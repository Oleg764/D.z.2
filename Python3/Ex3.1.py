a =[3,6,7,23,45,67,2]
def sum_elem(a):
    sum=0
    for i in range (7):
        if i%2!=0:
         sum=sum+a[i]
    return sum         
print ('Сумма элементов на нечётных позициях  = ',sum_elem(a))       

