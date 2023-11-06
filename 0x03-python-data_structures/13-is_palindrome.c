#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *first, *rev, *tmp1 = NULL, *tmp2 = NULL;

	if (!*head || !(*head)->next)
		return (1);
	first = *head;
	rev = *head;
	while (rev->next)
		rev = rev->next;
	while (rev)
	{
		tmp1 = rev->next;
		rev->next = tmp2;
		tmp2 = rev;
		rev = tmp1;
	}
	rev = tmp2;
	while (first && rev)
	{
		if (first->n != rev->n)
			return (0);
		first = first->next;
		rev = rev->next;
	}
	return (1);
}
