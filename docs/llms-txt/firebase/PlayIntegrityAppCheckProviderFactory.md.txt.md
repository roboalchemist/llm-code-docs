# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory.md.txt

# PlayIntegrityAppCheckProviderFactory

# PlayIntegrityAppCheckProviderFactory


```
public class PlayIntegrityAppCheckProviderFactory implements AppCheckProviderFactory
```

<br />

*** ** * ** ***

Implementation of an `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory` that builds `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/internal/PlayIntegrityAppCheckProvider`s. This is the default implementation.

## Summary

| ### Constants |
|---|---|
| `static final https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#instance()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#PlayIntegrityAppCheckProviderFactory()()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#create(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp)` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#getInstance()()` Gets an instance of this class for installation into a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance. |

## Constants

### instance

```
public static final PlayIntegrityAppCheckProviderFactory instance
```

## Public constructors

### PlayIntegrityAppCheckProviderFactory

```
public PlayIntegrityAppCheckProviderFactory()
```

## Public methods

### create

```
public @NonNull AppCheckProvider create(@NonNull FirebaseApp firebaseApp)
```

### getInstance

```
public static @NonNull PlayIntegrityAppCheckProviderFactory getInstance()
```

Gets an instance of this class for installation into a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance.