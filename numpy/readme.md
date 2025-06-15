store arrays 1d,2d,3d
lists are slow. numpy is fast
why?
numpy uses fixed types 
list takes - size reference count, obj type, obj value
so it takes more binary which is of 8 bytes whereas in numpy it is just 4 bits

why numpy over lists?
> faster to read. takes less bytes of memory
> no type checking
> utilises contiguous memory. uses simd single instr mul data vector processing. effective cache utilization


difference
List has insertion, deletion, appending, concatenation etc.
numpy does all this but with a lot more
numpy does item wise arithemetic

Applications
> matlab replacement
> plotting (matplot lib)
> backend (pandas, connect 4, digital photography)
> Machine learning
