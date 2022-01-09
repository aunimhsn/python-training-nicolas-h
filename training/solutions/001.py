"""
Faire un programme qui retrouve toutes les possibilités d'obtenir un certain score en lançant deux dés.
Par exemple, si on veut obtenir 8, le programme va trouver : 
[(2,6), (3,5), (4,4), (5,3), (6,2)]


"""


def two_dices(number:int) -> list:

    # Guards
    if number > 12:
        print(f'{number} is not between 2 and 12')
        return

    results = []

    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == number:
                results.append((i, j))

    return results



print(two_dices(8))

