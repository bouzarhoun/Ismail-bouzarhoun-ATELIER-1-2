#un programme pour calculer la somme des nombres de 1 a n avec la recursivite
def somme(i):
    if i==0: #car ona la somme de 1 a n
        return i
    else :
        return (i + somme(i-1))
i = int(input(" enter the number "))
print(somme(i))