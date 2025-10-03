##
## EPITECH PROJECT, 2025
## thonny
## File description:
## iteration
##

from utils import my_putnbr, my_putstr

def my_strlen(str):
    length = 0

    while str[length] != '\0':
        length += 1
    return length

def array_iteration(arr):
    """
    Créer une fonction qui itère un tableau et affiche chaque ligne suivi d'un retour à la ligne
    Les caractères de chaque ligne doivent être séparés d'un espace

    Exemple : ["Hello", "World"] doit afficher:
    H e l l o
    W o r l d

    Vous avez a votre disposition la fonction my_putstr et my_putchar
    """


    return None

def main():
    str = "Hello, World!\0"
    length = my_strlen(str)

    my_putstr("----- Length of a string -----\n");
    my_putnbr(length)
    my_putstr("----- Array iteration -----\n");
    array_iteration(["Hello", "World"]) # Vous pouvez modifier le tableau pour tester
    return 0

main()
