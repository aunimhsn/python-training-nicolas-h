"""
Écrire un programme qui demande en continue à l'utilisateur d'entrer des notes d'élèves.
La boucle se terminera seulement si l'utilisateur entre une valeur négative. 
Lorsque cela arrive, afficher le nombre de notes entrées, et calculer la moyenne de toutes les notes.

Si l'utilisateur entre autre chose qu'un nombre, l'erreur doit être traitée.
Si l'utilisateur ne rentre aucune note et quitte le programme immédiatement, 
l'erreur doit également être traitée. 


"""

# Entering marks...
marks = []

while True:
    mark = input("Enter a mark  (or a negative number to exit)) :")
    
    try:
        mark_float = float(mark)
    except ValueError:
        print("The entered value is not a number")
    else:
        if mark_float < 0:
            break
        else:
            marks.append(mark_float)

print(f"There are {len(marks)} marks.")

# Average calculation
try:
    average = sum(marks) / len(marks)
except ZeroDivisionError:
    print('There is no mark.')
else:
    print(f"The average of all the marks entered is {average}")

