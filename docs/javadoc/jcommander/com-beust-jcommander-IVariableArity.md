Package com.beust.jcommander

## Interface IVariableArity







- 

---


```
public interface IVariableArity
```

Must be implemented by argument classes that contain at least one
 \@Parameter with "variableArity = true".








- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`int`
`processVariableArity​(java.lang.String optionName,
                    java.lang.String[] options)`
 














- 





  - 



### Method Detail







    - 

#### processVariableArity


```
int processVariableArity​(java.lang.String optionName,
                         java.lang.String[] options)
```


Parameters:
`optionName` - the name of the option to process.
`options` - the entire list of options.
Returns:
how many options were processed.