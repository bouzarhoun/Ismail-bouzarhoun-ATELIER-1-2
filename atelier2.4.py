#'intersection (commune) de deux Sets et supprimez ces éléments du premier Set
set1 = {23,11,3,4,13,8,34,54,6,29}
set2 = {11,4,2,36,345,78,23,867,788}
intersection = set1 & set2 #l'intersection de set 1 et de set 2
print("intercection",intersection)
set1 = set1 - intersection #set 2 apres la suppression
print("Set 1 après suppression :",set1)