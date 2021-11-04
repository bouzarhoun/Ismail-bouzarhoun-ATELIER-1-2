# creer une liste en choisissant des element d'imdex impair dans la premier liste et des element d'index pair dans la seconde
def element(list):
    pair = []
    impaire = []
    for x in list:
        if (x%2==0):
            pair.append(x) #pour chaisir les nombres  pair dans liste 1
        else:
            impaire.append(x) #pour chaoisir les nombres impaire
    print( "list des nombres pair est:", pair)
    print("list des nombre impaire est",impaire)
list = [4, 18, 6, 345, 14, 34, 11, 20, 45, 120]
element(list)
