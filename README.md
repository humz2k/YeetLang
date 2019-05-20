# YeetLang

### What is YeetLang?

YeetLang is an esoteric programming language that centers around the word **"yeet"**. All syntax contains either the word yeet or words associated with yeet.



### Initializing variables

All variables must be initialized in the first line of the file, separated by semicolons with no spaces.

For example:

```
a;b;c;variable;variable_1
```



### Assigning variables

Assignments are done with the keyword `yoink`. You can yoink together two values, setting one equal to the other. The value on the right of the yoink is the value that will be yoinked from, and the value on the left of the yoink is the value that will be yoinked to.

For example:

```
b yoink 5
```

will set variable b to value 5.

You can yoink from more complicated expressions:

```
b yoink 5+5/2
```

You can also yoink from other variables. In order to do this, you have to get the contents of the variable. This is done by surrounding the variable in square brackets - `[b]`. This will give the contents of variable b. This can be done infinitely - `[[[[b]]]]` will point to the contents of the contents of the contents of the contents of the variable b. This can be used for indirect addressing or arrays.

```
b yoink [c] + 5
```

If we just set the variable b to the variable c,

```
b yoink c
```

we make the variable b point to variable c. So, the contents of the contents of b will be the contents of c. We can use this to set the value of c thus:

```
b yoink c
[b] yoink 5
```

This will set the contents of c to 5. Again, this can be repeated indefinitely.



### Outputting variables

You can output variables using the keyword `yeet`. This will output the ascii character with the decimal code contained in the variable after the keyword. 

For example:

```
b yoink 65
yeet b
```

This will print `A`.



### Inputting variables

You can input one character to a variable using the keyword `yote`. This will take a single character as input, and set the variable after the keyword to the ascii code of the inputted value.

For example:

```
yote b
yeet b
```

With this, if I pressed the key `a`, an `a` would be printed to the screen.



### Comparisons

The syntax for comparisons are as follows:

```
expression comparator expression; jump_if_true; jump_if_false
```

The spaces after the semi-colons are important.

If the comparison is true, the interpreter will jump to wherever the words `jump_if_true` appear in the program. If the comparison is false, the interpreter will jump to wherever the words `jump_if_false` appear in the program. Any keywords can be used, so multiple comparisons can happen.

The different comparators and their equivalents are:

| YeetLang | Python |
| -------- | ------ |
| yeequals | ==     |
| yeeter   | >      |
| yoinker  | <      |

In an expression, referencing a variable will reference the *contents* of the variable - `b` will refer to the contents of the variable b.

For example, `b yeequals 5` will check if the contents of b are equal to 5.

A simple if statement would look like:

```
b yeequals 5; true; false
true
... do stuff
false
... do stuff
```

A simple loop would look like

```
false
b yoink [b] + 1
b yeequals 5; true; false
true
... continue
```



### Comments

Any line without a keyword is ignored by the interpreter, and is thus a comment.

