# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder.md.txt

# WebpushNotification.Builder

public static class **WebpushNotification.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [addAction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#addAction(com.google.firebase.messaging.WebpushNotification.Action))([WebpushNotification.Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action) action) Adds a notification action to the notification.                                              |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [addAllActions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#addAllActions(java.util.List<com.google.firebase.messaging.WebpushNotification.Action>))(List\<[WebpushNotification.Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action)\> actions) Adds all the actions in the given list to the notification. |
| [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#build())() Creates a new [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification) from the parameters set on this builder.                                                                                                                           |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [putAllCustomData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#putAllCustomData(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> fields) Puts all the key-value pairs in the specified map to the notification.                                                                                                                                                 |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [putCustomData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#putCustomData(java.lang.String, java.lang.Object))(String key, Object value) Puts a custom key-value pair to the notification.                                                                                                                                                                                               |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setBadge](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setBadge(java.lang.String))(String badge) Sets the URL of the image used to represent the notification when there is not enough space to display the notification itself.                                                                                                                                                         |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setBody](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setBody(java.lang.String))(String body) Sets the body text of the notification.                                                                                                                                                                                                                                                    |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setData(java.lang.Object))(Object data) Sets any arbitrary data that should be associated with the notification.                                                                                                                                                                                                                   |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setDirection](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setDirection(com.google.firebase.messaging.WebpushNotification.Direction))([WebpushNotification.Direction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Direction) direction) Sets the direction in which to display the notification.                   |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setIcon](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setIcon(java.lang.String))(String icon) Sets the URL to the icon of the notification.                                                                                                                                                                                                                                              |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setImage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setImage(java.lang.String))(String image) Sets the URL of an image to be displayed in the notification.                                                                                                                                                                                                                           |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setLanguage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setLanguage(java.lang.String))(String language) Sets the language of the notification.                                                                                                                                                                                                                                         |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setRenotify](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setRenotify(boolean))(boolean renotify) Sets whether the user should be notified after a new notification replaces an old one.                                                                                                                                                                                                 |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setRequireInteraction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setRequireInteraction(boolean))(boolean requireInteraction) Sets whether a notification should remain active until the user clicks or dismisses it, rather than closing automatically.                                                                                                                               |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setSilent](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setSilent(boolean))(boolean silent) Sets whether the notification should be silent.                                                                                                                                                                                                                                              |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setTag](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setTag(java.lang.String))(String tag) Sets an identifying tag on the notification.                                                                                                                                                                                                                                                  |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setTimestampMillis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setTimestampMillis(long))(long timestampMillis) Sets a timestamp value in milliseconds on the notification.                                                                                                                                                                                                             |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setTitle](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setTitle(java.lang.String))(String title) Sets the title text of the notification.                                                                                                                                                                                                                                                |
| [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [setVibrate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder#setVibrate(int[]))(int\[\] pattern) Sets a vibration pattern for the device's vibration hardware to emit when the notification fires.                                                                                                                                                                                           |

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

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**addAction**
([WebpushNotification.Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action) action)

Adds a notification action to the notification.  

##### Parameters

| action | A non-null [WebpushNotification.Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action). |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**addAllActions**
(List\<[WebpushNotification.Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action)\> actions)

Adds all the actions in the given list to the notification.  

##### Parameters

| actions | A non-null list of actions. |
|---------|-----------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification)
**build**
()

Creates a new [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification) from the parameters set on this builder.  

##### Returns

- A new [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification) instance.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**putAllCustomData**
(Map\<String, Object\> fields)

Puts all the key-value pairs in the specified map to the notification.  

##### Parameters

| fields | A non-null map. Map must not contain null keys or values. |
|--------|-----------------------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**putCustomData**
(String key, Object value)

Puts a custom key-value pair to the notification.  

##### Parameters

|  key  |           A non-null key.            |
| value | A non-null, json-serializable value. |
|-------|--------------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setBadge**
(String badge)

Sets the URL of the image used to represent the notification when there is
not enough space to display the notification itself.  

##### Parameters

| badge | Badge URL. |
|-------|------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setBody**
(String body)

Sets the body text of the notification.  

##### Parameters

| body | Body text. |
|------|------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setData**
(Object data)

Sets any arbitrary data that should be associated with the notification.  

##### Parameters

| data | A JSON-serializable object. |
|------|-----------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setDirection**
([WebpushNotification.Direction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Direction) direction)

Sets the direction in which to display the notification.  

##### Parameters

| direction | Direction enum value. |
|-----------|-----------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setIcon**
(String icon)

Sets the URL to the icon of the notification.  

##### Parameters

| icon | Icon URL. |
|------|-----------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setImage**
(String image)

Sets the URL of an image to be displayed in the notification.  

##### Parameters

| image | Image URL |
|-------|-----------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setLanguage**
(String language)

Sets the language of the notification.  

##### Parameters

| language | Notification language. |
|----------|------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setRenotify**
(boolean renotify)

Sets whether the user should be notified after a new notification replaces an old one.  

##### Parameters

| renotify | true to notify the user on replacement. |
|----------|-----------------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setRequireInteraction**
(boolean requireInteraction)

Sets whether a notification should remain active until the user clicks or dismisses it,
rather than closing automatically.  

##### Parameters

| requireInteraction | true to keep the notification active until user interaction. |
|--------------------|--------------------------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setSilent**
(boolean silent)

Sets whether the notification should be silent.  

##### Parameters

| silent | true to indicate that the notification should be silent. |
|--------|----------------------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setTag**
(String tag)

Sets an identifying tag on the notification.  

##### Parameters

| tag | A tag to be associated with the notification. |
|-----|-----------------------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setTimestampMillis**
(long timestampMillis)

Sets a timestamp value in milliseconds on the notification.  

##### Parameters

| timestampMillis | A timestamp value as a number. |
|-----------------|--------------------------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setTitle**
(String title)

Sets the title text of the notification.  

##### Parameters

| title | Title text. |
|-------|-------------|

##### Returns

- This builder.  

#### public [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**setVibrate**
(int\[\] pattern)

Sets a vibration pattern for the device's vibration hardware to emit
when the notification fires.  

##### Parameters

| pattern | An integer array representing a vibration pattern. |
|---------|----------------------------------------------------|

##### Returns

- This builder.