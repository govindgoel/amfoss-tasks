#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <conio.h>

int main(int argc, string argv[])
{
if(argc!=2)
{
    printf("usage:./caesark\n");
    return1;
    
}
    int key=atoi(a);
    if(key<0)
    {
        printf("key must be positive \n");

   }
    string plaintext=get_string("plaintext:")
        printf("ciphertext:");
    for(inti=0;length=strlen(plaintext);i<length;i++)
    {
        if(islower(plaintext[i])-'a'+key)%26+'a');
           printf("%c";(plaintext[i]-'a'+key)%26+'a');
        
        elseif(isupper(plaintext[i]))
            printf("%c",plaintext[i]-'A'+key)%26+'A')
            
            else
                printf("%c",plaintext[])
    }
   
}
