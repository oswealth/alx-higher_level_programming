#include "lists.h"

/**
 * reverse - reverses the second half of a linked list
 * @head: pointer to the head of the list
 * @middle: pointer to the middle node of the list
 * Return: pointer to the head of the reversed list
 */

listint_t *reverse(listint_t *head, listint_t *middle)
{
	listint_t *prev = middle;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != middle)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}


/**
 * compare - compares two linked lists recursively
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if they are equal, 0 if not
 */

int compare(listint_t **head1, listint_t *head2)
{
	int result;

	if(head2 == NULL)
		return (1);

	result = compare(head1, head2->next) && ((*head1)->n == head2->n);

	*head1 = (*head1)->next;
	return (result);
}


/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *middle = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast)
		middle = slow->next;
	else
		middle = slow;

	middle = reverse(middle, slow);
	return (compare(head, middle));
}
