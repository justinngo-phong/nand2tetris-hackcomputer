// sort.asm by Justin Ngo, 11/3/2022

@22
M=1		// CONTINUE = 1 (RAM[22] contains continue)

// while loop
(WHILE)	
	@22
	D=M-1 	// D = continue - 1
	@END
	D;JLT	// end loop if CONTINUE < 1 (aka CONTINUE = 0)
	
	@22
	M=0
	
	// start for loop
	@23
	M=0		// i = 0, RAM[23] contains i
	(FOR)
		@17
		D=M-1	// D = n-1
		@23
		D=M-D	// D = i - (n-1)
		@WHILE
		D;JGE	// jump back to start of while loop if i >= n-1, aka for loop i ends
		
		// Compare A[i] to A[i+1]
		@23
		D=M		// D = i
		@16
		D=M+D	// D = idx + i (A[i] pointer)
		@18
		M=D		// M = D -> RAM[18] contains address of A[i]
		A=M 	// set address to A[i] address
		D=M 	// D contains value of A[i]
		@20 	// temp location for A[i]
		M=D 	// RAM[20] contains value of A[i]
		@18
		D=M 	// D contains idx + i
		@19
		M=D+1	// M = idx + i + 1 -> RAM[19] contains address of A[i+1]
		A=M 	// set address to A[i+1]
		D=M 	// D contains value of A[i+1]
		@20
		D=M-D 	// D contains value of A[i] - A[i+1]
		@SWAP	
		D;JGT	// check if A[i] > A[i+1]
		@INCREMENT
		0;JMP	// jump to increment i step
		
		(SWAP)
			@19
			A=M 	// set address to A[i+1] address
			D=M 	// D contains value of A[i+1]
			@18
			A=M 	// set address to A[i] address
			M=D 	// set A[i] value to A[i+1] value
			@20
			D=M 	// D contains value of A[i]
			@19
			A=M 	// set address to A[i+1] address
			M=D 	// set A[i+1] value to A[i] value
			@22
			M=1 	// 22 = 1
			@INCREMENT
			0;JMP
		
		(INCREMENT)
		@23
		M=M+1	// i++
		@FOR
		0;JMP	// jump back to start of for loop
(END)

@END
0;JMP