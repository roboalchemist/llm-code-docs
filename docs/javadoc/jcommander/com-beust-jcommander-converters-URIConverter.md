Package com.beust.jcommander.converters

## Class URIConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.BaseConverter<java.net.URI>

  - 



    - com.beust.jcommander.converters.URIConverter












- 

All Implemented Interfaces:
`IStringConverter<java.net.URI>`


---


```
public class URIConverter
extends BaseConverter<java.net.URI>
```

Convert a string into a URI.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`URIConverter​(java.lang.String optionName)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.net.URI`
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

#### URIConverter


```
public URIConverter​(java.lang.String optionName)
```













  - 



### Method Detail







    - 

#### convert


```
public java.net.URI convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.