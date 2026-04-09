Package org.jbake.launcher

# Class JettyServer

java.lang.Object
org.jbake.launcher.JettyServer

All Implemented Interfaces:
`Closeable`, `AutoCloseable`

---

public class JettyServer
extends Object
implements Closeable
Provides Jetty server related functions

- 

## Constructor Summary

Constructors

Constructor
Description
`JettyServer()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`close()`
 
`boolean`
`isStarted()`
 
`void`
`run(String resourceBase,
 String port)`

Deprecated.

`void`
`run(String resourceBase,
 JBakeConfiguration configuration)`
 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### JettyServer

public JettyServer()

- 

## Method Details

  - 

### run

@Deprecated
public void run(String resourceBase,
 String port)
Deprecated.

  - 

### run

public void run(String resourceBase,
 JBakeConfiguration configuration)

  - 

### isStarted

public boolean isStarted()

  - 

### close

public void close()
           throws IOException

Specified by:
`close` in interface `AutoCloseable`
Specified by:
`close` in interface `Closeable`
Throws:
`IOException`