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

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#hashCode()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder` with default configurations. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#toString()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings#sizeBytes()` |

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
java-static fun newBuilder(): MemoryLruGcSettings.Builder
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder` with default configurations.

### toString

```
fun toString(): String
```

## Public properties

### sizeBytes

```
val sizeBytes: Long
```