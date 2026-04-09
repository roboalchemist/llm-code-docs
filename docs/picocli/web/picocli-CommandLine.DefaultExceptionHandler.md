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

## Class CommandLine.DefaultExceptionHandler<R>






- java.lang.Object

- 



  - picocli.CommandLine.AbstractHandler<R,CommandLine.DefaultExceptionHandler<R>>

  - 



    - picocli.CommandLine.DefaultExceptionHandler<R>












- 

All Implemented Interfaces:
CommandLine.IExceptionHandler, CommandLine.IExceptionHandler2<R>


Enclosing class:
CommandLine


---

Deprecated. 
see `CommandLine.execute(String...)`, `CommandLine.getParameterExceptionHandler()` and `CommandLine.getExecutionExceptionHandler()`




```
@Deprecated
public static class CommandLine.DefaultExceptionHandler<R>
extends CommandLine.AbstractHandler<R,CommandLine.DefaultExceptionHandler<R>>
implements CommandLine.IExceptionHandler, CommandLine.IExceptionHandler2<R>
```

Default exception handler that handles invalid user input by printing the exception message, followed by the usage
 message for the command or subcommand whose input was invalid.
 

`ParameterExceptions` (invalid user input) is handled like this:
 

```

     err().println(paramException.getMessage());
     paramException.getCommandLine().usage(err(), ansi());
     if (hasExitCode()) System.exit(exitCode()); else return returnValue;
 
```

 

`ExecutionExceptions` that occurred while executing the `Runnable` or `Callable` command are simply rethrown and not handled.

Since:
2.0









- 




  - 



### Constructor Summary


Constructors 

Constructor and Description


`DefaultExceptionHandler()`
Deprecated. 
 









  - 



### Method Summary


All Methods Instance Methods Concrete Methods Deprecated Methods 

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



`R`
`handleExecutionException(CommandLine.ExecutionException ex,
                        CommandLine.ParseResult parseResult)`
Deprecated. 
This implementation always simply rethrows the specified exception.



`R`
`handleParseException(CommandLine.ParameterException ex,
                    String[] args)`
Deprecated. 
Prints the message of the specified exception, followed by the usage message for the command or subcommand
 whose input was invalid, to the stream returned by `CommandLine.AbstractHandler.err()`.



`protected CommandLine.DefaultExceptionHandler<R>`
`self()`
Deprecated. 
Returns `this` to allow method chaining when calling the setters for a fluent API.






    - 



### Methods inherited from class picocli.CommandLine.AbstractHandler

`andExit, ansi, colorScheme, err, exit, exitCode, hasExitCode, out, returnResultOrExit, throwOrExit, useAnsi, useErr, useOut`





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Constructor Detail







    - 

#### DefaultExceptionHandler


```
public DefaultExceptionHandler()
```

Deprecated. 










  - 



### Method Detail







    - 

#### handleException


```
public List<Object> handleException(CommandLine.ParameterException ex,
                                    PrintStream out,
                                    CommandLine.Help.Ansi ansi,
                                    String... args)
```

Deprecated. 
Description copied from interface: `CommandLine.IExceptionHandler`
Handles a `ParameterException` that occurred while parsing the command
 line arguments and optionally returns a list of results.

Specified by:
`handleException` in interface `CommandLine.IExceptionHandler`
Parameters:
`ex` - the ParameterException describing the problem that occurred while parsing the command line arguments,
           and the CommandLine representing the command or subcommand whose input was invalid
`out` - the `PrintStream` to print help to if requested
`ansi` - for printing help messages using ANSI styles and colors
`args` - the command line arguments that could not be parsed
Returns:
a list of results, or an empty list if there are no results










    - 

#### handleParseException


```
public R handleParseException(CommandLine.ParameterException ex,
                              String[] args)
```

Deprecated. 
Prints the message of the specified exception, followed by the usage message for the command or subcommand
 whose input was invalid, to the stream returned by `CommandLine.AbstractHandler.err()`.

Specified by:
`handleParseException` in interface `CommandLine.IExceptionHandler2<R>`
Parameters:
`ex` - the ParameterException describing the problem that occurred while parsing the command line arguments,
           and the CommandLine representing the command or subcommand whose input was invalid
`args` - the command line arguments that could not be parsed
Returns:
the empty list
Since:
3.0










    - 

#### handleExecutionException


```
public R handleExecutionException(CommandLine.ExecutionException ex,
                                  CommandLine.ParseResult parseResult)
```

Deprecated. 
This implementation always simply rethrows the specified exception.

Specified by:
`handleExecutionException` in interface `CommandLine.IExceptionHandler2<R>`
Parameters:
`ex` - the ExecutionException describing the problem that occurred while executing the `Runnable` or `Callable` command
`parseResult` - the result of parsing the command line arguments
Returns:
nothing: this method always rethrows the specified exception
Throws:
`CommandLine.ExecutionException` - always rethrows the specified exception
Since:
3.0










    - 

#### self


```
protected CommandLine.DefaultExceptionHandler<R> self()
```

Deprecated. 
Description copied from class: `CommandLine.AbstractHandler`
Returns `this` to allow method chaining when calling the setters for a fluent API.

Specified by:
`self` in class `CommandLine.AbstractHandler<R,CommandLine.DefaultExceptionHandler<R>>`

















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