# -*- coding: utf-8 -*-
"""
Compiler back end for the Hack processor.
Translates from a register-based VM language to Hack assembly code.

Author: Naga Kandasamy
Date modified: June 3, 2022

Student name: Justin Ngo
Date modified: 12/7/2022
"""
import os
import sys

"""Generate some epilogue code that places the program, upon completion, into 
an infinite loop. 
"""
def generate_exit_code():
    s = []
    s.append('(THATS_ALL_FOLKS)')
    s.append('@THATS_ALL_FOLKS')
    s.append('0;JMP')
    return s

d0 = 1024
"""Generate assembly code for:
    add dest src1 src2
"""
def generate_add_code(dest, src1, src2):
    global d0
    s = [] 
    
    src_reg_1 = src1[1:]    # Source 1 register number
    src_reg_2 = src2[1:]    # Source 2 register number
    dest_reg = dest[1:]     # Dest register number
    
    s.append('// Calculate location of src1 register within register file and store in R13')
    s.append('@{}'.format(d0 + int(src_reg_1)))
    s.append('D=A')
    s.append('@R13')
    s.append('M=D')
    
    s.append('// Calculate location of src2 register within register file and store in R14')
    s.append('@{}'.format(d0 + int(src_reg_2)))
    s.append('D=A')
    s.append('@R14')
    s.append('M=D')
    
    s.append('// Calculate location of dest register within register file and store in R15')
    s.append('@{}'.format(d0 + int(dest_reg)))
    s.append('D=A')
    s.append('@R15')
    s.append('M=D')
    
    s.append('// D <-- operand 1')
    s.append('@R13')
    s.append('A=M')
    s.append('D=M')   
    
    s.append('// D <-- D + operand 2')
    s.append('@R14')
    s.append('A=M')
    s.append('D=D+M')    
    
    s.append('// dest <-- D')
    s.append('@R15')
    s.append('A=M')
    s.append('M=D')   
    
    return s
    

"""Generate assembly code for:
    addi dest src1 constant
"""
def generate_addi_code(dest, src1, constant):
    global d0
    s = [] 
    
    src_reg_1 = src1[1:]    # Source 1 register number
    dest_reg = dest[1:]     # Destination register number
    
    s.append('// Calculate location of src1 register within register file and store in R13')
    s.append('@{}'.format(d0 + int(src_reg_1)))
    s.append('D=A')
    s.append('@R13')
    s.append('M=D')
      
    s.append('// Calculate location of dest register within register file and store in R15')
    s.append('@{}'.format(d0 + int(dest_reg)))
    s.append('D=A')
    s.append('@R15')
    s.append('M=D')
    
    s.append('// D <-- operand 1')
    s.append('@R13')
    s.append('A=M')
    s.append('D=M')   
    
    s.append('// D <-- D + constant')
    s.append('@{}'.format(constant))
    s.append('D=D+A')
    
    s.append('// dest <-- D')
    s.append('@R15')
    s.append('A=M')
    s.append('M=D')      
    
    return s


"""Generate assembly code for:
    sub dest src1 src2
"""
def generate_sub_code(dest, src1, src2):
    global d0
    s = [] 
    src_reg_1 = src1[1:]
    src_reg_2 = src2[1:]
    dest_reg = dest[1:]

    s.append('// Calculate location of src1 register within register file and store in R13')
    s.append('@{}'.format(d0 + int(src_reg_1)))
    s.append('D=A')
    s.append('@R13')
    s.append('M=D')
    
    s.append('// Calculate location of src2 register within register file and store in R14')
    s.append('@{}'.format(d0 + int(src_reg_2)))
    s.append('D=A')
    s.append('@R14')
    s.append('M=D')
    
    s.append('// Calculate location of dest register within register file and store in R15')
    s.append('@{}'.format(d0 + int(dest_reg)))
    s.append('D=A')
    s.append('@R15')
    s.append('M=D')
    
    s.append('// D <-- operand 1')
    s.append('@R13')
    s.append('A=M')
    s.append('D=M')   
    
    s.append('// D <-- D - operand 2')
    s.append('@R14')
    s.append('A=M')
    s.append('D=D-M')    
    
    s.append('// dest <-- D')
    s.append('@R15')
    s.append('A=M')
    s.append('M=D')   

         
    return s
    

"""Generate assembly code for:
    subi dest src1 constant
"""
def generate_subi_code(dest, src1, constant):
    s = [] 
    
    src_reg_1 = src1[1:]
    dest_reg = dest[1:]

    s.append('// Calculate location of src1 register within register file and store in R13')
    s.append('@{}'.format(d0 + int(src_reg_1)))
    s.append('D=A')
    s.append('@R13')
    s.append('M=D')
      
    s.append('// Calculate location of dest register within register file and store in R15')
    s.append('@{}'.format(d0 + int(dest_reg)))
    s.append('D=A')
    s.append('@R15')
    s.append('M=D')
    
    s.append('// D <-- operand 1')
    s.append('@R13')
    s.append('A=M')
    s.append('D=M')   
    
    s.append('// D <-- D - constant')
    s.append('@{}'.format(constant))
    s.append('D=D-A')
    
    s.append('// dest <-- D')
    s.append('@R15')
    s.append('A=M')
    s.append('M=D')      
         
    return s


