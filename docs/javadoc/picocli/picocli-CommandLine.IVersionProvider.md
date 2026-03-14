JavaScript is disabled on your browser.





Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method









picocli

## Interface CommandLine.IVersionProvider







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IVersionProvider
```

Provides version information for a command. Commands may configure a provider with the
 `CommandLine.Command.versionProvider()` annotation attribute.

Since:
2.2









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`String[]`
`getVersion()`
Returns version information for a command.














- 




  - 



### Method Detail







    - 

#### getVersion


```
String[] getVersion()
             throws Exception
```

Returns version information for a command.

Returns:
version information (each string in the array is displayed on a separate line)
Throws:
`Exception` - an exception detailing what went wrong when obtaining version information

















Skip navigation links






- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help







- Prev Class

- Next Class





- Frames

- No Frames





- All Classes









- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method





- Detail: 

- Field | 

- Constr | 

- Method