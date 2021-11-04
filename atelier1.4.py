#un programme pour imprimer la serie fibomacci en recursivite
def recu_fibo(n):
    if n<=1:
        return n
    else:
        return(recu_fibo(n-1)+recu_fibo(n-2)) #nombre de fibonacci en recursivite
a=int(input("enter le nombre de line a= "))
for i in range(a):#pour saisie plusieur nombre des fibonacci
    print(recu_fibo(i))