Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class BaseContainer

java.lang.Object
org.glassfish.tyrus.core.ExecutorServiceProvider
org.glassfish.tyrus.core.BaseContainer

All Implemented Interfaces:
`jakarta.websocket.WebSocketContainer`

---

public abstract class BaseContainer
extends ExecutorServiceProvider
implements jakarta.websocket.WebSocketContainer
Base WebSocket container.

 Client and Server containers extend this to provide additional functionality.

Author:
Jitendra Kotamraju

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`protected static interface`
`BaseContainer.ShutDownCondition`

-

## Constructor Summary

Constructors

Constructor
Description
`BaseContainer()`

-

## Method Summary

Modifier and Type
Method
Description
`ExecutorService`
`getExecutorService()`

Returns a container-managed `ExecutorService` registered under
 `java:comp/DefaultManagedExecutorService` or if the lookup has failed, it returns a
 `ExecutorService` created and managed by this instance of
 `BaseContainer`.

`abstract Map<String,Object>`
`getProperties()`

Container properties.

`ScheduledExecutorService`
`getScheduledExecutorService()`

Returns a container-managed `ScheduledExecutorService` registered under
 `java:comp/DefaultManagedScheduledExecutorService` or if the lookup has failed it returns a
 `ScheduledExecutorService` created and managed by this instance of
 `BaseContainer`.

`void`
`shutdown()`

Release executor services managed by this instance.

`protected void`
`shutdown(BaseContainer.ShutDownCondition shutDownCondition)`

Release executor services managed by this instance if the condition passed in the parameter is fulfilled.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface jakarta.websocket.WebSocketContainer

`connectToServer, connectToServer, connectToServer, connectToServer, getDefaultAsyncSendTimeout, getDefaultMaxBinaryMessageBufferSize, getDefaultMaxSessionIdleTimeout, getDefaultMaxTextMessageBufferSize, getInstalledExtensions, setAsyncSendTimeout, setDefaultMaxBinaryMessageBufferSize, setDefaultMaxSessionIdleTimeout, setDefaultMaxTextMessageBufferSize`

-

## Constructor Details

-

### BaseContainer

public BaseContainer()

-

## Method Details

-

### getExecutorService

public ExecutorService getExecutorService()
Returns a container-managed `ExecutorService` registered under
 `java:comp/DefaultManagedExecutorService` or if the lookup has failed, it returns a
 `ExecutorService` created and managed by this instance of
 `BaseContainer`.

Specified by:
`getExecutorService` in class `ExecutorServiceProvider`
Returns:
executor service.

-

### getScheduledExecutorService

public ScheduledExecutorService getScheduledExecutorService()
Returns a container-managed `ScheduledExecutorService` registered under
 `java:comp/DefaultManagedScheduledExecutorService` or if the lookup has failed it returns a
 `ScheduledExecutorService` created and managed by this instance of
 `BaseContainer`.

Specified by:
`getScheduledExecutorService` in class `ExecutorServiceProvider`
Returns:
scheduled executor service.

-

### shutdown

public void shutdown()
Release executor services managed by this instance. Executor services obtained via JNDI lookup won't be
 shut down.

-

### shutdown

protected void shutdown(BaseContainer.ShutDownCondition shutDownCondition)
Release executor services managed by this instance if the condition passed in the parameter is fulfilled.
 Executor services obtained via JNDI lookup won't be shut down.

Parameters:
`shutDownCondition` - condition that will be evaluated before executor services are released and they will be
                          released only if the condition is evaluated to `true`. The condition will be
                          evaluated in a synchronized block in order to make the process of its evaluation
                          and executor services release an atomic operation.

-

### getProperties

public abstract Map<String,Object> getProperties()
Container properties.

 Used to set container specific configuration.

Returns:
map containing container properties.
