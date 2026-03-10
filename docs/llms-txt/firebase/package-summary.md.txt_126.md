# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/package-summary.md.txt

# com.google.firebase.crashlytics

# com.google.firebase.crashlytics

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/CustomKeysAndValues` | Helper class which handles the storage and conversion to strings of key/value pairs with heterogeneous value types. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/CustomKeysAndValues.Builder` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` | The Firebase Crashlytics API provides methods to annotate and manage fatal crashes, non-fatal errors, and ANRs captured and reported to Firebase Crashlytics. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/KeyValueBuilder` | Helper class to enable convenient syntax in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).recordException(kotlin.Throwable,kotlin.Function1)` |

## Extension functions summary

|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).recordException(kotlin.Throwable,kotlin.Function1)( throwable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/KeyValueBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html )` Records a non-fatal report to send to Crashlytics with additional custom keys |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/package-summary#(com.google.firebase.crashlytics.FirebaseCrashlytics).setCustomKeys(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/KeyValueBuilder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Associates all key-value parameters with the reports |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/package-summary#(com.google.firebase.Firebase).crashlytics()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Extension functions

### recordException

```
fun FirebaseCrashlytics.recordException(
    throwable: Throwable,
    init: KeyValueBuilder.() -> Unit
): Unit
```

Records a non-fatal report to send to Crashlytics with additional custom keys

### setCustomKeys

```
fun FirebaseCrashlytics.setCustomKeys(init: KeyValueBuilder.() -> Unit): Unit
```

Associates all key-value parameters with the reports

## Extension properties

### crashlytics

```
val Firebase.crashlytics: FirebaseCrashlytics
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/crashlytics/FirebaseCrashlytics` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.