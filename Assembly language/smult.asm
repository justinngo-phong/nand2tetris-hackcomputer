// smult.asm by Justin Ngo, 11/3/2022

// c = 0
@18
M = 0

// compare b to 0
// if b > 0, jump to while
@17
D=M
@WHILE_POSITIVE
D;JGT

// if b <= 0, jump to end
@WHILE_NEGATIVE
D;JLT

// while loop
(WHILE_POSITIVE)
	@16
	D=M		// D = a
	@18
	M=M+D	// c = c + a
	@17
	M=M-1	// b = b - 1
	@17
	D=M		// jump back to start of while if b > 0
	@WHILE_POSITIVE
	D;JGT
	@END
	0;JMP	// else jump to end
(WHILE_NEGATIVE)
	@16
	D=M		// D = a
	@18
	M=M-D	// c = c - a
	@17
	M=M+1	// b = b+1
	@17
	D=M		// jump back to start of while negative if b < 0
	@WHILE_NEGATIVE
	D;JLT
	@END
	0;JMP	// else jump to end
(END)

@END
0;JMP