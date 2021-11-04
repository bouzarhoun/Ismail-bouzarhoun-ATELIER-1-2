#fonction pour trouver la frequence d'un caractere dans un chaine
def fequence(chaine,lettre):
   nbr = 1
   for i in range(len(chaine)):
       if chaine[i]==lettre:
        nbr+=1
   return nbr
chaine = input("Entrez un chaine: ")
lettre=input("lettre : ")
print("nombre de lettre est ",fequence(chaine,lettre))