#include <stdio.h>
#include "multi.h"
#include "add.h"

int multiNumber(int a, int b)
{
	int i = 0, res = 0;
	for (i = 0; i < a; i++) {
		res = addNumber(res, b);
	}
	return res;
}