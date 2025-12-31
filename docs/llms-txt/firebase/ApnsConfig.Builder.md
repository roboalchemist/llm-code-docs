# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder.md.txt

# ApnsConfig.Builder

public static class **ApnsConfig.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#build())() Creates a new [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) instance from the parameters set on this builder.                                                                                                                                                                                                                                                                                                                                            |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [putAllCustomData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#putAllCustomData(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> map) Adds all the key-value pairs in the given map as APNS custom data fields.                                                                                                                                                                                                                                                                                                                                                         |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [putAllHeaders](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#putAllHeaders(java.util.Map<java.lang.String, java.lang.String>))(Map\<String, String\> map) Adds all the key-value pairs in the given map as APNS headers.                                                                                                                                                                                                                                                                                                                                                                          |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [putCustomData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#putCustomData(java.lang.String, java.lang.Object))(String key, Object value) Adds the given key-value pair as an APNS custom data field.                                                                                                                                                                                                                                                                                                                                                                                             |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [putHeader](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#putHeader(java.lang.String, java.lang.String))(String key, String value) Adds the given key-value pair as an APNS header.                                                                                                                                                                                                                                                                                                                                                                                                                |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [setAps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#setAps(com.google.firebase.messaging.Aps))([Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps) aps) Sets the aps dictionary of the APNS message.                                                                                                                                                                                                                                                                                                                                       |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [setFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#setFcmOptions(com.google.firebase.messaging.ApnsFcmOptions))([ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) apnsFcmOptions) Sets the [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions), which will override values set in the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) for APNS messages. |
| [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder) | [setLiveActivityToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder#setLiveActivityToken(java.lang.String))(String liveActivityToken) Sets the Live Activity token.                                                                                                                                                                                                                                                                                                                                                                                                                               |

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

#### public [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig)
**build**
()

Creates a new [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) instance from the parameters set on this builder.  

##### Returns

- A new [ApnsConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**putAllCustomData**
(Map\<String, Object\> map)

Adds all the key-value pairs in the given map as APNS custom data fields.  

##### Parameters

| map | A non-null map. Map must not contain null keys or values. |
|-----|-----------------------------------------------------------|

##### Returns

- This builder.  

#### public [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**putAllHeaders**
(Map\<String, String\> map)

Adds all the key-value pairs in the given map as APNS headers.  

##### Parameters

| map | A non-null map of headers. Map must not contain null keys or values. |
|-----|----------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**putCustomData**
(String key, Object value)

Adds the given key-value pair as an APNS custom data field.  

##### Parameters

|  key  | Name of the data field. Must not be null.  |
| value | Value of the data field. Must not be null. |
|-------|--------------------------------------------|

##### Returns

- This builder.  

#### public [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**putHeader**
(String key, String value)

Adds the given key-value pair as an APNS header.  

##### Parameters

|  key  | Name of the header field. Must not be null.  |
| value | Value of the header field. Must not be null. |
|-------|----------------------------------------------|

##### Returns

- This builder.  

#### public [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**setAps**
([Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps) aps)

Sets the aps dictionary of the APNS message.  

##### Parameters

| aps | A non-null instance of [Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps). |
|-----|----------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**setFcmOptions**
([ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions) apnsFcmOptions)

Sets the [ApnsFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsFcmOptions), which will override values set in the [FcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/FcmOptions) for
APNS messages.  

#### public [ApnsConfig.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApnsConfig.Builder)
**setLiveActivityToken**
(String liveActivityToken)

Sets the Live Activity token.  

##### Parameters

| liveActivityToken | Live Activity token. |
|-------------------|----------------------|

##### Returns

- This builder.