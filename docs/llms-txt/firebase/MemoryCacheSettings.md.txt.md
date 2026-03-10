# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.md.txt

# MemoryCacheSettings

# MemoryCacheSettings


```
public final class MemoryCacheSettings implements LocalCacheSettings
```

<br />

*** ** * ** ***

Configures the SDK to use a memory cache. Firestore documents and mutations are NOT persisted across App restart.

To use, create an instance using `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#newBuilder()`, then set the instance to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)`, and use the built `FirebaseFirestoreSettings` instance to configure the Firestore SDK.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder` A Builder for creating `MemoryCacheSettings` instance. |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#equals(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html obj)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#getGarbageCollectorSettings()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings` object used to configure the SDK cache. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#hashCode()()` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder` with default configurations. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings#toString()()` |

## Public methods

### equals

```
public boolean equals(@Nullable Object obj)
```

### getGarbageCollectorSettings

```
public @NonNull MemoryGarbageCollectorSettings getGarbageCollectorSettings()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryGarbageCollectorSettings` object used to configure the SDK cache.

### hashCode

```
public int hashCode()
```

### newBuilder

```
public static @NonNull MemoryCacheSettings.Builder newBuilder()
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings.Builder` with default configurations.

### toString

```
public String toString()
```