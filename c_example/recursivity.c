/*
** EPITECH PROJECT, 2025
** thonny
** File description:
** recursivity
*/

void my_putnbr(int nb);

void my_putstr(char const *str);

int factorial(int n)
{
    int result = 0;

    if (n <= 1) {
        return 1;
    }
    result = n * factorial(n - 1);
    my_putnbr(n);
    return result;
}

void countdown(int n)
{
    if (n < 0) {
        return;
    }
    my_putnbr(n);
    countdown(n - 1);
}

int main(void)
{
    my_putstr("----- Factorial -----\n");
    factorial(5);
    my_putstr("----- Countdown -----\n");
    countdown(5);
    return (0);
}
