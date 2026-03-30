# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.md.txt

# FirebaseFirestoreSettings

# FirebaseFirestoreSettings


```
public final class FirebaseFirestoreSettings
```

<br />

*** ** * ** ***

Settings used to configure a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore` instance.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` A Builder for creating `FirebaseFirestoreSettings`. |

| ### Constants |
|---|---|
| `static final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#CACHE_SIZE_UNLIMITED() = -1` Constant to use with `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long)` to disable garbage collection. |

| ### Public fields |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LocalCacheSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#cacheSettings()` |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#cacheSizeBytes()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#host()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LocalCacheSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()()` Returns the cache settings configured for the SDK. |
| `long` | `[getCacheSizeBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSizeBytes())()` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()` to check cache size. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getHost()()` Returns the host of the Cloud Firestore backend. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#hashCode()()` |
| `boolean` | `[isPersistenceEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#isPersistenceEnabled())()` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()` to check which cache is used. <br /> |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#isSslEnabled()()` Returns whether or not to use SSL for communication. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#toString()()` |

## Constants

### CACHE_SIZE_UNLIMITED

```
public static final long CACHE_SIZE_UNLIMITED = -1
```

Constant to use with `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long)` to disable garbage collection.

## Public fields

### cacheSettings

```
public LocalCacheSettings cacheSettings
```

### cacheSizeBytes

```
public final long cacheSizeBytes
```

### host

```
public final String host
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### getCacheSettings

```
public @Nullable LocalCacheSettings getCacheSettings()
```

Returns the cache settings configured for the SDK. Returns null if it is not configured, in which case a default `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` instance is used.

### getCacheSizeBytes

```
public long [getCacheSizeBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSizeBytes())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()` to check cache size.

Returns the threshold for the cache size above which the SDK will attempt to collect the least recently used documents.

### getHost

```
public @NonNull String getHost()
```

Returns the host of the Cloud Firestore backend.

### hashCode

```
public int hashCode()
```

### isPersistenceEnabled

```
public boolean [isPersistenceEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#isPersistenceEnabled())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()` to check which cache is used.

Returns whether or not to use local persistent storage.

### isSslEnabled

```
public boolean isSslEnabled()
```

Returns whether or not to use SSL for communication.

### toString

```
public @NonNull String toString()
```