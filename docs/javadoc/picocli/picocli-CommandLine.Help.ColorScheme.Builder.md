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

## Class CommandLine.Help.ColorScheme.Builder






- java.lang.Object

- 



  - picocli.CommandLine.Help.ColorScheme.Builder









- 

Enclosing class:
CommandLine.Help.ColorScheme


---




```
public static class CommandLine.Help.ColorScheme.Builder
extends Object
```

Builder class to create `ColorScheme` instances.

Since:
4.0









- 




  - 



### Constructor Summary


Constructors 

Constructor and Description


`Builder()`
Constructs an empty color scheme builder with Ansi.AUTO.



`Builder(CommandLine.Help.Ansi ansi)`
Constructs an empty color scheme builder with the specified Ansi value.



`Builder(CommandLine.Help.ColorScheme existing)`
Constructs a color scheme builder with all attributes copied from the specified color scheme.










  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`CommandLine.Help.Ansi`
`ansi()`
Returns the `Ansi` setting of this color scheme builder.



`CommandLine.Help.ColorScheme.Builder`
`ansi(CommandLine.Help.Ansi ansi)`
Set the `Ansi` setting of this color scheme builder.



`CommandLine.Help.ColorScheme.Builder`
`applySystemProperties()`
Replaces colors and styles in this scheme builder with ones specified in system properties, and returns this builder.



`CommandLine.Help.ColorScheme`
`build()`
Creates and returns a new `ColorScheme` with the values configured on this builder.



`CommandLine.Help.ColorScheme.Builder`
`commands(CommandLine.Help.Ansi.IStyle... styles)`
Adds the specified styles to the registered styles for commands in this color scheme builder and returns this builder.



`List<CommandLine.Help.Ansi.IStyle>`
`commandStyles()`
Returns the registered styles for commands in this color scheme builder.



`Map<String,CommandLine.Help.Ansi.IStyle>`
`customMarkupMap()`
Returns the custom mapping from markup names (the names of the `CommandLine.Help.Ansi.Style` enum constants, like bold, italic, fg_blue, bg_green, etc) to `CommandLine.Help.Ansi.IStyle` objects in this color scheme.



`CommandLine.Help.ColorScheme.Builder`
`customMarkupMap(Map<String,CommandLine.Help.Ansi.IStyle> newValue)`
Sets the custom mapping from markup names (the names of the `CommandLine.Help.Ansi.Style` enum constants, like bold, italic, fg_blue, bg_green, etc) to `CommandLine.Help.Ansi.IStyle` objects in this color scheme.



`CommandLine.Help.ColorScheme.Builder`
`errors(CommandLine.Help.Ansi.IStyle... styles)`
Adds the specified styles to the registered styles for errors in this color scheme builder and returns this builder.



`List<CommandLine.Help.Ansi.IStyle>`
`errorStyles()`
Returns the registered styles for errors in this color scheme builder.



`CommandLine.Help.ColorScheme.Builder`
`optionParams(CommandLine.Help.Ansi.IStyle... styles)`
Adds the specified styles to the registered styles for option parameters in this color scheme builder and returns this builder.



`List<CommandLine.Help.Ansi.IStyle>`
`optionParamStyles()`
Returns the registered styles for option parameters in this color scheme builder.



`CommandLine.Help.ColorScheme.Builder`
`options(CommandLine.Help.Ansi.IStyle... styles)`
Adds the specified styles to the registered styles for options in this color scheme and returns this color scheme.



`List<CommandLine.Help.Ansi.IStyle>`
`optionStyles()`
Returns the registered styles for options in this color scheme builder.



`CommandLine.Help.ColorScheme.Builder`
`parameters(CommandLine.Help.Ansi.IStyle... styles)`
Adds the specified styles to the registered styles for positional parameters in this color scheme builder and returns this builder.



`List<CommandLine.Help.Ansi.IStyle>`
`parameterStyles()`
Returns the registered styles for positional parameters in this color scheme builder.



`CommandLine.Help.ColorScheme.Builder`
`stackTraces(CommandLine.Help.Ansi.IStyle... styles)`
Adds the specified styles to the registered styles for stack traces in this color scheme builder and returns this builder.



`List<CommandLine.Help.Ansi.IStyle>`
`stackTraceStyles()`
Returns the registered styles for stack traces in this color scheme builder.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Constructor Detail







    - 

#### Builder


```
public Builder()
```

Constructs an empty color scheme builder with Ansi.AUTO.









    - 

#### Builder


```
public Builder(CommandLine.Help.Ansi ansi)
```

Constructs an empty color scheme builder with the specified Ansi value.









    - 

#### Builder


```
public Builder(CommandLine.Help.ColorScheme existing)
```

Constructs a color scheme builder with all attributes copied from the specified color scheme.










  - 



### Method Detail







    - 

#### ansi


```
public CommandLine.Help.Ansi ansi()
```

Returns the `Ansi` setting of this color scheme builder.









    - 

#### ansi


```
public CommandLine.Help.ColorScheme.Builder ansi(CommandLine.Help.Ansi ansi)
```

Set the `Ansi` setting of this color scheme builder.









    - 

#### commandStyles


