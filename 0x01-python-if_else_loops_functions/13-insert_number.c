#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 *insert_node - inserts node in list
 *@head: head pointer  address
 *@num: number to insert
 *Return: node
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = num;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
