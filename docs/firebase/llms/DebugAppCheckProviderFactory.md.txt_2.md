# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory.md.txt

# DebugAppCheckProviderFactory

# DebugAppCheckProviderFactory


```
class DebugAppCheckProviderFactory : AppCheckProviderFactory
```

<br />

*** ** * ** ***

Implementation of an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory` that builds `DebugAppCheckProvider`s.

## Summary

| ### Constants |
|---|---|
| `const https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory#instance()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/debug/DebugAppCheckProviderFactory#create(com.google.firebase.FirebaseApp)(firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` |

## Constants

### instance

```
const val instance: DebugAppCheckProviderFactory!
```

## Public functions

### create

```
fun create(firebaseApp: FirebaseApp): AppCheckProvider
```