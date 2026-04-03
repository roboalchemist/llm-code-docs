# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder.md.txt

# AndroidConfig.Builder

public static class **AndroidConfig.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#build())() Creates a new [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) instance from the parameters set on this builder.                                                                                                                                                                                                                                                                                                                                                       |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [putAllData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>))(Map\<String, String\> map) Adds all the key-value pairs in the given map to the message as data fields.                                                                                                                                                                                                                                                                                                                                                                                   |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [putData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#putData(java.lang.String, java.lang.String))(String key, String value) Adds the given key-value pair to the message as a data field.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [setCollapseKey](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#setCollapseKey(java.lang.String))(String collapseKey) Sets a collapse key for the message.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [setDirectBootOk](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#setDirectBootOk(boolean))(boolean directBootOk) Sets the `direct_boot_ok` flag.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [setFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#setFcmOptions(com.google.firebase.messaging.AndroidFcmOptions))([AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) androidFcmOptions) Sets the [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions), which overrides values set in the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) for Android messages. |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [setNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#setNotification(com.google.firebase.messaging.AndroidNotification))([AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification) notification) Sets the Android notification to be included in the message.                                                                                                                                                                                                                                                             |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [setPriority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#setPriority(com.google.firebase.messaging.AndroidConfig.Priority))([AndroidConfig.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Priority) priority) Sets the priority of the message.                                                                                                                                                                                                                                                                                           |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [setRestrictedPackageName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#setRestrictedPackageName(java.lang.String))(String restrictedPackageName) Sets the package name of the application where the registration tokens must match in order to receive the message.                                                                                                                                                                                                                                                                                                                                               |
| [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder) | [setTtl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder#setTtl(long))(long ttl) Sets the time-to-live duration of the message in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

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

#### public [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig)
**build**
()

Creates a new [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) instance from the parameters set on this builder.  

##### Returns

- A new [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**putAllData**
(Map\<String, String\> map)

Adds all the key-value pairs in the given map to the message as data fields. None of the
keys and values may be null. When set, overrides any data fields set on the top-level
[Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) via [putData(String, String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putData(java.lang.String, java.lang.String)) and
[putAllData(Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>)).  

##### Parameters

| map | A non-null map of data fields. Map must not contain null keys or values. |
|-----|--------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**putData**
(String key, String value)

Adds the given key-value pair to the message as a data field. Key and the value may not be
null. When set, overrides any data fields set on the top-level [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) via
[putData(String, String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putData(java.lang.String, java.lang.String)) and [putAllData(Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>)).  

##### Parameters

|  key  | Name of the data field. Must not be null.  |
| value | Value of the data field. Must not be null. |
|-------|--------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**setCollapseKey**
(String collapseKey)

Sets a collapse key for the message. The collapse key serves as an identifier for a group of
messages that can be collapsed, so that only the last message gets sent when delivery can be
resumed. A maximum of 4 different collapse keys may be active at any given time.

By default, the collapse key is the app package name registered in
the Firebase console.

<br />

##### Parameters

| collapseKey | A collapse key string. |
|-------------|------------------------|

##### Returns

- This builder.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**setDirectBootOk**
(boolean directBootOk)

Sets the `direct_boot_ok` flag. If set to true, messages are delivered to
the app while the device is in direct boot mode.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**setFcmOptions**
([AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions) androidFcmOptions)

Sets the [AndroidFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidFcmOptions), which overrides values set in the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions)
for Android messages.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**setNotification**
([AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification) notification)

Sets the Android notification to be included in the message.  

##### Parameters

| notification | An [AndroidNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidNotification) instance. |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**setPriority**
([AndroidConfig.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Priority) priority)

Sets the priority of the message.  

##### Parameters

| priority | A value from the [AndroidConfig.Priority](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Priority) enum. |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**setRestrictedPackageName**
(String restrictedPackageName)

Sets the package name of the application where the registration tokens must match in order
to receive the message.  

##### Parameters

| restrictedPackageName | A package name string. |
|-----------------------|------------------------|

##### Returns

- This builder.  

#### public [AndroidConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig.Builder)
**setTtl**
(long ttl)

Sets the time-to-live duration of the message in milliseconds.  

##### Parameters

| ttl | Time-to-live duration in milliseconds. |
|-----|----------------------------------------|

##### Returns

- This builder.