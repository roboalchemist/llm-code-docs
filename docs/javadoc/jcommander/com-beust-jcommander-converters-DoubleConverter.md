Package com.beust.jcommander.converters

## Class DoubleConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.lang.Double>

  - 



    - com.beust.jcommander.converters.DoubleConverter












- 

All Implemented Interfaces:
`IStringConverter<java.lang.Double>`


---


```
public class DoubleConverter
extends BaseConverter<java.lang.Double>
```

Convert a string to a double.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`DoubleConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.Double`
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

#### DoubleConverter


```
public DoubleConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.lang.Double convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.