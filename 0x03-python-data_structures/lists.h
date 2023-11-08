#include <stddef.h>
#include <stdio.h>
#ifndef LISTS_H
#define LISTS_H

/**
 *
 *  integer
 * next: points to the next node
 *  singly linked list node structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint_end(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
int is_palindrome(listint_t **head);
void free_listint(listint_t *head);

#endif
