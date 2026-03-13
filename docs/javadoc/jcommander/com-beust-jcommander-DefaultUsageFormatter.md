Package com.beust.jcommander

## Class DefaultUsageFormatter






- java.lang.Object

- 



  - com.beust.jcommander.DefaultUsageFormatter









- 

All Implemented Interfaces:
`IUsageFormatter`


Direct Known Subclasses:
`UnixStyleUsageFormatter`


---


```
public class DefaultUsageFormatter
extends java.lang.Object
implements IUsageFormatter
```

The default usage formatter.








- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`DefaultUsageFormatter​(JCommander commander)`
 











  - 



### Method Summary


All Methods Static Methods Instance Methods Concrete Methods 

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



`void`
`appendCommands​(java.lang.StringBuilder out,
              int indentCount,
              int descriptionIndent,
              java.lang.String indent)`

Appends the details of all commands to the argument string builder, indenting every line with
 indentCount-many indent.



`void`
`appendMainLine​(java.lang.StringBuilder out,
              boolean hasOptions,
              boolean hasCommands,
              int indentCount,
              java.lang.String indent)`

Appends the main line segment of the usage to the argument string builder, indenting every
 line with indentCount-many indent.



`java.lang.String`
`getCommandDescription​(java.lang.String commandName)`

Returns the description of the command corresponding to the argument command name.



`static java.lang.String`
`getI18nString​(java.util.ResourceBundle bundle,
             java.lang.String key,
             java.lang.String def)`

Returns the internationalized version of the string if available, otherwise it returns def.



`static java.lang.String`
`s​(int count)`

Returns count-many spaces.



`void`
`usage​(java.lang.String commandName)`

Prints the usage to `JCommander.getConsole()` on the underlying commander instance.



`void`
`usage​(java.lang.StringBuilder out)`

Store the usage in the argument string builder.



`void`
`usage​(java.lang.StringBuilder out,
     java.lang.String indent)`

Stores the usage in the argument string builder, with the argument indentation.



`void`
`usage​(java.lang.String commandName,
     java.lang.StringBuilder out)`

Store the usage for the argument command in the argument string builder.



`void`
`usage​(java.lang.String commandName,
     java.lang.StringBuilder out,
     java.lang.String indent)`

Store the usage for the command in the argument string builder, indenting every line with the
 value of indent.



`void`
`wrapDescription​(java.lang.StringBuilder out,
               int indent,
               int currentLineIndent,
               java.lang.String description)`

Wrap a potentially long line to the value obtained by calling `JCommander.getColumnSize()` on the
 underlying commander instance.



`void`
`wrapDescription​(java.lang.StringBuilder out,
               int indent,
               java.lang.String description)`

