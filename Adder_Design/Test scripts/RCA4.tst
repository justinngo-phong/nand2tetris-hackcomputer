output-file RCA4.out,
output-list x%B1.4.1 y%B1.4.1 cin%B2.1.2 z%B1.4.1 cout%B2.1.2;

set x %B0000,
set y %B0000,
set cin 0,
eval, 
output;

set x %B0000,
set y %B1111,
set cin 0,
eval, 
output;

set x %B1010,
set y %B1010,
set cin 0,
eval, 
output;

set x %B1010,
set y %B0101,
set cin 0,
eval, 
output;

set x %B1111,
set y %B1111,
set cin 0,
eval, 
output;

