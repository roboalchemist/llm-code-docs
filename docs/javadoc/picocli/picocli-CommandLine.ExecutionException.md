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

## Class CommandLine.ExecutionException






- java.lang.Object

- 



  - java.lang.Throwable

  - 



    - java.lang.Exception

    - 



      - java.lang.RuntimeException

      - 



        - picocli.CommandLine.PicocliException

        - 



          - picocli.CommandLine.ExecutionException





















- 

All Implemented Interfaces:
Serializable


Enclosing class:
CommandLine


---




```
public static class CommandLine.ExecutionException
extends CommandLine.PicocliException
```

Exception indicating a problem while invoking a command or subcommand.
 Keeps a reference to the `CommandLine` object where the cause exception occurred,
 so that client code can tailor their handling for the specific command (print the command's usage help message, for example).

Since:
2.0
See Also:
Serialized Form









- 




  - 



### Constructor Summary


Constructors 

Constructor and Description


`ExecutionException(CommandLine commandLine,
                  String msg)` 


`ExecutionException(CommandLine commandLine,
                  String msg,
                  Throwable t)` 









  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`CommandLine`
`getCommandLine()`
Returns the `CommandLine` object for the (sub)command that could not be invoked.






    - 



### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`





    - 



### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`













- 




  - 



### Constructor Detail







    - 

#### ExecutionException


```
public ExecutionException(CommandLine commandLine,
                          String msg)
```










    - 

#### ExecutionException


```
public ExecutionException(CommandLine commandLine,
                          String msg,
                          Throwable t)
```











  - 



### Method Detail







    - 

#### getCommandLine


```
public CommandLine getCommandLine()
```

Returns the `CommandLine` object for the (sub)command that could not be invoked.

Returns:
the `CommandLine` object for the (sub)command where invocation failed.

















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