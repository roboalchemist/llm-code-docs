# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.md.txt

# FunctionsKt

# FunctionsKt


```
public final class FunctionsKt
```

<br />

*** ** * ** ***

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.Firebase).functions(kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp app, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html regionOrCustomDomain )` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns a reference to the Callable HTTPS trigger with the given name and call options. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions receiver, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/net/URL.html url, @https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html Function1<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html> init )` Returns a reference to the Callable HTTPS trigger with the given URL and call options. |

## Public fields

### functions

```
public final @NonNull FirebaseFunctions functions
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

## Public methods

### FunctionsKt.functions

```
public static final @NonNull FirebaseFunctions FunctionsKt.functions(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`.

### FunctionsKt.functions

```
public static final @NonNull FirebaseFunctions FunctionsKt.functions(
    @NonNull Firebase receiver,
    @NonNull String regionOrCustomDomain
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(kotlin.String)`.

### FunctionsKt.functions

```
public static final @NonNull FirebaseFunctions FunctionsKt.functions(
    @NonNull Firebase receiver,
    @NonNull FirebaseApp app,
    @NonNull String regionOrCustomDomain
)
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions` instance of a given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)`.

### FunctionsKt.getHttpsCallable

```
public static final @NonNull HttpsCallableReference FunctionsKt.getHttpsCallable(
    @NonNull FirebaseFunctions receiver,
    @NonNull String name,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder, Unit> init
)
```

Returns a reference to the Callable HTTPS trigger with the given name and call options.

### FunctionsKt.getHttpsCallableFromUrl

```
public static final @NonNull HttpsCallableReference FunctionsKt.getHttpsCallableFromUrl(
    @NonNull FirebaseFunctions receiver,
    @NonNull URL url,
    @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder, Unit> init
)
```

Returns a reference to the Callable HTTPS trigger with the given URL and call options.