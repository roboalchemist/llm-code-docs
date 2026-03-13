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

## Interface CommandLine.IExecutionExceptionHandler







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IExecutionExceptionHandler
```

Classes implementing this interface know how to handle Exceptions that occurred while executing the `Runnable`, `Callable` or `Method` user object of the command.
 

**Implementation Requirements:**
 

Implementors that need to print messages to the console should use the output and error PrintWriters,
 and the color scheme from the CommandLine object obtained from the exception.
 

**API Note:**
 

This interface supersedes `CommandLine.IExceptionHandler2`.
 

Example usage:
 

```

 IExecutionExceptionHandler errorHandler = new IExecutionExceptionHandler() {
     public int handleExecutionException(Exception ex,
                                         CommandLine commandLine,
                                         ParseResult parseResult) {
         //ex.printStackTrace(); // no stack trace
         commandLine.getErr().println(ex.getMessage());
         commandLine.usage(commandLine.getErr());
         return commandLine.getCommandSpec().exitCodeOnExecutionException();
     }
 };
 int exitCode = new CommandLine(new App())
         .setExecutionExceptionHandler(errorHandler)
         .execute(args);
 
```


Since:
4.0
See Also:
`CommandLine.setExecutionExceptionHandler(IExecutionExceptionHandler)`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`int`
`handleExecutionException(Exception ex,
                        CommandLine commandLine,
                        CommandLine.ParseResult fullParseResult)`
Handles an `Exception` that occurred while executing the `Runnable` or
 `Callable` command and returns an exit code suitable for returning from `CommandLine.execute(String...)`.














- 




  - 



### Method Detail







    - 

#### handleExecutionException


```
int handleExecutionException(Exception ex,
                             CommandLine commandLine,
                             CommandLine.ParseResult fullParseResult)
                      throws Exception
```

Handles an `Exception` that occurred while executing the `Runnable` or
 `Callable` command and returns an exit code suitable for returning from `CommandLine.execute(String...)`.

Parameters:
`ex` - the Exception thrown by the `Runnable`, `Callable` or `Method` user object of the command
`commandLine` - the CommandLine representing the command or subcommand where the exception occurred
`fullParseResult` - the result of parsing the command line arguments.
                        This is the ParseResult of the **top-level command**.
               Note that if the exception occurred in a subcommand, you may want to inspect the ParseResult of
               the subcommand that threw the exception, which can be obtained by calling `commandLine.getParseResult()`
               on the CommandLine object passed to this method.
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