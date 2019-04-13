#include<stdio.h>
int main()
{
int a[10],i=0,n,k=0;
scanf("%d",&n);
if(n<=100000)
{
  m=n;
  while(n!=0)
  {
    k++;
    a[i]=n%10;
    i++;
    n=n/10;
   }
  for(i=0;i<k;i++)
  o=o+a[i]*a[i]*a[i];
  
   if(m==o)
   printf("yes");
   else
   printf("no");
}

retrurn 0;
}
