// mult.asm by Justin Ngo, 11/3/2022

// c = 0
@18
M = 0

// compare b to 0
// if b > 0, jump to while
@17
D=M
@WHILE
D;JGT

// if b <= 0, jump to end
@END
0;JMP

// while loop
(WHILE)
	@16
	D=M
	@18
	M=M+D
	@17
	M=M-1
	@17
	D=M
	@WHILE
	D;JGT
(END)

@END
0;JMP