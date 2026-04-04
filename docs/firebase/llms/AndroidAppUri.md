# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/AndroidAppUri.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri.md.txt

# AndroidAppUri

public final class **AndroidAppUri** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

Please [Migrate to the
Firebase App Indexing API](https://firebase.google.com/docs/app-indexing/android/migrate)  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                                                                                                                     | [equals](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#equals(java.lang.Object))([Object](https://developer.android.com/reference/java/lang/Object.html) object)                                                                                                                                                                                                                                                 |
| [Uri](https://developer.android.com/reference/android/net/Uri.html)                                                         | [getDeepLinkUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#getDeepLinkUri())()                                                                                                                                                                                                                                                                                                                               |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                     | [getPackageName](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#getPackageName())()                                                                                                                                                                                                                                                                                                                               |
| int                                                                                                                         | [hashCode](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#hashCode())()                                                                                                                                                                                                                                                                                                                                           |
| static [AndroidAppUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri) | [newAndroidAppUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#newAndroidAppUri(java.lang.String,%20android.net.Uri))([String](https://developer.android.com/reference/java/lang/String.html) packageName, [Uri](https://developer.android.com/reference/android/net/Uri.html) deepLink) *This method is deprecated. Please [Handling App Links](https://developer.android.com/training/app-links/index.html)* |
| static [AndroidAppUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri) | [newAndroidAppUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#newAndroidAppUri(android.net.Uri))([Uri](https://developer.android.com/reference/android/net/Uri.html) uri) *This method is deprecated. Please [Handling App Links](https://developer.android.com/training/app-links/index.html)*                                                                                                               |
| [String](https://developer.android.com/reference/java/lang/String.html)                                                     | [toString](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#toString())()                                                                                                                                                                                                                                                                                                                                           |
| [Uri](https://developer.android.com/reference/android/net/Uri.html)                                                         | [toUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri#toUri())()                                                                                                                                                                                                                                                                                                                                                 |

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

## Public Methods

#### public boolean **equals** ([Object](https://developer.android.com/reference/java/lang/Object.html) object)

#### public [Uri](https://developer.android.com/reference/android/net/Uri.html) **getDeepLinkUri** ()

##### Returns

- deep link [Uri](https://developer.android.com/reference/android/net/Uri.html) or `null`, if it does not have a deep link.  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **getPackageName** ()

##### Returns

- package name.  

#### public int **hashCode** ()

#### public static [AndroidAppUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri)
**newAndroidAppUri** ([String](https://developer.android.com/reference/java/lang/String.html) packageName, [Uri](https://developer.android.com/reference/android/net/Uri.html) deepLink)

**This method is deprecated.**   

Please [Handling App
Links](https://developer.android.com/training/app-links/index.html)  

#### public static [AndroidAppUri](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AndroidAppUri)
**newAndroidAppUri** ([Uri](https://developer.android.com/reference/android/net/Uri.html) uri)

**This method is deprecated.**   

Please [Handling App
Links](https://developer.android.com/training/app-links/index.html)  

#### public [String](https://developer.android.com/reference/java/lang/String.html) **toString** ()

#### public [Uri](https://developer.android.com/reference/android/net/Uri.html) **toUri** ()

##### Returns

- [Uri](https://developer.android.com/reference/android/net/Uri.html) form.