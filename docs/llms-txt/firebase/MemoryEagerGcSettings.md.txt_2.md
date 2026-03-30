# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings.md.txt

# MemoryEagerGcSettings

# MemoryEagerGcSettings


```
class MemoryEagerGcSettings : MemoryGarbageCollectorSettings
```

<br />

*** ** * ** ***

Configures the SDK to use an eager garbage collector for memory cache. The eager garbage collector will attempt to remove any documents from SDK's memory cache as soon as it is no longer used.

This is the default garbage collector unless specified explicitly otherwise.

To use, create an instance using `MemoryEagerGcSettings#newBuilder().build()`, then set the instance to `MemoryCacheSettings.Builder#setGcSettings`, and use the built `
MemoryCacheSettings` instance to configure the Firestore SDK.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings.Builder` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings#equals(java.lang.Object)(obj: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings#hashCode()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings#newBuilder()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryEagerGcSettings#toString()()` |

## Public functions

### equals

```
fun equals(obj: Any?): Boolean
```

### hashCode

```
fun hashCode(): Int
```

### newBuilder

```
java-static fun newBuilder(): MemoryEagerGcSettings.Builder
```

### toString

```
fun toString(): String
```