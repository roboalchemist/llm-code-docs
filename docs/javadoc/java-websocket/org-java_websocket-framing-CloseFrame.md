Package org.java_websocket.framing

# Class CloseFrame


java.lang.Object
org.java_websocket.framing.FramedataImpl1
org.java_websocket.framing.ControlFrame
org.java_websocket.framing.CloseFrame





All Implemented Interfaces:
`Framedata`


---

public class CloseFrame
extends ControlFrame
Class to represent a close frame






- 


## Field Summary

Fields

Modifier and Type
Field
Description
`static final int`
`ABNORMAL_CLOSE`

1006 is a reserved value and MUST NOT be set as a status code in a Close control frame by an
 endpoint.

`static final int`
`BAD_GATEWAY`

1014 indicates that the server was acting as a gateway or proxy and received an invalid
 response from the upstream server.

`static final int`
`BUGGYCLOSE`

The connection had a buggy close (this should not happen)

`static final int`
`EXTENSION`

1010 indicates that an endpoint (client) is terminating the connection because it has expected
 the server to negotiate one or more extension, but the server didn't return them in the
 response message of the WebSocket handshake.

`static final int`
`FLASHPOLICY`

The connection was flushed and closed

`static final int`
`GOING_AWAY`

1001 indicates that an endpoint is "going away", such as a server going down, or a browser
 having navigated away from a page.

`static final int`
`NEVER_CONNECTED`

The connection had never been established

`static final int`
`NO_UTF8`

1007 indicates that an endpoint is terminating the connection because it has received data
 within a message that was not consistent with the type of the message (e.g., non-UTF-8
 [RFC3629] data within a text message).

`static final int`
`NOCODE`

1005 is a reserved value and MUST NOT be set as a status code in a Close control frame by an
 endpoint.

`static final int`
`NORMAL`

indicates a normal closure, meaning whatever purpose the connection was established for has
 been fulfilled.

`static final int`
`POLICY_VALIDATION`

1008 indicates that an endpoint is terminating the connection because it has received a message
 that violates its policy.

`static final int`
`PROTOCOL_ERROR`

1002 indicates that an endpoint is terminating the connection due to a protocol error.

`static final int`
`REFUSE`

1003 indicates that an endpoint is terminating the connection because it has received a type of
 data it cannot accept (e.g. an endpoint that understands only text data MAY send this if it
 receives a binary message).

`static final int`
`SERVICE_RESTART`

1012 indicates that the service is restarted.

`static final int`
`TLS_ERROR`

1015 is a reserved value and MUST NOT be set as a status code in a Close control frame by an
 endpoint.

`static final int`
`TOOBIG`

1009 indicates that an endpoint is terminating the connection because it has received a message
 which is too big for it to process.

`static final int`
`TRY_AGAIN_LATER`

1013 indicates that the service is experiencing overload.

`static final int`
`UNEXPECTED_CONDITION`

1011 indicates that a server is terminating the connection because it encountered an unexpected
 condition that prevented it from fulfilling the request.






- 


## Constructor Summary

Constructors

Constructor
Description
`CloseFrame()`

Constructor for a close frame






- 


## Method Summary





Modifier and Type
Method
Description
`boolean`
`equals(Object o)`
 
`int`
`getCloseCode()`

Get the used close code

`String`
`getMessage()`

Get the message that closeframe is containing

`ByteBuffer`
`getPayloadData()`

The "Payload data" which was sent in this frame

`int`
`hashCode()`
 
`void`
`isValid()`

Check if the frame is valid due to specification

`void`
`setCode(int code)`

Set the close code for this close frame

`void`
`setPayload(ByteBuffer payload)`

Set the payload of this frame to the provided payload

`void`
`setReason(String reason)`

Set the close reason for this close frame

`String`
`toString()`
 





### Methods inherited from class org.java_websocket.framing.FramedataImpl1

`append, get, getOpcode, getTransfereMasked, isFin, isRSV1, isRSV2, isRSV3, setFin, setRSV1, setRSV2, setRSV3, setTransferemasked`


### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`










- 


## Field Details




  - 


### NORMAL

public static final int NORMAL
indicates a normal closure, meaning whatever purpose the connection was established for has
 been fulfilled.

See Also:




    - Constant Field Values







  - 


### GOING_AWAY

public static final int GOING_AWAY
1001 indicates that an endpoint is "going away", such as a server going down, or a browser
 having navigated away from a page.

See Also:




    - Constant Field Values







  - 


### PROTOCOL_ERROR

public static final int PROTOCOL_ERROR
1002 indicates that an endpoint is terminating the connection due to a protocol error.

See Also:




    - Constant Field Values







  - 


### REFUSE

public static final int REFUSE
1003 indicates that an endpoint is terminating the connection because it has received a type of
 data it cannot accept (e.g. an endpoint that understands only text data MAY send this if it
 receives a binary message).

See Also:




    - Constant Field Values







  - 


### NOCODE

public static final int NOCODE
1005 is a reserved value and MUST NOT be set as a status code in a Close control frame by an
 endpoint. It is designated for use in applications expecting a status code to indicate that no
 status code was actually present.

See Also:




    - Constant Field Values







  - 


### ABNORMAL_CLOSE

public static final int ABNORMAL_CLOSE
1006 is a reserved value and MUST NOT be set as a status code in a Close control frame by an
 endpoint. It is designated for use in applications expecting a status code to indicate that the
 connection was closed abnormally, e.g. without sending or receiving a Close control frame.

