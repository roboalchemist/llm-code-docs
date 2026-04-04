# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider.md.txt

# AppCheckProvider

# AppCheckProvider


```
public interface AppCheckProvider
```

<br />

*** ** * ** ***

Interface for a provider that generates `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken`s. This provider can be called at any time by any Firebase library that depends (optionally or otherwise) on `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken`s. This provider is responsible for determining if it can create a new token at the time of the call and returning that new token if it can.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProvider#getToken()()` Returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` which resolves to a valid `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` or an `https://developer.android.com/reference/kotlin/java/lang/Exception.html` in the case that an unexpected failure occurred while getting the token. |

## Public methods

### getToken

```
abstract @NonNull Task<AppCheckToken> getToken()
```

Returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` which resolves to a valid `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` or an `https://developer.android.com/reference/kotlin/java/lang/Exception.html` in the case that an unexpected failure occurred while getting the token.