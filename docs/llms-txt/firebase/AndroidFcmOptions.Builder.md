# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder.md.txt

# AndroidFcmOptions.Builder

public static class **AndroidFcmOptions.Builder** extends Object  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder#build())() Creates a new [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) instance from the parameters set on this builder. |
| [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder) | [setAnalyticsLabel](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder#setAnalyticsLabel(java.lang.String))(String analyticsLabel)                                                                                                                                         |

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

#### public [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions)
**build**
()

Creates a new [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) instance from the parameters set on this builder.  

##### Returns

- A new [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [AndroidFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions.Builder)
**setAnalyticsLabel**
(String analyticsLabel)

<br />

##### Parameters

| analyticsLabel | A string representing the analytics label used for Android messages. |
|----------------|----------------------------------------------------------------------|

##### Returns

- This builder