# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary.md.txt

# com.google.firebase.functions

# com.google.firebase.functions

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | FirebaseFunctions lets you call Cloud Functions for Firebase. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions` | Options for configuring the callable function. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder` | A builder for creating `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | A reference to a particular Callable HTTPS trigger in Cloud Functions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableResult` | The result of calling a `HttpsCallableReference` function. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse` | Represents a response from a Server-Sent Event (SSE) stream. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Message` | An event message received during the stream. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/StreamResponse.Result` | The final result of the computation, marking the end of the stream. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException` | The class for all Exceptions thrown by FirebaseFunctions. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctionsException.Code` | The set of error status codes that can be returned from a Callable HTTPS tigger. |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(kotlin.String)(regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a reference to the Callable HTTPS trigger with the given name and call options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1)(url: https://developer.android.com/reference/kotlin/java/net/URL.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a reference to the Callable HTTPS trigger with the given URL and call options. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Extension functions

### functions

```
fun Firebase.functions(app: FirebaseApp, regionOrCustomDomain: String): FirebaseFunctions
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)`.

### functions

```
fun Firebase.functions(app: FirebaseApp): FirebaseFunctions
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

### functions

```
fun Firebase.functions(regionOrCustomDomain: String): FirebaseFunctions
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(kotlin.String)`.

### getHttpsCallable

```
fun FirebaseFunctions.getHttpsCallable(name: String, init: HttpsCallableOptions.Builder.() -> Unit): HttpsCallableReference
```

Returns a reference to the Callable HTTPS trigger with the given name and call options.

### getHttpsCallableFromUrl

```
fun FirebaseFunctions.getHttpsCallableFromUrl(url: URL, init: HttpsCallableOptions.Builder.() -> Unit): HttpsCallableReference
```

Returns a reference to the Callable HTTPS trigger with the given URL and call options.

## Extension properties

### functions

```
val Firebase.functions: FirebaseFunctions
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.