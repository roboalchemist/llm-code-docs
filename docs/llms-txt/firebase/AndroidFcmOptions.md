# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.md.txt

# AndroidFcmOptions

public final class **AndroidFcmOptions** extends Object  
Represents the Android-specific FCM options that can be included in an [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig).
Instances of this class are thread-safe and immutable.  

### Nested Class Summary

|-------|---|---|---|
| class | [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder) ||   |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions#builder())() Creates a new [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder).                                                                                      |
| static [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions)                 | [withAnalyticsLabel](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions#withAnalyticsLabel(java.lang.String))(String analyticsLabel) Creates a new [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) object with the specified analytics label. |

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

#### public static [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder)
**builder**
()

Creates a new [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder).  

##### Returns

- A [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder) instance.  

#### public static [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions)
**withAnalyticsLabel**
(String analyticsLabel)

Creates a new [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) object with the specified analytics label.  

##### Parameters

| analyticsLabel | An analytics label |
|----------------|--------------------|

##### Returns

- An [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) object with the analytics label set to the supplied value.