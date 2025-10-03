/*
** EPITECH PROJECT, 2025
** thonny
** File description:
** my_strlen
*/

void my_putnbr(int nb);

int my_strlen(char const *str)
{
    int i = 0;

    while (str[i] != '\0') {
        i++;
    }
    return (i);
}

int main(void)
{
    char str[] = "Hello, World!";

    my_putnbr(my_strlen(str));
    return (0);
}
