#un programme pour convertir le nombre decimal en binaire avec fonction
def conversion(n):
    if n > 1:
        conversion(n // 2)
        print(n % 2, end="  ")
x = int(input("Entre un nombre decimal: ",))
conversion(x)