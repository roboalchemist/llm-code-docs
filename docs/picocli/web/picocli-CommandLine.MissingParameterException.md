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

## Class CommandLine.MissingParameterException






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



          - picocli.CommandLine.ParameterException

          - 



            - picocli.CommandLine.MissingParameterException
























- 

All Implemented Interfaces:
Serializable


Enclosing class:
CommandLine


---




```
public static class CommandLine.MissingParameterException
extends CommandLine.ParameterException
```

Exception indicating that a required parameter was not specified.

See Also:
Serialized Form









- 




  - 



### Field Summary




    - 



### Fields inherited from class picocli.CommandLine.ParameterException

`commandLine`









  - 



### Constructor Summary


Constructors 

Constructor and Description


`MissingParameterException(CommandLine commandLine,
                         Collection<CommandLine.Model.ArgSpec> missing,
                         String msg)` 


`MissingParameterException(CommandLine commandLine,
                         CommandLine.Model.ArgSpec missing,
                         String msg)` 









  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description


`List<CommandLine.Model.ArgSpec>`
`getMissing()` 





    - 



### Methods inherited from class picocli.CommandLine.ParameterException

`getArgSpec, getCommandLine, getValue`





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

#### MissingParameterException


```
public MissingParameterException(CommandLine commandLine,
                                 CommandLine.Model.ArgSpec missing,
                                 String msg)
```










    - 

#### MissingParameterException


```
public MissingParameterException(CommandLine commandLine,
                                 Collection<CommandLine.Model.ArgSpec> missing,
                                 String msg)
```











  - 



### Method Detail







    - 

#### getMissing


```
public List<CommandLine.Model.ArgSpec> getMissing()
```

















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