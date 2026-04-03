# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.md.txt

# MulticastMessage

public class **MulticastMessage** extends Object  
Represents a message that can be sent to multiple devices via Firebase Cloud Messaging (FCM).
Contains payload information as well as the list of device registration tokens to which the
message should be sent. A single `MulticastMessage` may contain up to 500 registration
tokens.

Instances of this class are thread-safe and immutable. Use [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
to create new instances. See [sendMulticast(MulticastMessage)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticast(com.google.firebase.messaging.MulticastMessage)) for
details on how to send the message to FCM for multicast delivery.

This class and the associated Builder retain the order of tokens. Therefore the order of
the responses list obtained by calling [getResponses()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/BatchResponse#getResponses()) on the return value
of [sendMulticast(MulticastMessage)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FirebaseMessaging#sendMulticast(com.google.firebase.messaging.MulticastMessage)) corresponds to the order in which
tokens were added to the [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder).  

### Nested Class Summary

|-------|---|---|---|
| class | [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) ||   |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage#builder())() Creates a new [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder). |

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

#### public static [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**builder**
()

Creates a new [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder).  

##### Returns

- A [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) instance.