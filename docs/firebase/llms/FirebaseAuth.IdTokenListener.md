# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth.IdTokenListener.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener.md.txt

# FirebaseAuth.IdTokenListener

# FirebaseAuth.IdTokenListener


```
public interface FirebaseAuth.IdTokenListener
```

<br />

*** ** * ** ***

Listener called when the id token is changed.

Use [addIdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)) and [removeIdTokenListener](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)) to register or unregister listeners.

## Summary

| ### Public methods |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract void`    | [onIdTokenChanged](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth))`(` ` @`[UnknownInitialization](https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` @`[UnknownInitialization](https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html)` `[FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth)` auth` `)` This method gets invoked in the UI thread on changes in the authentication state: |

## Public methods

### onIdTokenChanged

```
abstractÂ voidÂ onIdTokenChanged(
Â Â Â Â @UnknownInitialization @NonNull @UnknownInitialization FirebaseAuthÂ auth
)
```

This method gets invoked in the UI thread on changes in the authentication state:

- Right after the listener has been registered
- When a user is signed in
- When the current user is signed out
- When the current user changes
- When there is a change in the current user's token

|                                                                                                                                                                                                                                         Parameters                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[UnknownInitialization](https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html)` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` @`[UnknownInitialization](https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html)` `[FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth)` auth` | use it to disambiguate which [FirebaseAuth](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) instance the event corresponds to, in the case where you are using more than one at the same time. |