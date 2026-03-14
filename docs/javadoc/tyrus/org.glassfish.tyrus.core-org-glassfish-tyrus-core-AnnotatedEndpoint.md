Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class AnnotatedEndpoint

java.lang.Object
jakarta.websocket.Endpoint
org.glassfish.tyrus.core.AnnotatedEndpoint

---

public class AnnotatedEndpoint
extends jakarta.websocket.Endpoint
`Endpoint` descendant which represents deployed annotated endpoint.

Author:
Martin Matula, Stepan Kopriva, Pavel Bucek

-

## Method Summary

Modifier and Type
Method
Description
`static AnnotatedEndpoint`
`fromClass(Class<?> annotatedClass,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector,
 EndpointEventListener endpointEventListener)`

Create `AnnotatedEndpoint` from class.

`static AnnotatedEndpoint`
`fromClass(Class<?> annotatedClass,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector,
 EndpointEventListener endpointEventListener,
 Set<jakarta.websocket.Extension> extensions)`

Create `AnnotatedEndpoint` from class.

`static AnnotatedEndpoint`
`fromInstance(Object annotatedInstance,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector)`

Create `AnnotatedEndpoint` from instance.

`static AnnotatedEndpoint`
`fromInstance(Object annotatedInstance,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector,
 Set<jakarta.websocket.Extension> extensions)`

Create `AnnotatedEndpoint` from instance.

`jakarta.websocket.EndpointConfig`
`getEndpointConfig()`

`void`
`onClose(jakarta.websocket.Session session,
 jakarta.websocket.CloseReason closeReason)`

`void`
`onError(jakarta.websocket.Session session,
 Throwable thr)`

`void`
`onOpen(jakarta.websocket.Session session,
 jakarta.websocket.EndpointConfig configuration)`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Method Details

-

### fromClass

public static AnnotatedEndpoint fromClass(Class<?> annotatedClass,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector,
 EndpointEventListener endpointEventListener)
Create `AnnotatedEndpoint` from class.

Parameters:
`annotatedClass` - annotated class.
`componentProvider` - used for instantiating.
`isServerEndpoint` - `true` iff annotated endpoint is deployed on server side.
`incomingBufferSize` - size limit of the incoming buffer.
`collector` - error collector.
`endpointEventListener` - listener of monitored endpoint events.
Returns:
new instance.

-

### fromClass

public static AnnotatedEndpoint fromClass(Class<?> annotatedClass,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector,
 EndpointEventListener endpointEventListener,
 Set<jakarta.websocket.Extension> extensions)
Create `AnnotatedEndpoint` from class.

Parameters:
`annotatedClass` - annotated class.
`componentProvider` - used for instantiating.
`isServerEndpoint` - `true` iff annotated endpoint is deployed on server side.
`incomingBufferSize` - size limit of the incoming buffer.
`collector` - error collector.
`endpointEventListener` - listener of monitored endpoint events.
`extensions` - installed extentions.
Returns:
new instance.

-

### fromInstance

public static AnnotatedEndpoint fromInstance(Object annotatedInstance,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector)
Create `AnnotatedEndpoint` from instance.

Parameters:
`annotatedInstance` - annotated instance.
`componentProvider` - used for instantiating.
`isServerEndpoint` - `true` iff annotated endpoint is deployed on server side.
`incomingBufferSize` - size limit of the incoming buffer
`collector` - error collector.
Returns:
new instance.

-

### fromInstance

public static AnnotatedEndpoint fromInstance(Object annotatedInstance,
 ComponentProviderService componentProvider,
 boolean isServerEndpoint,
 int incomingBufferSize,
 ErrorCollector collector,
 Set<jakarta.websocket.Extension> extensions)
Create `AnnotatedEndpoint` from instance.

Parameters:
`annotatedInstance` - annotated instance.
`componentProvider` - used for instantiating.
`isServerEndpoint` - `true` iff annotated endpoint is deployed on server side.
`incomingBufferSize` - size limit of the incoming buffer
`collector` - error collector.
`extensions` - installed extentions.
Returns:
new instance.

-

### onClose

public void onClose(jakarta.websocket.Session session,
 jakarta.websocket.CloseReason closeReason)

Overrides:
`onClose` in class `jakarta.websocket.Endpoint`

-

### onError

public void onError(jakarta.websocket.Session session,
 Throwable thr)

Overrides:
`onError` in class `jakarta.websocket.Endpoint`

-

### getEndpointConfig

public jakarta.websocket.EndpointConfig getEndpointConfig()

-

### onOpen

public void onOpen(jakarta.websocket.Session session,
 jakarta.websocket.EndpointConfig configuration)

Specified by:
`onOpen` in class `jakarta.websocket.Endpoint`
