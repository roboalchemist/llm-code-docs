Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusServerEndpointConfigurator

java.lang.Object
jakarta.websocket.server.ServerEndpointConfig.Configurator
org.glassfish.tyrus.core.TyrusServerEndpointConfigurator

---

public class TyrusServerEndpointConfigurator
extends jakarta.websocket.server.ServerEndpointConfig.Configurator
Tyrus' implementation of `ServerEndpointConfig.Configurator`.

Author:
Pavel Bucek

-

## Constructor Summary

Constructors

Constructor
Description
`TyrusServerEndpointConfigurator()`

-

## Method Summary

Modifier and Type
Method
Description
`boolean`
`checkOrigin(String originHeaderValue)`

`<T> T`
`getEndpointInstance(Class<T> endpointClass)`

`List<jakarta.websocket.Extension>`
`getNegotiatedExtensions(List<jakarta.websocket.Extension> installed,
 List<jakarta.websocket.Extension> requested)`

`String`
`getNegotiatedSubprotocol(List<String> supported,
 List<String> requested)`

`void`
`modifyHandshake(jakarta.websocket.server.ServerEndpointConfig sec,
 jakarta.websocket.server.HandshakeRequest request,
 jakarta.websocket.HandshakeResponse response)`

### Methods inherited from class jakarta.websocket.server.ServerEndpointConfig.Configurator

`getContainerDefaultConfigurator`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### TyrusServerEndpointConfigurator

public TyrusServerEndpointConfigurator()

-

## Method Details

-

### getNegotiatedSubprotocol

public String getNegotiatedSubprotocol(List<String> supported,
 List<String> requested)

Overrides:
`getNegotiatedSubprotocol` in class `jakarta.websocket.server.ServerEndpointConfig.Configurator`

-

### getNegotiatedExtensions

public List<jakarta.websocket.Extension> getNegotiatedExtensions(List<jakarta.websocket.Extension> installed,
 List<jakarta.websocket.Extension> requested)

Overrides:
`getNegotiatedExtensions` in class `jakarta.websocket.server.ServerEndpointConfig.Configurator`

-

### checkOrigin

public boolean checkOrigin(String originHeaderValue)

Overrides:
`checkOrigin` in class `jakarta.websocket.server.ServerEndpointConfig.Configurator`

-

### modifyHandshake

public void modifyHandshake(jakarta.websocket.server.ServerEndpointConfig sec,
 jakarta.websocket.server.HandshakeRequest request,
 jakarta.websocket.HandshakeResponse response)

Overrides:
`modifyHandshake` in class `jakarta.websocket.server.ServerEndpointConfig.Configurator`

-

### getEndpointInstance

public <T> T getEndpointInstance(Class<T> endpointClass)
                          throws InstantiationException

Overrides:
`getEndpointInstance` in class `jakarta.websocket.server.ServerEndpointConfig.Configurator`
Throws:
`InstantiationException`