```
public List<CommandLine.Help.Ansi.IStyle> commandStyles()
```

Returns the registered styles for commands in this color scheme builder.









    - 

#### optionStyles


```
public List<CommandLine.Help.Ansi.IStyle> optionStyles()
```

Returns the registered styles for options in this color scheme builder.









    - 

#### parameterStyles


```
public List<CommandLine.Help.Ansi.IStyle> parameterStyles()
```

Returns the registered styles for positional parameters in this color scheme builder.









    - 

#### optionParamStyles


```
public List<CommandLine.Help.Ansi.IStyle> optionParamStyles()
```

Returns the registered styles for option parameters in this color scheme builder.









    - 

#### errorStyles


```
public List<CommandLine.Help.Ansi.IStyle> errorStyles()
```

Returns the registered styles for errors in this color scheme builder.

Since:
4.3










    - 

#### stackTraceStyles


```
public List<CommandLine.Help.Ansi.IStyle> stackTraceStyles()
```

Returns the registered styles for stack traces in this color scheme builder.

Since:
4.3










    - 

#### customMarkupMap


```
public Map<String,CommandLine.Help.Ansi.IStyle> customMarkupMap()
```

Returns the custom mapping from markup names (the names of the `CommandLine.Help.Ansi.Style` enum constants, like bold, italic, fg_blue, bg_green, etc) to `CommandLine.Help.Ansi.IStyle` objects in this color scheme.
 By default this returns `null`, unless a custom map was configured.

Since:
4.2










    - 

#### customMarkupMap


```
public CommandLine.Help.ColorScheme.Builder customMarkupMap(Map<String,CommandLine.Help.Ansi.IStyle> newValue)
```

Sets the custom mapping from markup names (the names of the `CommandLine.Help.Ansi.Style` enum constants, like bold, italic, fg_blue, bg_green, etc) to `CommandLine.Help.Ansi.IStyle` objects in this color scheme.

Returns:
this color scheme builder to enable method chaining for a more fluent API
Since:
4.2










    - 

#### commands


```
public CommandLine.Help.ColorScheme.Builder commands(CommandLine.Help.Ansi.IStyle... styles)
```

Adds the specified styles to the registered styles for commands in this color scheme builder and returns this builder.

Parameters:
`styles` - the styles to add to the registered styles for commands in this color scheme builder
Returns:
this color scheme builder to enable method chaining for a more fluent API










    - 

#### options


```
public CommandLine.Help.ColorScheme.Builder options(CommandLine.Help.Ansi.IStyle... styles)
```

Adds the specified styles to the registered styles for options in this color scheme and returns this color scheme.

Parameters:
`styles` - the styles to add to registered the styles for options in this color scheme builder
Returns:
this color scheme builder to enable method chaining for a more fluent API










    - 

#### parameters


```
public CommandLine.Help.ColorScheme.Builder parameters(CommandLine.Help.Ansi.IStyle... styles)
```

Adds the specified styles to the registered styles for positional parameters in this color scheme builder and returns this builder.

Parameters:
`styles` - the styles to add to registered the styles for parameters in this color scheme builder
Returns:
this color scheme builder to enable method chaining for a more fluent API










    - 

#### optionParams


```
public CommandLine.Help.ColorScheme.Builder optionParams(CommandLine.Help.Ansi.IStyle... styles)
```

Adds the specified styles to the registered styles for option parameters in this color scheme builder and returns this builder.

Parameters:
`styles` - the styles to add to the registered styles for option parameters in this color scheme builder
Returns:
this color scheme builder to enable method chaining for a more fluent API










    - 

#### errors


```
public CommandLine.Help.ColorScheme.Builder errors(CommandLine.Help.Ansi.IStyle... styles)
```

Adds the specified styles to the registered styles for errors in this color scheme builder and returns this builder.

Parameters:
`styles` - the styles to add to the registered styles for errors in this color scheme builder
Returns:
this color scheme builder to enable method chaining for a more fluent API
Since:
4.3










    - 

#### stackTraces


```
public CommandLine.Help.ColorScheme.Builder stackTraces(CommandLine.Help.Ansi.IStyle... styles)
```

Adds the specified styles to the registered styles for stack traces in this color scheme builder and returns this builder.

Parameters:
`styles` - the styles to add to the registered styles for stack traces in this color scheme builder
Returns:
this color scheme builder to enable method chaining for a more fluent API
Since:
4.3










    - 

#### applySystemProperties


```
public CommandLine.Help.ColorScheme.Builder applySystemProperties()
```

Replaces colors and styles in this scheme builder with ones specified in system properties, and returns this builder.
 Supported property names:

     
      - `picocli.color.commands`
     
      - `picocli.color.options`
     
      - `picocli.color.parameters`
     
      - `picocli.color.optionParams`
     
      - `picocli.color.errors`
     
      - `picocli.color.stackTraces`
 

Property values can be anything that `CommandLine.Help.Ansi.Style.parse(String)` can handle.

Returns:
this ColorScheme builder










    - 

#### build


```
public CommandLine.Help.ColorScheme build()
```

Creates and returns a new `ColorScheme` with the values configured on this builder.
















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