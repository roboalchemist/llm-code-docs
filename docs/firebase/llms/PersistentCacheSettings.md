# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/PersistentCacheSettings.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.md.txt

# PersistentCacheSettings

# PersistentCacheSettings


```
class PersistentCacheSettings : LocalCacheSettings
```

<br />

*** ** * ** ***

Configures the SDK to use a persistent cache. Firestore documents and mutations are persisted across App restart.

This is the default cache type unless explicitly specified otherwise.

To use, create an instance using [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#newBuilder()), then set the instance to [setLocalCacheSettings](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)), and use the built `FirebaseFirestoreSettings` instance to configure the Firestore SDK.

## Summary

|                                                                                                   ### Nested types                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[PersistentCacheSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder) A Builder for creating `PersistentCacheSettings` instance. |

|                                                                       ### Public functions                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                               | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                                   |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                       | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#hashCode())`()`                                                                                                                                                                                                               |
| `java-static `[PersistentCacheSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder) | [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#newBuilder())`()` Returns a new instance of [PersistentCacheSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder) with default configurations. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                              | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#toString())`()`                                                                                                                                                                                                               |

|                            ### Public properties                             |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [sizeBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#sizeBytes()) |

## Public functions

### equals

```
funÂ equals(o:Â Any!):Â Boolean
```  

### hashCode

```
funÂ hashCode():Â Int
```  

### newBuilder

```
java-staticÂ funÂ newBuilder():Â PersistentCacheSettings.Builder
```

Returns a new instance of [PersistentCacheSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder) with default configurations.  

### toString

```
funÂ toString():Â String!
```  

## Public properties

### sizeBytes

```
valÂ sizeBytes:Â Long
```