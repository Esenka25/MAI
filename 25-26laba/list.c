#include <stdlib.h>
#include "list.h"

struct node *start=NULL;

void create()
{
    struct node *temp,*ptr;
    temp=(struct node *)malloc(sizeof(struct node));
    if(temp==NULL)
    {
        printf("Out of Memory Space:\n");
        exit(0);
    }
    printf("\nEnter the data value for the node:\n");
    scanf("%d",&temp->info);
    temp->next=NULL;
    if(start==NULL)
    {
            start=temp;
    }
    else
    {
        ptr=start;
        while(ptr->next!=NULL)
        {
            ptr=ptr->next;
        }
        ptr->next=temp;
    }
}
void display()
{
    struct node *ptr;
    if(start==NULL)
    {
        printf("\nList is empty:\n");
        return;
    }
    else
    {
        ptr=start;
        printf("\nThe List elements are:\n");
        while(ptr!=NULL)\
        {
            printf("%d ",ptr->info );
            ptr=ptr->next ;
        }
        printf("\n");
    }
}

void insert()
{
    struct node *temp,*ptr;
    temp=(struct node *)malloc(sizeof(struct node));
    int x = 2;
    if(temp==NULL)
    {
        printf("\nOut of Memory Space:\n");
        return;
    }
    printf("\nEnter the data value for the node:\n" );
    scanf("%d",&temp->info );

    temp->next =NULL;
    if(start==NULL)
    {
        start=temp;
    }
    else
    {
        ptr=start;
        while(ptr->next !=NULL)
        {
            x++;
            ptr=ptr->next ;
            
        }
        ptr->next =temp;
    }

    // start of sorting - actually this is my sorting fuction
    int arr[x];
    ptr=start;
    int c = 0;
    while(ptr!=NULL)
    {
        arr[c] = ptr->info;
        c++;
        ptr=ptr->next ;
    }
    int new_arr[c - 1];
    for (int i = 0; i < c - 1; i++)
    {
        new_arr[i] = arr[i];
    }
    int p = sizeof(new_arr) / sizeof(new_arr[0]); // nim of el in new_arr
    int y = sizeof(arr) / sizeof(arr[0]); // nim of el in arr
    int q = arr[y - 1];
    int counter = 0;
    for (int i = p - 1; i >= 0; i--)
    {
        if (q < new_arr[i])
        {
            counter++;
        }
        else
        {
            break;
        }
    }
    counter = p - counter;
    delete_end();
    insert_position(counter, q);
}

void delete_begin()
{
    struct node *ptr;
    if(ptr==NULL)
    {
        printf("\nList is Empty:\n");
        return;
    }
    else
    {
        ptr=start;
        start=start->next ;
        free(ptr);
    }
}
void delete_end()
{
    struct node *temp,*ptr;
    if(start==NULL)
    {
        printf("\nList is Empty:\n");
        exit(0);
    }
    else if(start->next ==NULL)
    {
        ptr=start;
        start=NULL;
        free(ptr);
    }
    else
    {
        ptr=start;
        while(ptr->next!=NULL)
        {
            temp=ptr;
            ptr=ptr->next;
        }
        temp->next=NULL;
        free(ptr);
        }
}
void delete_pos()
{
    int i,pos;
    struct node *temp,*ptr;
    if(start==NULL)
    {
        printf("\nThe List is Empty:\n");
        exit(0);
    }
    else
    {
        printf("\nEnter the position of the node to be deleted:\n");
        scanf("%d",&pos);
        if(pos==0)
        {
            ptr=start;
            start=start->next ;
            printf("\nThe deleted element is:%d\n",ptr->info  );
            free(ptr);
        }
        else
        {
            ptr=start;
            for(i=0;i<pos;i++) { temp=ptr; ptr=ptr->next ;
                if(ptr==NULL)
                {
                    printf("\nPosition not Found:\n");
                    return;
                }
            }
            temp->next =ptr->next ;
            printf("\nThe deleted element is:%d\n",ptr->info );
            free(ptr);
        }
    }
}

void size()
{
    int a = 0;
    struct node *ptr;
    if(start==NULL)
    {
        printf("\nList is empty:\n");
        return;
    }
    else
    {
        ptr=start;
        while(ptr!=NULL)
        {
            a++;
            ptr=ptr->next ;
        }
        printf("\nCurrent size:");
        printf("\n%d\n", a);
    }
    printf("\n");
}

void insert_position(int position, int val)
{
    struct node *ptr,*temp;
    int i,pos = position;
    temp->info = val;
    temp=(struct node *)malloc(sizeof(struct node));
    if(temp==NULL)
    {
        return;
    }
    temp->next=NULL;
    if(pos==0)
    {
        temp->next=start;
        start=temp;
    }
    else
    {
        for(i=0,ptr=start;i<pos-1;i++) { ptr=ptr->next;
            if(ptr==NULL)
            {
                return;
                }
            }
            temp->next =ptr->next ;
            ptr->next=temp;
        }
}