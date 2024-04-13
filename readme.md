# Assembly-Like Interpreted Language
The name tells it all.

# Syntax
The language is like assembly but it can be on one line.

# Keyword
|keyword|usage|how to use|
|----|----|---|
|`st[a x y z]`|stores a number to `[a x y z]`|`st[a x y x] [@<0 .. 31> number]`|
|`ld[a x y z]`|load a from `a` to a register(?)|`ld[a x y z] @<0 .. 31>`|
|`str`|moves a number to a register(?)|`str @<0 .. 31> number`|
|`cmp`|compares `a` to a number|`cmp [@<0 .. 31> number]`|
|`j[mp eq ne lt le gt ge]`|jumps to a label/line (with condition)|`j[mp eq ne lt le gt ge] [label linenum]`|
|`inc`|increase `a` once|`inc`|
|`dec`|decrease `a` once|^^^|
