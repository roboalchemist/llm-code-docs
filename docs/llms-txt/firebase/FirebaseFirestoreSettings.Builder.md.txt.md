# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder.md.txt

# FirebaseFirestoreSettings.Builder

# FirebaseFirestoreSettings.Builder


```
public final class FirebaseFirestoreSettings.Builder
```

<br />

*** ** * ** ***

A Builder for creating `FirebaseFirestoreSettings`.

## Summary

| ### Public fields |
|---|---|
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#cacheSizeBytes()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#host()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#Builder()()` Constructs a new `FirebaseFirestoreSettings` Builder object. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#Builder(com.google.firebase.firestore.FirebaseFirestoreSettings)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings settings)` Constructs a new `FirebaseFirestoreSettings` Builder based on an existing ` FirebaseFirestoreSettings` object. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#build()()` |
| `long` | `[getCacheSizeBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#getCacheSizeBytes())()` **This method is deprecated.** Instead, build the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` instance to check the SDK cache configurations. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#getHost()()` |
| `boolean` | `[isPersistenceEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isPersistenceEnabled())()` **This method is deprecated.** Instead, build the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` instance to check the SDK cache configurations. <br /> |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isSslEnabled()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `[setCacheSizeBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long))(long value)` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)` to configure SDK cache. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setHost(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host)` Sets the host of the Cloud Firestore backend. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/LocalCacheSettings settings)` Specifies the cache used by the SDK. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `[setPersistenceEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setPersistenceEnabled(boolean))(boolean value)` **This method is deprecated.** Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)` to configure SDK cache. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setSslEnabled(boolean)(boolean value)` Enables or disables SSL for communication. |

## Public fields

### cacheSizeBytes

```
public long cacheSizeBytes
```

### host

```
public String host
```

## Public constructors

### Builder

```
public Builder()
```

Constructs a new `FirebaseFirestoreSettings` Builder object.

### Builder

```
public Builder(@NonNull FirebaseFirestoreSettings settings)
```

Constructs a new `FirebaseFirestoreSettings` Builder based on an existing `
FirebaseFirestoreSettings` object.

## Public methods

### build

```
public @NonNull FirebaseFirestoreSettings build()
```

### getCacheSizeBytes

```
public long [getCacheSizeBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#getCacheSizeBytes())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, build the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` instance to check the SDK cache configurations.

| Returns |
|---|---|
| `long` | cache size for on-disk data. |

### getHost

```
public @NonNull String getHost()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the host of the Cloud Firestore backend. |

### isPersistenceEnabled

```
public boolean [isPersistenceEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isPersistenceEnabled())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, build the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings` instance to check the SDK cache configurations.

| Returns |
|---|---|
| `boolean` | boolean indicating whether local persistent storage is enabled or not. |

### isSslEnabled

```
public boolean isSslEnabled()
```

| Returns |
|---|---|
| `boolean` | boolean indicating whether SSL is enabled or not. |

### setCacheSizeBytes

```
public @NonNull FirebaseFirestoreSettings.Builder [setCacheSizeBytes](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long))(long value)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)` to configure SDK cache.

Sets an approximate cache size threshold for the on-disk data. If the cache grows beyond this size, Cloud Firestore will start removing data that hasn't been recently used. The size is not a guarantee that the cache will stay below that size, only that if the cache exceeds the given size, cleanup will be attempted.

By default, collection is enabled with a cache size of 100 MB. The minimum value is 1 MB.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object on which the cache size is configured as specified by the given `value`. |

### setHost

```
public @NonNull FirebaseFirestoreSettings.Builder setHost(@NonNull String host)
```

Sets the host of the Cloud Firestore backend.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host` | The host string |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object with the host set. |

### setLocalCacheSettings

```
public @NonNull FirebaseFirestoreSettings.Builder setLocalCacheSettings(@NonNull LocalCacheSettings settings)
```

Specifies the cache used by the SDK. Available options are `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/MemoryCacheSettings`, each with different configuration options.

When unspecified, `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` will be used by default.

NOTE: Calling this setter and `setPersistenceEnabled()` or `
setCacheSizeBytes()` at the same time will throw an exception during SDK initialization. Instead, use the configuration in the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PersistentCacheSettings` object to specify the cache size.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object on which the cache settings is configured as specified by the given `settings`. |

### setPersistenceEnabled

```
public @NonNull FirebaseFirestoreSettings.Builder [setPersistenceEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setPersistenceEnabled(boolean))(boolean value)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)` to configure SDK cache.

Enables or disables local persistent storage. The default is to use local persistent storage.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object that uses local persistent storage as specified by the given value. |

### setSslEnabled

```
public @NonNull FirebaseFirestoreSettings.Builder setSslEnabled(boolean value)
```

Enables or disables SSL for communication. The default is to use SSL.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object that uses SSL as specified by the value. |