See Also:




    - Constant Field Values







  - 


### NO_UTF8

public static final int NO_UTF8
1007 indicates that an endpoint is terminating the connection because it has received data
 within a message that was not consistent with the type of the message (e.g., non-UTF-8
 [RFC3629] data within a text message).

See Also:




    - Constant Field Values







  - 


### POLICY_VALIDATION

public static final int POLICY_VALIDATION
1008 indicates that an endpoint is terminating the connection because it has received a message
 that violates its policy. This is a generic status code that can be returned when there is no
 other more suitable status code (e.g. 1003 or 1009), or if there is a need to hide specific
 details about the policy.

See Also:




    - Constant Field Values







  - 


### TOOBIG

public static final int TOOBIG
1009 indicates that an endpoint is terminating the connection because it has received a message
 which is too big for it to process.

See Also:




    - Constant Field Values







  - 


### EXTENSION

public static final int EXTENSION
1010 indicates that an endpoint (client) is terminating the connection because it has expected
 the server to negotiate one or more extension, but the server didn't return them in the
 response message of the WebSocket handshake. The list of extensions which are needed SHOULD
 appear in the /reason/ part of the Close frame. Note that this status code is not used by the
 server, because it can fail the WebSocket handshake instead.

See Also:




    - Constant Field Values







  - 


### UNEXPECTED_CONDITION

public static final int UNEXPECTED_CONDITION
1011 indicates that a server is terminating the connection because it encountered an unexpected
 condition that prevented it from fulfilling the request.

See Also:




    - Constant Field Values







  - 


### SERVICE_RESTART

public static final int SERVICE_RESTART
1012 indicates that the service is restarted. A client may reconnect, and if it choses to do,
 should reconnect using a randomized delay of 5 - 30s. See https://www.ietf.org/mail-archive/web/hybi/current/msg09670.html
 for more information.

Since:
1.3.8
See Also:




    - Constant Field Values







  - 


### TRY_AGAIN_LATER

public static final int TRY_AGAIN_LATER
1013 indicates that the service is experiencing overload. A client should only connect to a
 different IP (when there are multiple for the target) or reconnect to the same IP upon user
 action. See https://www.ietf.org/mail-archive/web/hybi/current/msg09670.html for more
 information.

Since:
1.3.8
See Also:




    - Constant Field Values







  - 


### BAD_GATEWAY

public static final int BAD_GATEWAY
1014 indicates that the server was acting as a gateway or proxy and received an invalid
 response from the upstream server. This is similar to 502 HTTP Status Code See
 https://www.ietf.org/mail-archive/web/hybi/current/msg10748.html fore more information.

Since:
1.3.8
See Also:




    - Constant Field Values







  - 


### TLS_ERROR

public static final int TLS_ERROR
1015 is a reserved value and MUST NOT be set as a status code in a Close control frame by an
 endpoint. It is designated for use in applications expecting a status code to indicate that the
 connection was closed due to a failure to perform a TLS handshake (e.g., the server certificate
 can't be verified).

See Also:




    - Constant Field Values







  - 


### NEVER_CONNECTED

public static final int NEVER_CONNECTED
The connection had never been established

See Also:




    - Constant Field Values







  - 


### BUGGYCLOSE

public static final int BUGGYCLOSE
The connection had a buggy close (this should not happen)

See Also:




    - Constant Field Values







  - 


### FLASHPOLICY

public static final int FLASHPOLICY
The connection was flushed and closed

See Also:




    - Constant Field Values












- 


## Constructor Details




  - 


### CloseFrame

public CloseFrame()
Constructor for a close frame
 


 Using opcode closing and fin = true








- 


## Method Details




  - 


### setCode

public void setCode(int code)
Set the close code for this close frame

Parameters:
`code` - the close code




  - 


### setReason

public void setReason(String reason)
Set the close reason for this close frame

Parameters:
`reason` - the reason code




  - 


### getCloseCode

public int getCloseCode()
Get the used close code

Returns:
the used close code




  - 


### getMessage

public String getMessage()
Get the message that closeframe is containing

Returns:
the message in this frame




  - 


### toString

public String toString()

Overrides:
`toString` in class `FramedataImpl1`




  - 


### isValid

public void isValid()
             throws InvalidDataException
Description copied from class: `FramedataImpl1`
Check if the frame is valid due to specification

Overrides:
`isValid` in class `ControlFrame`
Throws:
`InvalidDataException` - thrown if the frame is not a valid frame




  - 


### setPayload

public void setPayload(ByteBuffer payload)
Description copied from class: `FramedataImpl1`
Set the payload of this frame to the provided payload

Overrides:
`setPayload` in class `FramedataImpl1`
Parameters:
`payload` - the payload which is to set




  - 


### getPayloadData

public ByteBuffer getPayloadData()
Description copied from interface: `Framedata`
The "Payload data" which was sent in this frame

Specified by:
`getPayloadData` in interface `Framedata`
Overrides:
`getPayloadData` in class `FramedataImpl1`
Returns:
the "Payload data" as ByteBuffer




  - 


### equals

public boolean equals(Object o)

Overrides:
`equals` in class `FramedataImpl1`




  - 


### hashCode

public int hashCode()

Overrides:
`hashCode` in class `FramedataImpl1`