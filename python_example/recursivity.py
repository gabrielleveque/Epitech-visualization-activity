##
## EPITECH PROJECT, 2025
## thonny
## File description:
## recursivity
##

from utils import my_putnbr, my_putstr

def factorial(n):
    result = 0

    if n <= 1:
        return 1
    result = n * factorial(n - 1)
    my_putnbr(n)
    return result

def countdown(n):
    if n < 0:
        return
    my_putnbr(n)
    countdown(n - 1)

def main():
    my_putstr("----- Factorial -----\n");
    factorial(5);
    my_putstr("----- Countdown -----\n");
    countdown(5);
    return 0

main()
