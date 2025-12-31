# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder.md.txt

# WebpushFcmOptions.Builder

public static class **WebpushFcmOptions.Builder** extends Object  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder#build())() Creates a new [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions) instance from the parameters set on this builder. |
| [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder) | [setLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder#setLink(java.lang.String))(String link)                                                                                                                                                                       |

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

#### public [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions)
**build**
()

Creates a new [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions) instance from the parameters set on this builder.  

##### Returns

- A new [WebpushFcmOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions) instance.  

#### public [WebpushFcmOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushFcmOptions.Builder)
**setLink**
(String link)

<br />

##### Parameters

| link | The link to open when the user clicks on the notification. For all URL values, HTTPS is required. |
|------|---------------------------------------------------------------------------------------------------|

##### Returns

- This builder