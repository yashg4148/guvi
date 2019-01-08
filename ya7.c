/*Program for checking whether a character is vowel or consonent*/
#include<stdio.h>
int main()
{
char c;
scanf("%c",&c);
if(c>=65&&c<=116)
{
if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
printf("Vowel");
else
printf("Consonent");
}
else
printf("invalid");
}
