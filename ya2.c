/*progam for finding a number 'a' with given exponent(b)*/
#include<stdio.h>
int main()
{
int a,b,i,c=1;
scanf("%d%d",&a,&b);
for(i=0;i<b;i++)
{
c=c*a;
}
printf("%d",c);
return 0;
}
