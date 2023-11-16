#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: a pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: a pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, max;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	max = size + 1 > 10 ? 10 : size + 1;
	printf("  first %ld bytes: ", max);
	for (i = 0; i < max; i++)
	{
		printf("%02hhx", str[i]);
		if (i < max - 1)
			printf(" ");
	}
	printf("\n");
}
