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

## Class CommandLine.Help.Layout






- java.lang.Object

- 



  - picocli.CommandLine.Help.Layout









- 

Enclosing class:
CommandLine.Help


---




```
public static class CommandLine.Help.Layout
extends Object
```

Use a Layout to format usage help text for options and parameters in tabular format.
 

Delegates to the renderers to create `CommandLine.Help.Ansi.Text` values for the annotated fields, and uses a
 `CommandLine.Help.TextTable` to display these values in tabular format. Layout is responsible for deciding which values
 to display where in the table. By default, Layout shows one option or parameter per table row.
 

Customize by overriding the `layout(CommandLine.Model.ArgSpec, CommandLine.Help.Ansi.Text[][])` method.

See Also:
`rendering options to text`, 
`rendering parameters to text`, 
`showing values in a tabular format`









- 




  - 



### Field Summary


Fields 

Modifier and Type
Field and Description


`protected CommandLine.Help.ColorScheme`
`colorScheme` 


`protected CommandLine.Help.IOptionRenderer`
`optionRenderer` 


`protected CommandLine.Help.IParameterRenderer`
`parameterRenderer` 


`protected CommandLine.Help.TextTable`
`table` 









  - 



### Constructor Summary


Constructors 

Constructor and Description


`Layout(CommandLine.Help.ColorScheme colorScheme,
      CommandLine.Help.TextTable textTable)`
Constructs a Layout with the specified color scheme, the specified TextTable, the
 default option renderer, and the
 default parameter renderer.



`Layout(CommandLine.Help.ColorScheme colorScheme,
      CommandLine.Help.TextTable textTable,
      CommandLine.Help.IOptionRenderer optionRenderer,
      CommandLine.Help.IParameterRenderer parameterRenderer)`
Constructs a Layout with the specified color scheme, the specified TextTable, the
 specified option renderer and the specified parameter renderer.



`Layout(CommandLine.Help.ColorScheme colorScheme,
      int tableWidth)`
Constructs a Layout with the specified color scheme, a new default TextTable, the
 default option renderer, and the
 default parameter renderer.










  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`void`
`addAllOptions(List<CommandLine.Model.OptionSpec> options,
             CommandLine.Help.IParamLabelRenderer paramLabelRenderer)`
Calls `addOption(CommandLine.Model.OptionSpec, CommandLine.Help.IParamLabelRenderer)` for all Options in the specified list.



`void`
`addAllPositionalParameters(List<CommandLine.Model.PositionalParamSpec> params,
                          CommandLine.Help.IParamLabelRenderer paramLabelRenderer)`
Calls `addPositionalParameter(CommandLine.Model.PositionalParamSpec, CommandLine.Help.IParamLabelRenderer)` for all positional parameters in the specified list.



`void`
`addOption(CommandLine.Model.OptionSpec option,
         CommandLine.Help.IParamLabelRenderer paramLabelRenderer)`
Delegates to the `option renderer` of this layout to obtain
 text values for the specified `CommandLine.Model.OptionSpec`, and then calls the `layout(CommandLine.Model.ArgSpec, CommandLine.Help.Ansi.Text[][])`
 method to write these text values into the correct cells in the TextTable.



`void`
`addOptions(List<CommandLine.Model.OptionSpec> options,
          CommandLine.Help.IParamLabelRenderer paramLabelRenderer)`
Calls `addOption(CommandLine.Model.OptionSpec, CommandLine.Help.IParamLabelRenderer)` for all non-hidden Options in the list.



`void`
`addPositionalParameter(CommandLine.Model.PositionalParamSpec param,
                      CommandLine.Help.IParamLabelRenderer paramLabelRenderer)`
Delegates to the `parameter renderer` of this layout
 to obtain text values for the specified positional parameter, and then calls
 `layout(CommandLine.Model.ArgSpec, CommandLine.Help.Ansi.Text[][])` to write these text values into the correct cells in the TextTable.



