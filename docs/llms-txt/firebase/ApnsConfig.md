# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.md.txt

# ApnsConfig

public class **ApnsConfig** extends Object  
Represents the APNS-specific options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message).
Instances of this class are thread-safe and immutable. Refer to
[Apple documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html) for various headers and payload fields supported by APNS.  

### Nested Class Summary

|-------|---|---|---|
| class | [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) ||   |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig#builder())() Creates a new [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder). |

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

#### public static [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**builder**
()

Creates a new [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder).  

##### Returns

- A [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) instance.