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

## Interface CommandLine.IExceptionHandler







- 

All Known Implementing Classes:
CommandLine.DefaultExceptionHandler


Enclosing class:
CommandLine


---

Deprecated. 
see `CommandLine.execute(String...)`, `CommandLine.IParameterExceptionHandler` and `CommandLine.IExecutionExceptionHandler`




```
@Deprecated
public static interface CommandLine.IExceptionHandler
```

Represents a function that can handle a `ParameterException` that occurred while
 parsing the command line arguments. This is a
 functional interface
 whose functional method is `handleException(CommandLine.ParameterException, PrintStream, CommandLine.Help.Ansi, String...)`.
 


 Implementations of this function can be passed to the `CommandLine::parseWithHandlers`
 methods to handle situations when the command line could not be parsed.
 

Since:
2.0









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods Deprecated Methods 

Modifier and Type
Method and Description


`List<Object>`
`handleException(CommandLine.ParameterException ex,
               PrintStream out,
               CommandLine.Help.Ansi ansi,
               String... args)`
Deprecated. 
Handles a `ParameterException` that occurred while parsing the command
 line arguments and optionally returns a list of results.














- 




  - 



### Method Detail







    - 

#### handleException


```
List<Object> handleException(CommandLine.ParameterException ex,
                             PrintStream out,
                             CommandLine.Help.Ansi ansi,
                             String... args)
```

Deprecated. 
Handles a `ParameterException` that occurred while parsing the command
 line arguments and optionally returns a list of results.

Parameters:
`ex` - the ParameterException describing the problem that occurred while parsing the command line arguments,
           and the CommandLine representing the command or subcommand whose input was invalid
`out` - the `PrintStream` to print help to if requested
`ansi` - for printing help messages using ANSI styles and colors
`args` - the command line arguments that could not be parsed
Returns:
a list of results, or an empty list if there are no results

















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