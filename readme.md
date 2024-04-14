# Assembly-Like Interpreted Language
The name tells it all.

# Syntax
The language is like assembly but it can be on one line.

# Keyword
|keyword|usage|arguments|
|----|----|---|
|`st[a x y z]`|stores a number to `[a x y z]`|register \| number|
|`ld[a x y z]`|load a from `a` to a register|a register|
|`str`|moves a number to a register|a register and a number|
|`cmp`|compares `a` to a number|a number|
|`j[mp eq ne lt le gt ge]`|jumps to a label/line (with additional condition)|a label|
|`inc`|increase `a` once|NONE|
|`dec`|decrease `a` once|NONE|
