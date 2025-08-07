# Code-Gen-From-UDB-to-Implementations---Coding-Challenge

This task demonstrates a data transformation pipeline from YAML-based instruction specification (from the RISC-V Unified Database) to C header format, and back to YAML, ensuring reproducibility of the transformation process.

The workflow comprises:
1. YAML to C Header (read_yaml__generate_header.py , Python Script)
  It parses the YAML key and values and writes them in the header file as const strings inside the struct.
2. C Program: Header to YAML
  It reads the instruction data from the generated header(clmul.h) and emits it as YAML
3. Repeatability
  The emitted YAML is used as new input for the Python program, after repeating the pipeline, the final YAML will match the last input YAML.

YAML - Python script - C Header - C Program - YAML - Python script - C Header - C Program - YAML 
