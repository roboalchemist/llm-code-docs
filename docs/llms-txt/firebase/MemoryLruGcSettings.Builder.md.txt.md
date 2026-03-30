# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder.md.txt

# MemoryLruGcSettings.Builder

# MemoryLruGcSettings.Builder


```
public class MemoryLruGcSettings.Builder
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder#build()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder#setSizeBytes(long)(long size)` Sets an approximate cache size threshold for the memory cache. |

## Public methods

### build

```
public @NonNull MemoryLruGcSettings build()
```

### setSizeBytes

```
public @NonNull MemoryLruGcSettings.Builder setSizeBytes(long size)
```

Sets an approximate cache size threshold for the memory cache. If the cache grows beyond this size, Firestore SDK will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

A default size of 100MB (100 \* 1024 \* 1024) is used if unset. The minimum value to set is 1 MB (1024 \* 1024).

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryLruGcSettings.Builder` | this `Builder` instance. |