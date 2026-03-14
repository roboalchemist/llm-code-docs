Package com.beust.jcommander.converters

## Class PathConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.nio.file.Path>

  - 



    - com.beust.jcommander.converters.PathConverter












- 

All Implemented Interfaces:
`IStringConverter<java.nio.file.Path>`


---


```
public class PathConverter
extends BaseConverter<java.nio.file.Path>
```

Convert a string into a path.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`PathConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.nio.file.Path`
`convert​(java.lang.String value)`
 





    - 



### Methods inherited from class com.beust.jcommander.converters.BaseConverter

`getErrorString, getOptionName`





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### PathConverter


```
public PathConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.nio.file.Path convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.