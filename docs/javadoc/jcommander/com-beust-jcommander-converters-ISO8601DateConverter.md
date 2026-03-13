Package com.beust.jcommander.converters

## Class ISO8601DateConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.util.Date>

  - 



    - com.beust.jcommander.converters.ISO8601DateConverter












- 

All Implemented Interfaces:
`IStringConverter<java.util.Date>`


---


```
public class ISO8601DateConverter
extends BaseConverter<java.util.Date>
```

Converts a String to a Date.
 TODO Modify to work with all valid ISO 8601 date formats (currently only works with yyyy-MM-dd).








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`ISO8601DateConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.util.Date`
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

#### ISO8601DateConverter


```
public ISO8601DateConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.util.Date convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.