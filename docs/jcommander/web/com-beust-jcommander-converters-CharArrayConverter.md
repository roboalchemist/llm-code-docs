Package com.beust.jcommander.converters

## Class CharArrayConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.CharArrayConverter









- 

All Implemented Interfaces:
`IStringConverter<char[]>`


---


```
public class CharArrayConverter
extends java.lang.Object
implements IStringConverter<char[]>
```

Converts a String to a char[].








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`CharArrayConverter()`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`char[]`
`convert​(java.lang.String value)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### CharArrayConverter


```
public CharArrayConverter()
```













  - 



### Method Detail







    - 

#### convert


```
public char[] convert​(java.lang.String value)
```


Specified by:
`convert` in interface `IStringConverter<char[]>`
Returns:
an object of type T created from the parameter value.