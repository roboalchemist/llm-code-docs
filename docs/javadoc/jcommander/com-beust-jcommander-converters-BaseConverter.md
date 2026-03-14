Package com.beust.jcommander.converters

## Class BaseConverter<T>






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<T>









- 

All Implemented Interfaces:
`IStringConverter<T>`


Direct Known Subclasses:
`BigDecimalConverter`, `BooleanConverter`, `DoubleConverter`, `FloatConverter`, `IntegerConverter`, `ISO8601DateConverter`, `LongConverter`, `PathConverter`, `URIConverter`, `URLConverter`


---


```
public abstract class BaseConverter<T>
extends java.lang.Object
implements IStringConverter<T>
```

Base class for converters that store the name of the option.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`BaseConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`protected java.lang.String`
`getErrorString​(java.lang.String value,
              java.lang.String to)`
 


`java.lang.String`
`getOptionName()`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`





    - 



### Methods inherited from interface com.beust.jcommander.IStringConverter

`convert`














- 





  - 



### Constructor Detail







    - 

#### BaseConverter


```
public BaseConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### getOptionName


```
public java.lang.String getOptionName()
```










    - 

#### getErrorString


```
protected java.lang.String getErrorString​(java.lang.String value,
                                          java.lang.String to)
```