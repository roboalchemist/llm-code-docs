# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Protocols/AppCheckProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider.md.txt

# AppCheckProvider

# AppCheckProvider


```
interface AppCheckProvider
```

<br />

*** ** * ** ***

Interface for a provider that generates [AppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken)s. This provider can be called at any time by any Firebase library that depends (optionally or otherwise) on [AppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken)s. This provider is responsible for determining if it can create a new token at the time of the call and returning that new token if it can.

## Summary

|                                                                                                ### Public functions                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken)`!>` | [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProvider#getToken())`()` Returns a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) which resolves to a valid [AppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken) or an [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) in the case that an unexpected failure occurred while getting the token. |

## Public functions

### getToken

```
funÂ getToken():Â Task<AppCheckToken!>
```

Returns a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) which resolves to a valid [AppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken) or an [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html) in the case that an unexpected failure occurred while getting the token.