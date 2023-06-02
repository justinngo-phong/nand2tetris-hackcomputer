// lshift.asm by Justin Ngo, 11/3/2022

// set result to A
@16
D=M		// D = a
@18
M=D

(WHILE)
	@17
	MD=M-1		// s = s-1
	@END
	D;JLT		// if s < 0, jump to end
	@18
	D=M			// D = a
	M=M+D		// R[18] = 2*a
	@WHILE
	0;JMP		// jump back to start of while loop
(END)

@END
0;JMP