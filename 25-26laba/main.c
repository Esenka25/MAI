#include <stdlib.h>
#include <stdio.h>
#include "list.h"

int main(int argc,char *argv[])     
{

    int choice;
    while(1) {   
        printf("MENU\n");
        printf("1.Create\n");
        printf("2.Display\n");
        printf("3.Insert\n");
        printf("4.Delete from the begin\n");
        printf("5.Delete from the end\n");
        printf("6.Delete from specified position\n");
        printf("7.Determining the number of elements\n");
        printf("8.Exit\n");
        printf("--------------------------------\n");
        printf("Enter your choice:\n");
        scanf("%d", &choice);
        switch(choice)
        {
            case 1:
                create();
                break;
            case 2:
                display();
                break;
            case 3: 
                insert();
                break;
            case 4:
                delete_begin();
                break;
            case 5:
                delete_end();
                break;
            case 6:
                delete_pos();
                break;    
            case 7:
                size();
                break;
            case 8:
                exit(0);
                break;         
            default:
                printf("Wrong Choice:\n");
                break;
            }
    }
    return 0;
}
