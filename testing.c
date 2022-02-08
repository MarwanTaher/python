#include <stdio.h>

double average(int a, int b)
{
    return a + b / 2;
}

#ifndef RunTests
int main()
{
    printf("%f", average(2, 1));
}
#endif