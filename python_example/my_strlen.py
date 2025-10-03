##
## EPITECH PROJECT, 2025
## thonny
## File description:
## my_strlen
##

from utils import my_putnbr

def my_strlen(str):
    length = 0

    while str[length] != '\0':
        length += 1
    return length

def main():
    str = "Hello, World!\0"
    length = my_strlen(str)

    my_putnbr(length)
    return 0

main()
