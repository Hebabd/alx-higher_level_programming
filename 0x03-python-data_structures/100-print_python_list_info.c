#include <python.h>

/**
 * print_python_list_info - prints basic info about python lists.
 * @p: A Pyobject list
 */
void print_python_list_info(py0bject *p)
{
	int size, alloc, i;
	py0bject *obj;

	size = py_SIZE(p);
	alloc = ((pyList0bjet *)p)->allocated;

	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = pyList_GetItem(p, i);
		printf("%s\n", py_TYPE(obj)->tp_name);
	}
}

