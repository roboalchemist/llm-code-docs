Package org.java_websocket.extensions.permessage_deflate

# Class PerMessageDeflateExtension


java.lang.Object
org.java_websocket.extensions.DefaultExtension
org.java_websocket.extensions.CompressionExtension
org.java_websocket.extensions.permessage_deflate.PerMessageDeflateExtension





All Implemented Interfaces:
`IExtension`


---

public class PerMessageDeflateExtension
extends CompressionExtension
PerMessage Deflate Extension (7. The
 "permessage-deflate" Extension in
 RFC 7692).

See Also:




- 7. The "permessage-deflate"
 Extension in RFC 7692










- 


## Constructor Summary

Constructors

Constructor
Description
`PerMessageDeflateExtension()`

Constructor for the PerMessage Deflate Extension (7. Thepermessage-deflate" Extension)

 Uses `Deflater.DEFAULT_COMPRESSION` as the compression level for the `Deflater(int)`

`PerMessageDeflateExtension(int compressionLevel)`

Constructor for the PerMessage Deflate Extension (7. Thepermessage-deflate" Extension)






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

`int`
`getCompressionLevel()`

Get the compression level used for the compressor.

`String`
`getProvidedExtensionAsClient()`

Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a client.

`String`
`getProvidedExtensionAsServer()`

Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a server.

`int`
`getThreshold()`

Get the size threshold for doing the compression

`boolean`
`isClientNoContextTakeover()`

Access the "client_no_context_takeover" extension parameter

`void`
`isFrameValid(Framedata inputFrame)`

This extension requires the RSV1 bit to be set only for the first frame.

`boolean`
`isServerNoContextTakeover()`

Access the "server_no_context_takeover" extension parameter

`void`
`setClientNoContextTakeover(boolean clientNoContextTakeover)`

Setter for the "client_no_context_takeover" extension parameter

`void`
`setServerNoContextTakeover(boolean serverNoContextTakeover)`

Setter for the "server_no_context_takeover" extension parameter

`void`
`setThreshold(int threshold)`

Set the size when payloads smaller than this will not be compressed.

`String`
`toString()`

Return a string which should contain the class name as well as additional information about the
 current configurations for this extension (DEBUG purposes)






### Methods inherited from class org.java_websocket.extensions.DefaultExtension

`equals, hashCode, reset`


### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### PerMessageDeflateExtension

public PerMessageDeflateExtension()
Constructor for the PerMessage Deflate Extension (7. Thepermessage-deflate" Extension)

 Uses `Deflater.DEFAULT_COMPRESSION` as the compression level for the `Deflater(int)`



  - 


### PerMessageDeflateExtension

public PerMessageDeflateExtension(int compressionLevel)
Constructor for the PerMessage Deflate Extension (7. Thepermessage-deflate" Extension)

Parameters:
`compressionLevel` - The compression level passed to the `Deflater(int)`









- 


## Method Details




  - 


### getCompressionLevel

public int getCompressionLevel()
Get the compression level used for the compressor.

Returns:
the compression level




  - 


### getThreshold

public int getThreshold()
Get the size threshold for doing the compression

Returns:
Size (in bytes) below which messages will not be compressed
Since:
1.5.3




  - 


### setThreshold

public void setThreshold(int threshold)
Set the size when payloads smaller than this will not be compressed.

Parameters:
`threshold` - the size in bytes
Since:
1.5.3




  - 


### isServerNoContextTakeover

public boolean isServerNoContextTakeover()
Access the "server_no_context_takeover" extension parameter

Returns:
serverNoContextTakeover is the server no context parameter active
See Also:




    - The "server_no_context_takeover" Extension Parameter







  - 


### setServerNoContextTakeover

public void setServerNoContextTakeover(boolean serverNoContextTakeover)
Setter for the "server_no_context_takeover" extension parameter

Parameters:
`serverNoContextTakeover` - set the server no context parameter
See Also:




    - The "server_no_context_takeover" Extension Parameter







  - 


### isClientNoContextTakeover

public boolean isClientNoContextTakeover()
Access the "client_no_context_takeover" extension parameter

Returns:
clientNoContextTakeover is the client no context parameter active
See Also:




    - The "client_no_context_takeover" Extension Parameter







  - 


### setClientNoContextTakeover

public void setClientNoContextTakeover(boolean clientNoContextTakeover)
Setter for the "client_no_context_takeover" extension parameter

Parameters:
`clientNoContextTakeover` - set the client no context parameter
See Also:




    - The "client_no_context_takeover" Extension Parameter







  - 


### decodeFrame

public void decodeFrame(Framedata inputFrame)
                 throws InvalidDataException
Description copied from interface: `IExtension`
Decode a frame with a extension specific algorithm. The algorithm is subject to be implemented
 by the specific extension. The resulting frame will be used in the application

Specified by:
`decodeFrame` in interface `IExtension`
Overrides:
`decodeFrame` in class `DefaultExtension`
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
Overrides:
`encodeFrame` in class `DefaultExtension`
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
Overrides:
`acceptProvidedExtensionAsServer` in class `DefaultExtension`
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
Overrides:
`acceptProvidedExtensionAsClient` in class `DefaultExtension`
Parameters:
`inputExtension` - the received Sec-WebSocket-Extensions header field offered by the
                             other endpoint
Returns:
true, if the offer does fit to this specific extension




  - 


### getProvidedExtensionAsClient

public String getProvidedExtensionAsClient()
Description copied from interface: `IExtension`
Return the specific Sec-WebSocket-Extensions header offer for this extension if the endpoint is
 in the role of a client. If the extension returns an empty string (""), the offer will not be
 included in the handshake.

Specified by:
`getProvidedExtensionAsClient` in interface `IExtension`
Overrides:
`getProvidedExtensionAsClient` in class `DefaultExtension`
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
Overrides:
`getProvidedExtensionAsServer` in class `DefaultExtension`
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
Overrides:
`copyInstance` in class `DefaultExtension`
Returns:
a copy of the extension




  - 


### isFrameValid

public void isFrameValid(Framedata inputFrame)
                  throws InvalidDataException
This extension requires the RSV1 bit to be set only for the first frame. If the frame is type
 is CONTINUOUS, RSV1 bit must be unset.

Specified by:
`isFrameValid` in interface `IExtension`
Overrides:
`isFrameValid` in class `CompressionExtension`
Parameters:
`inputFrame` - the received frame
Throws:
`InvalidDataException` - Throw InvalidDataException if the received frame is not correctly
                              implementing the specification for the specific extension




  - 


### toString

public String toString()
Description copied from interface: `IExtension`
Return a string which should contain the class name as well as additional information about the
 current configurations for this extension (DEBUG purposes)

Specified by:
`toString` in interface `IExtension`
Overrides:
`toString` in class `DefaultExtension`
Returns:
a string containing the class name as well as additional information