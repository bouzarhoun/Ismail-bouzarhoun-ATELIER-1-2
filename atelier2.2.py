#Deviser la liste en 3 morceaux égaux et inverser chaque morceau
list=[132,345,45,5,8,23,43,12,2,23,76,4]
list1=[]
list2=[]
list3=[]

n=len(list)
for i in range (0,n) :#pour devise la list
    if i < n/3 :
        list1.append(list[i])
    elif i >= (2*n)/3 :
        list3.append(list[i])
    else:
        list2.append(list[i])
#pour inverser les listes
list1.reverse()
print(list1)
list2.reverse()
print(list2)
list3.reverse()
print(list3)