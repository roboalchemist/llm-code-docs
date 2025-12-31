# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.md.txt

# Notification

public class **Notification** extends Object  
Represents the notification parameters that can be included in a [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message). Instances
of this class are thread-safe and immutable.  

### Nested Class Summary

|-------|---|---|---|
| class | [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder) ||   |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification#builder())() Creates a new [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder). |

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

#### public static [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder)
**builder**
()

Creates a new [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder).  

##### Returns

- A [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder) instance.