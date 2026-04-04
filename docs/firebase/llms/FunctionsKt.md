# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/ktx/FunctionsKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt.md.txt

# FunctionsKt

# FunctionsKt


```
public final class FunctionsKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                       ### Public fields                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) | [functions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions()) Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |

|                                                                                                               ### Public methods                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions)           | [FunctionsKt](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt)`.`[functions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` `)` Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions)           | [FunctionsKt](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt)`.`[functions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.Firebase).functions(kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` regionOrCustomDomain` `)` Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of a given [regionOrCustomDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(kotlin.String)).                                                                                                                                                                                                                                                                                                                                                                                     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions)           | [FunctionsKt](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt)`.`[functions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` regionOrCustomDomain` `)` Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [regionOrCustomDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)).     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableReference](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference) | [FunctionsKt](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt)`.`[getHttpsCallable](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallable(kotlin.String,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns a reference to the Callable HTTPS trigger with the given name and call options.     |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableReference](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableReference) | [FunctionsKt](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt)`.`[getHttpsCallableFromUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FunctionsKt#(com.google.firebase.functions.FirebaseFunctions).getHttpsCallableFromUrl(java.net.URL,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[URL](https://developer.android.com/reference/kotlin/java/net/URL.html)` url,` ` @`[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html)` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[HttpsCallableOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/HttpsCallableOptions.Builder)`, `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`> init` `)` Returns a reference to the Callable HTTPS trigger with the given URL and call options. |

## Public fields

### functions

```
publicÂ finalÂ @NonNull FirebaseFunctionsÂ functions
```

Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

## Public methods

### FunctionsKt.functions

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsÂ FunctionsKt.functions(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app
)
```

Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### FunctionsKt.functions

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsÂ FunctionsKt.functions(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull StringÂ regionOrCustomDomain
)
```

Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of a given [regionOrCustomDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(kotlin.String)).  

### FunctionsKt.functions

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsÂ FunctionsKt.functions(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app,
Â Â Â Â @NonNull StringÂ regionOrCustomDomain
)
```

Returns the [FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) and [regionOrCustomDomain](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/package-summary#(com.google.firebase.Firebase).functions(com.google.firebase.FirebaseApp,kotlin.String)).  

### FunctionsKt.getHttpsCallable

```
publicÂ staticÂ finalÂ @NonNull HttpsCallableReferenceÂ FunctionsKt.getHttpsCallable(
Â Â Â Â @NonNull FirebaseFunctionsÂ receiver,
Â Â Â Â @NonNull StringÂ name,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder,Â Unit>Â init
)
```

Returns a reference to the Callable HTTPS trigger with the given name and call options.  

### FunctionsKt.getHttpsCallableFromUrl

```
publicÂ staticÂ finalÂ @NonNull HttpsCallableReferenceÂ FunctionsKt.getHttpsCallableFromUrl(
Â Â Â Â @NonNull FirebaseFunctionsÂ receiver,
Â Â Â Â @NonNull URLÂ url,
Â Â Â Â @ExtensionFunctionType @NonNull Function1<@NonNull HttpsCallableOptions.Builder,Â Unit>Â init
)
```

Returns a reference to the Callable HTTPS trigger with the given URL and call options.