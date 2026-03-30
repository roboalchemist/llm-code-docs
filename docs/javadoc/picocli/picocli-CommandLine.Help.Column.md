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

## Class CommandLine.Help.Column






- java.lang.Object

- 



  - picocli.CommandLine.Help.Column









- 

Enclosing class:
CommandLine.Help


---




```
public static class CommandLine.Help.Column
extends Object
```

Columns define the width, indent (leading number of spaces in a column before the value) and
 Overflow policy of a column in a TextTable.








- 




  - 



### Nested Class Summary


Nested Classes 

Modifier and Type
Class and Description


`static class `
`CommandLine.Help.Column.Overflow`
Policy for handling text that is longer than the column width:
  span multiple columns, wrap to the next row, or simply truncate the portion that doesn't fit.










  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`int`
`indent`
Indent (number of empty spaces at the start of the column preceding the text value)



`CommandLine.Help.Column.Overflow`
`overflow`
Policy that determines how to handle values larger than the column width.



`int`
`width`
Column width in characters










  - 



### Constructor Summary


Constructors 

Constructor and Description


`Column(int width,
      int indent,
      CommandLine.Help.Column.Overflow overflow)` 









  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`boolean`
`equals(Object obj)` 


`int`
`hashCode()` 


`String`
`toString()` 





    - 



### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### width


```
public final int width
```

Column width in characters









    - 

#### indent


```
public int indent
```

Indent (number of empty spaces at the start of the column preceding the text value)









    - 

#### overflow


```
public final CommandLine.Help.Column.Overflow overflow
```

Policy that determines how to handle values larger than the column width.










  - 



### Constructor Detail







    - 

#### Column


```
public Column(int width,
              int indent,
              CommandLine.Help.Column.Overflow overflow)
```











  - 



### Method Detail







    - 

#### equals


```
public boolean equals(Object obj)
```


Overrides:
`equals` in class `Object`










    - 

#### hashCode


```
public int hashCode()
```


Overrides:
`hashCode` in class `Object`










    - 

#### toString


```
public String toString()
```


Overrides:
`toString` in class `Object`

















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