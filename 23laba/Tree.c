#include <stdio.h>
#include <stdlib.h>

#include "Tree.h"

int i = 0;

Tree *root_create(int value)
{
    Tree *tree = (Tree*)malloc(sizeof(Tree));
    tree->data = value;
    tree->left = NULL;
    tree->right = NULL;
    tree->parent = NULL;
    return tree;
}

Tree *tree_add_element(Tree *root, int value)
{
    if (root == NULL) {
        printf("Done!\n");
        return root_create(value);
    }

    Tree *NewTree = (Tree*)malloc(sizeof(Tree));
    NewTree->data = value;
    Tree *tree1 = root;
    Tree *tree2 = NULL;

    while (tree1 != NULL) {
        tree2 = tree1;
        if (value < tree1->data) {
            tree1 = tree1->left;
        }
        else if (value > tree1->data) {
            tree1 = tree1->right;
        }
        else {
            printf("This value is already exist in tree! Use other values!\n");
            return root;
        }
    }
    NewTree->parent = tree2;
    NewTree->left = NULL;
    NewTree->right = NULL;
    if (value < tree2->data) {
        tree2->left = NewTree;
    } else {
        tree2->right = NewTree;
    }
    printf("Done!\n");
    return root;
}

void tree_print(Tree *root, int n)
{
    if (root != NULL) {
        tree_print(root->right, n + 1);
        for (int i = 0; i < n; i++) printf("\t");
        printf("%d\n", root->data);
        tree_print(root->left, n + 1);
    }
}

Tree *delete_element(Tree *root, int value)
{
    Tree* tree1 = NULL, * tree2 = NULL, *tree3 = root, *tree4 = NULL;

    if (root == NULL) {
        printf("Delete error! Your tree isn't exist!\n");
        return root;
    }
    tree1 = search_in_tree(tree3, value);
    if (tree1 == NULL) {
        printf("Your element already isn't exist!\n");
        return root;
    }
    // First case. element == leaf
    if (tree1->left == NULL && tree1->right == NULL) {
        if (tree1->parent == NULL) { // If this is root
            free(tree1);
            tree1 = NULL;
            printf("Successful deletion\n");
            return NULL;
        }
        tree2 = tree1->parent;
        if (tree2->left == tree1) {
            tree2->left = NULL;
        }
        else {
            tree2->right = NULL;
        }
        free(tree1);
    }
    // Second case. one of subtrees are available
    else if (tree1->left != NULL && tree1->right == NULL) { // left subtrees is exist
        if (tree1->parent == NULL) { // If this is root
            tree4 = tree1->left;
            tree4->parent = NULL;
            free(tree1);
            printf("Successful deletion\n");
            return tree4;
        }
        tree2 = tree1->parent;
        if (tree2->left == tree1) {
            tree2->left = tree1->left;
        }
        else {
            tree2->right = tree1->left;
        }
        free(tree1);
    }
    else if (tree1->left == NULL && tree1->right != NULL) { // right subtrees is exist
        if (tree1->parent == NULL) { // If this is root
            tree4 = tree1->right;
            tree4->parent = NULL;
            free(tree1);
            printf("Successful deletion\n");
            return tree4;
        }
        tree2 = tree1->parent;
        if (tree2->left == tree1) {
            tree2->left = tree1->right;
        }
        else {
            tree2->right = tree1->right;
        }
        free(tree1);
    }
    // Third case. Both subtrees are available
    else if (tree1->left != NULL && tree1->right != NULL) {
        tree2 = minimum(tree1->right);
        tree1->data = tree2->data;
        tree4 = tree2->parent;
        if (tree4->left == tree2) {
            free(tree2);
            tree4->left = NULL;
        }
        if (tree4->right == tree2) {
            free(tree2);
            tree4->right = NULL;
        }
    }
    printf("Successful deletion\n");
    return root;
}

Tree *search_in_tree(Tree *root, int value)
{
    if (root == NULL) {
        return NULL;
    }
    if (root->data == value) {
        return root;
    }
    if (value > root->data) {
        return search_in_tree(root->right,value);
    } else {
        return search_in_tree(root->left, value);
    }
}

Tree *minimum(Tree *t)
{
    if (t->left == NULL) {
        return t;
    }
    return minimum(t->left);
}

void depth(Tree *root, int n) {
    if (root == NULL) return;
    int c = 1, a[n+1];
    for (int q = 0; q < n+1; ++q) a[q] = 0;
    if (root->left != NULL) traversal(root->left, c, a);
    if (root->right != NULL) traversal(root->right, c, a);
    printf("array done\n");
    int o = a[0];
    for (int j = 0; a[j] != 0 && j < n+1; j+=2) {
        if (a[j] < o) o = a[j];
    }
    printf("Lists with minimum depth:\n");
    for (int j = 0; a[j] != 0 && j < n+1; j+=2) {

        if (a[j] == o) printf("%d\n", a[j+1]);
    }
}


void traversal(Tree *root, int c, int a []) {
    c++;
    if (root->left != NULL) traversal(root->left, c, a);
    if (root->right != NULL) traversal(root->right, c, a);
    if (root->left == NULL && root->right == NULL) {
        a[i] = c;
        a[++i] = root->data;
        printf("i=%d %d %d\n", c, a[i-1], a[i]);
        ++i;
    }
}

