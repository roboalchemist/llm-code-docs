Package com.beust.jcommander

## Interface IValueValidator<T>







- 

All Known Implementing Classes:
`NoValueValidator`


---


```
public interface IValueValidator<T>
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
        T value)`

Validate the parameter.















- 





  - 



### Method Detail









    - 

#### validate


```
void validate​(java.lang.String name,
              T value)
       throws ParameterException
```

Validate the parameter.

Parameters:
`name` - The name of the parameter (e.g. "-host").
`value` - The value of the parameter that we need to validate
Throws:
`ParameterException` - Thrown if the value of the parameter is invalid.