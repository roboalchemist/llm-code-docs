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

## Interface CommandLine.IModelTransformer







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IModelTransformer
```

Provides a way to modify how the command model is built.
 This is useful for applications that need to modify the model dynamically depending on the runtime environment.
 


 Commands may configure a model transformer using the
 `CommandLine.Command.modelTransformer()` annotation attribute, or via the
 `CommandSpec#modelTransformer(IModelTransformer)` programmatic API.
 


 Model transformers are invoked only once, after the full command hierarchy is constructed.

Since:
4.6









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`CommandLine.Model.CommandSpec`
`transform(CommandLine.Model.CommandSpec commandSpec)`
Given an original CommandSpec, return the object that should be used
 instead.














- 




  - 



### Method Detail







    - 

#### transform


```
CommandLine.Model.CommandSpec transform(CommandLine.Model.CommandSpec commandSpec)
```

Given an original CommandSpec, return the object that should be used
 instead. Implementors may modify the specified CommandSpec and return it,
 or create a full or partial copy of the specified CommandSpec, and return
 that, or even return a completely new CommandSpec.
 


 Implementors are free to add or remove options, positional parameters,
 subcommands or modify the command in any other way.
 


 This method is called once, after the full command hierarchy is
 constructed, and before any command line arguments are parsed.
 

Returns:
the CommandSpec to use instead of the specified one

















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