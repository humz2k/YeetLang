#include <stdlib.h>
#include <stdio.h>
union Addr {
    int asInt;
    float asFloat;
};
typedef union Addr addr;

int main(){
	addr* arr = malloc(100*sizeof(addr));
	addr var1;var1.asInt = 0;
	addr var2;var2.asInt = 1;
	addr var3;var3.asInt = 2;
	var1.asFloat = 10.5;
	printf("%f",(float)var1.asFloat);
	free(arr);
	return 0;
}