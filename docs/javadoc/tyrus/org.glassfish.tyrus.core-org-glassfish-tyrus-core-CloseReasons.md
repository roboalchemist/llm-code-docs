Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Enum Class CloseReasons

java.lang.Object
java.lang.Enum<CloseReasons>
org.glassfish.tyrus.core.CloseReasons

All Implemented Interfaces:
`Serializable`, `Comparable<CloseReasons>`, `Constable`

---

public enum CloseReasons
extends Enum<CloseReasons>
Enum containing standard CloseReasons defined in RFC 6455, see chapter
 7.4.1 Defined Status Codes.

Author:
Pavel Bucek

-

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

-

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`CANNOT_ACCEPT`

1003 indicates that an endpoint is terminating the connection
 because it has received a type of data it cannot accept (e.g., an
 endpoint that understands only text data MAY send this if it
 receives a binary message).

`CLOSED_ABNORMALLY`

1006 is a reserved value and MUST NOT be set as a status code in a
 Close control frame by an endpoint.

`GOING_AWAY`

1001 indicates that an endpoint is "going away", such as a server
 going down or a browser having navigated away from a page.

`NO_EXTENSION`

1010 indicates that an endpoint (client) is terminating the
 connection because it has expected the server to negotiate one or
 more extension, but the server didn't return them in the response
 message of the WebSocket handshake.

`NO_STATUS_CODE`

1005 is a reserved value and MUST NOT be set as a status code in a
 Close control frame by an endpoint.

`NORMAL_CLOSURE`

1000 indicates a normal closure, meaning that the purpose for
 which the connection was established has been fulfilled.

`NOT_CONSISTENT`

1007 indicates that an endpoint is terminating the connection
 because it has received data within a message that was not
 consistent with the type of the message (e.g., non-UTF-8
 data within a text message).

`PROTOCOL_ERROR`

1002 indicates that an endpoint is terminating the connection due
 to a protocol error.

`RESERVED`

Reserved.

`SERVICE_RESTART`

1012 indicates that the service will be restarted.

`TLS_HANDSHAKE_FAILURE`

1015 is a reserved value and MUST NOT be set as a status code in a
 Close control frame by an endpoint.

`TOO_BIG`

1009 indicates that an endpoint is terminating the connection
 because it has received a message that is too big for it to
 process.

`TRY_AGAIN_LATER`

1013 indicates that the service is experiencing overload

`UNEXPECTED_CONDITION`

1011 indicates that a server is terminating the connection because
 it encountered an unexpected condition that prevented it from
 fulfilling the request.

`VIOLATED_POLICY`

1008 indicates that an endpoint is terminating the connection
 because it has received a message that violates its policy.

-

## Method Summary

Modifier and Type
Method
Description
`static jakarta.websocket.CloseReason`
`create(jakarta.websocket.CloseReason.CloseCode closeCode,
 String reasonPhrase)`

`jakarta.websocket.CloseReason`
`getCloseReason()`

Get close reason.

`static CloseReasons`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static CloseReasons[]`
`values()`

Returns an array containing the constants of this enum class, in
the order they are declared.

### Methods inherited from class java.lang.Enum

`clone, compareTo, describeConstable, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

-

## Enum Constant Details

-

### NORMAL_CLOSURE

public static final CloseReasons NORMAL_CLOSURE
1000 indicates a normal closure, meaning that the purpose for
 which the connection was established has been fulfilled.

-

### GOING_AWAY

public static final CloseReasons GOING_AWAY
1001 indicates that an endpoint is "going away", such as a server
 going down or a browser having navigated away from a page.

-

### PROTOCOL_ERROR

public static final CloseReasons PROTOCOL_ERROR
1002 indicates that an endpoint is terminating the connection due
 to a protocol error.

-

### CANNOT_ACCEPT

public static final CloseReasons CANNOT_ACCEPT
1003 indicates that an endpoint is terminating the connection
 because it has received a type of data it cannot accept (e.g., an
 endpoint that understands only text data MAY send this if it
 receives a binary message).

-

### RESERVED

public static final CloseReasons RESERVED
Reserved.  The specific meaning might be defined in the future.

-

### NO_STATUS_CODE

public static final CloseReasons NO_STATUS_CODE
1005 is a reserved value and MUST NOT be set as a status code in a
 Close control frame by an endpoint.  It is designated for use in
 applications expecting a status code to indicate that no status
 code was actually present.

-

### CLOSED_ABNORMALLY

public static final CloseReasons CLOSED_ABNORMALLY
1006 is a reserved value and MUST NOT be set as a status code in a
 Close control frame by an endpoint.  It is designated for use in
 applications expecting a status code to indicate that the
 connection was closed abnormally, e.g., without sending or
 receiving a Close control frame.

-

### NOT_CONSISTENT

public static final CloseReasons NOT_CONSISTENT
1007 indicates that an endpoint is terminating the connection
 because it has received data within a message that was not
 consistent with the type of the message (e.g., non-UTF-8
 data within a text message).

-

### VIOLATED_POLICY

public static final CloseReasons VIOLATED_POLICY
1008 indicates that an endpoint is terminating the connection
 because it has received a message that violates its policy.  This
 is a generic status code that can be returned when there is no
 other more suitable status code (e.g., 1003 or 1009) or if there
 is a need to hide specific details about the policy.

-

### TOO_BIG

public static final CloseReasons TOO_BIG
1009 indicates that an endpoint is terminating the connection
 because it has received a message that is too big for it to
 process.

-

### NO_EXTENSION

public static final CloseReasons NO_EXTENSION
1010 indicates that an endpoint (client) is terminating the
 connection because it has expected the server to negotiate one or
 more extension, but the server didn't return them in the response
 message of the WebSocket handshake.  The list of extensions that
 are needed SHOULD appear in the /reason/ part of the Close frame.
 Note that this status code is not used by the server, because it
 can fail the WebSocket handshake instead.

-

### UNEXPECTED_CONDITION

public static final CloseReasons UNEXPECTED_CONDITION
1011 indicates that a server is terminating the connection because
 it encountered an unexpected condition that prevented it from
 fulfilling the request.

-

### SERVICE_RESTART

public static final CloseReasons SERVICE_RESTART
1012 indicates that the service will be restarted.

-

### TRY_AGAIN_LATER

public static final CloseReasons TRY_AGAIN_LATER
1013 indicates that the service is experiencing overload

-

### TLS_HANDSHAKE_FAILURE

public static final CloseReasons TLS_HANDSHAKE_FAILURE
1015 is a reserved value and MUST NOT be set as a status code in a
 Close control frame by an endpoint.  It is designated for use in
 applications expecting a status code to indicate that the
 connection was closed due to a failure to perform a TLS handshake
 (e.g., the server certificate can't be verified).

-

## Method Details

-

### values

public static CloseReasons[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

-

### valueOf

public static CloseReasons valueOf(String name)
Returns the enum constant of this class with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum class has no constant with the specified name
`NullPointerException` - if the argument is null

-

### getCloseReason

public jakarta.websocket.CloseReason getCloseReason()
Get close reason.

Returns:
close reason represented by this value;

-

### create

public static jakarta.websocket.CloseReason create(jakarta.websocket.CloseReason.CloseCode closeCode,
 String reasonPhrase)
