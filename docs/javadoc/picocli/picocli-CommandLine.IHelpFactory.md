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

## Interface CommandLine.IHelpFactory







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IHelpFactory
```

Creates the `CommandLine.Help` instance used to render the usage help message.

Since:
3.9









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`CommandLine.Help`
`create(CommandLine.Model.CommandSpec commandSpec,
      CommandLine.Help.ColorScheme colorScheme)`
Returns a `Help` instance to assist in rendering the usage help message














- 




  - 



### Method Detail







    - 

#### create


```
CommandLine.Help create(CommandLine.Model.CommandSpec commandSpec,
                        CommandLine.Help.ColorScheme colorScheme)
```

Returns a `Help` instance to assist in rendering the usage help message

Parameters:
`commandSpec` - the command to create usage help for
`colorScheme` - the color scheme to use when rendering usage help
Returns:
a `Help` instance

















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