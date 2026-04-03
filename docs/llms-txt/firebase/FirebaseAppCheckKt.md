# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/ktx/FirebaseAppCheckKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt.md.txt

# FirebaseAppCheckKt

# FirebaseAppCheckKt


```
public final class FirebaseAppCheckKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                     ### Public fields                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) | [appCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/package-summary#(com.google.firebase.Firebase).appCheck()) Returns the [FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |

|                                                                                                        ### Public methods                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) | [FirebaseAppCheckKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt)`.`[appCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt#(com.google.firebase.Firebase).appCheck(com.google.firebase.FirebaseApp))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` `)` Returns the [FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp). |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                       | [FirebaseAppCheckKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component1())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken)` receiver)` Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide token.                                                                                                                                                                                                                                                                                                     |
| `static final long`                                                                                                                                                                                                               | [FirebaseAppCheckKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt#(com.google.firebase.appcheck.AppCheckToken).component2())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken)` receiver)` Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide expireTimeMillis.                                                                                                                                                                                                                                                                                          |

## Public fields

### appCheck

```
publicÂ finalÂ @NonNull FirebaseAppCheckÂ appCheck
```

Returns the [FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) instance of the default [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

## Public methods

### FirebaseAppCheckKt.appCheck

```
publicÂ staticÂ finalÂ @NonNull FirebaseAppCheckÂ FirebaseAppCheckKt.appCheck(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull FirebaseAppÂ app
)
```

Returns the [FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) instance of a given [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### FirebaseAppCheckKt.component1

```
publicÂ staticÂ finalÂ @NonNull StringÂ FirebaseAppCheckKt.component1(@NonNull AppCheckTokenÂ receiver)
```

Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide token.  

|                                                                                    Returns                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | the token of the [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) |

### FirebaseAppCheckKt.component2

```
publicÂ staticÂ finalÂ longÂ FirebaseAppCheckKt.component2(@NonNull AppCheckTokenÂ receiver)
```

Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide expireTimeMillis.  

| Returns |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the expireTimeMillis of the [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) |