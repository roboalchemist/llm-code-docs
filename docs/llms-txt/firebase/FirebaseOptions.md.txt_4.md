# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.md.txt

# FirebaseOptions

# FirebaseOptions


```
class FirebaseOptions
```

<br />

*** ** * ** ***

Configurable Firebase options.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` Builder for constructing FirebaseOptions. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#fromResource(android.content.Context)(context: https://developer.android.com/reference/kotlin/android/content/Context.html)` Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` instance that is populated from string resources. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#toString()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#apiKey()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#applicationId()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#databaseUrl()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#gaTrackingId()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#gcmSenderId()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#projectId()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#storageBucket()` |

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### fromResource

```
java-static fun fromResource(context: Context): FirebaseOptions?
```

Creates a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` instance that is populated from string resources.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions?` | The populated options or null if applicationId is missing from resources. |

### hashCode

```
fun hashCode(): Int
```

### toString

```
fun toString(): String!
```

## Public properties

### apiKey

```
val apiKey: String!
```

### applicationId

```
val applicationId: String!
```

### databaseUrl

```
val databaseUrl: String!
```

### gaTrackingId

```
val gaTrackingId: String!
```

### gcmSenderId

```
val gcmSenderId: String!
```

### projectId

```
val projectId: String!
```

### storageBucket

```
val storageBucket: String!
```