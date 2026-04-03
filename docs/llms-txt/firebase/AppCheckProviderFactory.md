# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProviderFactory.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory.md.txt

# AppCheckProviderFactory

# AppCheckProviderFactory


```
interface AppCheckProviderFactory
```

<br />

*** ** * ** ***

Interface for a factory that generates [AppCheckProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider)s.

## Summary

|                                                ### Public functions                                                 |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AppCheckProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider) | [create](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory#create(com.google.firebase.FirebaseApp))`(firebaseApp: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)` Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance, or creates one if none already exists. |

## Public functions

### create

```
funÂ create(firebaseApp:Â FirebaseApp):Â AppCheckProvider
```

Gets the [AppCheckProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider) associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance, or creates one if none already exists.