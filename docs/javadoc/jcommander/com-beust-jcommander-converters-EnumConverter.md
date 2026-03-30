Package com.beust.jcommander.converters

## Class EnumConverter<T extends java.lang.Enum<T>>






- java.lang.Object

- 



  - com.beust.jcommander.converters.EnumConverter<T>









- 

Type Parameters:
`T` - the enum type


All Implemented Interfaces:
`IStringConverter<T>`


---


```
public class EnumConverter<T extends java.lang.Enum<T>>
extends java.lang.Object
implements IStringConverter<T>
```

A converter to parse enums








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`EnumConverter​(java.lang.String optionName,
             java.lang.Class<T> clazz)`

Constructs a new converter.












  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`T`
`convert​(java.lang.String value)`
 





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### EnumConverter


```
public EnumConverter​(java.lang.String optionName,
                     java.lang.Class<T> clazz)
```

Constructs a new converter.

Parameters:
`optionName` - the option name for error reporting
`clazz` - the enum class













  - 



### Method Detail







    - 

#### convert


```
public T convert​(java.lang.String value)
```


Specified by:
`convert` in interface `IStringConverter<T extends java.lang.Enum<T>>`
Returns:
an object of type T created from the parameter value.