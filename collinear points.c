#include<stdio.h>
int main()
{
int x[3],y[3],i,j;
for(i=0;i<3;i++)
scanf("%d%d",&x[i],&y[i]);
j=x[0]*(y[1]-y[2])+x[1]*(y[2]-y[0])+x[2]*(y[0]-y[1]);
if(j==0)
printf("yes");
else
printf("no");
return 0;
}
