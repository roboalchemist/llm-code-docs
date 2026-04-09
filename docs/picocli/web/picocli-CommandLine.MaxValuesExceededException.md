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

## Class CommandLine.MaxValuesExceededException






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



            - picocli.CommandLine.MaxValuesExceededException
























- 

All Implemented Interfaces:
Serializable


Enclosing class:
CommandLine


---




```
public static class CommandLine.MaxValuesExceededException
extends CommandLine.ParameterException
```

Exception indicating that more values were specified for an option or parameter than its `arity` allows.

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


`MaxValuesExceededException(CommandLine commandLine,
                          String msg)` 









  - 



### Method Summary




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

#### MaxValuesExceededException


```
public MaxValuesExceededException(CommandLine commandLine,
                                  String msg)
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