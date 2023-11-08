#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A pointer to a Python object
 */

void print_python_list(PyObject *p)
{
	PyObject *obj;
	long int size, i;
	PyListObject *list;

	list = (PyListObject *)p;
	size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}


/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A pointer to a Python object
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, max;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		max = 10;
	else
		max = size + 1;

	printf("  first %ld bytes:", max);

	for (i = 0; i < max; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
	printf(" %02x", 256 + string[i]);
}
