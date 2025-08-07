import yaml
# reconstructed_cmul.yaml is the yaml we generated from c file with header file generated
# by python script which reads the input clmul.yaml
with open('reconstructed_cmul.yaml', 'r') as f:
    data = yaml.safe_load(f)

with open('clmul_v2.h', 'w') as f:
    f.write("#ifndef CLMUL_V2_H\n#define CLMUL_V2_H\n\n")
    f.write("typedef struct {\n")
    f.write("    const char* name;\n")
    f.write("    const char* long_name;\n")
    f.write("    const char* assembly_format;\n")
    f.write("    const char* defined_by;\n")
    f.write("    const char* funct7;\n")
    f.write("    const char* funct3;\n")
    f.write("} Instruction;\n\n")

    f.write("const Instruction clmul_inst = {\n")
    f.write(f'    "{data["name"]}",\n')
    f.write(f'    "{data["long_name"]}",\n')
    f.write(f'    "{data["assembly_format"]}",\n')
    f.write(f'    "{data["defined_by"]}",\n')
    f.write(f'    "{data["funct7"]}",\n')
    f.write(f'    "{data["funct3"]}"\n')
    f.write("};\n\n")

    f.write("#endif // CLMUL_V2_H\n")

print("C header file 'clmul_v2.h' generated successfully.")
