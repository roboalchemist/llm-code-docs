# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.md.txt

# MemoryCacheSettings

# MemoryCacheSettings


```
class MemoryCacheSettings : LocalCacheSettings
```

<br />

*** ** * ** ***

Configures the SDK to use a memory cache. Firestore documents and mutations are NOT persisted across App restart.

To use, create an instance using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings#newBuilder()`, then set the instance to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)`, and use the built `FirebaseFirestoreSettings` instance to configure the Firestore SDK.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder` A Builder for creating `MemoryCacheSettings` instance. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings#equals(java.lang.Object)(obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryGarbageCollectorSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings#getGarbageCollectorSettings()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryGarbageCollectorSettings` object used to configure the SDK cache. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings#hashCode()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder` with default configurations. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings#toString()()` |

## Public functions

### equals

```
fun equals(obj: Any?): Boolean
```

### getGarbageCollectorSettings

```
fun getGarbageCollectorSettings(): MemoryGarbageCollectorSettings
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryGarbageCollectorSettings` object used to configure the SDK cache.

### hashCode

```
fun hashCode(): Int
```

### newBuilder

```
java-static fun newBuilder(): MemoryCacheSettings.Builder
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder` with default configurations.

### toString

```
fun toString(): String!
```