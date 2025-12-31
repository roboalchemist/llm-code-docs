# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.md.txt

# MemoryCacheSettings

# MemoryCacheSettings


```
public final class MemoryCacheSettings implements LocalCacheSettings
```

<br />

*** ** * ** ***

Configures the SDK to use a memory cache. Firestore documents and mutations are NOT persisted across App restart.

To use, create an instance using [newBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#newBuilder()), then set the instance to [setLocalCacheSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)), and use the built `FirebaseFirestoreSettings` instance to configure the Firestore SDK.

## Summary

|                                                                                                 ### Nested types                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public class `[MemoryCacheSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder) A Builder for creating `MemoryCacheSettings` instance. |

|                                                                                                                 ### Public methods                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `boolean`                                                                                                                                                                                                                                          | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#equals(java.lang.Object))`(@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` obj)`                                             |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryGarbageCollectorSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings)  | [getGarbageCollectorSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#getGarbageCollectorSettings())`()` Returns the [MemoryGarbageCollectorSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings) object used to configure the SDK cache. |
| `int`                                                                                                                                                                                                                                              | [hashCode](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#hashCode())`()`                                                                                                                                                                                                                                             |
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MemoryCacheSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder) | [newBuilder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#newBuilder())`()` Returns a new instance of [MemoryCacheSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder) with default configurations.                                      |
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                                                     | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#toString())`()`                                                                                                                                                                                                                                             |

## Public methods

### equals

```
publicÂ booleanÂ equals(@Nullable ObjectÂ obj)
```  

### getGarbageCollectorSettings

```
publicÂ @NonNull MemoryGarbageCollectorSettingsÂ getGarbageCollectorSettings()
```

Returns the [MemoryGarbageCollectorSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings) object used to configure the SDK cache.  

### hashCode

```
publicÂ intÂ hashCode()
```  

### newBuilder

```
publicÂ staticÂ @NonNull MemoryCacheSettings.BuilderÂ newBuilder()
```

Returns a new instance of [MemoryCacheSettings.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder) with default configurations.  

### toString

```
publicÂ StringÂ toString()
```