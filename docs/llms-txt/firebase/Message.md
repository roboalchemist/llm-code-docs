# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.md.txt

# Message

public class **Message** extends Object  
Represents a message that can be sent via Firebase Cloud Messaging (FCM). Contains payload
information as well as the recipient information. The recipient information must contain exactly
one token, topic or condition parameter. Instances of this class are thread-safe and immutable.
Use [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) to create new instances.  

##### See Also

- [FCM message
format](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)  

### Nested Class Summary

|-------|---|---|---|
| class | [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) ||   |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message#builder())() Creates a new [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder). |

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

#### public static [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**builder**
()

Creates a new [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder).  

##### Returns

- A [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) instance.