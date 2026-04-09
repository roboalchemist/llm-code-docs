Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ProtocolHandler

java.lang.Object
org.glassfish.tyrus.core.ProtocolHandler

---

public final class ProtocolHandler
extends Object
Tyrus protocol handler.

 Responsible for framing and unframing raw websocket frames. Tyrus creates exactly one instance per Session.

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final int`
`MASK_SIZE`

RFC 6455

-

## Method Summary

Modifier and Type
Method
Description
`Future<Frame>`
`close(int code,
 String reason)`

`Handshake`
`handshake(TyrusEndpointWrapper endpointWrapper,
 org.glassfish.tyrus.spi.UpgradeRequest request,
 org.glassfish.tyrus.spi.UpgradeResponse response,
 ExtendedExtension.ExtensionContext extensionContext)`

Server side handshake processing.

`boolean`
`hasExtensions()`

Returns true when current connection has some negotiated extension.

`void`
`process(Frame frame,
 TyrusWebSocket socket)`

TODO.

`Future<Frame>`
`send(byte[] data)`

Deprecated.

`void`
`send(byte[] data,
 jakarta.websocket.SendHandler handler)`

Deprecated.

`void`
`send(byte[] data,
 jakarta.websocket.SendHandler handler,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)`

`Future<Frame>`
`send(byte[] data,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)`

`Future<Frame>`
`send(String data)`

Deprecated.

`void`
`send(String data,
 jakarta.websocket.SendHandler handler)`

Deprecated.

`void`
`send(String data,
 jakarta.websocket.SendHandler handler,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)`

`Future<Frame>`
`send(String data,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)`

`Future<Frame>`
`sendRawFrame(ByteBuffer data)`

Raw frame is always whole (not partial).

`void`
`setExtensionContext(ExtendedExtension.ExtensionContext extensionContext)`

Client side.

`void`
`setExtensions(List<jakarta.websocket.Extension> extensions)`

Client side.

`void`
`setMessageEventListener(MessageEventListener messageEventListener)`

Set message event listener.

`void`
`setWebSocket(TyrusWebSocket webSocket)`

Client side.

`void`
`setWriter(org.glassfish.tyrus.spi.Writer writer)`

Set `Writer` instance.

`Future<Frame>`
`stream(boolean last,
 byte[] bytes,
 int off,
 int len)`

Deprecated.

`Future<Frame>`
`stream(boolean last,
 byte[] bytes,
 int off,
 int len,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)`

`Future<Frame>`
`stream(boolean last,
 String fragment)`

Deprecated.

`Future<Frame>`
`stream(boolean last,
 String fragment,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)`

`Frame`
`unframe(ByteBuffer buffer)`

TODO!

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Field Details

-

### MASK_SIZE

public static final int MASK_SIZE
RFC 6455

See Also:

    - Constant Field Values

-

## Method Details

-

### setWriter

public void setWriter(org.glassfish.tyrus.spi.Writer writer)
Set `Writer` instance.

 The set instance is used for "sending" all outgoing WebSocket frames.

Parameters:
`writer` - `Writer` to be set.

-

### hasExtensions

public boolean hasExtensions()
Returns true when current connection has some negotiated extension.

Returns:
`true` if there is at least one negotiated extension associated to this connection, `false`
 otherwise.

-

### handshake

public Handshake handshake(TyrusEndpointWrapper endpointWrapper,
 org.glassfish.tyrus.spi.UpgradeRequest request,
 org.glassfish.tyrus.spi.UpgradeResponse response,
 ExtendedExtension.ExtensionContext extensionContext)
                    throws HandshakeException
Server side handshake processing.

Parameters:
`endpointWrapper` - endpoint related to the handshake (path is already matched).
`request` - handshake request.
`response` - handshake response.
`extensionContext` - extension context.
Returns:
server handshake object.
Throws:
`HandshakeException` - when there is problem with received `UpgradeRequest`.

-

### setExtensions

public void setExtensions(List<jakarta.websocket.Extension> extensions)
Client side. Set extensions negotiated for this WebSocket session/connection.

Parameters:
`extensions` - list of negotiated extensions. Can be `null`.

-

### setWebSocket

public void setWebSocket(TyrusWebSocket webSocket)
Client side. Set WebSocket.

Parameters:
`webSocket` - client WebSocket connection.

-

### setExtensionContext

public void setExtensionContext(ExtendedExtension.ExtensionContext extensionContext)
Client side. Set extension context.

Parameters:
`extensionContext` - extension context.

-

### setMessageEventListener

public void setMessageEventListener(MessageEventListener messageEventListener)
Set message event listener.

Parameters:
`messageEventListener` - message event listener.

-

### send

@Deprecated
public Future<Frame> send(byte[] data)
Deprecated.

-

### send

public Future<Frame> send(byte[] data,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)

-

### send

@Deprecated
public void send(byte[] data,
 jakarta.websocket.SendHandler handler)
Deprecated.

-

### send

public void send(byte[] data,
 jakarta.websocket.SendHandler handler,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)

-

### send

@Deprecated
public Future<Frame> send(String data)
Deprecated.

-

### send

public Future<Frame> send(String data,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)

-

### send

@Deprecated
public void send(String data,
 jakarta.websocket.SendHandler handler)
Deprecated.

-

### send

public void send(String data,
 jakarta.websocket.SendHandler handler,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)

-

### sendRawFrame

public Future<Frame> sendRawFrame(ByteBuffer data)
Raw frame is always whole (not partial).

Parameters:
`data` - serialized frame.
Returns:
send future.

-

### stream

@Deprecated
public Future<Frame> stream(boolean last,
 byte[] bytes,
 int off,
 int len)
Deprecated.

-

### stream

public Future<Frame> stream(boolean last,
 byte[] bytes,
 int off,
 int len,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)

-

### stream

@Deprecated
public Future<Frame> stream(boolean last,
 String fragment)
Deprecated.

-

### stream

public Future<Frame> stream(boolean last,
 String fragment,
 org.glassfish.tyrus.spi.WriterInfo writerInfo)

-

### close

public Future<Frame> close(int code,
 String reason)

-

### unframe

public Frame unframe(ByteBuffer buffer)
TODO!

Parameters:
`buffer` - TODO.
Returns:
TODO.

-

### process

public void process(Frame frame,
 TyrusWebSocket socket)
TODO.

 called after Extension execution.

 validates frame + processes its content

Parameters:
`frame` - TODO.
`socket` - TODO.
