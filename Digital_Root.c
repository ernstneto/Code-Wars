#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int n;
    char text[20];
    scanf("%d",&n);
    sprintf(text,"%d",n);
    printf("%s\n",text);
    return 0;
}