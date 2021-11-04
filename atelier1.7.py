#fonction pour inverse la frequence d'un caractere d'un chaine
def envers(chaine):
    mot = ""
    for i in chaine: #pour chaque lettre
        mot = i + mot
    return mot #returner le mot
a = input("entrer un mot : ")
print   (envers(a)) #pour donner le resulta