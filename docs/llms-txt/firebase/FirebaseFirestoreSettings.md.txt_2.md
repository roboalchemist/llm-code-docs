# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.md.txt

# FirebaseFirestoreSettings

# FirebaseFirestoreSettings


```
class FirebaseFirestoreSettings
```

<br />

*** ** * ** ***

Settings used to configure a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore` instance.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder` A Builder for creating `FirebaseFirestoreSettings`. |

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#CACHE_SIZE_UNLIMITED() = -1` Constant to use with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long)` to disable garbage collection. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `[isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#isPersistenceEnabled())()` **This function is deprecated.** Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()` to check which cache is used. <br /> |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#isSslEnabled()()` Returns whether or not to use SSL for communication. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#toString()()` |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/LocalCacheSettings!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#cacheSettings()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#cacheSizeBytes()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#host()` |

## Constants

### CACHE_SIZE_UNLIMITED

```
const val CACHE_SIZE_UNLIMITED = -1: Long
```

Constant to use with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings.Builder#setCacheSizeBytes(long)` to disable garbage collection.

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### hashCode

```
fun hashCode(): Int
```

### isPersistenceEnabled

```
fun [isPersistenceEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#isPersistenceEnabled())(): Boolean
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Instead, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreSettings#getCacheSettings()` to check which cache is used.

Returns whether or not to use local persistent storage.

### isSslEnabled

```
fun isSslEnabled(): Boolean
```

Returns whether or not to use SSL for communication.

### toString

```
fun toString(): String
```

## Public properties

### cacheSettings

```
val cacheSettings: LocalCacheSettings!
```

### cacheSizeBytes

```
val cacheSizeBytes: Long
```

### host

```
val host: String!
```