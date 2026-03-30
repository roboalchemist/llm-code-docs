# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder.md.txt

# FirebaseOptions.Builder

# FirebaseOptions.Builder


```
class FirebaseOptions.Builder
```

<br />

*** ** * ** ***

Builder for constructing FirebaseOptions.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#Builder()()` Constructs an empty builder. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#Builder(com.google.firebase.FirebaseOptions)(options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)` Initializes the builder's values from the options object. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#build()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setApiKey(java.lang.String)(apiKey: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setApplicationId(java.lang.String)(applicationId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setDatabaseUrl(java.lang.String)(databaseUrl: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setGcmSenderId(java.lang.String)(gcmSenderId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setProjectId(java.lang.String)(projectId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String)(storageBucket: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` |

## Public constructors

### Builder

```
Builder()
```

Constructs an empty builder.

### Builder

```
Builder(options: FirebaseOptions)
```

Initializes the builder's values from the options object.

The new builder is not backed by this objects values, that is changes made to the new builder don't change the values of the origin object.

## Public functions

### build

```
fun build(): FirebaseOptions
```

### setApiKey

```
fun setApiKey(apiKey: String): FirebaseOptions.Builder
```

### setApplicationId

```
fun setApplicationId(applicationId: String): FirebaseOptions.Builder
```

### setDatabaseUrl

```
fun setDatabaseUrl(databaseUrl: String?): FirebaseOptions.Builder
```

### setGcmSenderId

```
fun setGcmSenderId(gcmSenderId: String?): FirebaseOptions.Builder
```

### setProjectId

```
fun setProjectId(projectId: String?): FirebaseOptions.Builder
```

### setStorageBucket

```
fun setStorageBucket(storageBucket: String?): FirebaseOptions.Builder
```