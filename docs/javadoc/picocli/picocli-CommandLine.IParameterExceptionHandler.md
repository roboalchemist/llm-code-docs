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

## Interface CommandLine.IParameterExceptionHandler







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IParameterExceptionHandler
```

Classes implementing this interface know how to handle `ParameterExceptions` (usually from invalid user input).
 

**Implementation Requirements:**
 

Implementors that need to print messages to the console should use the output and error PrintWriters,
 and the color scheme from the CommandLine object obtained from the exception.
 

**Implementation Note:**
 

See `CommandLine.getParameterExceptionHandler()` for a description of the default handler.
 

**API Note:**
 

This interface supersedes `CommandLine.IExceptionHandler2`.

Since:
4.0
See Also:
`CommandLine.setParameterExceptionHandler(IParameterExceptionHandler)`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`int`
`handleParseException(CommandLine.ParameterException ex,
                    String[] args)`
Handles a `ParameterException` that occurred while parsing the command
 line arguments and returns an exit code suitable for returning from `CommandLine.execute(String...)`.














- 




  - 



### Method Detail







    - 

#### handleParseException


```
int handleParseException(CommandLine.ParameterException ex,
                         String[] args)
                  throws Exception
```

Handles a `ParameterException` that occurred while parsing the command
 line arguments and returns an exit code suitable for returning from `CommandLine.execute(String...)`.

Parameters:
`ex` - the ParameterException describing the problem that occurred while parsing the command line arguments,
           and the CommandLine representing the command or subcommand whose input was invalid
`args` - the command line arguments that could not be parsed
Returns:
an exit code
Throws:
`Exception`

















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