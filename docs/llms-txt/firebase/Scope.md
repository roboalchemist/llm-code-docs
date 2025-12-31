# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Scope.md.txt

# Scope

public final class **Scope** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
The Scope options for an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).  

### Constant Summary

|-----|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int | [CROSS_DEVICE](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Scope#CROSS_DEVICE) | The [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) may get shared with the user's other devices, such as Google Home. |
| int | [ON_DEVICE](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Scope#ON_DEVICE)       | The default scope of an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).                                               |

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

## Constants

#### public static final int
**CROSS_DEVICE**

The [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
may get shared with the user's other devices, such as Google Home.  
Constant Value: 3  

#### public static final int
**ON_DEVICE**

The default scope of an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).
The [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
will stay on device and surface in Google apps.  
Constant Value: 2