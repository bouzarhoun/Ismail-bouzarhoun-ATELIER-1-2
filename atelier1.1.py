#un programme pour trouver la somme des serie 1!/1 + 2!/2 + 3!/3 +4!/4 + 5!/5
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1) #pour calculer le factorial
s=1       
for i in range(2,6):
        s=s+factorial(i)/i #pour calculer la somme des factorial
print(s)