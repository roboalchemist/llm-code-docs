# Class ConnectionManagerSupport

java.lang.Object
org.springframework.web.socket.client.ConnectionManagerSupport

All Implemented Interfaces:
`org.springframework.context.Lifecycle, org.springframework.context.Phased, org.springframework.context.SmartLifecycle`

Direct Known Subclasses:
`AnnotatedEndpointConnectionManager, EndpointConnectionManager, WebSocketConnectionManager`

---

public abstract class ConnectionManagerSupport
extends Object
implements org.springframework.context.SmartLifecycle
Base class for a connection manager that automates the process of connecting
to a WebSocket server with the Spring ApplicationContext lifecycle. Connects
to a WebSocket server on `start()` and disconnects on `stop()`.
If `setAutoStartup(boolean)` is set to `true` this will be done
automatically when the Spring `ApplicationContext` is refreshed.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected final org.apache.commons.logging.Log`
`logger`
 

### Fields inherited from interface org.springframework.context.SmartLifecycle

`DEFAULT_PHASE`

- 

## Constructor Summary

Constructors

Constructor
Description
`ConnectionManagerSupport(String uriTemplate,
 @Nullable Object... uriVariables)`

Constructor with a URI template and variables.

`ConnectionManagerSupport(URI uri)`

Constructor with a prepared `URI`.

- 

## Method Summary

Modifier and Type
Method
Description
`protected abstract void`
`closeConnection()`

Subclasses implement this to close the connection.

`int`
`getPhase()`

Return the phase in which this endpoint connection factory will be auto-connected
and stopped.

`protected URI`
`getUri()`
 
`boolean`
`isAutoStartup()`

Return the value for the 'autoStartup' property.

`abstract boolean`
`isConnected()`

Whether the connection is open/`true` or closed/`false`.

`boolean`
`isRunning()`

Return whether this ConnectionManager has been started.

`protected abstract void`
`openConnection()`

Subclasses implement this to actually establish the connection.

`void`
`setAutoStartup(boolean autoStartup)`

Set whether to auto-connect to the remote endpoint after this connection manager
has been initialized and the Spring context has been refreshed.

`void`
`setPhase(int phase)`

Specify the phase in which a connection should be established to the remote
endpoint and subsequently closed.

`final void`
`start()`

Start the WebSocket connection.

`protected void`
`startInternal()`
 
`final void`
`stop()`
 
`final void`
`stop(Runnable callback)`
 
`protected void`
`stopInternal()`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.springframework.context.SmartLifecycle

`isPauseable`

- 

## Field Details

  - 

### logger

protected final org.apache.commons.logging.Log logger

- 

## Constructor Details

  - 

### ConnectionManagerSupport

public ConnectionManagerSupport(String uriTemplate,
 @Nullable Object... uriVariables)
Constructor with a URI template and variables.

  - 

### ConnectionManagerSupport

public ConnectionManagerSupport(URI uri)
Constructor with a prepared `URI`.

Parameters:
`uri` - the url to connect to
Since:
6.0.5

- 

## Method Details

  - 

### getUri

protected URI getUri()

  - 

### setAutoStartup

public void setAutoStartup(boolean autoStartup)
Set whether to auto-connect to the remote endpoint after this connection manager
has been initialized and the Spring context has been refreshed.

Default is "false".

  - 

### isAutoStartup

public boolean isAutoStartup()
Return the value for the 'autoStartup' property. If "true", this endpoint
connection manager will connect to the remote endpoint upon a
ContextRefreshedEvent.

Specified by:
`isAutoStartup` in interface `org.springframework.context.SmartLifecycle`

  - 

### setPhase

public void setPhase(int phase)
Specify the phase in which a connection should be established to the remote
endpoint and subsequently closed. The startup order proceeds from lowest to
highest, and the shutdown order is the reverse of that. By default, this value is
Integer.MAX_VALUE meaning that this endpoint connection factory connects as late as
possible and is closed as soon as possible.

  - 

### getPhase

public int getPhase()
Return the phase in which this endpoint connection factory will be auto-connected
and stopped.

Specified by:
`getPhase` in interface `org.springframework.context.Phased`
Specified by:
`getPhase` in interface `org.springframework.context.SmartLifecycle`

  - 

### start

public final void start()
Start the WebSocket connection. If already connected, the method has no impact.

Specified by:
`start` in interface `org.springframework.context.Lifecycle`

  - 

### startInternal

protected void startInternal()

  - 

### stop

public final void stop()

Specified by:
`stop` in interface `org.springframework.context.Lifecycle`

  - 

### stop

public final void stop(Runnable callback)

Specified by:
`stop` in interface `org.springframework.context.SmartLifecycle`

  - 

### stopInternal

protected void stopInternal()
                     throws Exception

Throws:
`Exception`

  - 

### isRunning

public boolean isRunning()
Return whether this ConnectionManager has been started.

Specified by:
`isRunning` in interface `org.springframework.context.Lifecycle`

  - 

### isConnected

public abstract boolean isConnected()
Whether the connection is open/`true` or closed/`false`.

  - 

### openConnection

protected abstract void openConnection()
Subclasses implement this to actually establish the connection.

  - 

### closeConnection

protected abstract void closeConnection()
                                 throws Exception
Subclasses implement this to close the connection.

Throws:
`Exception`