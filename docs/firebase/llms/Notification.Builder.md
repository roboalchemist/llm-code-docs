# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder.md.txt

# Notification.Builder

public static class **Notification.Builder** extends Object  

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder#build())() Creates a new [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) instance from the parameters set on this builder. |
| [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder) | [setBody](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder#setBody(java.lang.String))(String body) Sets the body of the notification.                                                                                                                          |
| [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder) | [setImage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder#setImage(java.lang.String))(String imageUrl) Sets the URL of the image that is going to be displayed in the notification.                                                                          |
| [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder) | [setTitle](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder#setTitle(java.lang.String))(String title) Sets the title of the notification.                                                                                                                      |

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

#### public [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification)
**build**
()

Creates a new [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) instance from the parameters set on this builder.  

##### Returns

- A new [Notification](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification) instance.  

##### Throws

| IllegalArgumentException | If any of the parameters set on the builder are invalid. |
|--------------------------|----------------------------------------------------------|

#### public [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder)
**setBody**
(String body)

Sets the body of the notification.  

##### Parameters

| body | Body of the notification. |
|------|---------------------------|

##### Returns

- This builder.  

#### public [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder)
**setImage**
(String imageUrl)

Sets the URL of the image that is going to be displayed in the notification.  

##### Parameters

| imageUrl | URL of the image that is going to be displayed in the notification. |
|----------|---------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [Notification.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/Notification.Builder)
**setTitle**
(String title)

Sets the title of the notification.  

##### Parameters

| title | Title of the notification. |
|-------|----------------------------|

##### Returns

- This builder.