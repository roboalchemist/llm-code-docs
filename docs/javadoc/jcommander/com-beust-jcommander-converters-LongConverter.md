Package com.beust.jcommander.converters

## Class LongConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.lang.Long>

  - 



    - com.beust.jcommander.converters.LongConverter












- 

All Implemented Interfaces:
`IStringConverter<java.lang.Long>`


---


```
public class LongConverter
extends BaseConverter<java.lang.Long>
```

Convert a string to a long.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`LongConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.Long`
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

#### LongConverter


```
public LongConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.lang.Long convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.