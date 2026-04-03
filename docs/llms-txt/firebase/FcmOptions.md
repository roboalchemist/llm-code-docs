# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.md.txt

# FcmOptions

public final class **FcmOptions** extends Object  
Represents the platform-independent FCM options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message).
Instances of this class are thread-safe and immutable.  

### Nested Class Summary

|-------|---|---|---|
| class | [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder) ||   |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions#builder())() Creates a new [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder).                                                                                      |
| static [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions)                 | [withAnalyticsLabel](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions#withAnalyticsLabel(java.lang.String))(String analyticsLabel) Creates a new [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) object with the specified analytics label. |

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

#### public static [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder)
**builder**
()

Creates a new [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder).  

##### Returns

- An [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder) instance.  

#### public static [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions)
**withAnalyticsLabel**
(String analyticsLabel)

Creates a new [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) object with the specified analytics label.  

##### Parameters

| analyticsLabel | An analytics label |
|----------------|--------------------|

##### Returns

- An [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) object with the analytics label set to the supplied value.