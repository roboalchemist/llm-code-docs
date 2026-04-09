Package com.beust.jcommander

## Interface IParameterValidator







- 

All Known Subinterfaces:
`IParameterValidator2`


All Known Implementing Classes:
`NoValidator`, `PositiveInteger`


---


```
public interface IParameterValidator
```

The class used to validate parameters.








- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`void`
`validate​(java.lang.String name,
        java.lang.String value)`

Validate the parameter.















- 





  - 



### Method Detail







    - 

#### validate


```
void validate​(java.lang.String name,
              java.lang.String value)
       throws ParameterException
```

Validate the parameter.

Parameters:
`name` - The name of the parameter (e.g. "-host").
`value` - The value of the parameter that we need to validate
Throws:
`ParameterException` - Thrown if the value of the parameter is invalid.