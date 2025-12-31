# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder.md.txt

# Aps.Builder

public static class **Aps.Builder** extends Object  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#build())() Builds a new [Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps) instance from the fields set on this builder.                                                                             |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [putAllCustomData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#putAllCustomData(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> fields) Puts all the key-value pairs in the specified map to the aps dictionary.                                                                     |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [putCustomData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#putCustomData(java.lang.String, java.lang.Object))(String key, Object value) Puts a custom key-value pair to the aps dictionary.                                                                                                                   |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setAlert(com.google.firebase.messaging.ApsAlert))([ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert) alert) Sets the alert as a dictionary.                                             |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setAlert(java.lang.String))(String alert) Sets the alert field as a string.                                                                                                                                                                             |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setBadge](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setBadge(int))(int badge) Sets the badge to be displayed with the message.                                                                                                                                                                              |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setCategory](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setCategory(java.lang.String))(String category) Sets the notification type.                                                                                                                                                                          |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setContentAvailable](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setContentAvailable(boolean))(boolean contentAvailable) Specifies whether to configure a background update notification.                                                                                                                     |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setMutableContent](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setMutableContent(boolean))(boolean mutableContent) Specifies whether to set the `mutable-content` property on the message.                                                                                                                    |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setSound(java.lang.String))(String sound) Sets the sound to be played with the message.                                                                                                                                                                 |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setSound(com.google.firebase.messaging.CriticalSound))([CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound) sound) Sets the critical alert sound to be played with the message. |
| [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder) | [setThreadId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setThreadId(java.lang.String))(String threadId) Sets an app-specific identifier for grouping notifications.                                                                                                                                          |

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

#### public [Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps)
**build**
()

Builds a new [Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps) instance from the fields set on this builder.  

##### Returns

- A non-null [Aps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps).  

##### Throws

| IllegalArgumentException | If the alert is specified both as an object and a string. Or if the same field is set both using a setter method, and as a custom field. |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**putAllCustomData**
(Map\<String, Object\> fields)

Puts all the key-value pairs in the specified map to the aps dictionary.  

##### Parameters

| fields | A non-null map. Map must not contain null keys or values. |
|--------|-----------------------------------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**putCustomData**
(String key, Object value)

Puts a custom key-value pair to the aps dictionary.  

##### Parameters

|  key  |           A non-null key.            |
| value | A non-null, json-serializable value. |
|-------|--------------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setAlert**
([ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert) alert)

Sets the alert as a dictionary.  

##### Parameters

| alert | An instance of [ApsAlert](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/ApsAlert). |
|-------|------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setAlert**
(String alert)

Sets the alert field as a string.  

##### Parameters

| alert | A string alert. |
|-------|-----------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setBadge**
(int badge)

Sets the badge to be displayed with the message. Set to 0 to remove the badge. When not
invoked, the badge will remain unchanged.  

##### Parameters

| badge | An integer representing the badge. |
|-------|------------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setCategory**
(String category)

Sets the notification type.  

##### Parameters

| category | A string identifier. |
|----------|----------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setContentAvailable**
(boolean contentAvailable)

Specifies whether to configure a background update notification.  

##### Parameters

| contentAvailable | True to perform a background update. |
|------------------|--------------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setMutableContent**
(boolean mutableContent)

Specifies whether to set the `mutable-content` property on the message. When set, this
property allows clients to modify the notification via app extensions.  

##### Parameters

| mutableContent | True to make the content mutable via app extensions. |
|----------------|------------------------------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setSound**
(String sound)

Sets the sound to be played with the message. For critical alerts use the
[setSound(CriticalSound)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder#setSound(com.google.firebase.messaging.CriticalSound)) method.  

##### Parameters

| sound | Sound file name or `"default"`. |
|-------|---------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setSound**
([CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound) sound)

Sets the critical alert sound to be played with the message.  

##### Parameters

| sound | A [CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound) instance containing the alert sound configuration. |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Aps.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Aps.Builder)
**setThreadId**
(String threadId)

Sets an app-specific identifier for grouping notifications.  

##### Parameters

| threadId | A string identifier. |
|----------|----------------------|

##### Returns

- This builder.