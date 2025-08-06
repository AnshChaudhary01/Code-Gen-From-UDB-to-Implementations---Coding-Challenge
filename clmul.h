#ifndef CLMUL_H
#define CLMUL_H

typedef struct {
    const char* name;
    const char* long_name;
    const char* assembly_format;
    const char* defined_by;
    const char* funct7;
    const char* funct3;
} Instruction;

const Instruction inst = {
    "clmul",
    "Carry-less multiply (low-part)",
    "xd, xs1, xs2",
    "Zbc, Zbkc",
    "5",
    "1"
};

#endif // CLMUL_H
