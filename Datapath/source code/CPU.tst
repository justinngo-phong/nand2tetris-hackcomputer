load CPU.hdl,
output-file CPU.out,
compare-to CPU.cmp,
output-list time%S0.4.0 inM%D0.6.0 instruction%B0.16.0 reset%B2.1.2 outM%D1.6.0 writeM%B3.1.3 addressM%D0.5.0 pc%D0.5.0 DRegister[]%D1.6.1;


set instruction %B0011000000111001, // @12345
tick, output, tock, output;

set instruction %B1110110000010000, // D=A
tick, output, tock, output;

set instruction %B0101101110100000, // @23456
tick, output, tock, output;

set instruction %B1110010011010000, // D=D-A. Should cause no overflow
tick, output, tock, output;

set instruction %B0011000000111001, // @12345
tick, output, tock, output;

set instruction %B1110110000010000, // D=A
tick, output, tock, output;

set instruction %B0101101110100000, // @23456
tick, output, tock, output;

set instruction %B1110000010010000, // D=D+A. Should cause overflow
tick, output, tock, output;

set instruction %B0000000000000000, // @0
tick, output, tock, output;

set instruction %B1110001100000111, // D;JMP
tick, output, tock, output;

set instruction %B0011000000111001, // @12345
tick, output, tock, output;

set instruction %B1110110011010000, // D=-A
tick, output, tock, output;

set instruction %B0101101110100000, // @23456
tick, output, tock, output;

set instruction %B1110010011010000, // D=D-A. Should cause overflow 
tick, output, tock, output;

set instruction %B0011000000111001, // @12345
tick, output, tock, output;

set instruction %B1110110000010000, // D=A
tick, output, tock, output;

set instruction %B0101101110100000, // @23456
tick, output, tock, output;

set instruction %B1110000111010000, // D=A-D. Should cause no overflow
tick, output, tock, output;

set instruction %B0000000000010101, // @21
tick, output, tock, output;

set instruction %B1110000010010000, // D+A;jeq. Should cause no overflow
tick, output, tock, output;

set instruction %B0000000000000000, // @0
tick, output, tock, output;

set instruction %B1110001100000111, // D;JMP
tick, output, tock, output;

set instruction %B0011000000111001, // @12345
tick, output, tock, output;

set instruction %B1110110000010000, // D=A
tick, output, tock, output;

set instruction %B0000001111101000, // @1000
tick, output, tock, output;

set instruction %B1110001100001000, // M=D
tick, output, tock, output;

set instruction %B0101101110100000, // @23456
tick, output, tock, output;

set instruction %B1110110000010000, // D=A
tick, output, tock, output;

set instruction %B0000001111101000, // @1000
tick, output, tock, output;

set instruction %B1111000010010000, // D=D+M. Should cause overflow
set inM %B0011000000111001,
tick, output, tock, output;
