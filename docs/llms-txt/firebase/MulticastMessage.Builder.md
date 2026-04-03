# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder.md.txt

# MulticastMessage.Builder

public static class **MulticastMessage.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [addAllTokens](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#addAllTokens(java.util.Collection<java.lang.String>))(Collection\<String\> tokens) Adds a collection of tokens to which the message should be sent.                                                                                                                                                                                                                                                  |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [addToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#addToken(java.lang.String))(String token) Adds a token to which the message should be sent.                                                                                                                                                                                                                                                                                                              |
| [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#build())() Creates a new [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) instance from the parameters set on this builder.                                                                                                                                                                                               |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [putAllData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>))(Map\<String, String\> map) Adds all the key-value pairs in the given map to the message as data fields.                                                                                                                                                                                                                                 |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [putData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#putData(java.lang.String, java.lang.String))(String key, String value) Adds the given key-value pair to the message as a data field.                                                                                                                                                                                                                                                                      |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [setAndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#setAndroidConfig(com.google.firebase.messaging.AndroidConfig))([AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) androidConfig) Sets the Android-specific information to be included in the message.                                                                                                                  |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [setApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#setApnsConfig(com.google.firebase.messaging.ApnsConfig))([ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) apnsConfig) Sets the information specific to APNS (Apple Push Notification Service).                                                                                                                                |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [setFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#setFcmOptions(com.google.firebase.messaging.FcmOptions))([FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) fcmOptions) Sets the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions), which can be overridden by the platform-specific `fcm_options` fields. |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [setNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#setNotification(com.google.firebase.messaging.Notification))([Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) notification) Sets the notification information to be included in the message.                                                                                                                            |
| [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder) | [setWebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder#setWebpushConfig(com.google.firebase.messaging.WebpushConfig))([WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) webpushConfig) Sets the Webpush-specific information to be included in the message.                                                                                                                  |

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

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**addAllTokens**
(Collection\<String\> tokens)

Adds a collection of tokens to which the message should be sent. Up to 500 tokens can be
specified on a single instance of [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage).  

##### Parameters

| tokens | Collection of Firebase device registration tokens. |
|--------|----------------------------------------------------|

##### Returns

- This builder.  

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**addToken**
(String token)

Adds a token to which the message should be sent. Up to 500 tokens can be specified on
a single instance of [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage).  

##### Parameters

| token | A non-null, non-empty Firebase device registration token. |
|-------|-----------------------------------------------------------|

##### Returns

- This builder.  

#### public [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage)
**build**
()

Creates a new [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) instance from the parameters set on this builder.  

##### Returns

- A new [MulticastMessage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**putAllData**
(Map\<String, String\> map)

Adds all the key-value pairs in the given map to the message as data fields. None of the
keys or values may be null.  

##### Parameters

| map | A non-null map of data fields. Map must not contain null keys or values. |
|-----|--------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
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

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**setAndroidConfig**
([AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) androidConfig)

Sets the Android-specific information to be included in the message.  

##### Parameters

| androidConfig | An [AndroidConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/AndroidConfig) instance. |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**setApnsConfig**
([ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) apnsConfig)

Sets the information specific to APNS (Apple Push Notification Service).  

##### Parameters

| apnsConfig | An [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) instance. |
|------------|-------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**setFcmOptions**
([FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) fcmOptions)

Sets the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions), which can be overridden by the platform-specific `fcm_options` fields.  

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**setNotification**
([Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) notification)

Sets the notification information to be included in the message.  

##### Parameters

| notification | A [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) instance. |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [MulticastMessage.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/MulticastMessage.Builder)
**setWebpushConfig**
([WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) webpushConfig)

Sets the Webpush-specific information to be included in the message.  

##### Parameters

| webpushConfig | A [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) instance. |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.