# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.md.txt

# FirebaseFunctions

# FirebaseFunctions


```
public final class FirebaseFunctions
```

<br />

*** ** * ** ***

FirebaseFunctions lets you call Cloud Functions for Firebase.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#getHttpsCallable(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns a reference to the callable HTTPS trigger with the given name. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#getHttpsCallable(kotlin.String,com.google.firebase.functions.HttpsCallableOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions options )` Returns a reference to the callable HTTPS trigger with the given name and call options. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#getHttpsCallableFromUrl(java.net.URL)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/net/URL.html url)` Returns a reference to the callable HTTPS trigger with the provided URL. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#getHttpsCallableFromUrl(java.net.URL,com.google.firebase.functions.HttpsCallableOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/net/URL.html url, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions options )` Returns a reference to the callable HTTPS trigger with the provided URL and call options. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance()()` Creates a Cloud Functions client with the default app. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app)` Creates a Cloud Functions client with the given app. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain)` Creates a Cloud Functions client with the default app and given region or custom domain. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain)` Creates a Cloud Functions client with the given app and region or custom domain. |
| `final void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#useEmulator(kotlin.String,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host, int port)` Modifies this FirebaseFunctions instance to communicate with the Cloud Functions emulator. |
| `final void` | `[useFunctionsEmulator](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#useFunctionsEmulator(kotlin.String))(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html origin)` **This method is deprecated.** Use useEmulator to connect to the emulator. |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns a reference to the Callable HTTPS trigger with the given name and call options. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/net/URL.html url, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns a reference to the Callable HTTPS trigger with the given URL and call options. |

## Public methods

### getHttpsCallable

```
public final @NonNull HttpsCallableReference getHttpsCallable(@NonNull String name)
```

Returns a reference to the callable HTTPS trigger with the given name.

### getHttpsCallable

```
public final @NonNull HttpsCallableReference getHttpsCallable(
    @NonNull String name,
    @NonNull HttpsCallableOptions options
)
```

Returns a reference to the callable HTTPS trigger with the given name and call options.

### getHttpsCallableFromUrl

```
public final @NonNull HttpsCallableReference getHttpsCallableFromUrl(@NonNull URL url)
```

Returns a reference to the callable HTTPS trigger with the provided URL.

### getHttpsCallableFromUrl

```
public final @NonNull HttpsCallableReference getHttpsCallableFromUrl(
    @NonNull URL url,
    @NonNull HttpsCallableOptions options
)
```

Returns a reference to the callable HTTPS trigger with the provided URL and call options.

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance()
```

Creates a Cloud Functions client with the default app.

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance(@NonNull FirebaseApp app)
```

Creates a Cloud Functions client with the given app.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The app for the Firebase project. |

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance(@NonNull String regionOrCustomDomain)
```

Creates a Cloud Functions client with the default app and given region or custom domain.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain` | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

### getInstance

```
public static final @NonNull FirebaseFunctions getInstance(@NonNull FirebaseApp app, @NonNull String regionOrCustomDomain)
```

Creates a Cloud Functions client with the given app and region or custom domain.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app` | The app for the Firebase project. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain` | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

### useEmulator

```
public final void useEmulator(@NonNull String host, int port)
```

Modifies this FirebaseFunctions instance to communicate with the Cloud Functions emulator.

Note: Call this method before using the instance to do any functions operations.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html host` | the emulator host (for example, 10.0.2.2) |
| `int port` | the emulator port (for example, 5001) |

### useFunctionsEmulator

```
public final void [useFunctionsEmulator](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions#useFunctionsEmulator(kotlin.String))(@NonNull String origin)
```

> [!CAUTION]
> **This method is deprecated.**   
> Use useEmulator to connect to the emulator.

## Extension functions

### FunctionsKt.getHttpsCallable

```
public final @NonNull HttpsCallableReference FunctionsKt.getHttpsCallable(
    @NonNull FirebaseFunctions receiver,
    @NonNull String name,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder, Unit> init
)
```

Returns a reference to the Callable HTTPS trigger with the given name and call options.

### FunctionsKt.getHttpsCallableFromUrl

```
public final @NonNull HttpsCallableReference FunctionsKt.getHttpsCallableFromUrl(
    @NonNull FirebaseFunctions receiver,
    @NonNull URL url,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder, Unit> init
)
```

Returns a reference to the Callable HTTPS trigger with the given URL and call options.