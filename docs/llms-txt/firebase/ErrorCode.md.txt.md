# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ErrorCode.md.txt

# ErrorCode

public final enum **ErrorCode** extends Enum\<E extends Enum\<E\>\>  
Platform-wide error codes that can be raised by Admin SDK APIs.

### Inherited Method Summary

From class java.lang.Enum

|---|---|
| final Object | clone() |
| final int | compareTo(E arg0) |
| int | compareTo(Object arg0) |
| final boolean | equals(Object arg0) |
| final void | finalize() |
| final Class\<E\> | getDeclaringClass() |
| final int | hashCode() |
| final String | name() |
| final int | ordinal() |
| String | toString() |
| static \<T extends Enum\<T\>\> T | valueOf(Class\<T\> arg0, String arg1) |

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

From interface java.lang.Comparable

|---|---|
| abstract int | compareTo(T arg0) |

## Enum Values

#### public static final ErrorCode
**ABORTED**

Concurrency conflict, such as read-modify-write conflict.

#### public static final ErrorCode
**ALREADY_EXISTS**

The resource that a client tried to create already exists.

#### public static final ErrorCode
**CANCELLED**

Request cancelled by the client.

#### public static final ErrorCode
**CONFLICT**

Concurrency conflict, such as read-modify-write conflict.

#### public static final ErrorCode
**DATA_LOSS**

Unrecoverable data loss or data corruption. The client should report the error to the user.

#### public static final ErrorCode
**DEADLINE_EXCEEDED**

Request deadline exceeded. This happens only if the caller sets a deadline that is
shorter than the method's default deadline (i.e. requested deadline is not enough for the
server to process the request) and the request did not finish within the deadline.

#### public static final ErrorCode
**FAILED_PRECONDITION**

Request cannot be executed in the current system state, such as deleting a non-empty
directory.

#### public static final ErrorCode
**INTERNAL**

Internal server error. Typically a server bug.

#### public static final ErrorCode
**INVALID_ARGUMENT**

Client specified an invalid argument.

#### public static final ErrorCode
**NOT_FOUND**

A specified resource is not found, or the request is rejected for unknown reasons,
such as a blocked network address.

#### public static final ErrorCode
**OUT_OF_RANGE**

Client specified an invalid range.

#### public static final ErrorCode
**PERMISSION_DENIED**

Client does not have sufficient permission. This can happen because the OAuth token does
not have the right scopes, the client doesn't have permission, or the API has not been
enabled for the client project.

#### public static final ErrorCode
**RESOURCE_EXHAUSTED**

Either out of resource quota or rate limited.

#### public static final ErrorCode
**UNAUTHENTICATED**

Request not authenticated due to missing, invalid, or expired OAuth token.

#### public static final ErrorCode
**UNAVAILABLE**

Service unavailable. Typically the server is down.

#### public static final ErrorCode
**UNKNOWN**

Unknown server error. Typically a server bug.