# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory.md.txt

# DebugAppCheckProviderFactory

# DebugAppCheckProviderFactory


```
public class DebugAppCheckProviderFactory implements AppCheckProviderFactory
```

<br />

*** ** * ** ***

Implementation of an `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory` that builds `DebugAppCheckProvider`s.

## Summary

| ### Constants |
|---|---|
| `static final https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory#instance()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory#create(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp)` |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory#getInstance()()` Gets an instance of this class for installation into a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance. |

## Constants

### instance

```
public static final DebugAppCheckProviderFactory instance
```

## Public methods

### create

```
public @NonNull AppCheckProvider create(@NonNull FirebaseApp firebaseApp)
```

### getInstance

```
public static @NonNull DebugAppCheckProviderFactory getInstance()
```

Gets an instance of this class for installation into a `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` instance. If no debug secret is found in `https://developer.android.com/reference/kotlin/android/content/SharedPreferences.html`, a new debug secret will be generated and printed to the logcat. The debug secret should then be added to the allow list in the Firebase Console.