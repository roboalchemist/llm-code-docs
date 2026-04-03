# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MessagingErrorCode.md.txt

# MessagingErrorCode

public final enum **MessagingErrorCode** extends Enum\<E extends Enum\<E\>\>  
Error codes that can be raised by the Cloud Messaging APIs.  

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

#### public static final MessagingErrorCode
**INTERNAL**

Internal server error.  

#### public static final MessagingErrorCode
**INVALID_ARGUMENT**

One or more arguments specified in the request were invalid.  

#### public static final MessagingErrorCode
**QUOTA_EXCEEDED**

Sending limit exceeded for the message target.  

#### public static final MessagingErrorCode
**SENDER_ID_MISMATCH**

The authenticated sender ID is different from the sender ID for the registration token.  

#### public static final MessagingErrorCode
**THIRD_PARTY_AUTH_ERROR**

APNs certificate or web push auth key was invalid or missing.  

#### public static final MessagingErrorCode
**UNAVAILABLE**

Cloud Messaging service is temporarily unavailable.  

#### public static final MessagingErrorCode
**UNREGISTERED**

App instance was unregistered from FCM. This usually means that the token used is no longer
valid and a new one must be used.