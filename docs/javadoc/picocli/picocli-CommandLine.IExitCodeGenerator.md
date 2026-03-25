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

## Interface CommandLine.IExitCodeGenerator







- 

Enclosing class:
CommandLine


---




```
public static interface CommandLine.IExitCodeGenerator
```

`@Command`-annotated classes can implement this interface to specify an exit code that will be returned
 from the `execute` method when the command is successfully invoked.

 

Example usage:
 

```

 @Command
 class MyCommand implements Runnable, IExitCodeGenerator {
     public void run() { System.out.println("Hello"); }
     public int getExitCode() { return 123; }
 }
 CommandLine cmd = new CommandLine(new MyCommand());
 int exitCode = cmd.execute(args);
 assert exitCode == 123;
 System.exit(exitCode);
 
```


Since:
4.0









- 




  - 



### Method Summary


All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description


`int`
`getExitCode()`
Returns the exit code that should be returned from the `execute` method.














- 




  - 



### Method Detail







    - 

#### getExitCode


```
int getExitCode()
```

Returns the exit code that should be returned from the `execute` method.

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