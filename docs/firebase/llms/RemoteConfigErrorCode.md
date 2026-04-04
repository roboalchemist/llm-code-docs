# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/RemoteConfigErrorCode.md.txt

# RemoteConfigErrorCode

public final enum **RemoteConfigErrorCode** extends Enum\<E extends Enum\<E\>\>  
Error codes that can be raised by the Remote Config APIs.  

### Inherited Method Summary

From class java.lang.Enum  

|----------------------------------|---------------------------------------|
| final Object                     | clone()                               |
| final int                        | compareTo(E arg0)                     |
| int                              | compareTo(Object arg0)                |
| final boolean                    | equals(Object arg0)                   |
| final void                       | finalize()                            |
| final Class\<E\>                 | getDeclaringClass()                   |
| final int                        | hashCode()                            |
| final String                     | name()                                |
| final int                        | ordinal()                             |
| String                           | toString()                            |
| static \<T extends Enum\<T\>\> T | valueOf(Class\<T\> arg0, String arg1) |

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

From interface java.lang.Comparable  

|--------------|-------------------|
| abstract int | compareTo(T arg0) |

## Enum Values

#### public static final RemoteConfigErrorCode
**ALREADY_EXISTS**

The resource that a client tried to create already exists.  

#### public static final RemoteConfigErrorCode
**FAILED_PRECONDITION**

Request cannot be executed in the current system state, such as deleting a non-empty
directory.  

#### public static final RemoteConfigErrorCode
**INTERNAL**

Internal server error.  

#### public static final RemoteConfigErrorCode
**INVALID_ARGUMENT**

One or more arguments specified in the request were invalid.  

#### public static final RemoteConfigErrorCode
**UNAUTHENTICATED**

User is not authenticated.  

#### public static final RemoteConfigErrorCode
**VALIDATION_ERROR**

Failed to validate Remote Config data.  

#### public static final RemoteConfigErrorCode
**VERSION_MISMATCH**

The current version specified in an update request
did not match the actual version in the database.