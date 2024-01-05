#include "lists.h"

/**
 * palindrom - recursivepalind or not
 * @head: head list
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - funct to know if is palindrome
 * @head: head list
 * @end: end list
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)-> == end->n)
	{
		*head = (*hea)->next;
		return (1);
	}
	return (0);
}
