Package com.beust.jcommander.converters

## Class InetAddressConverter






- java.lang.Object

- 



  - com.beust.jcommander.converters.InetAddressConverter









- 

All Implemented Interfaces:
`IStringConverter<java.net.InetAddress>`


---


```
public class InetAddressConverter
extends java.lang.Object
implements IStringConverter<java.net.InetAddress>
```

Converts `String`s to `InetAddress`'.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`InetAddressConverter()`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.net.InetAddress`
`convert​(java.lang.String host)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### InetAddressConverter


```
public InetAddressConverter()
```













  - 



### Method Detail







    - 

#### convert


```
public java.net.InetAddress convert​(java.lang.String host)
```


Specified by:
`convert` in interface `IStringConverter<java.net.InetAddress>`
Returns:
an object of type T created from the parameter value.