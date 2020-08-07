#include <stdio.h>
#include "multi.h"
#include "add.h"
int main()
{
	int a = 4, b = 5;
	int res = 0;
	res = addNumber(a, b);
	printf("addNumber res = %d\n", res);
	res = multiNumber(a, b);
	printf("multiNumber res = %d\n", res);
	return 0;
}