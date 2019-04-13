#include<stdio.h>
int main()
{
int i,c=0,n;
scanf("%d",&n);
if(n<=1000)
{
  for(i=2;i<n;i++)
  {
    if(n%i==0)
    {
     c++;
     break;
    }
   }
  if(c==0)
  printf("yes");
  else
   printf("no");
  }
return 0;
}
