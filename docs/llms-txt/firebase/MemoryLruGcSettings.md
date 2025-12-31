# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.md.txt

# MemoryLruGcSettings

# MemoryLruGcSettings


```
class MemoryLruGcSettings : MemoryGarbageCollectorSettings
```

<br />

*** ** * ** ***

Configures the SDK to use a Least-Recently-Used garbage collector for memory cache.

To use, create an instance using `MemoryLruGcSettings#newBuilder().build()`, then set the instance to `MemoryCacheSettings.Builder#setGcSettings`, and use the built `
MemoryCacheSettings` instance to configure the Firestore SDK.

## Summary

|                                                                  ### Nested types                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[MemoryLruGcSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder) |

|                                                                   ### Public functions                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                       | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                           |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                               | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#hashCode())`()`                                                                                                                                                                                                       |
| `java-static `[MemoryLruGcSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder) | [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#newBuilder())`()` Returns a new instance of [MemoryLruGcSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder) with default configurations. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                         | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#toString())`()`                                                                                                                                                                                                       |

|                            ### Public properties                             |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | [sizeBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#sizeBytes()) |

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
java-staticÂ funÂ newBuilder():Â MemoryLruGcSettings.Builder
```

Returns a new instance of [MemoryLruGcSettings.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder) with default configurations.  

### toString

```
funÂ toString():Â String
```  

## Public properties

### sizeBytes

```
valÂ sizeBytes:Â Long
```