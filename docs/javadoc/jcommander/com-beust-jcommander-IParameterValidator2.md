Package com.beust.jcommander

## Interface IParameterValidator2







- 

All Superinterfaces:
`IParameterValidator`


---


```
public interface IParameterValidator2
extends IParameterValidator
```









- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`void`
`validate​(java.lang.String name,
        java.lang.String value,
        ParameterDescription pd)`

Validate the parameter.






    - 



### Methods inherited from interface com.beust.jcommander.IParameterValidator

`validate`














- 





  - 



### Method Detail







    - 

#### validate


```
void validate​(java.lang.String name,
              java.lang.String value,
              ParameterDescription pd)
       throws ParameterException
```

Validate the parameter.

Parameters:
`name` - The name of the parameter (e.g. "-host").
`value` - The value of the parameter that we need to validate
`pd` - The description of this parameter
Throws:
`ParameterException` - Thrown if the value of the parameter is invalid.