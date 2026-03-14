Package com.beust.jcommander

## Interface IStringConverter<T>







- 

All Known Implementing Classes:
`BaseConverter`, `BigDecimalConverter`, `BooleanConverter`, `CharArrayConverter`, `DefaultListConverter`, `DoubleConverter`, `EnumConverter`, `FileConverter`, `FloatConverter`, `InetAddressConverter`, `IntegerConverter`, `ISO8601DateConverter`, `LongConverter`, `NoConverter`, `PathConverter`, `StringConverter`, `URIConverter`, `URLConverter`


---


```
public interface IStringConverter<T>
```

An interface that converts strings to any arbitrary type.
 
 If your class implements a constructor that takes a String, this
 constructor will be used to instantiate your converter and the
 parameter will receive the name of the option that's being parsed,
 which can be useful to issue a more useful error message if the
 conversion fails.
 
 You can also extend BaseConverter to make your life easier.








- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`T`
`convert​(java.lang.String value)`
 














- 





  - 



### Method Detail







    - 

#### convert


```
T convert​(java.lang.String value)
```


Returns:
an object of type T created from the parameter value.