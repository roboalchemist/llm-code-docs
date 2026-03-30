Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ExecutorServiceProvider

java.lang.Object
org.glassfish.tyrus.core.ExecutorServiceProvider

Direct Known Subclasses:
`BaseContainer`

---

public abstract class ExecutorServiceProvider
extends Object

Author:
Stepan Kopriva

-

## Constructor Summary

Constructors

Constructor
Description
`ExecutorServiceProvider()`

-

## Method Summary

Modifier and Type
Method
Description
`abstract ExecutorService`
`getExecutorService()`

Get the `ExecutorService`.

`abstract ScheduledExecutorService`
`getScheduledExecutorService()`

Get the `ScheduledExecutorService`.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ExecutorServiceProvider

public ExecutorServiceProvider()

-

## Method Details

-

### getExecutorService

public abstract ExecutorService getExecutorService()
Get the `ExecutorService`.

Returns:
executor service.

-

### getScheduledExecutorService

public abstract ScheduledExecutorService getScheduledExecutorService()
Get the `ScheduledExecutorService`.

Returns:
scheduled executor service.
