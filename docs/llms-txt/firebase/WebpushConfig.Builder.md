# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder.md.txt

# WebpushConfig.Builder

public static class **WebpushConfig.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder#build())() Creates a new [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) instance from the parameters set on this builder.                                                                                           |
| [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder) | [putAllData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>))(Map\<String, String\> map) Adds all the key-value pairs in the given map as Webpush data fields.                                                                                                                              |
| [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder) | [putAllHeaders](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder#putAllHeaders(java.util.Map<java.lang.String, java.lang.String>))(Map\<String, String\> map) Adds all the key-value pairs in the given map as Webpush headers.                                                                                                                            |
| [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder) | [putData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder#putData(java.lang.String, java.lang.String))(String key, String value) Sets the given key-value pair as a Webpush data field.                                                                                                                                                                   |
| [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder) | [putHeader](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder#putHeader(java.lang.String, java.lang.String))(String key, String value) Adds the given key-value pair as a Webpush HTTP header.                                                                                                                                                              |
| [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder) | [setFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder#setFcmOptions(com.google.firebase.messaging.WebpushFcmOptions))([WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions) fcmOptions) Sets the Webpush FCM options to be included in the Webpush config.       |
| [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder) | [setNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder#setNotification(com.google.firebase.messaging.WebpushNotification))([WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification) notification) Sets the Webpush notification to be included in the message. |

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

#### public [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig)
**build**
()

Creates a new [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) instance from the parameters set on this builder.  

##### Returns

- A new [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder)
**putAllData**
(Map\<String, String\> map)

Adds all the key-value pairs in the given map as Webpush data fields. When set, overrides any
data fields set using the methods [putData(String, String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putData(java.lang.String, java.lang.String)) and
[putAllData(Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>)).  

##### Parameters

| map | A non-null map of data values. Map must not contain null keys or values. |
|-----|--------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder)
**putAllHeaders**
(Map\<String, String\> map)

Adds all the key-value pairs in the given map as Webpush headers. Refer to
[Webpush specification](https://tools.ietf.org/html/rfc8030#section-5)
for supported headers.  

##### Parameters

| map | A non-null map of header values. Map must not contain null keys or values. |
|-----|----------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder)
**putData**
(String key, String value)

Sets the given key-value pair as a Webpush data field. When set, overrides any data fields
set using the methods [putData(String, String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putData(java.lang.String, java.lang.String)) and
[putAllData(Map)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message.Builder#putAllData(java.util.Map<java.lang.String, java.lang.String>)).  

##### Parameters

|  key  | Name of the data field. Must not be null.  |
| value | Value of the data field. Must not be null. |
|-------|--------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder)
**putHeader**
(String key, String value)

Adds the given key-value pair as a Webpush HTTP header. Refer to
[Webpush specification](https://tools.ietf.org/html/rfc8030#section-5)
for supported headers.  

##### Parameters

|  key  | Name of the header. Must not be null.  |
| value | Value of the header. Must not be null. |
|-------|----------------------------------------|

##### Returns

- This builder.  

#### public [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder)
**setFcmOptions**
([WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions) fcmOptions)

Sets the Webpush FCM options to be included in the Webpush config.  

##### Parameters

| fcmOptions | A [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions) instance. |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig.Builder)
**setNotification**
([WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification) notification)

Sets the Webpush notification to be included in the message.  

##### Parameters

| notification | A [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification) instance. |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.