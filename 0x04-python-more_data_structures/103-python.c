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

        printf("[*] Python list info\n"); 
        if (!PyList_Check(p)) 
        { 
                printf("  [ERROR] Invalid List Object\n"); 
                return; 
        } 
        list = (PyListObject *)p; 
        **size = PyList_Size(p);** 
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
        size = PyBytes_Size(p); 
        **string = PyBytes_AsStringAndSize(p, NULL, NULL);** 

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
}