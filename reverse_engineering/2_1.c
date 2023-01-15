/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
int num(int a, int b){
    int c = a+b;
    return c;
}
int main()
{
    int a;
    a = num(1,4);
    printf("%d",a);
    return 0;
}
