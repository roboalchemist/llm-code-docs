# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory.md.txt

# AppCheckProviderFactory

# AppCheckProviderFactory


```
public interface AppCheckProviderFactory
```

<br />

*** ** * ** ***

Interface for a factory that generates `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider`s.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory#create(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp)` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider` associated with the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance, or creates one if none already exists. |

## Public methods

### create

```
abstract @NonNull AppCheckProvider create(@NonNull FirebaseApp firebaseApp)
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider` associated with the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance, or creates one if none already exists.