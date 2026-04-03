# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata.Builder.md.txt

# Action.Metadata.Builder

public static class **Action.Metadata.Builder** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
The builder for [Action.Metadata](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata).  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------|
|   | [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata.Builder#Builder())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Action.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata.Builder) | [setUpload](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata.Builder#setUpload(boolean))(boolean uploadable) Sets whether the action can be uploaded to the cloud. |

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

## Public Methods

#### public [Action.Metadata.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Action.Metadata.Builder)
**setUpload** (boolean uploadable)

Sets whether the action can be uploaded to the cloud. The default is
`true`.