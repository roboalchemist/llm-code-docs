# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ktx/FirebaseKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt.md.txt

# FirebaseKt

# FirebaseKt


```
public final class FirebaseKt
```

<br />

*** ** * ** ***

## Summary

|                                                                                                ### Public fields                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)         | [app](https://firebase.google.com/docs/reference/android/com/google/firebase/package-summary#(com.google.firebase.Firebase).app()) Returns the default firebase app instance.     |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions) | [options](https://firebase.google.com/docs/reference/android/com/google/firebase/package-summary#(com.google.firebase.Firebase).options()) Returns options of default FirebaseApp |

|                                                                                               ### Public methods                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) | [FirebaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt)`.`[app](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).app(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name)` Returns a named firebase app instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `static final `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)                                                                                               | [FirebaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt)`.`[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).initialize(android.content.Context))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` context` `)` Initializes and returns a FirebaseApp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) | [FirebaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt)`.`[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` context,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions)` options` `)` Initializes and returns a FirebaseApp.                                                                                                                                                                                                       |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp) | [FirebaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt)`.`[initialize](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseKt#(com.google.firebase.Firebase).initialize(android.content.Context,com.google.firebase.FirebaseOptions,kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Firebase](https://firebase.google.com/docs/reference/android/com/google/firebase/Firebase)` receiver,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)` context,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions)` options,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name` `)` Initializes and returns a FirebaseApp. |

## Public fields

### app

```
publicÂ finalÂ @NonNull FirebaseAppÂ app
```

Returns the default firebase app instance.  

### options

```
publicÂ finalÂ @NonNull FirebaseOptionsÂ options
```

Returns options of default FirebaseApp  

## Public methods

### FirebaseKt.app

```
publicÂ staticÂ finalÂ @NonNull FirebaseAppÂ FirebaseKt.app(@NonNull FirebaseÂ receiver,Â @NonNull StringÂ name)
```

Returns a named firebase app instance.  

### FirebaseKt.initialize

```
publicÂ staticÂ finalÂ FirebaseAppÂ FirebaseKt.initialize(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull ContextÂ context
)
```

Initializes and returns a FirebaseApp.  

### FirebaseKt.initialize

```
publicÂ staticÂ finalÂ @NonNull FirebaseAppÂ FirebaseKt.initialize(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull ContextÂ context,
Â Â Â Â @NonNull FirebaseOptionsÂ options
)
```

Initializes and returns a FirebaseApp.  

### FirebaseKt.initialize

```
publicÂ staticÂ finalÂ @NonNull FirebaseAppÂ FirebaseKt.initialize(
Â Â Â Â @NonNull FirebaseÂ receiver,
Â Â Â Â @NonNull ContextÂ context,
Â Â Â Â @NonNull FirebaseOptionsÂ options,
Â Â Â Â @NonNull StringÂ name
)
```

Initializes and returns a FirebaseApp.