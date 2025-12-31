# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.md.txt

# WebpushNotification

public class **WebpushNotification** extends Object  
Represents the Webpush-specific notification options that can be included in a [Message](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Message).
Instances of this class are thread-safe and immutable. Supports most standard options defined
in the [Web
Notification specification](https://developer.mozilla.org/en-US/docs/Web/API/notification/Notification).  

### Nested Class Summary

|-------|---|---|-----------------------------------------------------------------------------|
| class | [WebpushNotification.Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action) || Represents an action available to users when the notification is presented. |
| class | [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) ||                                                                             |
| enum  | [WebpushNotification.Direction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Direction) || Different directions a notification can be displayed in.                    |

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification#WebpushNotification(java.lang.String, java.lang.String))(String title, String body) Creates a new notification with the given title and body.                                      |
|   | [WebpushNotification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification#WebpushNotification(java.lang.String, java.lang.String, java.lang.String))(String title, String body, String icon) Creates a new notification with the given title, body and icon. |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification#builder())() Creates a new [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder). |

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

## Public Constructors

#### public
**WebpushNotification**
(String title, String body)

Creates a new notification with the given title and body. Overrides the options set via
[Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification).  

##### Parameters

| title | Title of the notification. |
| body  | Body of the notification.  |
|-------|----------------------------|

#### public
**WebpushNotification**
(String title, String body, String icon)

Creates a new notification with the given title, body and icon. Overrides the options set via
[Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification).  

##### Parameters

| title |   Title of the notification.   |
| body  |   Body of the notification.    |
| icon  | URL to the notifications icon. |
|-------|--------------------------------|

## Public Methods

#### public static [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder)
**builder**
()

Creates a new [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder).  

##### Returns

- A [WebpushNotification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Builder) instance.