`void`
`addPositionalParameters(List<CommandLine.Model.PositionalParamSpec> params,
                       CommandLine.Help.IParamLabelRenderer paramLabelRenderer)`
Calls `addPositionalParameter(CommandLine.Model.PositionalParamSpec, CommandLine.Help.IParamLabelRenderer)` for all non-hidden Parameters in the list.



`CommandLine.Help.ColorScheme`
`colorScheme()`
Returns the ColorScheme used to create Text objects in this layout.



`void`
`layout(CommandLine.Model.ArgSpec argSpec,
      CommandLine.Help.Ansi.Text[][] cellValues)`
Copies the specified text values into the correct cells in the `CommandLine.Help.TextTable`.



`CommandLine.Help.IOptionRenderer`
`optionRenderer()`
Returns the IOptionRenderer used to render options to Text before adding this text to the TextTable in this layout.



`CommandLine.Help.IParameterRenderer`
`parameterRenderer()`
Returns the IParameterRenderer used to render positional params to Text before adding this text to the TextTable in this layout.



`CommandLine.Help.TextTable`
`textTable()`
Returns the TextTable used in this layout.



`String`
`toString()`
Returns the section of the usage help message accumulated in the TextTable owned by this layout.






    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`













- 




  - 



### Field Detail







    - 

#### colorScheme


```
protected final CommandLine.Help.ColorScheme colorScheme
```










    - 

#### table


```
protected final CommandLine.Help.TextTable table
```










    - 

#### optionRenderer


```
protected CommandLine.Help.IOptionRenderer optionRenderer
```










    - 

#### parameterRenderer


```
protected CommandLine.Help.IParameterRenderer parameterRenderer
```











  - 



### Constructor Detail







    - 

#### Layout


```
public Layout(CommandLine.Help.ColorScheme colorScheme,
              int tableWidth)
```

Constructs a Layout with the specified color scheme, a new default TextTable, the
 default option renderer, and the
 default parameter renderer.

Parameters:
`colorScheme` - the color scheme to use for common, auto-generated parts of the usage help message










    - 

#### Layout


```
public Layout(CommandLine.Help.ColorScheme colorScheme,
              CommandLine.Help.TextTable textTable)
```

Constructs a Layout with the specified color scheme, the specified TextTable, the
 default option renderer, and the
 default parameter renderer.

Parameters:
`colorScheme` - the color scheme to use for common, auto-generated parts of the usage help message
`textTable` - the TextTable to lay out parts of the usage help message in tabular format










    - 

#### Layout


```
public Layout(CommandLine.Help.ColorScheme colorScheme,
              CommandLine.Help.TextTable textTable,
              CommandLine.Help.IOptionRenderer optionRenderer,
              CommandLine.Help.IParameterRenderer parameterRenderer)
```

Constructs a Layout with the specified color scheme, the specified TextTable, the
 specified option renderer and the specified parameter renderer.

Parameters:
`colorScheme` - the color scheme to use for common, auto-generated parts of the usage help message
`optionRenderer` - the object responsible for rendering Options to Text
`parameterRenderer` - the object responsible for rendering Parameters to Text
`textTable` - the TextTable to lay out parts of the usage help message in tabular format











  - 



### Method Detail







    - 

#### layout


```
public void layout(CommandLine.Model.ArgSpec argSpec,
                   CommandLine.Help.Ansi.Text[][] cellValues)
```

Copies the specified text values into the correct cells in the `CommandLine.Help.TextTable`. This implementation
 delegates to `CommandLine.Help.TextTable.addRowValues(CommandLine.Help.Ansi.Text...)` for each row of values.
 

Subclasses may override.

Parameters:
`argSpec` - the Option or Parameters
`cellValues` - the text values representing the Option/Parameters, to be displayed in tabular form
Since:
3.0










    - 

#### addOptions


```
public void addOptions(List<CommandLine.Model.OptionSpec> options,
                       CommandLine.Help.IParamLabelRenderer paramLabelRenderer)
