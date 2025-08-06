import yaml
import os
#Loading the riscv-unified-db/spec/std/isa/inst/B/clmul.yaml file
yaml_files = [f for f in os.listdir("input") if f.endswith(('.yaml', '.yml'))]

if not yaml_files:
    raise FileNotFoundError("No YAML files found in input folder")
for yaml_filename in yaml_files:
    yaml_file_path = os.path.join("input", yaml_filename)
    with open(yaml_file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    # Extracting the essential data

    name = data['name']
    long_name = data['long_name']
    assembly = data['assembly']
    # Joining the list from 'definedBy' into a single string
    defined_by = ", ".join(data['definedBy']['anyOf'])
    funct7 = data['format']['opcodes']['funct7']['value']
    funct3 = data['format']['opcodes']['funct3']['value']


    base = os.path.splitext(yaml_filename)[0]
    header_file = f"{base}.h"
    include_guard = base.upper() + "_H"

    with open(header_file, 'w+') as f:
        f.write(f"#ifndef {include_guard}\n#define {include_guard}\n\n")
        f.write("typedef struct {\n")
        f.write("    const char* name;\n")
        f.write("    const char* long_name;\n")
        f.write("    const char* assembly_format;\n")
        f.write("    const char* defined_by;\n")
        f.write("    const char* funct7;\n")
        f.write("    const char* funct3;\n")
        f.write("} Instruction;\n\n")

        f.write("const Instruction inst = {\n")
        f.write(f'    "{name}",\n')
        f.write(f'    "{long_name}",\n')
        f.write(f'    "{assembly}",\n')
        f.write(f'    "{defined_by}",\n')
        f.write(f'    "{funct7}",\n')
        f.write(f'    "{funct3}"\n')
        f.write("};\n\n")

        f.write(f"#endif // {include_guard}\n")

    print("C header file named as 'clmul.h' generated successfully.")