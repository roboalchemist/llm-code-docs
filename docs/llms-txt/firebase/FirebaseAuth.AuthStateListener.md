# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth.AuthStateListener.md.txt

# FirebaseAuth.AuthStateListener

# FirebaseAuth.AuthStateListener


```
interface FirebaseAuth.AuthStateListener
```

<br />

*** ** * ** ***

Listener called when there is a change in the authentication state.

Use [addAuthStateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#addAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)) and [removeAuthStateListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#removeAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)) to register or unregister listeners.

## Summary

|                             ### Public functions                             |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [onAuthStateChanged](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth))`(auth: `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)`)` This method gets invoked in the UI thread on changes in the authentication state: |

## Public functions

### onAuthStateChanged

```
funÂ onAuthStateChanged(auth:Â FirebaseAuth):Â Unit
```

This method gets invoked in the UI thread on changes in the authentication state:

- Right after the listener has been registered
- When a user is signed in
- When the current user is signed out
- When the current user changes

|                                                   Parameters                                                    |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `auth: `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth) | use it to disambiguate which [FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth) instance the event corresponds to, in the case where you are using more than one at the same time. |