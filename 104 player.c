#include<stdio.h>
#include<stdlib.h>
int main()
{
int i,*p,n,s=0;
scanf("%d",&n);
  if(n<=100000)
  {
p=(int*)malloc(n*sizeof(int));

for(i=0;i<n;i++)
scanf("%d",(p+i));

for(i=0;i<n-1;i++)
s=s+(p[i]+p[i+1]);

printf("%d",s);
  }
return 0;
}
