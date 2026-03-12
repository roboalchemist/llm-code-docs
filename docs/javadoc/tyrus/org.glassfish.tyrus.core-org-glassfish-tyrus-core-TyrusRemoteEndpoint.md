Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusRemoteEndpoint

java.lang.Object
org.glassfish.tyrus.core.TyrusRemoteEndpoint

All Implemented Interfaces:
`jakarta.websocket.RemoteEndpoint`

---

public abstract class TyrusRemoteEndpoint
extends Object
implements jakarta.websocket.RemoteEndpoint
Wraps the `RemoteEndpoint` and represents the other side of the websocket connection.

Author:
Danny Coward, Martin Matula, Stepan Kopriva, Pavel Bucek

-

## Method Summary

Modifier and Type
Method
Description
`void`
`close(jakarta.websocket.CloseReason cr)`

`void`
`flushBatch()`

`boolean`
`getBatchingAllowed()`

`void`
`sendPing(ByteBuffer applicationData)`

`void`
`sendPong(ByteBuffer applicationData)`

`void`
`setBatchingAllowed(boolean allowed)`

`String`
`toString()`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Method Details

-

### sendPing

public void sendPing(ByteBuffer applicationData)
              throws IOException

Specified by:
`sendPing` in interface `jakarta.websocket.RemoteEndpoint`
Throws:
`IOException`

-

### sendPong

public void sendPong(ByteBuffer applicationData)
              throws IOException

Specified by:
`sendPong` in interface `jakarta.websocket.RemoteEndpoint`
Throws:
`IOException`

-

### toString

public String toString()

Overrides:
`toString` in class `Object`

-

### setBatchingAllowed

public void setBatchingAllowed(boolean allowed)

Specified by:
`setBatchingAllowed` in interface `jakarta.websocket.RemoteEndpoint`

-

### getBatchingAllowed

public boolean getBatchingAllowed()

Specified by:
`getBatchingAllowed` in interface `jakarta.websocket.RemoteEndpoint`

-

### flushBatch

public void flushBatch()

Specified by:
`flushBatch` in interface `jakarta.websocket.RemoteEndpoint`

-

### close

public void close(jakarta.websocket.CloseReason cr)
