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

- Enum Constants | 

- Field | 

- Method





- Detail: 

- Enum Constants | 

- Field | 

- Method









picocli

## Enum CommandLine.Help.Column.Overflow






- java.lang.Object

- 



  - java.lang.Enum<CommandLine.Help.Column.Overflow>

  - 



    - picocli.CommandLine.Help.Column.Overflow












- 

All Implemented Interfaces:
Serializable, Comparable<CommandLine.Help.Column.Overflow>


Enclosing class:
CommandLine.Help.Column


---




```
public static enum CommandLine.Help.Column.Overflow
extends Enum<CommandLine.Help.Column.Overflow>
```

Policy for handling text that is longer than the column width:
  span multiple columns, wrap to the next row, or simply truncate the portion that doesn't fit.








- 




  - 



### Enum Constant Summary


Enum Constants 

Enum Constant and Description


`SPAN` 


`TRUNCATE` 


`WRAP` 









  - 



### Method Summary


All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description


`static CommandLine.Help.Column.Overflow`
`valueOf(String name)`
Returns the enum constant of this type with the specified name.



`static CommandLine.Help.Column.Overflow[]`
`values()`
Returns an array containing the constants of this enum type, in
the order they are declared.






    - 



### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`





    - 



### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`













- 




  - 



### Enum Constant Detail







    - 

#### TRUNCATE


```
public static final CommandLine.Help.Column.Overflow TRUNCATE
```










    - 

#### SPAN


```
public static final CommandLine.Help.Column.Overflow SPAN
```










    - 

#### WRAP


```
public static final CommandLine.Help.Column.Overflow WRAP
```











  - 



### Method Detail







    - 

#### values


```
public static CommandLine.Help.Column.Overflow[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared.  This method may be used to iterate
over the constants as follows:

```

for (CommandLine.Help.Column.Overflow c : CommandLine.Help.Column.Overflow.values())
    System.out.println(c);

```


Returns:
an array containing the constants of this enum type, in the order they are declared










    - 

#### valueOf


```
public static CommandLine.Help.Column.Overflow valueOf(String name)
```

Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type.  (Extraneous whitespace characters are 
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum type has no constant with the specified name
`NullPointerException` - if the argument is null

















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

- Enum Constants | 

- Field | 

- Method





- Detail: 

- Enum Constants | 

- Field | 

- Method