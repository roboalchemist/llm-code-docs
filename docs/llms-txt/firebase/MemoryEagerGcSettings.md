# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.md.txt

# MemoryEagerGcSettings

# MemoryEagerGcSettings


```
public final class MemoryEagerGcSettings implements MemoryGarbageCollectorSettings
```

<br />

*** ** * ** ***

Configures the SDK to use an eager garbage collector for memory cache. The eager garbage collector will attempt to remove any documents from SDK's memory cache as soon as it is no longer used.

This is the default garbage collector unless specified explicitly otherwise.

To use, create an instance using `MemoryEagerGcSettings#newBuilder().build()`, then set the instance to `MemoryCacheSettings.Builder#setGcSettings`, and use the built `
MemoryCacheSettings` instance to configure the Firestore SDK.

## Summary

|                                                                        ### Nested types                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public class `[MemoryEagerGcSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.Builder) |

|                                                                                                                   ### Public methods                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `boolean`                                                                                                                                                                                                                                              | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#equals(java.lang.Object))`(@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` obj)` |
| `int`                                                                                                                                                                                                                                                  | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#hashCode())`()`                                                                                                                                                                                                 |
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryEagerGcSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings.Builder) | [newBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#newBuilder())`()`                                                                                                                                                                                             |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                         | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryEagerGcSettings#toString())`()`                                                                                                                                                                                                 |

## Public methods

### equals

```
publicÂ booleanÂ equals(@Nullable ObjectÂ obj)
```  

### hashCode

```
publicÂ intÂ hashCode()
```  

### newBuilder

```
publicÂ staticÂ @NonNull MemoryEagerGcSettings.BuilderÂ newBuilder()
```  

### toString

```
publicÂ @NonNull StringÂ toString()
```