Wrap a potentially long line to { @link #commander#getColumnSize()}.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`














- 





  - 



### Constructor Detail







    - 

#### DefaultUsageFormatter


```
public DefaultUsageFormatter​(JCommander commander)
```













  - 



### Method Detail







    - 

#### usage


```
public final void usage​(java.lang.String commandName)
```

Prints the usage to `JCommander.getConsole()` on the underlying commander instance.

Specified by:
`usage` in interface `IUsageFormatter`










    - 

#### usage


```
public final void usage​(java.lang.String commandName,
                        java.lang.StringBuilder out)
```

Store the usage for the argument command in the argument string builder.

Specified by:
`usage` in interface `IUsageFormatter`










    - 

#### usage


```
public final void usage​(java.lang.StringBuilder out)
```

Store the usage in the argument string builder.

Specified by:
`usage` in interface `IUsageFormatter`










    - 

#### usage


```
public final void usage​(java.lang.String commandName,
                        java.lang.StringBuilder out,
                        java.lang.String indent)
```

Store the usage for the command in the argument string builder, indenting every line with the
 value of indent.

Specified by:
`usage` in interface `IUsageFormatter`










    - 

#### usage


```
public void usage​(java.lang.StringBuilder out,
                  java.lang.String indent)
```

Stores the usage in the argument string builder, with the argument indentation. This works by appending
 each portion of the help in the following order. Their outputs can be modified by overriding them in a
 subclass of this class.

 

     
      - Main line - `appendMainLine(StringBuilder, boolean, boolean, int, String)`
     
      - Parameters - `appendAllParametersDetails(StringBuilder, int, String, List)`
     
      - Commands - `appendCommands(StringBuilder, int, int, String)`
 


Specified by:
`usage` in interface `IUsageFormatter`










    - 

#### appendMainLine


```
public void appendMainLine​(java.lang.StringBuilder out,
                           boolean hasOptions,
                           boolean hasCommands,
                           int indentCount,
                           java.lang.String indent)
```

Appends the main line segment of the usage to the argument string builder, indenting every
 line with indentCount-many indent.

Parameters:
`out` - the builder to append to
`hasOptions` - if the options section should be appended
`hasCommands` - if the comments section should be appended
`indentCount` - the amount of indentation to apply
`indent` - the indentation










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

Parameters:
`out` - the builder to append to
`indentCount` - the amount of indentation to apply
`indent` - the indentation
`sortedParameters` - the parameters to append to the builder










    - 

#### appendCommands


```
public void appendCommands​(java.lang.StringBuilder out,
                           int indentCount,
                           int descriptionIndent,
                           java.lang.String indent)
```

Appends the details of all commands to the argument string builder, indenting every line with
 indentCount-many indent. The commands are obtained from calling
 `JCommander.getRawCommands()` and the commands are resolved using
 `JCommander.findCommandByAlias(String)` on the underlying commander instance.

Parameters:
`out` - the builder to append to
`indentCount` - the amount of indentation to apply
`descriptionIndent` - the indentation for the description
`indent` - the indentation










    - 

#### getCommandDescription


```
public java.lang.String getCommandDescription​(java.lang.String commandName)
```

Returns the description of the command corresponding to the argument command name. The commands are resolved
 by calling `JCommander.findCommandByAlias(String)`, and the default resource bundle used from
 `JCommander.getBundle()` on the underlying commander instance.

Specified by:
`getCommandDescription` in interface `IUsageFormatter`
Parameters:
`commandName` - the name of the command to get the description for
Returns:
the description of the command.










    - 

#### wrapDescription


```
public void wrapDescription​(java.lang.StringBuilder out,
                            int indent,
                            int currentLineIndent,
                            java.lang.String description)
```

Wrap a potentially long line to the value obtained by calling `JCommander.getColumnSize()` on the
 underlying commander instance.

Parameters:
`out` - the output
`indent` - the indentation in spaces for lines after the first line.
`currentLineIndent` - the length of the indentation of the initial line
`description` - the text to wrap. No extra spaces are inserted before `
                          description`. If the first line needs to be indented prepend the
                          correct number of spaces to `description`.










    - 

#### wrapDescription


```
public void wrapDescription​(java.lang.StringBuilder out,
                            int indent,
                            java.lang.String description)
```

Wrap a potentially long line to { @link #commander#getColumnSize()}.

Parameters:
`out` - the output
`indent` - the indentation in spaces for lines after the first line.
`description` - the text to wrap. No extra spaces are inserted before `
                    description`. If the first line needs to be indented prepend the
                    correct number of spaces to `description`.
See Also:
`wrapDescription(StringBuilder, int, int, String)`










    - 

#### getI18nString


```
public static java.lang.String getI18nString​(java.util.ResourceBundle bundle,
                                             java.lang.String key,
                                             java.lang.String def)
```

Returns the internationalized version of the string if available, otherwise it returns def.

Returns:
the internationalized version of the string if available, otherwise it returns def










    - 

#### s


```
public static java.lang.String s​(int count)
```

Returns count-many spaces.

Returns:
count-many spaces