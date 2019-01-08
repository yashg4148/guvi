#include<stdio.h>
int main()
{
int a,b,c;
scanf("%d%d%d",&a,&b,&c);
if((C>b&&c>a)||(c==b&&c>a)||(c==a&&c>b))
printf("%d",c);
else if((b>a&&b>c)||(b==a&&b>c))
printf("%d",b);
else if(a>b&&a>c)
printf("%d",a);
else
printf("%d",a);
return 0;
}
