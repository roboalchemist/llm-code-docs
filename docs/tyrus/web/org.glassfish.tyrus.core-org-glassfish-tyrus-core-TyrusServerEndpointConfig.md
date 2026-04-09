Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Interface TyrusServerEndpointConfig

All Superinterfaces:
`jakarta.websocket.EndpointConfig`, `jakarta.websocket.server.ServerEndpointConfig`

---

public interface TyrusServerEndpointConfig
extends jakarta.websocket.server.ServerEndpointConfig
Configuration `ServerEndpointConfig` enhanced
 to offer tyrus specific attributes like maxSessions.
 Declarative way to define maxSessions is also available using
 annotation `MaxSessions`.

Author:
Ondrej Kosatka
See Also:

- `MaxSessions`

-

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static final class`
`TyrusServerEndpointConfig.Builder`

The TyrusServerEndpointConfig.Builder is a class used for creating
 `TyrusServerEndpointConfig.Builder` objects for the purposes of
 deploying a server endpoint.

## Nested classes/interfaces inherited from interface jakarta.websocket.server.ServerEndpointConfig

`jakarta.websocket.server.ServerEndpointConfig.Configurator`

-

## Method Summary

Modifier and Type
Method
Description
`int`
`getMaxSessions()`

Returns configured maximal number of open sessions.

### Methods inherited from interface jakarta.websocket.EndpointConfig

`getDecoders, getEncoders, getUserProperties`

### Methods inherited from interface jakarta.websocket.server.ServerEndpointConfig

`getConfigurator, getEndpointClass, getExtensions, getPath, getSubprotocols`

-

## Method Details

-

### getMaxSessions

int getMaxSessions()
Returns configured maximal number of open sessions.

Returns:
tne maximal number of open sessions.