```

Calls `addOption(CommandLine.Model.OptionSpec, CommandLine.Help.IParamLabelRenderer)` for all non-hidden Options in the list.

Parameters:
`options` - options to add usage descriptions for
`paramLabelRenderer` - object that knows how to render option parameters
Since:
3.0










    - 

#### addAllOptions


```
public void addAllOptions(List<CommandLine.Model.OptionSpec> options,
                          CommandLine.Help.IParamLabelRenderer paramLabelRenderer)
```

Calls `addOption(CommandLine.Model.OptionSpec, CommandLine.Help.IParamLabelRenderer)` for all Options in the specified list.

Parameters:
`options` - options to add usage descriptions for;
                it is the responsibility of the caller to exclude options that should not be shown
`paramLabelRenderer` - object that knows how to render option parameters
Since:
4.4










    - 

#### addOption


```
public void addOption(CommandLine.Model.OptionSpec option,
                      CommandLine.Help.IParamLabelRenderer paramLabelRenderer)
```

Delegates to the `option renderer` of this layout to obtain
 text values for the specified `CommandLine.Model.OptionSpec`, and then calls the `layout(CommandLine.Model.ArgSpec, CommandLine.Help.Ansi.Text[][])`
 method to write these text values into the correct cells in the TextTable.

Parameters:
`option` - the option argument
`paramLabelRenderer` - knows how to render option parameters
Since:
3.0










    - 

#### addPositionalParameters


```
public void addPositionalParameters(List<CommandLine.Model.PositionalParamSpec> params,
                                    CommandLine.Help.IParamLabelRenderer paramLabelRenderer)
```

Calls `addPositionalParameter(CommandLine.Model.PositionalParamSpec, CommandLine.Help.IParamLabelRenderer)` for all non-hidden Parameters in the list.

Parameters:
`params` - positional parameters to add usage descriptions for
`paramLabelRenderer` - knows how to render option parameters
Since:
3.0










    - 

#### addAllPositionalParameters


```
public void addAllPositionalParameters(List<CommandLine.Model.PositionalParamSpec> params,
                                       CommandLine.Help.IParamLabelRenderer paramLabelRenderer)
```

Calls `addPositionalParameter(CommandLine.Model.PositionalParamSpec, CommandLine.Help.IParamLabelRenderer)` for all positional parameters in the specified list.

Parameters:
`params` - positional parameters to add usage descriptions for;
               it is the responsibility of the caller to exclude positional parameters that should not be shown
`paramLabelRenderer` - knows how to render option parameters
Since:
4.4










    - 

#### addPositionalParameter


```
public void addPositionalParameter(CommandLine.Model.PositionalParamSpec param,
                                   CommandLine.Help.IParamLabelRenderer paramLabelRenderer)
```

Delegates to the `parameter renderer` of this layout
 to obtain text values for the specified positional parameter, and then calls
 `layout(CommandLine.Model.ArgSpec, CommandLine.Help.Ansi.Text[][])` to write these text values into the correct cells in the TextTable.

Parameters:
`param` - the positional parameter
`paramLabelRenderer` - knows how to render option parameters
Since:
3.0










    - 

#### toString


```
public String toString()
```

Returns the section of the usage help message accumulated in the TextTable owned by this layout.

Overrides:
`toString` in class `Object`










    - 

#### colorScheme


```
public CommandLine.Help.ColorScheme colorScheme()
```

Returns the ColorScheme used to create Text objects in this layout.

Since:
4.6










    - 

#### textTable


```
public CommandLine.Help.TextTable textTable()
```

Returns the TextTable used in this layout.

Since:
4.6










    - 

#### optionRenderer


```
public CommandLine.Help.IOptionRenderer optionRenderer()
```

Returns the IOptionRenderer used to render options to Text before adding this text to the TextTable in this layout.

Since:
4.6










    - 

#### parameterRenderer


```
public CommandLine.Help.IParameterRenderer parameterRenderer()
```

Returns the IParameterRenderer used to render positional params to Text before adding this text to the TextTable in this layout.

Since:
4.6

















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