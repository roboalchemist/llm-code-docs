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

To use, create an instance using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#newBuilder()`, then set the instance to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)`, and use the built `FirebaseFirestoreSettings` instance to configure the Firestore SDK.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder` A Builder for creating `PersistentCacheSettings` instance. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#hashCode()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder` with default configurations. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#toString()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings#sizeBytes()` |

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### hashCode

```
fun hashCode(): Int
```

### newBuilder

```
java-static fun newBuilder(): PersistentCacheSettings.Builder
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings.Builder` with default configurations.

### toString

```
fun toString(): String!
```

## Public properties

### sizeBytes

```
val sizeBytes: Long
```