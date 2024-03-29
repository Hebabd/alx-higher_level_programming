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
	if (list == NULL || list->next == NULL)
		return (0)
	
			slow = list->next;
	fast = list->next->next;

	while (fast && fast->next)
	{
	
		if (slow == fast)
			retuen (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
