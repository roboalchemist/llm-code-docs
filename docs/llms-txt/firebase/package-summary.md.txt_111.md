# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/package-summary.md.txt

# com.google.firebase

# com.google.firebase

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The entry point of Firebase SDKs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` | Configurable Firebase options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder` | Builder for constructing FirebaseOptions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` | A Timestamp represents a point in time independent of any time zone or calendar. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseNetworkException` | Exception thrown when a request to a Firebase service has failed due to a network error. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseTooManyRequestsException` | Exception thrown when a request to a Firebase service has been blocked due to having received too many consecutive requests from the same device. |

## Objects

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase` | Single access point to all firebase SDKs from Kotlin. |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/package-summary#(com.google.firebase.Firebase).app(kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a named firebase app instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/package-summary#(com.google.firebase.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String)( context: https://developer.android.com/reference/kotlin/android/content/Context.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions, name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Initializes and returns a FirebaseApp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/package-summary#(com.google.firebase.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions)(context: https://developer.android.com/reference/kotlin/android/content/Context.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)` Initializes and returns a FirebaseApp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/package-summary#(com.google.firebase.Firebase).initialize(android.content.Context)(context: https://developer.android.com/reference/kotlin/android/content/Context.html)` Initializes and returns a FirebaseApp. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/package-summary#(com.google.firebase.Firebase).app()` Returns the default firebase app instance. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/package-summary#(com.google.firebase.Firebase).options()` Returns options of default FirebaseApp |

## Extension functions

### app

```
fun Firebase.app(name: String): FirebaseApp
```

Returns a named firebase app instance.

### initialize

```
fun Firebase.initialize(
    context: Context,
    options: FirebaseOptions,
    name: String
): FirebaseApp
```

Initializes and returns a FirebaseApp.

### initialize

```
fun Firebase.initialize(context: Context, options: FirebaseOptions): FirebaseApp
```

Initializes and returns a FirebaseApp.

### initialize

```
fun Firebase.initialize(context: Context): FirebaseApp?
```

Initializes and returns a FirebaseApp.

## Extension properties

### app

```
val Firebase.app: FirebaseApp
```

Returns the default firebase app instance.

### options

```
val Firebase.options: FirebaseOptions
```

Returns options of default FirebaseApp