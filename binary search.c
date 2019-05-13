#include<stdio.h>
#include<stdlib.h>
int main()
{
int *y,i,mid,l,r,c=0,n,key;
scanf("%d",&n);
y=(int*)malloc(n*sizeof(int));
for(i=0;i<n;i++)
scanf("%d",(y+i));
scanf("%d",&key);
l=y[0];
r=y[n-1];
while(l<=r)
{
mid=(l+r)/2;
if(y[mid]==key)
c++;
break;
if(key>y[mid])
l=mid+1;
if(key<y[mid])
r=mid-1;
}
if(c==1)
printf("yes");
else
printf("no");
return 0;
}
