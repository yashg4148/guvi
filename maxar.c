#include<stdio.h>
#include<stdlib.h>
int main()
{
  int n,i,*p,max;
  scanf("%d",&n);
  if(n>=1&&n<=100000)
  {
    p=(int*)malloc(n*sizeof(int));
     for(i=0;i<n;i++)
     scanf("%d",p+i);
    
   max=p[1];
    for(i=1;i<n;i++)
    {
     if(p[i]>max)
     max=p[i];
    }
    
    printf("%d",max);
  }
}
