# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory.md.txt

# AppCheckProviderFactory

# AppCheckProviderFactory


```
interface AppCheckProviderFactory
```

<br />

*** ** * ** ***

Interface for a factory that generates `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider`s.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory#create(com.google.firebase.FirebaseApp)(firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Gets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider` associated with the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance, or creates one if none already exists. |

## Public functions

### create

```
fun create(firebaseApp: FirebaseApp): AppCheckProvider
```

Gets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider` associated with the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance, or creates one if none already exists.