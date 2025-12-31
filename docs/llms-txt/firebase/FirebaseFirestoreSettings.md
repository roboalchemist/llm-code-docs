# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.md.txt

# FirebaseFirestoreSettings

# FirebaseFirestoreSettings


```
class FirebaseFirestoreSettings
```

<br />

*** ** * ** ***

Settings used to configure a [FirebaseFirestore](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore) instance.

## Summary

|                                                                                                  ### Nested types                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[FirebaseFirestoreSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder) A Builder for creating `FirebaseFirestoreSettings`. |

|                                    ### Constants                                     |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [CACHE_SIZE_UNLIMITED](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#CACHE_SIZE_UNLIMITED())` = -1` Constant to use with [setCacheSizeBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long)) to disable garbage collection. |

|                                ### Public functions                                |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                                                                                     |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)         | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#hashCode())`()`                                                                                                                                                                                                                                                                 |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | ~~[isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#isPersistenceEnabled())~~`()` **This function is deprecated.** Instead, use [getCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()) to check which cache is used. <br /> |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [isSslEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#isSslEnabled())`()` Returns whether or not to use SSL for communication.                                                                                                                                                                                                    |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)   | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#toString())`()`                                                                                                                                                                                                                                                                 |

|                                                    ### Public properties                                                    |
|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [LocalCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LocalCacheSettings)`!` | [cacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#cacheSettings())   |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)                                                | [cacheSizeBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#cacheSizeBytes()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                         | [host](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#host())                     |

## Constants

### CACHE_SIZE_UNLIMITED

```
constÂ valÂ CACHE_SIZE_UNLIMITED = -1:Â Long
```

Constant to use with [setCacheSizeBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long)) to disable garbage collection.  

## Public functions

### equals

```
funÂ equals(o:Â Any!):Â Boolean
```  

### hashCode

```
funÂ hashCode():Â Int
```  

### isPersistenceEnabled

```
funÂ [isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#isPersistenceEnabled())():Â Boolean
```
| **This function is deprecated.**   
|
| Instead, use [getCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()) to check which cache is used.

Returns whether or not to use local persistent storage.  

### isSslEnabled

```
funÂ isSslEnabled():Â Boolean
```

Returns whether or not to use SSL for communication.  

### toString

```
funÂ toString():Â String
```  

## Public properties

### cacheSettings

```
valÂ cacheSettings:Â LocalCacheSettings!
```  

### cacheSizeBytes

```
valÂ cacheSizeBytes:Â Long
```  

### host

```
valÂ host:Â String!
```