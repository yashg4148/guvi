#include<stdio.h>
int main()
{
int a=0,b,c,n;
scanf("%d",&n);
c=n;
while(n!=0)
{
b=n%10;
a=10*a+b;
n=n/10;
}
if(a==c)
printf("yes");
else 
printf("no");
return 0;
}
