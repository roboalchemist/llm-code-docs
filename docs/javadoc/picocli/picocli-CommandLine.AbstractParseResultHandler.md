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

## Class CommandLine.AbstractParseResultHandler<R>






- java.lang.Object

- 



  - picocli.CommandLine.AbstractHandler<R,CommandLine.AbstractParseResultHandler<R>>

  - 



    - picocli.CommandLine.AbstractParseResultHandler<R>












- 

All Implemented Interfaces:
CommandLine.IExecutionStrategy, CommandLine.IParseResultHandler2<R>


Direct Known Subclasses:
CommandLine.RunAll, CommandLine.RunFirst, CommandLine.RunLast


Enclosing class:
CommandLine


---

Deprecated. 
see `CommandLine.execute(String...)`, `CommandLine.getExecutionStrategy()`, `CommandLine.getParameterExceptionHandler()`, `CommandLine.getExecutionExceptionHandler()`




```
@Deprecated
public abstract static class CommandLine.AbstractParseResultHandler<R>
extends CommandLine.AbstractHandler<R,CommandLine.AbstractParseResultHandler<R>>
implements CommandLine.IParseResultHandler2<R>, CommandLine.IExecutionStrategy
```

Command line parse result handler that returns a value. This handler prints help if requested, and otherwise calls
 `handle(CommandLine.ParseResult)` with the parse result. Facilitates implementation of the `CommandLine.IParseResultHandler2` interface.
 

Note that `AbstractParseResultHandler` is a generic type. This, along with the abstract `self` method,
 allows method chaining to work properly in subclasses, without the need for casts. An example subclass can look like this:
 

```

 class MyResultHandler extends AbstractParseResultHandler<MyReturnType> {

     protected MyReturnType handle(ParseResult parseResult) throws ExecutionException { ... }

     protected MyResultHandler self() { return this; }
 }
 
```


Since:
3.0









- 




  - 



### Constructor Summary


Constructors 

Constructor and Description


`AbstractParseResultHandler()`
Deprecated. 
 









  - 



### Method Summary


All Methods Instance Methods Abstract Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description


`int`
`execute(CommandLine.ParseResult parseResult)`
Deprecated. 
"Executes" the user input and returns an exit code.



`protected List<CommandLine.IExitCodeGenerator>`
`extractExitCodeGenerators(CommandLine.ParseResult parseResult)`
Deprecated. 
 


`protected abstract R`
`handle(CommandLine.ParseResult parseResult)`
Deprecated. 
Processes the specified `ParseResult` and returns the result as a list of objects.



`R`
`handleParseResult(CommandLine.ParseResult parseResult)`
Deprecated. 
Prints help if requested, and otherwise calls `handle(CommandLine.ParseResult)`.






    - 



### Methods inherited from class picocli.CommandLine.AbstractHandler

`andExit, ansi, colorScheme, err, exit, exitCode, hasExitCode, out, returnResultOrExit, self, throwOrExit, useAnsi, useErr, useOut`





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Constructor Detail







    - 

#### AbstractParseResultHandler


```
public AbstractParseResultHandler()
```

Deprecated. 










  - 



### Method Detail







    - 

#### handleParseResult


```
public R handleParseResult(CommandLine.ParseResult parseResult)
                    throws CommandLine.ExecutionException
```

Deprecated. 
Prints help if requested, and otherwise calls `handle(CommandLine.ParseResult)`.
 Finally, either a list of result objects is returned, or the JVM is terminated if an exit code was set.

Specified by:
`handleParseResult` in interface `CommandLine.IParseResultHandler2<R>`
Parameters:
`parseResult` - the `ParseResult` that resulted from successfully parsing the command line arguments
Returns:
the result of `processing parse results`
Throws:
`CommandLine.ParameterException` - if the `HelpCommand` was invoked for an unknown subcommand. Any `ParameterExceptions`
      thrown from this method are treated as if this exception was thrown during parsing and passed to the `CommandLine.IExceptionHandler2`
`CommandLine.ExecutionException` - if a problem occurred while processing the parse results; client code can use
      `CommandLine.ExecutionException.getCommandLine()` to get the command or subcommand where processing failed










    - 

#### execute


```
public int execute(CommandLine.ParseResult parseResult)
            throws CommandLine.ExecutionException
```

Deprecated. 
Description copied from interface: `CommandLine.IExecutionStrategy`
"Executes" the user input and returns an exit code.
 Execution often means invoking a method on the selected CommandSpec's user object,
 and making the return value of that invocation available via `setExecutionResult`.

Specified by:
`execute` in interface `CommandLine.IExecutionStrategy`
Parameters:
`parseResult` - the parse result from which to select one or more `CommandSpec` instances to execute.
Returns:
an exit code
Throws:
`CommandLine.ExecutionException` - if any problem occurred while executing the command. Any exceptions (other than ParameterException) should be wrapped in a ExecutionException and not thrown as is.










    - 

#### handle


```
protected abstract R handle(CommandLine.ParseResult parseResult)
                     throws CommandLine.ExecutionException
```

Deprecated. 
Processes the specified `ParseResult` and returns the result as a list of objects.
 Implementations are responsible for catching any exceptions thrown in the `handle` method, and
 rethrowing an `ExecutionException` that details the problem and captures the offending `CommandLine` object.

Parameters:
`parseResult` - the `ParseResult` that resulted from successfully parsing the command line arguments
Returns:
the result of processing parse results
Throws:
`CommandLine.ExecutionException` - if a problem occurred while processing the parse results; client code can use
      `CommandLine.ExecutionException.getCommandLine()` to get the command or subcommand where processing failed










    - 

#### extractExitCodeGenerators


```
protected List<CommandLine.IExitCodeGenerator> extractExitCodeGenerators(CommandLine.ParseResult parseResult)
```

Deprecated. 
















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