// divide.asm by Justin Ngo, 11/3/2022

// q = 0
@18
M=0

// if b == 0, jump to end
@17
D=M
@END
D;JEQ

// r = a
@16
D=M		// D = a
@19
M=D		// r = D = a

// compare r to b, go to while loop if r >= b, else go to end
@17
D=M 	// D = b
@19
D=M-D	// D = r-b
@END
D;JLT	// jump to end if r<b

// while loop
(WHILE)
	@17
	D=M 	// D = b
	@19
	MD=M-D	// r,D = r-b	
	@REMAINDER
	D;JLT	// jump to remainder handler function
	@18
	M=M+1	// q = q+1	
	@WHILE
	0;JMP	// go back to start of while loop
(REMAINDER)
	@17
	D=M		// D = b
	@19
	M=M+D 	// r = r+b (because r is now negative)
(END)

// infinite end
@END
0;JMP
	