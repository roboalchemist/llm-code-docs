Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class Handshake

java.lang.Object
org.glassfish.tyrus.core.Handshake

---

public final class Handshake
extends Object
Class responsible for performing and validating handshake.

Author:
Justin Lee, Pavel Bucek

-

## Method Summary

Modifier and Type
Method
Description
`static Handshake`
`createClientHandshake(RequestContext webSocketRequest)`

Client-side handshake.

`RequestContext`
`getRequest()`

Client side only - get the `UpgradeRequest`.

`org.glassfish.tyrus.spi.UpgradeRequest`
`prepareRequest()`

Client side only - compose the `UpgradeRequest` and store it for further use.

`void`
`setExtensions(List<jakarta.websocket.Extension> extensions)`

Client side only - set the list of supported extensions.

`void`
`setSubProtocols(List<String> subProtocols)`

Client side only - set the list of supported subprotocols.

`static void`
`updateHostAndOrigin(org.glassfish.tyrus.spi.UpgradeRequest upgradeRequest)`

Client side only - Generate host and origin header and put them to the upgrade request headers.

`void`
`validateServerResponse(org.glassfish.tyrus.spi.UpgradeResponse response)`

Client side only - validate server response.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Method Details

-

### createClientHandshake

public static Handshake createClientHandshake(RequestContext webSocketRequest)
Client-side handshake.

Parameters:
`webSocketRequest` - request representation to be modified for use as WebSocket handshake request.
Returns:
handshake instance.

-

### getRequest

public RequestContext getRequest()
Client side only - get the `UpgradeRequest`.

Returns:
`UpgradeRequest` created on this HandShake.

-

### setSubProtocols

public void setSubProtocols(List<String> subProtocols)
Client side only - set the list of supported subprotocols.

Parameters:
`subProtocols` - list of supported subprotocol.

-

### setExtensions

public void setExtensions(List<jakarta.websocket.Extension> extensions)
Client side only - set the list of supported extensions.

Parameters:
`extensions` - list of supported extensions.

-

### prepareRequest

public org.glassfish.tyrus.spi.UpgradeRequest prepareRequest()
Client side only - compose the `UpgradeRequest` and store it for further use.

Returns:
composed `UpgradeRequest`.

-

### validateServerResponse

public void validateServerResponse(org.glassfish.tyrus.spi.UpgradeResponse response)
                            throws HandshakeException
Client side only - validate server response.

Parameters:
`response` - response to be validated.
Throws:
`HandshakeException` - when HTTP Status of received response is not 101 - Switching protocols.

-

### updateHostAndOrigin

public static void updateHostAndOrigin(org.glassfish.tyrus.spi.UpgradeRequest upgradeRequest)
Client side only - Generate host and origin header and put them to the upgrade request headers.

Parameters:
`upgradeRequest` - upgrade request to be updated.
