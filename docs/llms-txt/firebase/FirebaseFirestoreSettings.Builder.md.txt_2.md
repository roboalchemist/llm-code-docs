# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder.md.txt

# FirebaseFirestoreSettings.Builder

# FirebaseFirestoreSettings.Builder


```
class FirebaseFirestoreSettings.Builder
```

<br />

*** ** * ** ***

A Builder for creating `FirebaseFirestoreSettings`.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#Builder()()` Constructs a new `FirebaseFirestoreSettings` Builder object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#Builder(com.google.firebase.firestore.FirebaseFirestoreSettings)(settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings)` Constructs a new `FirebaseFirestoreSettings` Builder based on an existing ` FirebaseFirestoreSettings` object. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#build()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `[isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isPersistenceEnabled())()` **This function is deprecated.** Instead, build the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` instance to check the SDK cache configurations. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isSslEnabled()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)(settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LocalCacheSettings)` Specifies the cache used by the SDK. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `[setPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setPersistenceEnabled(boolean))(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` **This function is deprecated.** Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)` to configure SDK cache. <br /> |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setSslEnabled(boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Enables or disables SSL for communication. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#cacheSizeBytes()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#host()` |

## Public constructors

### Builder

```
Builder()
```

Constructs a new `FirebaseFirestoreSettings` Builder object.

### Builder

```
Builder(settings: FirebaseFirestoreSettings)
```

Constructs a new `FirebaseFirestoreSettings` Builder based on an existing `
FirebaseFirestoreSettings` object.

## Public functions

### build

```
fun build(): FirebaseFirestoreSettings
```

### isPersistenceEnabled

```
fun [isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#isPersistenceEnabled())(): Boolean
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead, build the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings` instance to check the SDK cache configurations.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | boolean indicating whether local persistent storage is enabled or not. |

### isSslEnabled

```
fun isSslEnabled(): Boolean
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | boolean indicating whether SSL is enabled or not. |

### setLocalCacheSettings

```
fun setLocalCacheSettings(settings: LocalCacheSettings): FirebaseFirestoreSettings.Builder
```

Specifies the cache used by the SDK. Available options are `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/MemoryCacheSettings`, each with different configuration options.

When unspecified, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings` will be used by default.

NOTE: Calling this setter and `setPersistenceEnabled()` or `
setCacheSizeBytes()` at the same time will throw an exception during SDK initialization. Instead, use the configuration in the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PersistentCacheSettings` object to specify the cache size.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object on which the cache settings is configured as specified by the given `settings`. |

### setPersistenceEnabled

```
fun [setPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setPersistenceEnabled(boolean))(value: Boolean): FirebaseFirestoreSettings.Builder
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setLocalCacheSettings(com.google.firebase.firestore.LocalCacheSettings)` to configure SDK cache.

Enables or disables local persistent storage. The default is to use local persistent storage.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object that uses local persistent storage as specified by the given value. |

### setSslEnabled

```
fun setSslEnabled(value: Boolean): FirebaseFirestoreSettings.Builder
```

Enables or disables SSL for communication. The default is to use SSL.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` | A settings object that uses SSL as specified by the value. |

## Public properties

### cacheSizeBytes

```
var cacheSizeBytes: Long
```

### host

```
var host: String!
```