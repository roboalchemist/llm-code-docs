# Class CloseStatus

java.lang.Object
org.springframework.web.socket.CloseStatus

All Implemented Interfaces:
`Serializable`

---

public final class CloseStatus
extends Object
implements Serializable
Represents a WebSocket close status code and reason. Status codes in the 1xxx range are
pre-defined by the protocol. Optionally, a status code may be sent with a reason.

See RFC 6455, Section 7.4.1
"Defined Status Codes".

Since:
4.0
Author:
Rossen Stoyanchev
See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final CloseStatus`
`BAD_DATA`

"1007 indicates that an endpoint is terminating the connection because it has
received data within a message that was not consistent with the type of the message
(for example, non-UTF-8 [RFC3629] data within a text message)."

`static final CloseStatus`
`GOING_AWAY`

"1001 indicates that an endpoint is "going away", such as a server going down or a
browser having navigated away from a page."

`static final CloseStatus`
`NO_CLOSE_FRAME`

"1006 is a reserved value and MUST NOT be set as a status code in a Close control
frame by an endpoint.

`static final CloseStatus`
`NO_STATUS_CODE`

"1005 is a reserved value and MUST NOT be set as a status code in a Close control
frame by an endpoint.

`static final CloseStatus`
`NORMAL`

"1000 indicates a normal closure, meaning that the purpose for which the connection
was established has been fulfilled."

`static final CloseStatus`
`NOT_ACCEPTABLE`

"1003 indicates that an endpoint is terminating the connection because it has
received a type of data it cannot accept (for example, an endpoint that understands only
text data MAY send this if it receives a binary message)."

`static final CloseStatus`
`POLICY_VIOLATION`

"1008 indicates that an endpoint is terminating the connection because it has
received a message that violates its policy.

`static final CloseStatus`
`PROTOCOL_ERROR`

"1002 indicates that an endpoint is terminating the connection due to a protocol
error."

`static final CloseStatus`
`REQUIRED_EXTENSION`

"1010 indicates that an endpoint (client) is terminating the connection because it
has expected the server to negotiate one or more extension, but the server didn't
return them in the response message of the WebSocket handshake.

`static final CloseStatus`
`SERVER_ERROR`

"1011 indicates that a server is terminating the connection because it encountered
an unexpected condition that prevented it from fulfilling the request."

`static final CloseStatus`
`SERVICE_OVERLOAD`

"1013 indicates that the service is experiencing overload.

`static final CloseStatus`
`SERVICE_RESTARTED`

"1012 indicates that the service is restarted.

`static final CloseStatus`
`SESSION_NOT_RELIABLE`

A status code for use within the framework that indicates a session has
become unreliable (for example, timed out while sending a message) and extra
care should be exercised, for example, avoid sending any further data to the
client that may be done during normal shutdown.

`static final CloseStatus`
`TLS_HANDSHAKE_FAILURE`

"1015 is a reserved value and MUST NOT be set as a status code in a Close control
frame by an endpoint.

`static final CloseStatus`
`TOO_BIG_TO_PROCESS`

"1009 indicates that an endpoint is terminating the connection because it has
received a message that is too big for it to process."

- 

## Constructor Summary

Constructors

Constructor
Description
`CloseStatus(int code)`

Create a new `CloseStatus` instance.

`CloseStatus(int code,
 @Nullable String reason)`

Create a new `CloseStatus` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`equals(@Nullable Object other)`
 
`boolean`
`equalsCode(CloseStatus other)`
 
`int`
`getCode()`

Return the status code.

`@Nullable String`
`getReason()`

Return the reason, or `null` if none.

`int`
`hashCode()`
 
`String`
`toString()`
 
`CloseStatus`
`withReason(String reason)`

Create a new `CloseStatus` from this one with the specified reason.

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### NORMAL

public static final CloseStatus NORMAL
"1000 indicates a normal closure, meaning that the purpose for which the connection
was established has been fulfilled."

  - 

### GOING_AWAY

public static final CloseStatus GOING_AWAY
"1001 indicates that an endpoint is "going away", such as a server going down or a
browser having navigated away from a page."

  - 

### PROTOCOL_ERROR

public static final CloseStatus PROTOCOL_ERROR
"1002 indicates that an endpoint is terminating the connection due to a protocol
error."

  - 

### NOT_ACCEPTABLE

public static final CloseStatus NOT_ACCEPTABLE
"1003 indicates that an endpoint is terminating the connection because it has
received a type of data it cannot accept (for example, an endpoint that understands only
text data MAY send this if it receives a binary message)."

  - 

### NO_STATUS_CODE

public static final CloseStatus NO_STATUS_CODE
"1005 is a reserved value and MUST NOT be set as a status code in a Close control
frame by an endpoint. It is designated for use in applications expecting a status
code to indicate that no status code was actually present."

  - 

### NO_CLOSE_FRAME

public static final CloseStatus NO_CLOSE_FRAME
"1006 is a reserved value and MUST NOT be set as a status code in a Close control
frame by an endpoint. It is designated for use in applications expecting a status
code to indicate that the connection was closed abnormally, for example, without sending
or receiving a Close control frame."

  - 

### BAD_DATA

public static final CloseStatus BAD_DATA
"1007 indicates that an endpoint is terminating the connection because it has
received data within a message that was not consistent with the type of the message
(for example, non-UTF-8 [RFC3629] data within a text message)."

  - 

### POLICY_VIOLATION

public static final CloseStatus POLICY_VIOLATION
"1008 indicates that an endpoint is terminating the connection because it has
received a message that violates its policy. This is a generic status code that can
be returned when there is no other more suitable status code (for example, 1003 or 1009)
or if there is a need to hide specific details about the policy."

  - 

### TOO_BIG_TO_PROCESS

public static final CloseStatus TOO_BIG_TO_PROCESS
"1009 indicates that an endpoint is terminating the connection because it has
received a message that is too big for it to process."

  - 

### REQUIRED_EXTENSION

public static final CloseStatus REQUIRED_EXTENSION
"1010 indicates that an endpoint (client) is terminating the connection because it
has expected the server to negotiate one or more extension, but the server didn't
return them in the response message of the WebSocket handshake. The list of
extensions that are needed SHOULD appear in the /reason/ part of the Close frame.
Note that this status code is not used by the server, because it can fail the
WebSocket handshake instead."

  - 

### SERVER_ERROR

public static final CloseStatus SERVER_ERROR
"1011 indicates that a server is terminating the connection because it encountered
an unexpected condition that prevented it from fulfilling the request."

  - 

### SERVICE_RESTARTED

public static final CloseStatus SERVICE_RESTARTED
"1012 indicates that the service is restarted. A client may reconnect, and if it
chooses to do, should reconnect using a randomized delay of 5 - 30s."

  - 

### SERVICE_OVERLOAD

public static final CloseStatus SERVICE_OVERLOAD
"1013 indicates that the service is experiencing overload. A client should only
connect to a different IP (when there are multiple for the target) or reconnect to
the same IP upon user action."

  - 

### TLS_HANDSHAKE_FAILURE

public static final CloseStatus TLS_HANDSHAKE_FAILURE
"1015 is a reserved value and MUST NOT be set as a status code in a Close control
frame by an endpoint. It is designated for use in applications expecting a status
code to indicate that the connection was closed due to a failure to perform a TLS
handshake (for example, the server certificate can't be verified)."

  - 

### SESSION_NOT_RELIABLE

public static final CloseStatus SESSION_NOT_RELIABLE
A status code for use within the framework that indicates a session has
become unreliable (for example, timed out while sending a message) and extra
care should be exercised, for example, avoid sending any further data to the
client that may be done during normal shutdown.

Since:
4.0.3

- 

## Constructor Details

  - 

### CloseStatus

public CloseStatus(int code)
Create a new `CloseStatus` instance.

Parameters:
`code` - the status code

  - 

### CloseStatus

public CloseStatus(int code,
 @Nullable String reason)
Create a new `CloseStatus` instance.

Parameters:
`code` - the status code
`reason` - the reason

- 

## Method Details

  - 

### getCode

public int getCode()
Return the status code.

  - 

### getReason

public @Nullable String getReason()
Return the reason, or `null` if none.

  - 

### withReason

public CloseStatus withReason(String reason)
Create a new `CloseStatus` from this one with the specified reason.

Parameters:
`reason` - the reason
Returns:
a new `CloseStatus` instance

  - 

### equalsCode

public boolean equalsCode(CloseStatus other)

  - 

### equals

public boolean equals(@Nullable Object other)

Overrides:
`equals` in class `Object`

  - 

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`