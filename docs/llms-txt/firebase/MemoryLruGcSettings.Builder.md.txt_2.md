# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder.md.txt

# MemoryLruGcSettings.Builder

# MemoryLruGcSettings.Builder


```
class MemoryLruGcSettings.Builder
```

<br />

*** ** * ** ***

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder#build()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder#setSizeBytes(long)(size: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Sets an approximate cache size threshold for the memory cache. |

## Public functions

### build

```
fun build(): MemoryLruGcSettings
```

### setSizeBytes

```
fun setSizeBytes(size: Long): MemoryLruGcSettings.Builder
```

Sets an approximate cache size threshold for the memory cache. If the cache grows beyond this size, Firestore SDK will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

A default size of 100MB (100 \* 1024 \* 1024) is used if unset. The minimum value to set is 1 MB (1024 \* 1024).

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryLruGcSettings.Builder` | this `Builder` instance. |