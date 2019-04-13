#include<stdio.h>
int main()
{
int i,m,n,c,j;
scanf("%d%d",&m,&n);
 for(i=m+1;i<n;i++)
 {
  c=0;
   for(j=2;j<i;j++)
   {
    if(i%j==0)
    c++;
    break;
   }
   if(c==0)
   printf("%d ",i);
 }
return 0;
}
