#include <stdio.h>
#include "clmul.h"

int main() {
    printf("name: %s\n", inst.name);
    printf("long_name: %s\n", inst.long_name);
    printf("assembly_format: %s\n", inst.assembly_format);
    printf("defined_by: %s\n", inst.defined_by);
    printf("funct7: %s\n", inst.funct7);
    printf("funct3: %s\n", inst.funct3);

    return 0;
}
