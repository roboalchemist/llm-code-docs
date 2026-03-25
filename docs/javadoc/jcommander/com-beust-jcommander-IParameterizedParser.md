Package com.beust.jcommander

## Interface IParameterizedParser







- 

All Known Implementing Classes:
`DefaultParameterizedParser`


---


```
public interface IParameterizedParser
```

Thin interface allows the Parameterized parsing mechanism, which reflects an object to find the 
 JCommander annotations, to be replaced at runtime for cases where the source code cannot
 be directly annotated with JCommander annotations, but may have other annotations such as 
 JSON annotations that can be used to reflect as JCommander parameters.








- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`java.util.List<Parameterized>`
`parseArg​(java.lang.Object annotatedObj)`

Parses the given object for any command line related annotations and returns the list of 
 JCommander Parameterized definitions.















- 





  - 



### Method Detail







    - 

#### parseArg


```
java.util.List<Parameterized> parseArg​(java.lang.Object annotatedObj)
```

Parses the given object for any command line related annotations and returns the list of 
 JCommander Parameterized definitions.

Parameters:
`annotatedObj` - the object that contains the annotations.
Returns:
non-null List but may be empty