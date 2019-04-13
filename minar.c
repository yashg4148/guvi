#include<stdio.h>
#include<stdlib.h>
int main()
{
  int i,min,n,*p;
  scanf("%d",&n);
  p=(int*)malloc(n*sizeof(int));
   for(i=0;i<n;i++)
   scanf("%d",p+i);

  min=p[1];
  for(i=1;i<n;i++)
  {
   if(p[i]<min)
   min=p[i];
  }
printf("%d",min);
return 0;
}
