// Calculate location of dest register within register file and store in R15
@1025
D=A
@R15
M=D
// Store constant in dest
@5
D=A
@R15
A=M
M=D
// Calculate location of dest register within register file and store in R15
@1026
D=A
@R15
M=D
// Store constant in dest
@10
D=A
@R15
A=M
M=D
// Calculate location of src1 register within register file and store in R13
@1025
D=A
@R13
M=D
// Calculate location of src2 register within register file and store in R14
@1026
D=A
@R14
M=D
// Calculate location of dest register within register file and store in R15
@1025
D=A
@R15
M=D
// D <-- operand 1
@R13
A=M
D=M
// D <-- D + operand 2
@R14
A=M
D=D+M
// dest <-- D
@R15
A=M
M=D
// Calculate location of dest register within register file and store in R15
@1034
D=A
@R15
M=D
// Store constant in dest
@400
D=A
@R15
A=M
M=D
// Generate base + offset value and store in R13
@0
D=A
@1034
D=D+M
@R13
M=D
// Generate address for dest and store in R14
@1025
D=A
@R14
M=D
// Memory[base + offset] <-- dest
@R14
A=M
D=M
@R13
A=M
M=D
(THATS_ALL_FOLKS)
@THATS_ALL_FOLKS
0;JMP
