# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError.md.txt

# DatabaseError

public class **DatabaseError** extends Object  
Instances of DatabaseError are passed to callbacks when an operation failed. They contain a
description of the specific error that occurred.

### Constant Summary

|---|---|---|
| int | [DATA_STALE](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#DATA_STALE) | **Internal use.** |
| int | [DISCONNECTED](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#DISCONNECTED) | The operation had to be aborted due to a network disconnect. |
| int | [EXPIRED_TOKEN](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#EXPIRED_TOKEN) | The supplied auth token has expired. |
| int | [INVALID_TOKEN](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#INVALID_TOKEN) | The specified authentication token is invalid. |
| int | [MAX_RETRIES](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#MAX_RETRIES) | The transaction had too many retries |
| int | [NETWORK_ERROR](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#NETWORK_ERROR) | The operation could not be performed due to a network error. |
| int | [OPERATION_FAILED](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#OPERATION_FAILED) | The server indicated that this operation failed. |
| int | [OVERRIDDEN_BY_SET](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#OVERRIDDEN_BY_SET) | The transaction was overridden by a subsequent set |
| int | [PERMISSION_DENIED](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#PERMISSION_DENIED) | This client does not have permission to perform this operation. |
| int | [UNAVAILABLE](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#UNAVAILABLE) | The service is unavailable. |
| int | [UNKNOWN_ERROR](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#UNKNOWN_ERROR) | An unknown error occurred. |
| int | [USER_CODE_EXCEPTION](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#USER_CODE_EXCEPTION) | An exception occurred in user code. |
| int | [WRITE_CANCELED](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#WRITE_CANCELED) | The write was canceled locally. |

### Public Method Summary

|---|---|
| static [DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) | [fromException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#fromException(java.lang.Throwable))(Throwable e) |
| int | [getCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#getCode())() |
| String | [getDetails](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#getDetails())() |
| String | [getMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#getMessage())() |
| [DatabaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseException) | [toException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#toException())() Can be used if a third party needs an Exception from Firebase Database for integration purposes. |
| String | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError#toString())() |

### Inherited Method Summary

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

## Constants

#### public static final int
**DATA_STALE**

**Internal use.**
Constant Value: -1

#### public static final int
**DISCONNECTED**

The operation had to be aborted due to a network disconnect.
Constant Value: -4

#### public static final int
**EXPIRED_TOKEN**

The supplied auth token has expired.
Constant Value: -6

#### public static final int
**INVALID_TOKEN**

The specified authentication token is invalid. This can occur when the token is malformed,
expired, or the secret that was used to generate it has been revoked.
Constant Value: -7

#### public static final int
**MAX_RETRIES**

The transaction had too many retries
Constant Value: -8

#### public static final int
**NETWORK_ERROR**

The operation could not be performed due to a network error.
Constant Value: -24

#### public static final int
**OPERATION_FAILED**

The server indicated that this operation failed.
Constant Value: -2

#### public static final int
**OVERRIDDEN_BY_SET**

The transaction was overridden by a subsequent set
Constant Value: -9

#### public static final int
**PERMISSION_DENIED**

This client does not have permission to perform this operation.
Constant Value: -3

#### public static final int
**UNAVAILABLE**

The service is unavailable.
Constant Value: -10

#### public static final int
**UNKNOWN_ERROR**

An unknown error occurred. Please refer to the error message and error details for more
information.
Constant Value: -999

#### public static final int
**USER_CODE_EXCEPTION**

An exception occurred in user code.
Constant Value: -11

#### public static final int
**WRITE_CANCELED**

The write was canceled locally.
Constant Value: -25

## Public Methods

#### public static [DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError)
**fromException**
(Throwable e)

<br />

#### public int
**getCode**
()

<br />

##### Returns

- One of the defined status codes, depending on the error.

#### public String
**getDetails**
()

<br />

##### Returns

- Human-readable details on the error and additional information, e.g. links to docs;

#### public String
**getMessage**
()

<br />

##### Returns

- A human-readable description of the error.

#### public [DatabaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseException)
**toException**
()

Can be used if a third party needs an Exception from Firebase Database for integration
purposes.

##### Returns

- An exception wrapping this error, with an appropriate message and no stack trace.

#### public String
**toString**
()

<br />