# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse.md.txt

# SendResponse

public final class **SendResponse** extends Object  
The result of an individual send operation that was executed as part of a batch. See
[BatchResponse](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse) for more details.  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) | [getException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse#getException())() Returns an exception if the send operation failed.                |
| String                                                                                                                                                 | [getMessageId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse#getMessageId())() Returns a message ID string if the send operation was successful. |
| boolean                                                                                                                                                | [isSuccessful](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse#isSuccessful())() Returns whether the send operation was successful or not.         |

### Inherited Method Summary

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

## Public Methods

#### public [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException)
**getException**
()

Returns an exception if the send operation failed. Otherwise returns null.  

##### Returns

- A [FirebaseMessagingException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessagingException) or null.  

#### public String
**getMessageId**
()

Returns a message ID string if the send operation was successful. Otherwise returns null.  

##### Returns

- A message ID string or null.  

#### public boolean
**isSuccessful**
()

Returns whether the send operation was successful or not. When this method returns true,
[getMessageId()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse#getMessageId()) is guaranteed to return a non-null value. When this method returns
false [getException()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/SendResponse#getException()) is guaranteed to return a non-null value.  

##### Returns

- A boolean indicating success of the operation.