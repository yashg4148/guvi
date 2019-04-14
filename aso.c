#include<stdio.h>
#include<stdlib.h>
int main()
{
int n,i,j,*p,temp;
scanf("%d",&n);
if(n>=1&&n<=1000)
{
p=(int*)malloc(n*sizeof(int));
for(i=0;i<n;i++)
scanf("%d",p+i);

for(i=0;i<n;i++)
{
  for(j=0;j<n-i-1;j++)
  {
  if(p[j]>p[j+1])
  {
  temp=p[j];
  p[j]=p[j+1];
  p[j+1]=temp;
   }
  }
}
for(i=0;i<n;i++)
printf("%d ",p[i]);
}
return 0;
}
