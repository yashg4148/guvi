#include<stdio.h>
int main()
{
if(n<=20)
{
   int n,s=1;
   scanf("%d",&n);
   while(n!=0)
  {
    s=s*n;
     n--;
   }
 
  printf("%d",s);
}
  return 0;
}
