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

## Class CommandLine.AbstractHandler<R,T extends CommandLine.AbstractHandler<R,T>>






- java.lang.Object

- 



  - picocli.CommandLine.AbstractHandler<R,T>









- 

Type Parameters:
`R` - the return type of this handler
`T` - The type of the handler subclass; for fluent API method chaining


Direct Known Subclasses:
CommandLine.AbstractParseResultHandler, CommandLine.DefaultExceptionHandler


Enclosing class:
CommandLine


---

Deprecated. 
see `CommandLine.execute(String...)`




```
@Deprecated
public abstract static class CommandLine.AbstractHandler<R,T extends CommandLine.AbstractHandler<R,T>>
extends Object
```

Abstract superclass for `CommandLine.IParseResultHandler2` and `CommandLine.IExceptionHandler2` implementations.
 

Note that `AbstractHandler` is a generic type. This, along with the abstract `self` method,
 allows method chaining to work properly in subclasses, without the need for casts. An example subclass can look like this:
 

```

 class MyResultHandler extends AbstractHandler<MyReturnType, MyResultHandler> implements IParseResultHandler2<MyReturnType> {

     public MyReturnType handleParseResult(ParseResult parseResult) { ... }

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


`AbstractHandler()`
Deprecated. 
 









  - 



### Method Summary


All Methods Instance Methods Abstract Methods Concrete Methods Deprecated Methods 

Modifier and Type
Method and Description


`T`
`andExit(int exitCode)`
Deprecated. 
use `CommandLine.execute(String...)` instead, and call `System.exit()` in the application.




`CommandLine.Help.Ansi`
`ansi()`
Deprecated. 
use `colorScheme()` instead




`CommandLine.Help.ColorScheme`
`colorScheme()`
Deprecated. 
Returns the ColorScheme to use.



`PrintStream`
`err()`
Deprecated. 
Returns the stream to print diagnostic messages to.



`protected void`
`exit(int exitCode)`
Deprecated. 
Calls `System.exit(int)` with the specified exit code.



`Integer`
`exitCode()`
Deprecated. 
Returns the exit code to use as the termination status, or `null` (the default) if the handler should
 not call `System.exit(int)` after processing completes.



`boolean`
`hasExitCode()`
Deprecated. 
Returns `true` if an exit code was set with `andExit(int)`, or `false` (the default) if
 the handler should not call `System.exit(int)` after processing completes.



`PrintStream`
`out()`
Deprecated. 
Returns the stream to print command output to.



`protected R`
`returnResultOrExit(R result)`
Deprecated. 
Convenience method for subclasses that returns the specified result object if no exit code was set,
 or otherwise, if an exit code was set, calls `System.exit` with the configured
 exit code to terminate the currently running Java virtual machine.



`protected abstract T`
`self()`
Deprecated. 
Returns `this` to allow method chaining when calling the setters for a fluent API.



`protected R`
`throwOrExit(CommandLine.ExecutionException ex)`
Deprecated. 
Convenience method for subclasses that throws the specified ExecutionException if no exit code was set,
 or otherwise, if an exit code was set, prints the stacktrace of the specified exception
 to the diagnostic error stream and calls `System.exit` with the configured
 exit code to terminate the currently running Java virtual machine.



`T`
`useAnsi(CommandLine.Help.Ansi ansi)`
Deprecated. 
use `CommandLine.setColorScheme(Help.ColorScheme)` and `CommandLine.execute(String...)` instead




`T`
`useErr(PrintStream err)`
Deprecated. 
use `CommandLine.setErr(PrintWriter)` and `CommandLine.execute(String...)` instead




`T`
`useOut(PrintStream out)`
Deprecated. 
use `CommandLine.setOut(PrintWriter)` and `CommandLine.execute(String...)` instead







    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`













- 




  - 



### Constructor Detail







    - 

#### AbstractHandler


```
public AbstractHandler()
```

