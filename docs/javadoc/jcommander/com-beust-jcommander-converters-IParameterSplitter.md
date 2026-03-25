Package com.beust.jcommander.converters

## Interface IParameterSplitter







- 

All Known Implementing Classes:
`CommaParameterSplitter`


---


```
public interface IParameterSplitter
```

Convert a string representing several parameters (e.g. "a,b,c" or "d/e/f") into a
 list of arguments ([a,b,c] and [d,e,f]).








- 





  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description


`java.util.List<java.lang.String>`
`split​(java.lang.String value)`
 














- 





  - 



### Method Detail







    - 

#### split


```
java.util.List<java.lang.String> split​(java.lang.String value)
```