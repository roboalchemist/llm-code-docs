# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder.md.txt

# Message.Builder

public static class **Message.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#build())() Creates a new [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) instance from the parameters set on this builder.                                                                                                                                                                                                                 |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [putAllData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>))(Map\<String, String\> map) Adds all the key-value pairs in the given map to the message as data fields.                                                                                                                                                                                                                                 |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [putData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putData(java.lang.String, java.lang.String))(String key, String value) Adds the given key-value pair to the message as a data field.                                                                                                                                                                                                                                                                      |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setAndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setAndroidConfig(com.google.firebase.messaging.AndroidConfig))([AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) androidConfig) Sets the Android-specific information to be included in the message.                                                                                                                  |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setApnsConfig(com.google.firebase.messaging.ApnsConfig))([ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) apnsConfig) Sets the information specific to APNS (Apple Push Notification Service).                                                                                                                                |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setCondition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setCondition(java.lang.String))(String condition) Sets the FCM condition to which the message should be sent.                                                                                                                                                                                                                                                                                        |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setFcmOptions(com.google.firebase.messaging.FcmOptions))([FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) fcmOptions) Sets the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions), which can be overridden by the platform-specific `fcm_options` fields. |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setNotification(com.google.firebase.messaging.Notification))([Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) notification) Sets the notification information to be included in the message.                                                                                                                            |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setToken(java.lang.String))(String token) Sets the registration token of the device to which the message should be sent.                                                                                                                                                                                                                                                                                 |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setTopic](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setTopic(java.lang.String))(String topic) Sets the name of the FCM topic to which the message should be sent.                                                                                                                                                                                                                                                                                            |
| [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder) | [setWebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#setWebpushConfig(com.google.firebase.messaging.WebpushConfig))([WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) webpushConfig) Sets the Webpush-specific information to be included in the message.                                                                                                                  |

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

#### public [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message)
**build**
()

Creates a new [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) instance from the parameters set on this builder.  

##### Returns

- A new [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**putAllData**
(Map\<String, String\> map)

Adds all the key-value pairs in the given map to the message as data fields. None of the
keys or values may be null.  

##### Parameters

| map | A non-null map of data fields. Map must not contain null keys or values. |
|-----|--------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**putData**
(String key, String value)

Adds the given key-value pair to the message as a data field. Key or the value may not be
null.  

##### Parameters

|  key  | Name of the data field. Must not be null.  |
| value | Value of the data field. Must not be null. |
|-------|--------------------------------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setAndroidConfig**
([AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) androidConfig)

Sets the Android-specific information to be included in the message.  

##### Parameters

| androidConfig | An [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) instance. |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setApnsConfig**
([ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) apnsConfig)

Sets the information specific to APNS (Apple Push Notification Service).  

##### Parameters

| apnsConfig | An [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) instance. |
|------------|-------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setCondition**
(String condition)

Sets the FCM condition to which the message should be sent.  

##### Parameters

| condition | A valid condition string (e.g. `"'foo' in topics"`). |
|-----------|------------------------------------------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setFcmOptions**
([FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) fcmOptions)

Sets the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions), which can be overridden by the platform-specific `fcm_options` fields.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setNotification**
([Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) notification)

Sets the notification information to be included in the message.  

##### Parameters

| notification | A [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) instance. |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setToken**
(String token)

Sets the registration token of the device to which the message should be sent.  

##### Parameters

| token | A valid device registration token. |
|-------|------------------------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setTopic**
(String topic)

Sets the name of the FCM topic to which the message should be sent. Topic names may
contain the `/topics/` prefix.  

##### Parameters

| topic | A valid topic name. |
|-------|---------------------|

##### Returns

- This builder.  

#### public [Message.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder)
**setWebpushConfig**
([WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) webpushConfig)

Sets the Webpush-specific information to be included in the message.  

##### Parameters

| webpushConfig | A [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) instance. |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.