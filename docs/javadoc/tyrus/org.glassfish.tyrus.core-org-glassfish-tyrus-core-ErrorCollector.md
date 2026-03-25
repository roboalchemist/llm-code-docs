Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ErrorCollector

java.lang.Object
org.glassfish.tyrus.core.ErrorCollector

---

public class ErrorCollector
extends Object
Used to collect deployment errors to present these to the user together.

Author:
Stepan Kopriva

-

## Constructor Summary

Constructors

Constructor
Description
`ErrorCollector()`

-

## Method Summary

Modifier and Type
Method
Description
`void`
`addException(Exception exception)`

Add `Exception` to the collector.

`jakarta.websocket.DeploymentException`
`composeComprehensiveException()`

Create `DeploymentException` with message concatenated from collected exceptions.

`boolean`
`isEmpty()`

Checks whether any exception has been logged.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ErrorCollector

public ErrorCollector()

-

## Method Details

-

### addException

public void addException(Exception exception)
Add `Exception` to the collector.

Parameters:
`exception` - to be collected.

-

### composeComprehensiveException

public jakarta.websocket.DeploymentException composeComprehensiveException()
Create `DeploymentException` with message concatenated from collected exceptions.

Returns:
comprehensive exception.

-

### isEmpty

public boolean isEmpty()
Checks whether any exception has been logged.

Returns:
`true` iff no exception was logged, `false` otherwise.
