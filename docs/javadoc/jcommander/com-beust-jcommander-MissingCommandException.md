Package com.beust.jcommander

## Class MissingCommandException






- java.lang.Object

- 



  - java.lang.Throwable

  - 



    - java.lang.Exception

    - 



      - java.lang.RuntimeException

      - 



        - com.beust.jcommander.ParameterException

        - 



          - com.beust.jcommander.MissingCommandException





















- 

All Implemented Interfaces:
`java.io.Serializable`


---


```
public class MissingCommandException
extends ParameterException
```

Thrown when a command was expected.

See Also:
Serialized Form









- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`MissingCommandException​(java.lang.String message)`
 


`MissingCommandException​(java.lang.String message,
                       java.lang.String command)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`java.lang.String`
`getUnknownCommand()`
 





    - 



### Methods inherited from class com.beust.jcommander.ParameterException

`getJCommander, setJCommander, usage`





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

#### MissingCommandException


```
public MissingCommandException​(java.lang.String message)
```










    - 

#### MissingCommandException


```
public MissingCommandException​(java.lang.String message,
                               java.lang.String command)
```













  - 



### Method Detail







    - 

#### getUnknownCommand


```
public java.lang.String getUnknownCommand()
```