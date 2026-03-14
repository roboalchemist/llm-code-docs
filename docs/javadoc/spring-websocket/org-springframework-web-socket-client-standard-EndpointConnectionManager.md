# Class EndpointConnectionManager

java.lang.Object
org.springframework.web.socket.client.ConnectionManagerSupport
org.springframework.web.socket.client.standard.EndpointConnectionManager

All Implemented Interfaces:
`org.springframework.beans.factory.Aware, org.springframework.beans.factory.BeanFactoryAware, org.springframework.context.Lifecycle, org.springframework.context.Phased, org.springframework.context.SmartLifecycle`

---

public class EndpointConnectionManager
extends ConnectionManagerSupport
implements org.springframework.beans.factory.BeanFactoryAware
WebSocket `connection manager` that connects
to the server via `WebSocketContainer` and handles the session with an
`Endpoint`.

Since:
4.0
Author:
Rossen Stoyanchev
See Also:

- `AnnotatedEndpointConnectionManager`

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
`EndpointConnectionManager(jakarta.websocket.Endpoint endpoint,
 String uriTemplate,
 @Nullable Object... uriVariables)`
 
`EndpointConnectionManager(Class<? extends jakarta.websocket.Endpoint> endpointClass,
 String uriTemplate,
 @Nullable Object... uriVars)`
 

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
`setConfigurator(jakarta.websocket.ClientEndpointConfig.Configurator configurator)`
 
`void`
`setDecoders(List<Class<? extends jakarta.websocket.Decoder>> decoders)`
 
`void`
`setEncoders(List<Class<? extends jakarta.websocket.Encoder>> encoders)`
 
`void`
`setExtensions(jakarta.websocket.Extension... extensions)`
 
`void`
`setSupportedProtocols(String... protocols)`
 
`void`
`setTaskExecutor(org.springframework.core.task.TaskExecutor taskExecutor)`

Set a `TaskExecutor` to use to open connections.

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

### EndpointConnectionManager

public EndpointConnectionManager(jakarta.websocket.Endpoint endpoint,
 String uriTemplate,
 @Nullable Object... uriVariables)

  - 

### EndpointConnectionManager

public EndpointConnectionManager(Class<? extends jakarta.websocket.Endpoint> endpointClass,
 String uriTemplate,
 @Nullable Object... uriVars)

- 

## Method Details

  - 

### setSupportedProtocols

public void setSupportedProtocols(String... protocols)

  - 

### setExtensions

public void setExtensions(jakarta.websocket.Extension... extensions)

  - 

### setEncoders

public void setEncoders(List<Class<? extends jakarta.websocket.Encoder>> encoders)

  - 

### setDecoders

public void setDecoders(List<Class<? extends jakarta.websocket.Decoder>> decoders)

  - 

### setConfigurator

public void setConfigurator(jakarta.websocket.ClientEndpointConfig.Configurator configurator)

  - 

### setWebSocketContainer

public void setWebSocketContainer(jakarta.websocket.WebSocketContainer webSocketContainer)

  - 

### getWebSocketContainer

public jakarta.websocket.WebSocketContainer getWebSocketContainer()

  - 

### setBeanFactory

public void setBeanFactory(org.springframework.beans.factory.BeanFactory beanFactory)

Specified by:
`setBeanFactory` in interface `org.springframework.beans.factory.BeanFactoryAware`

  - 

### setTaskExecutor

public void setTaskExecutor(org.springframework.core.task.TaskExecutor taskExecutor)
Set a `TaskExecutor` to use to open connections.
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