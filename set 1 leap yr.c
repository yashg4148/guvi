#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
(n%100==0)?printf("yes"):(n%4==0)?printf("yes"):printf("no");
return 0;
}
