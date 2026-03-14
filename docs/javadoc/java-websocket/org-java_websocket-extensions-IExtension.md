Package org.java_websocket.extensions

# Interface IExtension




All Known Implementing Classes:
`CompressionExtension`, `DefaultExtension`, `PerMessageDeflateExtension`


---

public interface IExtension
Interface which specifies all required methods to develop a websocket extension.

Since:
1.3.5







- 


## Method Summary





Modifier and Type
Method
Description
`boolean`
`acceptProvidedExtensionAsClient(String inputExtensionHeader)`

Check if the received Sec-WebSocket-Extensions header field contains a offer for the specific
 extension if the endpoint is in the role of a client

`boolean`
`acceptProvidedExtensionAsServer(String inputExtensionHeader)`

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

`String`
`getProvidedExtensionAsClient()`

Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a client.

`String`
`getProvidedExtensionAsServer()`

Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a server.

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














- 


## Method Details




  - 


### decodeFrame

void decodeFrame(Framedata inputFrame)
          throws InvalidDataException
Decode a frame with a extension specific algorithm. The algorithm is subject to be implemented
 by the specific extension. The resulting frame will be used in the application

Parameters:
`inputFrame` - the frame, which has do be decoded to be used in the application
Throws:
`InvalidDataException` - Throw InvalidDataException if the received frame is not correctly
                              implemented by the other endpoint or there are other protocol
                              errors/decoding errors
Since:
1.3.5




  - 


### encodeFrame

void encodeFrame(Framedata inputFrame)
Encode a frame with a extension specific algorithm. The algorithm is subject to be implemented
 by the specific extension. The resulting frame will be send to the other endpoint.

Parameters:
`inputFrame` - the frame, which has do be encoded to be used on the other endpoint
Since:
1.3.5




  - 


### acceptProvidedExtensionAsServer

boolean acceptProvidedExtensionAsServer(String inputExtensionHeader)
Check if the received Sec-WebSocket-Extensions header field contains a offer for the specific
 extension if the endpoint is in the role of a server

Parameters:
`inputExtensionHeader` - the received Sec-WebSocket-Extensions header field offered by the
                             other endpoint
Returns:
true, if the offer does fit to this specific extension
Since:
1.3.5




  - 


### acceptProvidedExtensionAsClient

boolean acceptProvidedExtensionAsClient(String inputExtensionHeader)
Check if the received Sec-WebSocket-Extensions header field contains a offer for the specific
 extension if the endpoint is in the role of a client

Parameters:
`inputExtensionHeader` - the received Sec-WebSocket-Extensions header field offered by the
                             other endpoint
Returns:
true, if the offer does fit to this specific extension
Since:
1.3.5




  - 


### isFrameValid

void isFrameValid(Framedata inputFrame)
           throws InvalidDataException
Check if the received frame is correctly implemented by the other endpoint and there are no
 specification errors (like wrongly set RSV)

Parameters:
`inputFrame` - the received frame
Throws:
`InvalidDataException` - Throw InvalidDataException if the received frame is not correctly
                              implementing the specification for the specific extension
Since:
1.3.5




  - 


### getProvidedExtensionAsClient

String getProvidedExtensionAsClient()
Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a client. If the extension returns an empty string (""), the offer will not be
 included in the handshake.

Returns:
the specific Sec-WebSocket-Extensions header for this extension
Since:
1.3.5




  - 


### getProvidedExtensionAsServer

String getProvidedExtensionAsServer()
Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a server. If the extension returns an empty string (""), the offer will not be
 included in the handshake.

Returns:
the specific Sec-WebSocket-Extensions header for this extension
Since:
1.3.5




  - 


### copyInstance

IExtension copyInstance()
Extensions must only be by one websocket at all. To prevent extensions to be used more than
 once the Websocket implementation should call this method in order to create a new usable
 version of a given extension instance.
 The copy can be safely used in conjunction with a
 new websocket connection.

Returns:
a copy of the extension
Since:
1.3.5




  - 


### reset

void reset()
Cleaning up internal stats when the draft gets reset.

Since:
1.3.5




  - 


### toString

String toString()
Return a string which should contain the class name as well as additional information about the
 current configurations for this extension (DEBUG purposes)

Overrides:
`toString` in class `Object`
Returns:
a string containing the class name as well as additional information
Since:
1.3.5