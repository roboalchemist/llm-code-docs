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

## Interface CommandLine.IParseResultHandler2<R>







- 

Type Parameters:
`R` - the return type of this handler


All Known Implementing Classes:
CommandLine.AbstractParseResultHandler, CommandLine.RunAll, CommandLine.RunFirst, CommandLine.RunLast


Enclosing class:
CommandLine


---

Deprecated. 
use `CommandLine.IExecutionStrategy` instead, see `CommandLine.execute(String...)`




```
@Deprecated
public static interface CommandLine.IParseResultHandler2<R>
```

Represents a function that can process the `ParseResult` object resulting from successfully
 parsing the command line arguments. This is a
 functional interface
 whose functional method is `handleParseResult(CommandLine.ParseResult)`.
 


 Implementations of this function can be passed to the `CommandLine::parseWithHandlers`
 methods to take some next step after the command line was successfully parsed.
 


 This interface replaces the `CommandLine.IParseResultHandler` interface; it takes the parse result as a `ParseResult`
 object instead of a List of `CommandLine` objects, and it has the freedom to select the `CommandLine.Help.Ansi` style
 to use and what `PrintStreams` to print to.
 

Since:
3.0
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


`R`
`handleParseResult(CommandLine.ParseResult parseResult)`
Deprecated. 
Processes the `ParseResult` object resulting from successfully
 parsing the command line arguments and returns a return value.














- 




  - 



### Method Detail







    - 

#### handleParseResult


```
R handleParseResult(CommandLine.ParseResult parseResult)
             throws CommandLine.ExecutionException
```

Deprecated. 
Processes the `ParseResult` object resulting from successfully
 parsing the command line arguments and returns a return value.

Parameters:
`parseResult` - the `ParseResult` that resulted from successfully parsing the command line arguments
Throws:
`CommandLine.ParameterException` - if a help command was invoked for an unknown subcommand. Any `ParameterExceptions`
      thrown from this method are treated as if this exception was thrown during parsing and passed to the `CommandLine.IExceptionHandler2`
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