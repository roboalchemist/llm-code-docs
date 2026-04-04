# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/package-summary.md.txt

# com.google.firebase.appcheck

# com.google.firebase.appcheck

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider` | Interface for a provider that generates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken`s. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory` | Interface for a factory that generates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider`s. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` |   |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` | Class to hold tokens emitted by the Firebase App Check service which are minted upon a successful application verification. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` |   |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/package-summary#(com.google.firebase.Firebase).appCheck(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/package-summary#(com.google.firebase.appcheck.AppCheckToken).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide token. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/package-summary#(com.google.firebase.appcheck.AppCheckToken).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/package-summary#(com.google.firebase.Firebase).appCheck()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Extension functions

### appCheck

```
fun Firebase.appCheck(app: FirebaseApp): FirebaseAppCheck
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

### component1

```
operator fun AppCheckToken.component1(): String
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide token.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the token of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` |

### component2

```
operator fun AppCheckToken.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the expireTimeMillis of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` |

## Extension properties

### appCheck

```
val Firebase.appCheck: FirebaseAppCheck
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.