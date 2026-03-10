# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory.md.txt

# PlayIntegrityAppCheckProviderFactory

# PlayIntegrityAppCheckProviderFactory


```
class PlayIntegrityAppCheckProviderFactory : AppCheckProviderFactory
```

<br />

*** ** * ** ***

Implementation of an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory` that builds `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/playintegrity/internal/PlayIntegrityAppCheckProvider`s. This is the default implementation.

## Summary

| ### Constants |
|---|---|
| `const https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#instance()` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#PlayIntegrityAppCheckProviderFactory()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/playintegrity/PlayIntegrityAppCheckProviderFactory#create(com.google.firebase.FirebaseApp)(firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` |

## Constants

### instance

```
const val instance: PlayIntegrityAppCheckProviderFactory!
```

## Public constructors

### PlayIntegrityAppCheckProviderFactory

```
PlayIntegrityAppCheckProviderFactory()
```

## Public functions

### create

```
fun create(firebaseApp: FirebaseApp): AppCheckProvider
```