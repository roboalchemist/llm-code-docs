Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusEndpointWrapper

java.lang.Object
org.glassfish.tyrus.core.TyrusEndpointWrapper

---

public class TyrusEndpointWrapper
extends Object
Wraps the registered application class.

 There is one `TyrusEndpointWrapper` for each application class, which handles all the methods.

Author:
Danny Coward, Stepan Kopriva, Martin Matula, Pavel Bucek

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class`
`TyrusEndpointWrapper.SessionListener`

Session listener.

-

## Constructor Summary

Constructors

Constructor
Description
`TyrusEndpointWrapper(jakarta.websocket.Endpoint endpoint,
 jakarta.websocket.EndpointConfig configuration,
 ComponentProviderService componentProvider,
 jakarta.websocket.WebSocketContainer container,
 String contextPath,
 jakarta.websocket.server.ServerEndpointConfig.Configurator configurator,
 TyrusEndpointWrapper.SessionListener sessionListener,
 ClusterContext clusterContext,
 EndpointEventListener endpointEventListener,
 Boolean parallelBroadcastEnabled)`

Create `TyrusEndpointWrapper` for `Endpoint` instance or `AnnotatedEndpoint` instance.

`TyrusEndpointWrapper(Class<? extends jakarta.websocket.Endpoint> endpointClass,
 jakarta.websocket.EndpointConfig configuration,
 ComponentProviderService componentProvider,
 jakarta.websocket.WebSocketContainer container,
 String contextPath,
 jakarta.websocket.server.ServerEndpointConfig.Configurator configurator,
 TyrusEndpointWrapper.SessionListener sessionListener,
 ClusterContext clusterContext,
 EndpointEventListener endpointEventListener,
 Boolean parallelBroadcastEnabled)`

Create `TyrusEndpointWrapper` for class that extends `Endpoint`.

-

## Method Summary

Modifier and Type
Method
Description
`jakarta.websocket.Session`
`createSessionForRemoteEndpoint(TyrusWebSocket socket,
 String subprotocol,
 List<jakarta.websocket.Extension> extensions,
 DebugContext debugContext)`

Creates a Session based on the `TyrusWebSocket`, subprotocols and extensions.

`Object`
`doEncode(jakarta.websocket.Session session,
 Object message)`

`jakarta.websocket.EndpointConfig`
`getEndpointConfig()`

Get Endpoint configuration.

`String`
`getEndpointPath()`

Server-side; Get Endpoint absolute path.

`String`
`toString()`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### TyrusEndpointWrapper

public TyrusEndpointWrapper(Class<? extends jakarta.websocket.Endpoint> endpointClass,
 jakarta.websocket.EndpointConfig configuration,
 ComponentProviderService componentProvider,
 jakarta.websocket.WebSocketContainer container,
 String contextPath,
 jakarta.websocket.server.ServerEndpointConfig.Configurator configurator,
 TyrusEndpointWrapper.SessionListener sessionListener,
 ClusterContext clusterContext,
 EndpointEventListener endpointEventListener,
 Boolean parallelBroadcastEnabled)
                     throws jakarta.websocket.DeploymentException
Create `TyrusEndpointWrapper` for class that extends `Endpoint`.

Parameters:
`endpointClass` - endpoint class for which the wrapper is created.
`configuration` - endpoint configuration.
`componentProvider` - component provider.
`container` - container where the wrapper is running.
`contextPath` - context path of the application.
`configurator` - endpoint configurator.
`sessionListener` - session listener.
`clusterContext` - cluster context instance. `null` indicates standalone mode.
`endpointEventListener` - endpoint event listener.
`parallelBroadcastEnabled` - `true` if parallel broadcast should be enabled, `true` is default.
Throws:
`jakarta.websocket.DeploymentException` - when the endpoint is not valid.

-

### TyrusEndpointWrapper

public TyrusEndpointWrapper(jakarta.websocket.Endpoint endpoint,
 jakarta.websocket.EndpointConfig configuration,
 ComponentProviderService componentProvider,
 jakarta.websocket.WebSocketContainer container,
 String contextPath,
 jakarta.websocket.server.ServerEndpointConfig.Configurator configurator,
 TyrusEndpointWrapper.SessionListener sessionListener,
 ClusterContext clusterContext,
 EndpointEventListener endpointEventListener,
 Boolean parallelBroadcastEnabled)
                     throws jakarta.websocket.DeploymentException
Create `TyrusEndpointWrapper` for `Endpoint` instance or `AnnotatedEndpoint` instance.

Parameters:
`endpoint` - endpoint instance for which the wrapper is created.
`configuration` - endpoint configuration.
`componentProvider` - component provider.
`container` - container where the wrapper is running.
`contextPath` - context path of the application.
`configurator` - endpoint configurator.
`sessionListener` - session listener.
`clusterContext` - cluster context instance. `null` indicates standalone mode.
`endpointEventListener` - endpoint event listener.
`parallelBroadcastEnabled` - `true` if parallel broadcast should be enabled, `true` is default.
Throws:
`jakarta.websocket.DeploymentException` - when the endpoint is not valid.

-

## Method Details

-

### doEncode

public Object doEncode(jakarta.websocket.Session session,
 Object message)
                throws jakarta.websocket.EncodeException,
IOException

Throws:
`jakarta.websocket.EncodeException`
`IOException`

-

### getEndpointPath

public String getEndpointPath()
Server-side; Get Endpoint absolute path.

Returns:
endpoint absolute path.

-

### createSessionForRemoteEndpoint

public jakarta.websocket.Session createSessionForRemoteEndpoint(TyrusWebSocket socket,
 String subprotocol,
 List<jakarta.websocket.Extension> extensions,
 DebugContext debugContext)
Creates a Session based on the `TyrusWebSocket`, subprotocols and extensions.

Parameters:
`socket` - the other end of the connection.
`subprotocol` - used.
`extensions` - extensions used.
`debugContext` - debug context.
Returns:
`Session` representing the connection.

-

### getEndpointConfig

public jakarta.websocket.EndpointConfig getEndpointConfig()
Get Endpoint configuration.

Returns:
configuration.

-

### toString

public String toString()

Overrides:
`toString` in class `Object`
