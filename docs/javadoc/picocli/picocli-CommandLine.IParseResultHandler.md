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

## Interface CommandLine.IParseResultHandler







- 

All Known Implementing Classes:
CommandLine.RunAll, CommandLine.RunFirst, CommandLine.RunLast


Enclosing class:
CommandLine


---

Deprecated. 
Use `CommandLine.IExecutionStrategy` instead.




```
@Deprecated
public static interface CommandLine.IParseResultHandler
```

Represents a function that can process a List of `CommandLine` objects resulting from successfully
 parsing the command line arguments. This is a
 functional interface
 whose functional method is `handleParseResult(List, PrintStream, CommandLine.Help.Ansi)`.
 


 Implementations of this functions can be passed to the `CommandLine::parseWithHandler`
 methods to take some next step after the command line was successfully parsed.
 

Since:
2.0
See Also:
`CommandLine.RunFirst`, 
`CommandLine.RunLast`, 
`CommandLine.RunAll`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods Deprecated Methods 

Modifier and Type
Method and Description


`List<Object>`
`handleParseResult(List<CommandLine> parsedCommands,
                 PrintStream out,
                 CommandLine.Help.Ansi ansi)`
Deprecated. 
Processes a List of `CommandLine` objects resulting from successfully
 parsing the command line arguments and optionally returns a list of results.














- 




  - 



### Method Detail







    - 

#### handleParseResult


```
List<Object> handleParseResult(List<CommandLine> parsedCommands,
                               PrintStream out,
                               CommandLine.Help.Ansi ansi)
                        throws CommandLine.ExecutionException
```

Deprecated. 
Processes a List of `CommandLine` objects resulting from successfully
 parsing the command line arguments and optionally returns a list of results.

Parameters:
`parsedCommands` - the `CommandLine` objects that resulted from successfully parsing the command line arguments
`out` - the `PrintStream` to print help to if requested
`ansi` - for printing help messages using ANSI styles and colors
Returns:
a list of results, or an empty list if there are no results
Throws:
`CommandLine.ParameterException` - if a help command was invoked for an unknown subcommand. Any `ParameterExceptions`
      thrown from this method are treated as if this exception was thrown during parsing and passed to the `CommandLine.IExceptionHandler`
`CommandLine.ExecutionException` - if a problem occurred while processing the parse results; use
      `CommandLine.ExecutionException.getCommandLine()` to get the command or subcommand where processing failed

















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