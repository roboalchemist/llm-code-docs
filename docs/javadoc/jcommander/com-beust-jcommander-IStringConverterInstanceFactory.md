Package com.beust.jcommander

## Interface IStringConverterInstanceFactory







- 

---


```
public interface IStringConverterInstanceFactory
```

A factory to create `IStringConverter` instances.

 This interface lets you specify your converters in one place instead of having them repeated all over your argument classes.

See Also:
`IStringConverterFactory`









- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`IStringConverter<?>`
`getConverterInstance​(Parameter parameter,
                    java.lang.Class<?> forType,
                    java.lang.String optionName)`

Obtain a converter instance for parsing `parameter` as type `forType`















- 





  - 



### Method Detail







    - 

#### getConverterInstance


```
IStringConverter<?> getConverterInstance​(Parameter parameter,
                                         java.lang.Class<?> forType,
                                         java.lang.String optionName)
```

Obtain a converter instance for parsing `parameter` as type `forType`

Parameters:
`parameter` - the parameter to parse
`forType` - the type class
`optionName` - the name of the option used on the command line
Returns:
a converter instance