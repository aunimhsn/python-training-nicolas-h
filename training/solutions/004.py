"""
Faire une fonction qui permet de trier un nombre d'entiers passés en paramètre non défini (utilisation de *args)
Cette fonction doit retourner une liste contenant d'abord les nombres pairs dans l'ordre croissant 
puis les nombres impairs dans l'ordre croissant. 
Cette fonction doit prendre en paramètre une série de nombre d'une taille non définie.


"""

def sort_even_odd(*args):
    even = []
    odd = []

    for n in args:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    even.sort()
    odd.sort()

    return even + odd

print(sort_even_odd(1, 3, 154, 22, 31, 52))