Package com.beust.jcommander.converters

## Class IntegerConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.lang.Integer>

  - 



    - com.beust.jcommander.converters.IntegerConverter












- 

All Implemented Interfaces:
`IStringConverter<java.lang.Integer>`


---


```
public class IntegerConverter
extends BaseConverter<java.lang.Integer>
```

Convert a string to an integer.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`IntegerConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.Integer`
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

#### IntegerConverter


```
public IntegerConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.lang.Integer convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.