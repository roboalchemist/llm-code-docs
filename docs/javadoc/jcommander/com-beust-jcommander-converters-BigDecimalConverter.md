Package com.beust.jcommander.converters

## Class BigDecimalConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.math.BigDecimal>

  - 



    - com.beust.jcommander.converters.BigDecimalConverter












- 

All Implemented Interfaces:
`IStringConverter<java.math.BigDecimal>`


---


```
public class BigDecimalConverter
extends BaseConverter<java.math.BigDecimal>
```

Converts a String to a BigDecimal.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`BigDecimalConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.math.BigDecimal`
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

#### BigDecimalConverter


```
public BigDecimalConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.math.BigDecimal convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.