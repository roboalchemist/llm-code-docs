# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder.md.txt

# Indexable.Metadata.Builder

public static final class **Indexable.Metadata.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
The builder for [Indexable.Metadata](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata).  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder#Builder())() The constructor. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) | [setScope](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder#setScope(int))(int scope) Set the scope of the Indexable.                                                                                                                                                                                                               |
| [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) | [setScore](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder#setScore(int))(int score) Sets the score of the object.                                                                                                                                                                                                                 |
| [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) | [setSliceUri](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder#setSliceUri(android.net.Uri))([Uri](https://developer.android.com/reference/android/net/Uri.html) sliceUri) Set the Uri of the Slice that represents this [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable). |
| [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder) | [setWorksOffline](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder#setWorksOffline(boolean))(boolean worksOffline) Sets whether the object is available offline in the app.                                                                                                                                                         |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Public Constructors

#### public **Builder** ()

The constructor.

## Public Methods

#### public [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder)
**setScope** (int scope)

Set the scope of the Indexable. When it is not set explicitly, the default is
[Scope.ON_DEVICE](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Scope#ON_DEVICE).  

##### Parameters

| scope | It must be one of the values in [Scope](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Scope). |
|-------|------------------------------------------------------------------------------------------------------------------------------------|

#### public [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder)
**setScore** (int score)

Sets the score of the object.

The score signifies the relative importance of this compared to other objects in the
index from the app.  

##### Parameters

| score | The score. The default is zero (0), negative values are not allowed. |
|-------|----------------------------------------------------------------------|

#### public [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder)
**setSliceUri** ([Uri](https://developer.android.com/reference/android/net/Uri.html) sliceUri)

Set the Uri of the Slice that represents this [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).
Permissions needed to bind to the Slice will be automatically granted to apps that have
access to this [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
based on its [Scope](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Scope).  

##### Parameters

| sliceUri | It must be a valid [Uri](https://developer.android.com/reference/android/net/Uri.html). |
|----------|-----------------------------------------------------------------------------------------|

#### public [Indexable.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata.Builder)
**setWorksOffline** (boolean worksOffline)

Sets whether the object is available offline in the app.

Working offline means that a user is able to launch the app with the URL and
interact with the content without network connections, e.g. in airplane mode.  

##### Parameters

| worksOffline | Represents whether the object works offline. The default is `false`. |
|--------------|----------------------------------------------------------------------|