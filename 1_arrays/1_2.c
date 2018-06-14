#include <stdio.h>

void reverse (char *str)
{
    int i = 0, j = strlen(str)-1;

    while (i < j) {
        char t = str[i];
        str[i] = str[j];
        str[j] = t;
        i++;
        j--;
    }
}

int main (int argc, char *argv[])
{
    char s[] = "VAMSI IS A BAD BOY";
    reverse(s);
    printf("Str: %s\n", s);
}
