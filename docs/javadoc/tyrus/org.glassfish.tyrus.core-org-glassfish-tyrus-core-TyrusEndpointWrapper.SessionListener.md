Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusEndpointWrapper.SessionListener

java.lang.Object
org.glassfish.tyrus.core.TyrusEndpointWrapper.SessionListener

Enclosing class:
`TyrusEndpointWrapper`

---

public abstract static class TyrusEndpointWrapper.SessionListener
extends Object
Session listener.

 TODO: rename/consolidate with `EndpointEventListener`?

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static enum`
`TyrusEndpointWrapper.SessionListener.OnOpenResult`

Result of `onOpen(TyrusSession)`.

-

## Constructor Summary

Constructors

Constructor
Description
`SessionListener()`

-

## Method Summary

Modifier and Type
Method
Description
`void`
`onClose(TyrusSession session,
 jakarta.websocket.CloseReason closeReason)`

Invoked after `OnClose` annotated method
 or `Endpoint.onClose(jakarta.websocket.Session, jakarta.websocket.CloseReason)` execution.

`TyrusEndpointWrapper.SessionListener.OnOpenResult`
`onOpen(TyrusSession session)`

Invoked before `OnOpen` annotated method
 or `Endpoint.onOpen(jakarta.websocket.Session, jakarta.websocket.EndpointConfig)` is invoked.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### SessionListener

public SessionListener()

-

## Method Details

-

### onOpen

public TyrusEndpointWrapper.SessionListener.OnOpenResult onOpen(TyrusSession session)
Invoked before `OnOpen` annotated method
 or `Endpoint.onOpen(jakarta.websocket.Session, jakarta.websocket.EndpointConfig)` is invoked.

 Default implementation always returns `TyrusEndpointWrapper.SessionListener.OnOpenResult.SESSION_ALLOWED`.

Parameters:
`session` - session to be opened.
Returns:
`TyrusEndpointWrapper.SessionListener.OnOpenResult.SESSION_ALLOWED`
 if session can be opened or reason why not.

-

### onClose

public void onClose(TyrusSession session,
 jakarta.websocket.CloseReason closeReason)
Invoked after `OnClose` annotated method
 or `Endpoint.onClose(jakarta.websocket.Session, jakarta.websocket.CloseReason)` execution.

Parameters:
`session` - closed session.
`closeReason` - close reason.
