#include <stdio.h>
#include <stdlib.h>

#include "Tree.h"
#include "Tree.c"

void print_menu() {
	printf("\nSelect the desired action by writing the appropriate number:\n");
	printf("1) Add an item to the tree\n");
	printf("2) Print the tree\n");
	printf("3) Remove an item from the tree\n");
	printf("4) Search list with minimum depth\n");
	printf("Enter 0 for exit\n");
}

int main(void)
{
	Tree *t = NULL;
	int value;
	char c;
	int n = 0;
	printf("Welcome to the program for processing binary search trees!\n");
	print_menu();
	while ((c = getchar()) != EOF) {
		value = 0;
		if (c == '\n') continue;
		switch (c) {
		case '1':
			printf("\nEnter the value you want to add to the tree:");
			scanf("%d", &value);
			t = tree_add_element(t, value);
			n++;
			break;
		case '2':
			tree_print(t, 1);
			break;
		case '3':
			printf("\nEnter the value you want to delete from the tree: ");
			scanf("%d", &value);
			t = delete_element(t, value);
			n--;
			break;
        case '4':
            printf("\nSearcing list with minimum depth:\n");
            if (t == NULL) return 0;
            depth(t, n);
            //printf("\n%d", bfs(t));
            break;
		case '0':
			printf("\nHave a nice day!\n");
			return 0;
		default:
			printf("The number you entered isn't in the menu :(\nPlease try again, in case you made a mistake\n");
			break;
		}
		print_menu();
	}
}