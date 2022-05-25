#ifndef _TREE_H_
#define _TREE_H_

#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int data;
    struct Tree *left;
    struct Tree *right;
    struct Tree *parent;
} Tree;

Tree *root_create(int value);
Tree *tree_add_element(Tree *parent, int value);
Tree *delete_element(Tree *parent, int value);
void tree_print(Tree *t, int n);
Tree* search_in_tree(Tree *t, int value);
Tree* minimum(Tree *t);
void depth(Tree *parent, int n); //n - quantity elements
void traversal(Tree *parent, int c, int a []);

#endif //_TREE_H_
