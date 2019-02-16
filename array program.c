#include<stdio.h>
int main
{
int i,k,n,*temp,sum=0;
scanf("%d",&n);
scanf("%d",&k);
temp=(int*)malloc(size0f(n));
for(i=0;i<n;i++)
scanf("%d",(temp+i));
for(i=0;i<k;i++)
sum=sum+*(temp+i);
printf("%d",sum);
}
