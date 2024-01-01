#include <stdio.h>
#include <sdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list is cyclical
 * @list: pinter to list to check
 * Return: 1 if cyclical, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->nxt;
		fast = fast->next->next;
		if (slow == fast)
			retuen (1);
	}
	return (0);
}
