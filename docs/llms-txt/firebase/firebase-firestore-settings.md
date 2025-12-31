# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings.md.txt

# Firebase.Firestore.FirebaseFirestoreSettings Class Reference

# Firebase.Firestore.FirebaseFirestoreSettings

Settings used to configure a [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) instance.

## Summary

|                                                                                                                                                                                                                                                                                   ### Public static attributes                                                                                                                                                                                                                                                                                   ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CacheSizeUnlimited](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1aa27ed85eb86c8bb8bbd220e752bf923a)` = SettingsProxy.kCacheSizeUnlimited` | `readonly long` Constant to use when setting [FirebaseFirestoreSettings.CacheSizeBytes](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1a2859ffcf1acad31d0d33dc4c72c7e438) to disable garbage collection. |

|                                                                                                                                                                                          ### Properties                                                                                                                                                                                          ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CacheSizeBytes](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1a2859ffcf1acad31d0d33dc4c72c7e438)     | `long` Sets an approximate cache size threshold for the on-disk data.                                                                                               |
| [Host](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1a930ebf0a2af0328789bf5ccf48dcb4b3)               | `string` The host of the Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) backend. |
| [PersistenceEnabled](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1a00ff0b31f311b18ad2ac2a327e4324d9) | `bool` Whether or not to use local persistence storage.                                                                                                             |
| [SslEnabled](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1abfcc256c8d70077d0ea45489198f934d)         | `bool` Whether or not to use SSL for communication.                                                                                                                 |

|                                                                                                           ### Public functions                                                                                                           ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| [ToString](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1aa5a108acae866094c2dfa2a0a0ce1b4d)`()` | `override string` |

## Public static attributes

### CacheSizeUnlimited

```c#
readonly long CacheSizeUnlimited = SettingsProxy.kCacheSizeUnlimited
```  
Constant to use when setting [FirebaseFirestoreSettings.CacheSizeBytes](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore-settings#class_firebase_1_1_firestore_1_1_firebase_firestore_settings_1a2859ffcf1acad31d0d33dc4c72c7e438) to disable garbage collection.

## Properties

### CacheSizeBytes

```c#
long CacheSizeBytes
```  
Sets an approximate cache size threshold for the on-disk data.

If the cache grows beyond this size, Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

By default, collection is enabled with a cache size of 100 MB. The minimum value is 1 MB.

This property must not be modified after calling non-static methods in the owning [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) object. Attempting to do so will result in an exception.  

### Host

```c#
string Host
```  
The host of the Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) backend.

This property must not be modified after calling non-static methods in the owning [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) object. Attempting to do so will result in an exception.  

### PersistenceEnabled

```c#
bool PersistenceEnabled
```  
Whether or not to use local persistence storage.

This property must not be modified after calling non-static methods in the owning [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) object. Attempting to do so will result in an exception.  

### SslEnabled

```c#
bool SslEnabled
```  
Whether or not to use SSL for communication.

This property must not be modified after calling non-static methods in the owning [FirebaseFirestore](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore) object. Attempting to do so will result in an exception.

## Public functions

### ToString

```c#
override string ToString()
```