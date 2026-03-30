Package com.beust.jcommander.converters

## Class FileConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.FileConverter









- 

All Implemented Interfaces:
`IStringConverter<java.io.File>`


---


```
public class FileConverter
extends java.lang.Object
implements IStringConverter<java.io.File>
```

Convert a string into a file.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`FileConverter()`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.io.File`
`convert​(java.lang.String value)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### FileConverter


```
public FileConverter()
```













  - 



### Method Detail







    - 

#### convert


```
public java.io.File convert​(java.lang.String value)
```


Specified by:
`convert` in interface `IStringConverter<java.io.File>`
Returns:
an object of type T created from the parameter value.