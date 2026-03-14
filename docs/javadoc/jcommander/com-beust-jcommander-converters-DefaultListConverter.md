Package com.beust.jcommander.converters

## Class DefaultListConverter<T>






- java.lang.Object

- 



  - com.beust.jcommander.converters.DefaultListConverter<T>









- 

Type Parameters:
`T` - the element type


All Implemented Interfaces:
`IStringConverter<java.util.List<T>>`


---


```
public class DefaultListConverter<T>
extends java.lang.Object
implements IStringConverter<java.util.List<T>>
```

A converter to obtain a list of elements.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`DefaultListConverter​(IParameterSplitter splitter,
                    IStringConverter<T> converter)`

Constructs a new converter.












  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.util.List<T>`
`convert​(java.lang.String value)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### DefaultListConverter


```
public DefaultListConverter​(IParameterSplitter splitter,
                            IStringConverter<T> converter)
```

Constructs a new converter.

Parameters:
`splitter` - to split value into list of arguments
`converter` - to convert list of arguments to target element type













  - 



### Method Detail







    - 

#### convert


```
public java.util.List<T> convert​(java.lang.String value)
```


Specified by:
`convert` in interface `IStringConverter<T>`
Returns:
an object of type T created from the parameter value.