# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder.md.txt

# PersistentCacheSettings.Builder

# PersistentCacheSettings.Builder


```
public class PersistentCacheSettings.Builder
```

<br />

*** ** * ** ***

A Builder for creating `PersistentCacheSettings` instance.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder#build()()` Creates a `PersistentCacheSettings` instance from this builder instance. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder#setSizeBytes(long)(long sizeBytes)` Sets an approximate cache size threshold for the on-disk data. |

## Public methods

### build

```
public @NonNull PersistentCacheSettings build()
```

Creates a `PersistentCacheSettings` instance from this builder instance.

### setSizeBytes

```
public @NonNull PersistentCacheSettings.Builder setSizeBytes(long sizeBytes)
```

Sets an approximate cache size threshold for the on-disk data. If the cache grows beyond this size, Firestore SDK will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

By default, collection is enabled with a cache size of 100 MB. The minimum value is 1 MB.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings.Builder` | A settings object on which the cache size is configured as specified by the given `value`. |