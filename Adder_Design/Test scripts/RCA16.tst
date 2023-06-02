output-file RCA4.out,
output-list x%B1.16.1 y%B1.16.1 z%B1.16.1 cout%B2.1.2;

set x %B0000000000000000,
set y %B0000000000000000,
eval,
output;

set x %B0000000000000000,
set y %B1111111111111111,
eval,
output;

set x %B1111111111111111,
set y %B1111111111111111,
eval,
output;

set x %B1010101010101010,
set y %B0101010101010101,
eval,
output;

set x %B0100101100100101,
set y %B0000110011100001,
eval,
output;

set x %B1001001100101010,
set y %B1111111111111111,
eval,
output;