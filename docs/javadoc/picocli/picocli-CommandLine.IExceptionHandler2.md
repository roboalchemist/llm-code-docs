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

## Interface CommandLine.IExceptionHandler2<R>







- 

Type Parameters:
`R` - the return type of this handler


All Known Implementing Classes:
CommandLine.DefaultExceptionHandler


Enclosing class:
CommandLine


---

Deprecated. 
see `CommandLine.execute(String...)`, `CommandLine.IParameterExceptionHandler` and `CommandLine.IExecutionExceptionHandler`




```
@Deprecated
public static interface CommandLine.IExceptionHandler2<R>
```

Classes implementing this interface know how to handle `ParameterExceptions` (usually from invalid user input)
 and `ExecutionExceptions` that occurred while executing the `Runnable` or `Callable` command.
 


 Implementations of this interface can be passed to the
 `CommandLine::parseWithHandlers` method.
 


 This interface replaces the `CommandLine.IParseResultHandler` interface.
 

Since:
3.0
See Also:
`CommandLine.DefaultExceptionHandler`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods Deprecated Methods 

Modifier and Type
Method and Description


`R`
`handleExecutionException(CommandLine.ExecutionException ex,
                        CommandLine.ParseResult parseResult)`
Deprecated. 
Handles a `ExecutionException` that occurred while executing the `Runnable` or
 `Callable` command and optionally returns a list of results.



`R`
`handleParseException(CommandLine.ParameterException ex,
                    String[] args)`
Deprecated. 
Handles a `ParameterException` that occurred while parsing the command
 line arguments and optionally returns a list of results.














- 




  - 



### Method Detail







    - 

#### handleParseException


```
R handleParseException(CommandLine.ParameterException ex,
                       String[] args)
```

Deprecated. 
Handles a `ParameterException` that occurred while parsing the command
 line arguments and optionally returns a list of results.

Parameters:
`ex` - the ParameterException describing the problem that occurred while parsing the command line arguments,
           and the CommandLine representing the command or subcommand whose input was invalid
`args` - the command line arguments that could not be parsed
Returns:
an object resulting from handling the exception










    - 

#### handleExecutionException


```
R handleExecutionException(CommandLine.ExecutionException ex,
                           CommandLine.ParseResult parseResult)
```

Deprecated. 
Handles a `ExecutionException` that occurred while executing the `Runnable` or
 `Callable` command and optionally returns a list of results.

Parameters:
`ex` - the ExecutionException describing the problem that occurred while executing the `Runnable` or
          `Callable` command, and the CommandLine representing the command or subcommand that was being executed
`parseResult` - the result of parsing the command line arguments
Returns:
an object resulting from handling the exception

















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