# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion.md.txt

# FirebaseFunctions.Companion

# FirebaseFunctions.Companion


```
public static class FirebaseFunctions.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                                          ### Public methods                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance())`()` Creates a Cloud Functions client with the default app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app)` Creates a Cloud Functions client with the given app.                                                                                                                                                                                                                                                |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` regionOrCustomDomain)` Creates a Cloud Functions client with the default app and given region or custom domain.                                                                                                                                                                                                                                |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseFunctions](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/functions/FirebaseFunctions.Companion#getInstance(com.google.firebase.FirebaseApp,kotlin.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` regionOrCustomDomain)` Creates a Cloud Functions client with the given app and region or custom domain. |

## Public methods

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsÂ getInstance()
```

Creates a Cloud Functions client with the default app.  

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsÂ getInstance(@NonNull FirebaseAppÂ app)
```

Creates a Cloud Functions client with the given app.  

|                                                                                               Parameters                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` | The app for the Firebase project. |

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsÂ getInstance(@NonNull StringÂ regionOrCustomDomain)
```

Creates a Cloud Functions client with the default app and given region or custom domain.  

|                                                                                              Parameters                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` regionOrCustomDomain` | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |

### getInstance

```
publicÂ staticÂ finalÂ @NonNull FirebaseFunctionsÂ getInstance(@NonNull FirebaseAppÂ app,Â @NonNull StringÂ regionOrCustomDomain)
```

Creates a Cloud Functions client with the given app and region or custom domain.  

|                                                                                               Parameters                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` app` | The app for the Firebase project.                                                                       |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` regionOrCustomDomain`   | The region or custom domain for the HTTPS trigger, such as `"us-central1"` or `"https://mydomain.com"`. |