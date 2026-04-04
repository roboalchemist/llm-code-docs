# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.md.txt

# FirebaseFunctions

# FirebaseFunctions


```
class FirebaseFunctions
```

<br />

*** ** * ** ***

FirebaseFunctions lets you call Cloud Functions for Firebase.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance()()` Creates a Cloud Functions client with the default app. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Creates a Cloud Functions client with the given app. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(kotlin.String)(regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a Cloud Functions client with the default app and given region or custom domain. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a Cloud Functions client with the given app and region or custom domain. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallable(kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a reference to the callable HTTPS trigger with the given name. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallable(kotlin.String,com.google.firebase.functions.HttpsCallableOptions)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions)` Returns a reference to the callable HTTPS trigger with the given name and call options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallableFromUrl(java.net.URL)(url: https://developer.android.com/reference/kotlin/java/net/URL.html)` Returns a reference to the callable HTTPS trigger with the provided URL. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#getHttpsCallableFromUrl(java.net.URL,com.google.firebase.functions.HttpsCallableOptions)(url: https://developer.android.com/reference/kotlin/java/net/URL.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions)` Returns a reference to the callable HTTPS trigger with the provided URL and call options. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#useEmulator(kotlin.String,kotlin.Int)(host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Modifies this FirebaseFunctions instance to communicate with the Cloud Functions emulator. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `[useFunctionsEmulator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#useFunctionsEmulator(kotlin.String))(origin: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Use useEmulator to connect to the emulator. |

| ### Extension functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a reference to the Callable HTTPS trigger with the given name and call options. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1)(url: https://developer.android.com/reference/kotlin/java/net/URL.html, init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/HttpsCallableOptions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a reference to the Callable HTTPS trigger with the given URL and call options. |

## Public companion functions

### getInstance

```
fun getInstance(): FirebaseFunctions
```

Creates a Cloud Functions client with the default app.

### getInstance

```
fun getInstance(app: FirebaseApp): FirebaseFunctions
```

Creates a Cloud Functions client with the given app.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The app for the Firebase project. |

### getInstance

```
fun getInstance(regionOrCustomDomain: String): FirebaseFunctions
```

Creates a Cloud Functions client with the default app and given region or custom domain.

| Parameters |
|---|---|
| `regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

### getInstance

```
fun getInstance(app: FirebaseApp, regionOrCustomDomain: String): FirebaseFunctions
```

Creates a Cloud Functions client with the given app and region or custom domain.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The app for the Firebase project. |
| `regionOrCustomDomain: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

## Public functions

### getHttpsCallable

```
fun getHttpsCallable(name: String): HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the given name.

### getHttpsCallable

```
fun getHttpsCallable(name: String, options: HttpsCallableOptions): HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the given name and call options.

### getHttpsCallableFromUrl

```
fun getHttpsCallableFromUrl(url: URL): HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the provided URL.

### getHttpsCallableFromUrl

```
fun getHttpsCallableFromUrl(url: URL, options: HttpsCallableOptions): HttpsCallableReference
```

Returns a reference to the callable HTTPS trigger with the provided URL and call options.

### useEmulator

```
fun useEmulator(host: String, port: Int): Unit
```

Modifies this FirebaseFunctions instance to communicate with the Cloud Functions emulator.

Note: Call this method before using the instance to do any functions operations.

| Parameters |
|---|---|
| `host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the emulator host (for example, 10.0.2.2) |
| `port: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the emulator port (for example, 5001) |

### useFunctionsEmulator

```
fun [useFunctionsEmulator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/functions/FirebaseFunctions#useFunctionsEmulator(kotlin.String))(origin: String): Unit
```

> [!CAUTION]
> **This function is deprecated.**   
> Use useEmulator to connect to the emulator.

## Extension functions

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