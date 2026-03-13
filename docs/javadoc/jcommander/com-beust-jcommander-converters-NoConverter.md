Package com.beust.jcommander.converters

## Class NoConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.NoConverter









- 

All Implemented Interfaces:
`IStringConverter<java.lang.String>`


---


```
public class NoConverter
extends java.lang.Object
implements IStringConverter<java.lang.String>
```

Default value for a converter when none is specified.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`NoConverter()`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.String`
`convert​(java.lang.String value)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### NoConverter


```
public NoConverter()
```













  - 



### Method Detail







    - 

#### convert


```
public java.lang.String convert​(java.lang.String value)
```


Specified by:
`convert` in interface `IStringConverter<java.lang.String>`
Returns:
an object of type T created from the parameter value.