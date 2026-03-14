# Class AnnotatedEndpointConnectionManager

java.lang.Object
org.springframework.web.socket.client.ConnectionManagerSupport
org.springframework.web.socket.client.standard.AnnotatedEndpointConnectionManager

All Implemented Interfaces:
`org.springframework.beans.factory.Aware, org.springframework.beans.factory.BeanFactoryAware, org.springframework.context.Lifecycle, org.springframework.context.Phased, org.springframework.context.SmartLifecycle`

---

public class AnnotatedEndpointConnectionManager
extends ConnectionManagerSupport
implements org.springframework.beans.factory.BeanFactoryAware
WebSocket `connection manager` that connects
to the server via `WebSocketContainer` and handles the session with an
`@ClientEndpoint` endpoint.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Field Summary

### Fields inherited from class ConnectionManagerSupport

`logger`

### Fields inherited from interface org.springframework.context.SmartLifecycle

`DEFAULT_PHASE`

- 

## Constructor Summary

Constructors

Constructor
Description
`AnnotatedEndpointConnectionManager(Class<?> endpointClass,
 String uriTemplate,
 @Nullable Object... uriVariables)`
 
`AnnotatedEndpointConnectionManager(Object endpoint,
 String uriTemplate,
 @Nullable Object... uriVariables)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected void`
`closeConnection()`

Subclasses implement this to close the connection.

`org.springframework.core.task.TaskExecutor`
`getTaskExecutor()`

Return the configured `TaskExecutor`.

`jakarta.websocket.WebSocketContainer`
`getWebSocketContainer()`
 
`boolean`
`isConnected()`

Whether the connection is open/`true` or closed/`false`.

`protected void`
`openConnection()`

Subclasses implement this to actually establish the connection.

`void`
`setBeanFactory(org.springframework.beans.factory.BeanFactory beanFactory)`
 
`void`
`setTaskExecutor(org.springframework.core.task.TaskExecutor taskExecutor)`

Set a `TaskExecutor` to use to open the connection.

`void`
`setWebSocketContainer(jakarta.websocket.WebSocketContainer webSocketContainer)`
 

### Methods inherited from class ConnectionManagerSupport

`getPhase, getUri, isAutoStartup, isRunning, setAutoStartup, setPhase, start, startInternal, stop, stop, stopInternal`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.springframework.context.SmartLifecycle

`isPauseable`

- 

## Constructor Details

  - 

### AnnotatedEndpointConnectionManager

public AnnotatedEndpointConnectionManager(Object endpoint,
 String uriTemplate,
 @Nullable Object... uriVariables)

  - 

### AnnotatedEndpointConnectionManager

public AnnotatedEndpointConnectionManager(Class<?> endpointClass,
 String uriTemplate,
 @Nullable Object... uriVariables)

- 

## Method Details

  - 

### setWebSocketContainer

public void setWebSocketContainer(jakarta.websocket.WebSocketContainer webSocketContainer)

  - 

### getWebSocketContainer

public jakarta.websocket.WebSocketContainer getWebSocketContainer()

  - 

### setBeanFactory

public void setBeanFactory(org.springframework.beans.factory.BeanFactory beanFactory)
                    throws org.springframework.beans.BeansException

Specified by:
`setBeanFactory` in interface `org.springframework.beans.factory.BeanFactoryAware`
Throws:
`org.springframework.beans.BeansException`

  - 

### setTaskExecutor

public void setTaskExecutor(org.springframework.core.task.TaskExecutor taskExecutor)
Set a `TaskExecutor` to use to open the connection.
By default `SimpleAsyncTaskExecutor` is used.

  - 

### getTaskExecutor

public org.springframework.core.task.TaskExecutor getTaskExecutor()
Return the configured `TaskExecutor`.

  - 

### isConnected

public boolean isConnected()
Description copied from class: `ConnectionManagerSupport`
Whether the connection is open/`true` or closed/`false`.

Specified by:
`isConnected` in class `ConnectionManagerSupport`

  - 

### openConnection

protected void openConnection()
Description copied from class: `ConnectionManagerSupport`
Subclasses implement this to actually establish the connection.

Specified by:
`openConnection` in class `ConnectionManagerSupport`

  - 

### closeConnection

protected void closeConnection()
                        throws Exception
Description copied from class: `ConnectionManagerSupport`
Subclasses implement this to close the connection.

Specified by:
`closeConnection` in class `ConnectionManagerSupport`
Throws:
`Exception`