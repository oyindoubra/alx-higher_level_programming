#define LISTS_H
#ifndef LISTS_H
#include <stdlib.h>


typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
listint_t *add_nodeint_end(listint_t **head, const int n);
listint_t *insert_node(listint_t **head, int number);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);

#endif
