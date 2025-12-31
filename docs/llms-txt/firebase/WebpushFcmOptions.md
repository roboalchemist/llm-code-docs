# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.md.txt

# WebpushFcmOptions

public final class **WebpushFcmOptions** extends Object  
Represents options for features provided by the FCM SDK for Web.
Can be included in [WebpushConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushConfig). Instances of this class are thread-safe and immutable.  

### Nested Class Summary

|-------|---|---|---|
| class | [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder) ||   |

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions#builder())() Creates a new [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder). |
| static [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions)                 | [withLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions#withLink(java.lang.String))(String link) Creates a new `WebpushFcmOptions` using given link.                                                                                    |

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

#### public static [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder)
**builder**
()

Creates a new [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder).  

##### Returns

- An [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder) instance.  

#### public static [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions)
**withLink**
(String link)

Creates a new `WebpushFcmOptions` using given link.  

##### Parameters

| link | The link to open when the user clicks on the notification. For all URL values, HTTPS is required. |
|------|---------------------------------------------------------------------------------------------------|