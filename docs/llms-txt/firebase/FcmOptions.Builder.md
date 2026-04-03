# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder.md.txt

# FcmOptions.Builder

public static class **FcmOptions.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder#build())() Creates a new [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) instance from the parameters set on this builder. |
| [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder) | [setAnalyticsLabel](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder#setAnalyticsLabel(java.lang.String))(String analyticsLabel)                                                                                                                           |

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

#### public [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions)
**build**
()

Creates a new [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) instance from the parameters set on this builder.  

##### Returns

- A new [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [FcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions.Builder)
**setAnalyticsLabel**
(String analyticsLabel)

<br />

##### Parameters

| analyticsLabel | A string representing the analytics label used for messages where no platform-specific analytics label has been specified. |
|----------------|----------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder