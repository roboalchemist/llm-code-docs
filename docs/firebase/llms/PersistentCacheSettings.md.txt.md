# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.md.txt

# PersistentCacheSettings

# PersistentCacheSettings


```
public final class PersistentCacheSettings implements LocalCacheSettings
```

<br />

*** ** * ** ***

Configures the SDK to use a persistent cache. Firestore documents and mutations are persisted across App restart.

This is the default cache type unless explicitly specified otherwise.

To use, create an instance using `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings#newBuilder()`, then set the instance to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)`, and use the built `FirebaseFirestoreSettings` instance to configure the Firestore SDK.

## Summary

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder` A Builder for creating `PersistentCacheSettings` instance. |

| ### Public fields |
|---|---|
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings#sizeBytes()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings#getSizeBytes()()` Returns cache size threshold for the on-disk data. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings#hashCode()()` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder` with default configurations. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings#toString()()` |

## Public fields

### sizeBytes

```
public final long sizeBytes
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### getSizeBytes

```
public long getSizeBytes()
```

Returns cache size threshold for the on-disk data. If the cache grows beyond this size, Firestore SDK will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

By default, persistent cache is enabled with a cache size of 100 MB. The minimum value is 1 MB.

### hashCode

```
public int hashCode()
```

### newBuilder

```
public static @NonNull PersistentCacheSettings.Builder newBuilder()
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder` with default configurations.

### toString

```
public String toString()
```