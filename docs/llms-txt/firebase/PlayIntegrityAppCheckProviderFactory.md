# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory.md.txt

# PlayIntegrityAppCheckProviderFactory

# PlayIntegrityAppCheckProviderFactory


```
public class PlayIntegrityAppCheckProviderFactory implements AppCheckProviderFactory
```

<br />

*** ** * ** ***

Implementation of an [AppCheckProviderFactory](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory) that builds [PlayIntegrityAppCheckProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/internal/PlayIntegrityAppCheckProvider)s. This is the default implementation.

## Summary

|                                                                                       ### Constants                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final `[PlayIntegrityAppCheckProviderFactory](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory) | [instance](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#instance()) |

|                                                                                                ### Public constructors                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PlayIntegrityAppCheckProviderFactory](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#PlayIntegrityAppCheckProviderFactory())`()` |

|                                                                                                                                ### Public methods                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppCheckProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider)                                                              | [create](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#create(com.google.firebase.FirebaseApp))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp)` firebaseApp)` |
| `static @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[PlayIntegrityAppCheckProviderFactory](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#getInstance())`()` Gets an instance of this class for installation into a [FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) instance.                                             |

## Constants

### instance

```
publicÂ staticÂ finalÂ PlayIntegrityAppCheckProviderFactoryÂ instance
```  

## Public constructors

### PlayIntegrityAppCheckProviderFactory

```
publicÂ PlayIntegrityAppCheckProviderFactory()
```  

## Public methods

### create

```
publicÂ @NonNull AppCheckProviderÂ create(@NonNull FirebaseAppÂ firebaseApp)
```  

### getInstance

```
publicÂ staticÂ @NonNull PlayIntegrityAppCheckProviderFactoryÂ getInstance()
```

Gets an instance of this class for installation into a [FirebaseAppCheck](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck) instance.