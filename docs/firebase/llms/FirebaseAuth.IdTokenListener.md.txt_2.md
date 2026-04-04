# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth.IdTokenListener.md.txt

# FirebaseAuth.IdTokenListener

# FirebaseAuth.IdTokenListener


```
interface FirebaseAuth.IdTokenListener
```

<br />

*** ** * ** ***

Listener called when the id token is changed.

Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)` to register or unregister listeners.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth)( @https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html auth: @https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth )` This method gets invoked in the UI thread on changes in the authentication state: |

## Public functions

### onIdTokenChanged

```
fun onIdTokenChanged(
    @UnknownInitialization auth: @UnknownInitialization FirebaseAuth
): Unit
```

This method gets invoked in the UI thread on changes in the authentication state:

- Right after the listener has been registered
- When a user is signed in
- When the current user is signed out
- When the current user changes
- When there is a change in the current user's token

| Parameters |
|---|---|
| `@https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html auth: @https://checkerframework.org/api/org/checkerframework/checker/initialization/qual/UnknownInitialization.html https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` | use it to disambiguate which `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` instance the event corresponds to, in the case where you are using more than one at the same time. |