# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder.md.txt

# MemoryCacheSettings.Builder

# MemoryCacheSettings.Builder


```
public class MemoryCacheSettings.Builder
```

<br />

*** ** * ** ***

A Builder for creating `MemoryCacheSettings` instance.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder#build()()` Creates a `MemoryCacheSettings` instance. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder#setGcSettings(com.google.firebase.firestore.MemoryGarbageCollectorSettings)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings gcSettings)` Uses the given garbage collector settings to configure memory cache. |

## Public methods

### build

```
public @NonNull MemoryCacheSettings build()
```

Creates a `MemoryCacheSettings` instance.

### setGcSettings

```
public @NonNull MemoryCacheSettings.Builder setGcSettings(@NonNull MemoryGarbageCollectorSettings gcSettings)
```

Uses the given garbage collector settings to configure memory cache.