#include <stdio.h>

int main() {

    int age;
    char lis; 

    printf("enter your age:\n");
        
        scanf(" %d", &age);

    printf("do you have license Y or N:\n");
        
        scanf(" %c", &lis);


            if (age < 18 && (lis == 'Y' || lis == 'y')) {
                printf("you are not allowed to get a car\n");
    } 
    
            else if (lis == 'N' || lis == 'n') {
                printf("you are not allowed to get a car (No License)\n");
    } 
    
            else if (lis == 'Y' || lis == 'y') {
                printf("you are allowed to get a car\n");
    }
   
            else {
                printf("Invalid input for license!\n");
    }


    return 0;
}

