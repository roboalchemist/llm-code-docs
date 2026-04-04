# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder.md.txt

# MemoryCacheSettings.Builder

# MemoryCacheSettings.Builder


```
class MemoryCacheSettings.Builder
```

<br />

*** ** * ** ***

A Builder for creating `MemoryCacheSettings` instance.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder#build()()` Creates a `MemoryCacheSettings` instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings.Builder#setGcSettings(com.google.firebase.firestore.MemoryGarbageCollectorSettings)(gcSettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryGarbageCollectorSettings)` Uses the given garbage collector settings to configure memory cache. |

## Public functions

### build

```
fun build(): MemoryCacheSettings
```

Creates a `MemoryCacheSettings` instance.

### setGcSettings

```
fun setGcSettings(gcSettings: MemoryGarbageCollectorSettings): MemoryCacheSettings.Builder
```

Uses the given garbage collector settings to configure memory cache.