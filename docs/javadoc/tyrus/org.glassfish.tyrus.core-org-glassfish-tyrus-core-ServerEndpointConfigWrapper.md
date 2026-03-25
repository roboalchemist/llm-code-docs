Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ServerEndpointConfigWrapper

java.lang.Object
org.glassfish.tyrus.core.ServerEndpointConfigWrapper

All Implemented Interfaces:
`jakarta.websocket.EndpointConfig`, `jakarta.websocket.server.ServerEndpointConfig`

---

public class ServerEndpointConfigWrapper
extends Object
implements jakarta.websocket.server.ServerEndpointConfig
A public class that holds a wrapped ServerEndpointConfig.

-

## Nested Class Summary

## Nested classes/interfaces inherited from interface jakarta.websocket.server.ServerEndpointConfig

`jakarta.websocket.server.ServerEndpointConfig.Builder, jakarta.websocket.server.ServerEndpointConfig.Configurator`

-

## Field Summary

Fields

Modifier and Type
Field
Description
`protected final jakarta.websocket.server.ServerEndpointConfig`
`wrapped`

-

## Method Summary

Modifier and Type
Method
Description
`jakarta.websocket.server.ServerEndpointConfig.Configurator`
`getConfigurator()`

`List<Class<? extends jakarta.websocket.Decoder>>`
`getDecoders()`

`List<Class<? extends jakarta.websocket.Encoder>>`
`getEncoders()`

`Class<?>`
`getEndpointClass()`

`List<jakarta.websocket.Extension>`
`getExtensions()`

`String`
`getPath()`

`List<String>`
`getSubprotocols()`

`Map<String,Object>`
`getUserProperties()`

`jakarta.websocket.server.ServerEndpointConfig`
`getWrapped()`

Get the wrapped `ServerEndpointConfig`.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Field Details

-

### wrapped

protected final jakarta.websocket.server.ServerEndpointConfig wrapped

-

## Method Details

-

### getEndpointClass

public Class<?> getEndpointClass()

Specified by:
`getEndpointClass` in interface `jakarta.websocket.server.ServerEndpointConfig`

-

### getPath

public String getPath()

Specified by:
`getPath` in interface `jakarta.websocket.server.ServerEndpointConfig`

-

### getSubprotocols

public List<String> getSubprotocols()

Specified by:
`getSubprotocols` in interface `jakarta.websocket.server.ServerEndpointConfig`

-

### getExtensions

public List<jakarta.websocket.Extension> getExtensions()

Specified by:
`getExtensions` in interface `jakarta.websocket.server.ServerEndpointConfig`

-

### getConfigurator

public jakarta.websocket.server.ServerEndpointConfig.Configurator getConfigurator()

Specified by:
`getConfigurator` in interface `jakarta.websocket.server.ServerEndpointConfig`

-

### getEncoders

public List<Class<? extends jakarta.websocket.Encoder>> getEncoders()

Specified by:
`getEncoders` in interface `jakarta.websocket.EndpointConfig`

-

### getDecoders

public List<Class<? extends jakarta.websocket.Decoder>> getDecoders()

Specified by:
`getDecoders` in interface `jakarta.websocket.EndpointConfig`

-

### getUserProperties

public Map<String,Object> getUserProperties()

Specified by:
`getUserProperties` in interface `jakarta.websocket.EndpointConfig`

-

### getWrapped

public jakarta.websocket.server.ServerEndpointConfig getWrapped()
Get the wrapped `ServerEndpointConfig`.

Returns:
the wrapped `ServerEndpointConfig`.
