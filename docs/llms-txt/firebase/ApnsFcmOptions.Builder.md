# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder.md.txt

# ApnsFcmOptions.Builder

public static class **ApnsFcmOptions.Builder** extends Object  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder#build())() Creates a new [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) instance from the parameters set on this builder. |
| [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder) | [setAnalyticsLabel](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder#setAnalyticsLabel(java.lang.String))(String analyticsLabel)                                                                                                                                   |
| [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder) | [setImage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder#setImage(java.lang.String))(String imageUrl)                                                                                                                                                           |

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

#### public [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions)
**build**
()

Creates a new [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) instance from the parameters set on this builder.  

##### Returns

- A new [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder)
**setAnalyticsLabel**
(String analyticsLabel)

<br />

##### Parameters

| analyticsLabel | A string representing the analytics label used for APNS messages. |
|----------------|-------------------------------------------------------------------|

##### Returns

- This builder  

#### public [ApnsFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions.Builder)
**setImage**
(String imageUrl)

<br />

##### Parameters

| imageUrl | URL of the image that is going to be displayed in the notification. |
|----------|---------------------------------------------------------------------|

##### Returns

- This builder