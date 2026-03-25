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

## Interface CommandLine.Help.IParamLabelRenderer







- 

Enclosing class:
CommandLine.Help


---




```
public static interface CommandLine.Help.IParamLabelRenderer
```

When customizing online usage help for an option parameter or a positional parameter, a custom
 `IParamLabelRenderer` can be used to render the parameter name or label to a String.








- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`CommandLine.Help.Ansi.Text`
`renderParameterLabel(CommandLine.Model.ArgSpec argSpec,
                    CommandLine.Help.Ansi ansi,
                    List<CommandLine.Help.Ansi.IStyle> styles)`
Returns a text rendering of the option parameter or positional parameter; returns an empty string
 `""` if the option is a boolean and does not take a parameter.



`String`
`separator()`
Returns the separator between option name and param label.














- 




  - 



### Method Detail







    - 

#### renderParameterLabel


```
CommandLine.Help.Ansi.Text renderParameterLabel(CommandLine.Model.ArgSpec argSpec,
                                                CommandLine.Help.Ansi ansi,
                                                List<CommandLine.Help.Ansi.IStyle> styles)
```

Returns a text rendering of the option parameter or positional parameter; returns an empty string
 `""` if the option is a boolean and does not take a parameter.

Parameters:
`argSpec` - the named or positional parameter with a parameter label
`ansi` - determines whether ANSI escape codes should be emitted or not
`styles` - the styles to apply to the parameter label
Returns:
a text rendering of the Option parameter or positional parameter
Since:
3.0










    - 

#### separator


```
String separator()
```

Returns the separator between option name and param label.

Returns:
the separator between option name and param label

















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