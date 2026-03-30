Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class MessageHandlerManager

java.lang.Object
org.glassfish.tyrus.core.MessageHandlerManager

---

public class MessageHandlerManager
extends Object
Manages registered `MessageHandler`s and checks whether the new ones may be registered.

Author:
Stepan Kopriva, Pavel Bucek
See Also:

- `MessageHandler`

- `OnMessage`

-

## Constructor Summary

Constructors

Constructor
Description
`MessageHandlerManager()`

Construct manager with no decoders.

-

## Method Summary

Modifier and Type
Method
Description
`void`
`addMessageHandler(jakarta.websocket.MessageHandler handler)`

Add `MessageHandler` to the manager.

`<T> void`
`addMessageHandler(Class<T> clazz,
 jakarta.websocket.MessageHandler.Partial<T> handler)`

Add `MessageHandler.Partial` to the manager.

`<T> void`
`addMessageHandler(Class<T> clazz,
 jakarta.websocket.MessageHandler.Whole<T> handler)`

Add `MessageHandler.Whole` to the manager.

`static MessageHandlerManager`
`fromDecoderClasses(List<Class<? extends jakarta.websocket.Decoder>> decoderClasses)`

Construct manager.

`Set<jakarta.websocket.MessageHandler>`
`getMessageHandlers()`

Get all successfully registered `MessageHandler`s.

`List<Map.Entry<Class<?>,jakarta.websocket.MessageHandler>>`
`getOrderedWholeMessageHandlers()`

`boolean`
`isInputStreamHandlerPresent()`

`boolean`
`isReaderHandlerPresent()`

`void`
`removeMessageHandler(jakarta.websocket.MessageHandler handler)`

Remove `MessageHandler` from the manager.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### MessageHandlerManager

public MessageHandlerManager()
Construct manager with no decoders.

-

## Method Details

-

### fromDecoderClasses

public static MessageHandlerManager fromDecoderClasses(List<Class<? extends jakarta.websocket.Decoder>> decoderClasses)
Construct manager.

Parameters:
`decoderClasses` - registered `Decoder`s.
Returns:
constructed message handler manager.

-

### addMessageHandler

public void addMessageHandler(jakarta.websocket.MessageHandler handler)
                       throws IllegalStateException
Add `MessageHandler` to the manager.

Parameters:
`handler` - `MessageHandler` to be added to the manager.
Throws:
`IllegalStateException`

-

### addMessageHandler

public <T> void addMessageHandler(Class<T> clazz,
 jakarta.websocket.MessageHandler.Whole<T> handler)
                           throws IllegalStateException
Add `MessageHandler.Whole` to the manager.

Type Parameters:
`T` - type of message to be handled.
Parameters:
`clazz` - type handled by `MessageHandler`.
`handler` - `MessageHandler` to be added.
Throws:
`IllegalStateException` - when the message handler cannot be added.

-

### addMessageHandler

public <T> void addMessageHandler(Class<T> clazz,
 jakarta.websocket.MessageHandler.Partial<T> handler)
                           throws IllegalStateException
Add `MessageHandler.Partial` to the manager.

Type Parameters:
`T` - type of message to be handled.
Parameters:
`clazz` - type handled by `MessageHandler`.
`handler` - `MessageHandler` to be added.
Throws:
`IllegalStateException` - when the message handler cannot be added.

-

### removeMessageHandler

public void removeMessageHandler(jakarta.websocket.MessageHandler handler)
Remove `MessageHandler` from the manager.

Parameters:
`handler` - handler which will be removed.

-

### getMessageHandlers

public Set<jakarta.websocket.MessageHandler> getMessageHandlers()
Get all successfully registered `MessageHandler`s.

Returns:
unmodifiable `Set` of registered `MessageHandler`s.

-

### getOrderedWholeMessageHandlers

public List<Map.Entry<Class<?>,jakarta.websocket.MessageHandler>> getOrderedWholeMessageHandlers()

-

### isReaderHandlerPresent

public boolean isReaderHandlerPresent()

-

### isInputStreamHandlerPresent

public boolean isInputStreamHandlerPresent()
