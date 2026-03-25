Package com.beust.jcommander

## Interface IDefaultProvider







- 

All Known Implementing Classes:
`EnvironmentVariableDefaultProvider`, `PropertyFileDefaultProvider`


---


```
public interface IDefaultProvider
```

Allows the specification of default values.








- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`java.lang.String`
`getDefaultValueFor​(java.lang.String optionName)`
 














- 





  - 



### Method Detail







    - 

#### getDefaultValueFor


```
java.lang.String getDefaultValueFor​(java.lang.String optionName)
```


Parameters:
`optionName` - The name of the option as specified in the names() attribute
 of the @Parameter option (e.g. "-file").
Returns:
the default value for this option.