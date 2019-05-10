#include<stdio.h>
int main()
{
int m,n,i,j,c=0;
scanf("%d%d",&m,&n);
for(i=m;i<=n;i++)
{
if(i==2)
c++;
for(j=2;j<i;j++)
{
if(i%j==0)
break;
if(j==(i-1))
c++;
}
printf("%d",c);
}
return 0;
}
