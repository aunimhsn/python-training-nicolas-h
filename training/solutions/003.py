"""
Définir une fonction element_max(list, start, end) qui renvoie l'élément ayant la
plus grande valeur dans la liste transmise, les deux arguments début et fin indiqueront 
les indices entre lesquels doit s'exercer la recherche.
Chacun d'eux pourra être omis lors de l'appel à la fonction.

list = [9, 3, 6, 1, 7, 5, 4, 8, 2]


"""

list = [9, 3, 6, 1, 7, 5, 4, 8, 2]

def element_max(list, start=0, end=None):
    # define end
    if end is None:
        end = len(list) - 1
    
    sub_list = list[start:end+1]
    max_value = max(sub_list)

    return max_value


print(element_max(list)) # Returns 9
print(element_max(list, 3, 6)) # Returns 7
    
    
