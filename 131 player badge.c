#include<stdio.h>
int main()
{
int n,i,a,s=0;
scanf("%d",&n);
while(n!=0)
{
a=a%10;
if(a%2!=0)
s=s+a;
n=n/10;
}

if(s%2==0)
printf("E");
else
printf("O");
return 0;
}
