Package com.beust.jcommander.converters

## Class FloatConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.lang.Float>

  - 



    - com.beust.jcommander.converters.FloatConverter












- 

All Implemented Interfaces:
`IStringConverter<java.lang.Float>`


---


```
public class FloatConverter
extends BaseConverter<java.lang.Float>
```

Convert a string to a float.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`FloatConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.Float`
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

#### FloatConverter


```
public FloatConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.lang.Float convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.