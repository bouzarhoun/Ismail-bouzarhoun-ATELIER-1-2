#e un programme pour itérer une liste donnée et compter l'occurrence de chaque élément et créer un dictionnaire pour montrer le nombre de chaque élément
List= [7,8,45,7,234,5,21,678,1,345,234,1,1,1,7]
dict={} #la dictionnaire
for i in List:
    List.count(i)
    dict[i]=List.count(i)
print (dict)