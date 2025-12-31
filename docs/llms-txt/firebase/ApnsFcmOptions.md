# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.md.txt

# ApnsFcmOptions

public final class **ApnsFcmOptions** extends Object  
Represents the APNS-specific FCM options that can be included in an [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig). Instances
of this class are thread-safe and immutable.  

### Nested Class Summary

|-------|---|---|---|
| class | [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder) ||   |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions#builder())() Creates a new [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder).                                                                                      |
| static [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions)                 | [withAnalyticsLabel](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions#withAnalyticsLabel(java.lang.String))(String analyticsLabel) Creates a new [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) object with the specified analytics label. |

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

#### public static [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder)
**builder**
()

Creates a new [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder).  

##### Returns

- An [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder) instance.  

#### public static [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions)
**withAnalyticsLabel**
(String analyticsLabel)

Creates a new [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) object with the specified analytics label.  

##### Parameters

| analyticsLabel | An analytics label |
|----------------|--------------------|

##### Returns

- An [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) object with the analytics label set to the supplied value.