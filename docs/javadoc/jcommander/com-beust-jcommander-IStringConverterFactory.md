Package com.beust.jcommander

## Interface IStringConverterFactory







- 

All Known Implementing Classes:
`DefaultConverterFactory`


---


```
public interface IStringConverterFactory
```

A factory for IStringConverter. This interface lets you specify your
 converters in one place instead of having them repeated all over
 your argument classes.

See Also:
`IStringConverterInstanceFactory`









- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`java.lang.Class<? extends IStringConverter<?>>`
`getConverter​(java.lang.Class<?> forType)`
 














- 





  - 



### Method Detail







    - 

#### getConverter


```
java.lang.Class<? extends IStringConverter<?>> getConverter​(java.lang.Class<?> forType)
```