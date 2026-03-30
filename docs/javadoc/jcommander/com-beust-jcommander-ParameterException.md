Package com.beust.jcommander

## Class ParameterException






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

All Implemented Interfaces:
`java.io.Serializable`


Direct Known Subclasses:
`MissingCommandException`


---


```
public class ParameterException
extends java.lang.RuntimeException
```

The main exception that JCommand will throw when something goes wrong while
 parsing parameters.

See Also:
Serialized Form









- 





  - 



### Constructor Summary


Constructors 

Constructor
Description


`ParameterException​(java.lang.String string)`
 


`ParameterException​(java.lang.String string,
                  java.lang.Throwable t)`
 


`ParameterException​(java.lang.Throwable t)`
 











  - 



### Method Summary


All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description


`JCommander`
`getJCommander()`
 


`void`
`setJCommander​(JCommander jc)`
 


`void`
`usage()`
 





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

#### ParameterException


```
public ParameterException​(java.lang.Throwable t)
```










    - 

#### ParameterException


```
public ParameterException​(java.lang.String string)
```










    - 

#### ParameterException


```
public ParameterException​(java.lang.String string,
                          java.lang.Throwable t)
```













  - 



### Method Detail







    - 

#### setJCommander


```
public void setJCommander​(JCommander jc)
```










    - 

#### getJCommander


```
public JCommander getJCommander()
```










    - 

#### usage


```
public void usage()
```