Deprecated. 










  - 



### Method Detail







    - 

#### out


```
public PrintStream out()
```

Deprecated. 
Returns the stream to print command output to. Defaults to `System.out`, unless `useOut(PrintStream)`
 was called with a different stream.
 

`IParseResultHandler2` implementations should use this stream.
 By convention, when the user requests
 help with a `--help` or similar option, the usage help message is printed to the standard output stream so that it can be easily searched and paged.









    - 

#### err


```
public PrintStream err()
```

Deprecated. 
Returns the stream to print diagnostic messages to. Defaults to `System.err`, unless `useErr(PrintStream)`
 was called with a different stream. 

`IExceptionHandler2` implementations should use this stream to print error
 messages (which may include a usage help message) when an unexpected error occurs.









    - 

#### ansi


```
@Deprecated
public CommandLine.Help.Ansi ansi()
```

Deprecated. use `colorScheme()` instead
Returns the ANSI style to use. Defaults to `Help.Ansi.AUTO`, unless `useAnsi(CommandLine.Help.Ansi)` was called with a different setting.









    - 

#### colorScheme


```
public CommandLine.Help.ColorScheme colorScheme()
```

Deprecated. 
Returns the ColorScheme to use. Defaults to `Help#defaultColorScheme(Help.Ansi.AUTO)`.

Since:
4.0










    - 

#### exitCode


```
public Integer exitCode()
```

Deprecated. 
Returns the exit code to use as the termination status, or `null` (the default) if the handler should
 not call `System.exit(int)` after processing completes.

See Also:
`andExit(int)`










    - 

#### hasExitCode


```
public boolean hasExitCode()
```

Deprecated. 
Returns `true` if an exit code was set with `andExit(int)`, or `false` (the default) if
 the handler should not call `System.exit(int)` after processing completes.











    - 

#### returnResultOrExit


```
protected R returnResultOrExit(R result)
```

Deprecated. 
Convenience method for subclasses that returns the specified result object if no exit code was set,
 or otherwise, if an exit code was set, calls `System.exit` with the configured
 exit code to terminate the currently running Java virtual machine.









    - 

#### throwOrExit


```
protected R throwOrExit(CommandLine.ExecutionException ex)
```

Deprecated. 
Convenience method for subclasses that throws the specified ExecutionException if no exit code was set,
 or otherwise, if an exit code was set, prints the stacktrace of the specified exception
 to the diagnostic error stream and calls `System.exit` with the configured
 exit code to terminate the currently running Java virtual machine.









    - 

#### exit


```
protected void exit(int exitCode)
```

Deprecated. 
Calls `System.exit(int)` with the specified exit code.









    - 

#### self


```
protected abstract T self()
```

Deprecated. 
Returns `this` to allow method chaining when calling the setters for a fluent API.









    - 

#### useOut


```
@Deprecated
public T useOut(PrintStream out)
```

Deprecated. use `CommandLine.setOut(PrintWriter)` and `CommandLine.execute(String...)` instead
Sets the stream to print command output to.









    - 

#### useErr


```
@Deprecated
public T useErr(PrintStream err)
```

Deprecated. use `CommandLine.setErr(PrintWriter)` and `CommandLine.execute(String...)` instead
Sets the stream to print diagnostic messages to.









    - 

#### useAnsi


```
@Deprecated
public T useAnsi(CommandLine.Help.Ansi ansi)
```

Deprecated. use `CommandLine.setColorScheme(Help.ColorScheme)` and `CommandLine.execute(String...)` instead
Sets the ANSI style to use and resets the color scheme to the default.

See Also:
`ansi()`










    - 

#### andExit


```
@Deprecated
public T andExit(int exitCode)
```

Deprecated. use `CommandLine.execute(String...)` instead, and call `System.exit()` in the application.
Indicates that the handler should call `System.exit(int)` after processing completes and sets the exit code to use as the termination status.
















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