Package com.beust.jcommander

## Class UnixStyleUsageFormatter






- java.lang.Object

- 



  - com.beust.jcommander.DefaultUsageFormatter

  - 



    - com.beust.jcommander.UnixStyleUsageFormatter












- 

All Implemented Interfaces:
`IUsageFormatter`


---


```
public class UnixStyleUsageFormatter
extends DefaultUsageFormatter
```

A unix-style usage formatter. This works by overriding and modifying the output of
 `appendAllParametersDetails(StringBuilder, int, String, List)` which is inherited from
 `DefaultUsageFormatter`.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`UnixStyleUsageFormatter​(JCommander commander)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`void`
`appendAllParametersDetails​(java.lang.StringBuilder out,
                          int indentCount,
                          java.lang.String indent,
                          java.util.List<ParameterDescription> sortedParameters)`

Appends the details of all parameters in the given order to the argument string builder, indenting every
 line with indentCount-many indent.






    - 



### Methods inherited from class com.beust.jcommander.DefaultUsageFormatter

`appendCommands, appendMainLine, getCommandDescription, getI18nString, s, usage, usage, usage, usage, usage, wrapDescription, wrapDescription`





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### UnixStyleUsageFormatter


```
public UnixStyleUsageFormatter​(JCommander commander)
```













  - 



### Method Detail







    - 

#### appendAllParametersDetails


```
public void appendAllParametersDetails​(java.lang.StringBuilder out,
                                       int indentCount,
                                       java.lang.String indent,
                                       java.util.List<ParameterDescription> sortedParameters)
```

Appends the details of all parameters in the given order to the argument string builder, indenting every
 line with indentCount-many indent.

Overrides:
`appendAllParametersDetails` in class `DefaultUsageFormatter`
Parameters:
`out` - the builder to append to
`indentCount` - the amount of indentation to apply
`indent` - the indentation
`sortedParameters` - the parameters to append to the builder