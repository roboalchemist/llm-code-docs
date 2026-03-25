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

## Enum CommandLine.Help.Visibility






- java.lang.Object

- 



  - java.lang.Enum<CommandLine.Help.Visibility>

  - 



    - picocli.CommandLine.Help.Visibility












- 

All Implemented Interfaces:
Serializable, Comparable<CommandLine.Help.Visibility>


Enclosing class:
CommandLine.Help


---




```
public static enum CommandLine.Help.Visibility
extends Enum<CommandLine.Help.Visibility>
```

Controls the visibility of certain aspects of the usage help message.








- 




  - 



### Enum Constant Summary


Enum Constants 

Enum Constant and Description


`ALWAYS` 


`NEVER` 


`ON_DEMAND` 









  - 



### Method Summary


All Methods Static Methods Concrete Methods 

Modifier and Type
Method and Description


`static CommandLine.Help.Visibility`
`valueOf(String name)`
Returns the enum constant of this type with the specified name.



`static CommandLine.Help.Visibility[]`
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

#### ALWAYS


```
public static final CommandLine.Help.Visibility ALWAYS
```










    - 

#### NEVER


```
public static final CommandLine.Help.Visibility NEVER
```










    - 

#### ON_DEMAND


```
public static final CommandLine.Help.Visibility ON_DEMAND
```











  - 



### Method Detail







    - 

#### values


```
public static CommandLine.Help.Visibility[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared.  This method may be used to iterate
over the constants as follows:

```

for (CommandLine.Help.Visibility c : CommandLine.Help.Visibility.values())
    System.out.println(c);

```


Returns:
an array containing the constants of this enum type, in the order they are declared










    - 

#### valueOf


```
public static CommandLine.Help.Visibility valueOf(String name)
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