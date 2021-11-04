#exercice pour compter les chiffres d'un nombre donne
def compte(X):
    n=0
    while X!=0:
        X=int(X/10)
        n += 1
    return n #return le nombre de chiffre
X=int(input("X="))
print( "le nombre de chiffre est",compte(X))
