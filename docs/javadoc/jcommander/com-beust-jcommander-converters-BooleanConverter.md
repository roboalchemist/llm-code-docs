Package com.beust.jcommander.converters

## Class BooleanConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.lang.Boolean>

  - 



    - com.beust.jcommander.converters.BooleanConverter












- 

All Implemented Interfaces:
`IStringConverter<java.lang.Boolean>`


---


```
public class BooleanConverter
extends BaseConverter<java.lang.Boolean>
```

Converts a string to a boolean.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`BooleanConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.Boolean`
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

#### BooleanConverter


```
public BooleanConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.lang.Boolean convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.