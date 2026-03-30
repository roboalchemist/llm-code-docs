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

## Interface CommandLine.IExecutionStrategy







- 

All Known Implementing Classes:
CommandLine.AbstractParseResultHandler, CommandLine.RunAll, CommandLine.RunFirst, CommandLine.RunLast


Enclosing class:
CommandLine


---




```
public static interface CommandLine.IExecutionStrategy
```

Implementations are responsible for "executing" the user input and returning an exit code.
 The `CommandLine.execute(String...)` method delegates to a configured execution strategy.
 

**Implementation Requirements:**
 

Implementers responsibilities are:
 

   
  - From the `ParseResult`, select which `CommandSpec` should be executed. This is especially important for commands that have subcommands.
   
  - "Execute" the selected `CommandSpec`. Often this means invoking a method on the spec's user object.
   
  - Call `setExecutionResult` to make the return value of that method invocation available to the application
   
  - Return an exit code. Common sources of exit values are the invoked method's return value, or the user object if it implements `CommandLine.IExitCodeGenerator`.
 

 

Implementors that need to print messages to the console should use the output and error PrintWriters,
 and the color scheme from the CommandLine object obtained from ParseResult's CommandSpec.
 

**API Note:**
 

This interface supersedes `CommandLine.IParseResultHandler2`.

Since:
4.0









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`int`
`execute(CommandLine.ParseResult parseResult)`
"Executes" the user input and returns an exit code.














- 




  - 



### Method Detail







    - 

#### execute


```
int execute(CommandLine.ParseResult parseResult)
     throws CommandLine.ExecutionException,
            CommandLine.ParameterException
```

"Executes" the user input and returns an exit code.
 Execution often means invoking a method on the selected CommandSpec's user object,
 and making the return value of that invocation available via `setExecutionResult`.

Parameters:
`parseResult` - the parse result from which to select one or more `CommandSpec` instances to execute.
Returns:
an exit code
Throws:
`CommandLine.ParameterException` - if the invoked method on the CommandSpec's user object threw a ParameterException to signify invalid user input.
`CommandLine.ExecutionException` - if any problem occurred while executing the command. Any exceptions (other than ParameterException) should be wrapped in a ExecutionException and not thrown as is.

















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