"""Generate assembly code for:
    load dest base offset
"""
def generate_load_code(dest, base, offset):
    global d0
    s = [] 
    
    base_reg = base[1:]
    dest_reg = dest[1:]
    
    s.append('// Generate base + offset value and store in R13')
    s.append('@{}'.format(offset))
    s.append('D=A')
    s.append('@{}'.format(d0 + int(base_reg)))
    s.append('D=D+M')
    s.append('@R13')
    s.append('M=D')
    
    s.append('// Generate address for dest and store in R14')
    s.append('@{}'.format(d0 + int(dest_reg)))
    s.append('D=A')
    s.append('@R14')
    s.append('M=D')
    
    s.append('// dest <-- Memory[base + offset]')
    s.append('@R13')
    s.append('A=M')
    s.append('D=M')
    s.append('@R14')
    s.append('A=M')
    s.append('M=D')
         
    return s

"""Generate assembly code for:
    loadi dest constant
"""
def generate_loadi_code(dest, constant):
    global d0
    s = [] 
    dest_reg = dest[1:]
    
    s.append('// Calculate location of dest register within register file and store in R15')
    s.append('@{}'.format(d0 + int(dest_reg)))
    s.append('D=A')
    s.append('@R15')
    s.append('M=D')
    
    s.append('// Store constant in dest')
    s.append('@{}'.format(constant))
    s.append('D=A')
    s.append('@R15')
    s.append('A=M')
    s.append('M=D')
    
    return s

"""Generate assembly code for:
    store dest base offset
"""
def generate_store_code(dest, base, offset):
    global d0
    s = [] 
         
    base_reg = base[1:]
    dest_reg = dest[1:]
    
    s.append('// Generate base + offset value and store in R13')
    s.append('@{}'.format(offset))
    s.append('D=A')
    s.append('@{}'.format(d0 + int(base_reg)))
    s.append('D=D+M')
    s.append('@R13')
    s.append('M=D')
    
    s.append('// Generate address for dest and store in R14')
    s.append('@{}'.format(d0 + int(dest_reg)))
    s.append('D=A')
    s.append('@R14')
    s.append('M=D')
    
    s.append('// Memory[base + offset] <-- dest')
    s.append('@R14')
    s.append('A=M')
    s.append('D=M')
    s.append('@R13')
    s.append('A=M')
    s.append('M=D')
    
    return s

"""Translate a VM command/statement into the corresponding Hack assembly commands/statements.
"""
def translate(tokens):
    s = []
    
    if tokens[0] == 'add':
        s = generate_add_code(tokens[1], tokens[2], tokens[3])      # Generate code for add
        
    elif tokens[0] == 'addi':
        s = generate_addi_code(tokens[1], tokens[2], tokens[3])     # Generate code for addi
          
    elif tokens[0] == 'sub':
        s = generate_sub_code(tokens[1], tokens[2], tokens[3])      # Generate code for sub   
        
    elif tokens[0] == 'subi':
        s = generate_subi_code(tokens[1], tokens[2], tokens[3])     # Generate code for subi
        
    elif tokens[0] == 'load':
        s = generate_load_code(tokens[1], tokens[2], tokens[3])     # Generate code for load
          
    elif tokens[0] == 'loadi':
        s = generate_loadi_code(tokens[1], tokens[2])               # Generate code for loadi
        
    elif tokens[0] == 'store':
        s = generate_store_code(tokens[1], tokens[2], tokens[3])    # Generate code for store
    
    elif tokens[0] == 'end':
        s = generate_exit_code()
        
    else:
        print('translate: Unknown operation')           # Unknown operation 
    
    return s

"""Main translator code.
"""
def run_vm_translator(file_name):
    assembly_code = []
    
    with open(file_name, 'r') as f:
        for command in f:        
            print("Translating line:", command)
            tokens = (command.rstrip('\n')).split()
            
            # Ignore blank lines
            if not tokens:
                continue            
            
            if tokens[0] == '//':
                continue                                # Ignore comment       
            else:
                s = translate(tokens)
            
            if s:
                for i in s:
                    assembly_code.append(i)
            else:
                assembly_code = []
                return assembly_code
            
    
    return assembly_code

"""Main function."""
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: Python vm_translator.py file-name.vm")
        print("Example: Python vm_translator.py simple_add.vm")
    else:
        print("Translating VM file:", sys.argv[1])
        print()
        file_name_minus_extension, _ = os.path.splitext(sys.argv[1])
        output_file = file_name_minus_extension + '.asm'
        assembly_code = run_vm_translator(sys.argv[1])
        if assembly_code:
            print('Assembly code generated successfully');
            print('Writing output to file:', output_file)
            f = open(output_file, 'w')
            for s in assembly_code:
                f.write('%s\n' %s)
            f.close()
        else:
            print('Error generating assembly code')