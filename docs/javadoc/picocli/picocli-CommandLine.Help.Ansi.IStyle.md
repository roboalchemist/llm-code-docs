JavaScript is disabled on your browser.





Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method









picocli

## Interface CommandLine.Help.Ansi.IStyle







- 

All Known Implementing Classes:
CommandLine.Help.Ansi.Style


Enclosing class:
CommandLine.Help.Ansi


---




```
public static interface CommandLine.Help.Ansi.IStyle
```

Defines the interface for an ANSI escape sequence.








- 




  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`static String`
`CSI`
The Control Sequence Introducer (CSI) escape sequence "\u001b[".










  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`String`
`off()`
Returns the ANSI escape code for turning this style off.



`String`
`on()`
Returns the ANSI escape code for turning this style on.














- 




  - 



### Field Detail







    - 

#### CSI


```
static final String CSI
```

The Control Sequence Introducer (CSI) escape sequence "\u001b[".

See Also:
Constant Field Values











  - 



### Method Detail







    - 

#### on


```
String on()
```

Returns the ANSI escape code for turning this style on.

Returns:
the ANSI escape code for turning this style on










    - 

#### off


```
String off()
```

Returns the ANSI escape code for turning this style off.

Returns:
the ANSI escape code for turning this style off

















Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method