/*
** EPITECH PROJECT, 2025
** thonny
** File description:
** iteration
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
    int length = my_strlen(str);

    my_putnbr(length);
    return (0);
}
