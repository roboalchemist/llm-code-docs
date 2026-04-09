# Package org.java_websocket.exceptions



---

package org.java_websocket.exceptions

This package encapsulates all implementations in relation with the exceptions thrown in this
 lib.





- 

Related Packages

Package
Description
org.java_websocket
 




- 

Exception Classes

Class
Description
IncompleteException

Exception which indicates that the frame is not yet complete

IncompleteHandshakeException

exception which indicates that a incomplete handshake was received

InvalidDataException

exception which indicates that a invalid data was received

InvalidEncodingException

The Character Encoding is not supported.

InvalidFrameException

exception which indicates that a invalid frame was received (CloseFrame.PROTOCOL_ERROR)

InvalidHandshakeException

exception which indicates that a invalid handshake was received (CloseFrame.PROTOCOL_ERROR)

LimitExceededException

exception which indicates that the message limited was exceeded (CloseFrame.TOOBIG)

NotSendableException

exception which indicates the frame payload is not sendable

WebsocketNotConnectedException

exception which indicates the websocket is not yet connected (ReadyState.OPEN)

WrappedIOException

Exception to wrap an IOException and include information about the websocket which had the
 exception