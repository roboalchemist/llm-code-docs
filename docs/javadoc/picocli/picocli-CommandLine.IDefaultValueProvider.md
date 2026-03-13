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

## Interface CommandLine.IDefaultValueProvider







- 

All Known Implementing Classes:
CommandLine.PropertiesDefaultProvider


Enclosing class:
CommandLine


---




```
public static interface CommandLine.IDefaultValueProvider
```

Provides default value for a command. Commands may configure a provider with the
 `CommandLine.Command.defaultValueProvider()` annotation attribute.

Since:
3.6









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`String`
`defaultValue(CommandLine.Model.ArgSpec argSpec)`
Returns the default value for an option or positional parameter or `null`.














- 




  - 



### Method Detail







    - 

#### defaultValue


```
String defaultValue(CommandLine.Model.ArgSpec argSpec)
             throws Exception
```

Returns the default value for an option or positional parameter or `null`.
 The returned value is converted to the type of the option/positional parameter
 via the same type converter used when populating this option/positional
 parameter from a command line argument.

Parameters:
`argSpec` - the option or positional parameter, never `null`
Returns:
the default value for the option or positional parameter, or `null` if
       this provider has no default value for the specified option or positional parameter
Throws:
`Exception` - when there was a problem obtaining the default value

















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