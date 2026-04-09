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

## Interface CommandLine.IHelpCommandInitializable2







- 

All Known Implementing Classes:
CommandLine.HelpCommand


Enclosing class:
CommandLine


---




```
public static interface CommandLine.IHelpCommandInitializable2
```

Help commands that provide usage help for other commands can implement this interface to be initialized with the information they need.
 

The `CommandLine::printHelpIfRequested` method calls the
 `init` method on commands marked as `helpCommand`
 before the help command's `run` or `call` method is called.
 

**Implementation note:**


 If an error occurs in the `run` or `call` method while processing the help request, it is recommended custom Help
 commands throw a `ParameterException` with a reference to the parent command.
 The `default ParameterException handler` will print the error message and the usage for the parent command.
 

Since:
4.0









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`void`
`init(CommandLine helpCommandLine,
    CommandLine.Help.ColorScheme colorScheme,
    PrintWriter outWriter,
    PrintWriter errWriter)`
Initializes this object with the information needed to implement a help command that provides usage help for other commands.














- 




  - 



### Method Detail







    - 

#### init


```
void init(CommandLine helpCommandLine,
          CommandLine.Help.ColorScheme colorScheme,
          PrintWriter outWriter,
          PrintWriter errWriter)
```

Initializes this object with the information needed to implement a help command that provides usage help for other commands.

Parameters:
`helpCommandLine` - the `CommandLine` object associated with this help command. Implementors can use
                        this to walk the command hierarchy and get access to the help command's parent and sibling commands.
`colorScheme` - the color scheme to use when printing help, including whether to use Ansi colors or not
`outWriter` - the output writer to print the usage help message to
`errWriter` - the error writer to print any diagnostic messages to, in addition to the output from the exception handler

















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