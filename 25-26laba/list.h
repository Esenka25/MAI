#ifndef LIST_H_INCLUDED
#define LIST_H_INCLUDED

#include <stdio.h>
 
struct node
{
    int info;
    struct node *next;
};

void create();
void display();
void insert();
void delete_begin();
void delete_end();
void delete_pos();
void size();
void insert_position(int pos, int val);

#endif