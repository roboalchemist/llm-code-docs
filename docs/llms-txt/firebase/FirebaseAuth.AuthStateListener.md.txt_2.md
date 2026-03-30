# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth.AuthStateListener.md.txt

# FirebaseAuth.AuthStateListener

# FirebaseAuth.AuthStateListener


```
interface FirebaseAuth.AuthStateListener
```

<br />

*** ** * ** ***

Listener called when there is a change in the authentication state.

Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#addAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#removeAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)` to register or unregister listeners.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)(auth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)` This method gets invoked in the UI thread on changes in the authentication state: |

## Public functions

### onAuthStateChanged

```
fun onAuthStateChanged(auth: FirebaseAuth): Unit
```

This method gets invoked in the UI thread on changes in the authentication state:

- Right after the listener has been registered
- When a user is signed in
- When the current user is signed out
- When the current user changes

| Parameters |
|---|---|
| `auth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` | use it to disambiguate which `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth` instance the event corresponds to, in the case where you are using more than one at the same time. |