#include <stdio.h>
#include "clmul_v2.h"
int main() {
    printf("name: %s\n", clmul_inst.name);
    printf("long_name: %s\n", clmul_inst.long_name);
    printf("assembly_format: %s\n", clmul_inst.assembly_format);
    printf("defined_by: %s\n", clmul_inst.defined_by);
    printf("funct7: %s\n", clmul_inst.funct7);
    printf("funct3: %s\n", clmul_inst.funct3);

    return 0;
}