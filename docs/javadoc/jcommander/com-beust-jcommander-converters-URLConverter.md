Package com.beust.jcommander.converters

## Class URLConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.net.URL>

  - 



    - com.beust.jcommander.converters.URLConverter












- 

All Implemented Interfaces:
`IStringConverter<java.net.URL>`


---


```
public class URLConverter
extends BaseConverter<java.net.URL>
```

Convert a string into a URI.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`URLConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.net.URL`
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

#### URLConverter


```
public URLConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.net.URL convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.