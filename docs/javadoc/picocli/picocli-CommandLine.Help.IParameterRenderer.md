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

## Interface CommandLine.Help.IParameterRenderer







- 

Enclosing class:
CommandLine.Help


---




```
public static interface CommandLine.Help.IParameterRenderer
```

When customizing online help for positional parameters details, a custom `IParameterRenderer`
 can be used to create textual representation of a Parameters field in a tabular format: one or more rows,
 each containing one or more columns. The `Layout` is responsible for placing these text
 values in the `TextTable`.








- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`CommandLine.Help.Ansi.Text[][]`
`render(CommandLine.Model.PositionalParamSpec param,
      CommandLine.Help.IParamLabelRenderer parameterLabelRenderer,
      CommandLine.Help.ColorScheme scheme)`
Returns a text representation of the specified positional parameter.














- 




  - 



### Method Detail







    - 

#### render


```
CommandLine.Help.Ansi.Text[][] render(CommandLine.Model.PositionalParamSpec param,
                                      CommandLine.Help.IParamLabelRenderer parameterLabelRenderer,
                                      CommandLine.Help.ColorScheme scheme)
```

Returns a text representation of the specified positional parameter.

Parameters:
`param` - the positional parameter to show online usage help for
`parameterLabelRenderer` - responsible for rendering parameter labels to text
`scheme` - color scheme for applying ansi color styles to positional parameters
Returns:
a 2-dimensional array of text values: one or more rows, each containing one or more columns
Since:
3.0

















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