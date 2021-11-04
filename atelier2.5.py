#Itérer une liste donnée et vérifier si un élément donné existe en tant que valeur de clé dans un dictionnaire. Sinon, supprimez-le de la liste
list=[19, 64, 3, 37,11,34,12,234,45]
dictionary={'ismail':19, 'anass':3, 'nizar':11, 'zayd':12}
list1=[]
for x in list :
    if x not in dictionary.values() :
        list1.append(x)
for i in list1 :
    list.remove(i)
print(list)