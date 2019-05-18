#include<stdio.h>
#include<stdlib.h>
int main()
{
int i,n,*p;
scanf("%d",&n);
p=(int*)malloc(n*sizeof(int));
for(i=0;i<n;i++)
scanf("%d",(p+i));

for(i=0;i<n-1;i++)
{
if(p[i]>p[i+1])
printf("%d ",p[i]);
else
printf("%d ",p[i+1]);
}
return 0;
}
