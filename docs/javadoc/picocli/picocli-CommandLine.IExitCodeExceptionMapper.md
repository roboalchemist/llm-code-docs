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

## Interface CommandLine.IExitCodeExceptionMapper







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IExitCodeExceptionMapper
```

Interface that provides the appropriate exit code that will be returned from the `execute`
 method for an exception that occurred during parsing or while invoking the command's Runnable, Callable, or Method.
 

Example usage:
 

```

 @Command
 class FailingCommand implements Callable<Void> {
     public Void call() throws IOException {
         throw new IOException("error");
     }
 }
 IExitCodeExceptionMapper mapper = new IExitCodeExceptionMapper() {
     public int getExitCode(Throwable t) {
         if (t instanceof IOException && "error".equals(t.getMessage())) {
             return 123;
         }
         return 987;
     }
 }

 CommandLine cmd = new CommandLine(new FailingCommand());
 cmd.setExitCodeExceptionMapper(mapper);
 int exitCode = cmd.execute(args);
 assert exitCode == 123;
 System.exit(exitCode);
 
```


Since:
4.0
See Also:
`CommandLine.setExitCodeExceptionMapper(IExitCodeExceptionMapper)`









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`int`
`getExitCode(Throwable exception)`
Returns the exit code that should be returned from the `execute` method.














- 




  - 



### Method Detail







    - 

#### getExitCode


```
int getExitCode(Throwable exception)
```

Returns the exit code that should be returned from the `execute` method.

Parameters:
`exception` - the exception that occurred during parsing or while invoking the command's Runnable, Callable, or Method.
Returns:
the exit code

















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