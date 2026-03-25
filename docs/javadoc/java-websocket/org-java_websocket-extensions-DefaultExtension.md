Package org.java_websocket.extensions

# Class DefaultExtension


java.lang.Object
org.java_websocket.extensions.DefaultExtension



All Implemented Interfaces:
`IExtension`


Direct Known Subclasses:
`CompressionExtension`


---

public class DefaultExtension
extends Object
implements IExtension
Class which represents the normal websocket implementation specified by rfc6455.
 


 This is a fallback and will always be available for a Draft_6455

Since:
1.3.5







- 


## Constructor Summary

Constructors

Constructor
Description
`DefaultExtension()`
 





- 


## Method Summary





Modifier and Type
Method
Description
`boolean`
`acceptProvidedExtensionAsClient(String inputExtension)`

Check if the received Sec-WebSocket-Extensions header field contains a offer for the specific
 extension if the endpoint is in the role of a client

`boolean`
`acceptProvidedExtensionAsServer(String inputExtension)`

Check if the received Sec-WebSocket-Extensions header field contains a offer for the specific
 extension if the endpoint is in the role of a server

`IExtension`
`copyInstance()`

Extensions must only be by one websocket at all.

`void`
`decodeFrame(Framedata inputFrame)`

Decode a frame with a extension specific algorithm.

`void`
`encodeFrame(Framedata inputFrame)`

Encode a frame with a extension specific algorithm.

`boolean`
`equals(Object o)`
 
`String`
`getProvidedExtensionAsClient()`

Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a client.

`String`
`getProvidedExtensionAsServer()`

Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a server.

`int`
`hashCode()`
 
`void`
`isFrameValid(Framedata inputFrame)`

Check if the received frame is correctly implemented by the other endpoint and there are no
 specification errors (like wrongly set RSV)

`void`
`reset()`

Cleaning up internal stats when the draft gets reset.

`String`
`toString()`

Return a string which should contain the class name as well as additional information about the
 current configurations for this extension (DEBUG purposes)






### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### DefaultExtension

public DefaultExtension()








- 


## Method Details




  - 


### decodeFrame

public void decodeFrame(Framedata inputFrame)
                 throws InvalidDataException
Description copied from interface: `IExtension`
Decode a frame with a extension specific algorithm. The algorithm is subject to be implemented
 by the specific extension. The resulting frame will be used in the application

Specified by:
`decodeFrame` in interface `IExtension`
Parameters:
`inputFrame` - the frame, which has do be decoded to be used in the application
Throws:
`InvalidDataException` - Throw InvalidDataException if the received frame is not correctly
                              implemented by the other endpoint or there are other protocol
                              errors/decoding errors




  - 


### encodeFrame

public void encodeFrame(Framedata inputFrame)
Description copied from interface: `IExtension`
Encode a frame with a extension specific algorithm. The algorithm is subject to be implemented
 by the specific extension. The resulting frame will be send to the other endpoint.

Specified by:
`encodeFrame` in interface `IExtension`
Parameters:
`inputFrame` - the frame, which has do be encoded to be used on the other endpoint




  - 


### acceptProvidedExtensionAsServer

public boolean acceptProvidedExtensionAsServer(String inputExtension)
Description copied from interface: `IExtension`
Check if the received Sec-WebSocket-Extensions header field contains a offer for the specific
 extension if the endpoint is in the role of a server

Specified by:
`acceptProvidedExtensionAsServer` in interface `IExtension`
Parameters:
`inputExtension` - the received Sec-WebSocket-Extensions header field offered by the
                             other endpoint
Returns:
true, if the offer does fit to this specific extension




  - 


### acceptProvidedExtensionAsClient

public boolean acceptProvidedExtensionAsClient(String inputExtension)
Description copied from interface: `IExtension`
Check if the received Sec-WebSocket-Extensions header field contains a offer for the specific
 extension if the endpoint is in the role of a client

Specified by:
`acceptProvidedExtensionAsClient` in interface `IExtension`
Parameters:
`inputExtension` - the received Sec-WebSocket-Extensions header field offered by the
                             other endpoint
Returns:
true, if the offer does fit to this specific extension




  - 


### isFrameValid

public void isFrameValid(Framedata inputFrame)
                  throws InvalidDataException
Description copied from interface: `IExtension`
Check if the received frame is correctly implemented by the other endpoint and there are no
 specification errors (like wrongly set RSV)

Specified by:
`isFrameValid` in interface `IExtension`
Parameters:
`inputFrame` - the received frame
Throws:
`InvalidDataException` - Throw InvalidDataException if the received frame is not correctly
                              implementing the specification for the specific extension




  - 


### getProvidedExtensionAsClient

public String getProvidedExtensionAsClient()
Description copied from interface: `IExtension`
Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a client. If the extension returns an empty string (""), the offer will not be
 included in the handshake.

Specified by:
`getProvidedExtensionAsClient` in interface `IExtension`
Returns:
the specific Sec-WebSocket-Extensions header for this extension




  - 


### getProvidedExtensionAsServer

public String getProvidedExtensionAsServer()
Description copied from interface: `IExtension`
Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a server. If the extension returns an empty string (""), the offer will not be
 included in the handshake.

Specified by:
`getProvidedExtensionAsServer` in interface `IExtension`
Returns:
the specific Sec-WebSocket-Extensions header for this extension




  - 


### copyInstance

public IExtension copyInstance()
Description copied from interface: `IExtension`
Extensions must only be by one websocket at all. To prevent extensions to be used more than
 once the Websocket implementation should call this method in order to create a new usable
 version of a given extension instance.
 The copy can be safely used in conjunction with a
 new websocket connection.

Specified by:
`copyInstance` in interface `IExtension`
Returns:
a copy of the extension




  - 


### reset

public void reset()
Description copied from interface: `IExtension`
Cleaning up internal stats when the draft gets reset.

Specified by:
`reset` in interface `IExtension`




  - 


### toString

public String toString()
Description copied from interface: `IExtension`
Return a string which should contain the class name as well as additional information about the
 current configurations for this extension (DEBUG purposes)

Specified by:
`toString` in interface `IExtension`
Overrides:
`toString` in class `Object`
Returns:
a string containing the class name as well as additional information




  - 


### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`




  - 


### equals

public boolean equals(Object o)

Overrides:
`equals` in class `Object`