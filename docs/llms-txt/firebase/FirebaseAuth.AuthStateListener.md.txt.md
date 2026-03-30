# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener.md.txt

# FirebaseAuth.AuthStateListener

# FirebaseAuth.AuthStateListener


```
public interface FirebaseAuth.AuthStateListener
```

<br />

*** ** * ** ***

Listener called when there is a change in the authentication state.

Use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)` and `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)` to register or unregister listeners.

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth auth)` This method gets invoked in the UI thread on changes in the authentication state: |

## Public methods

### onAuthStateChanged

```
abstract void onAuthStateChanged(@NonNull FirebaseAuth auth)
```

This method gets invoked in the UI thread on changes in the authentication state:

- Right after the listener has been registered
- When a user is signed in
- When the current user is signed out
- When the current user changes

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth auth` | use it to disambiguate which `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance the event corresponds to, in the case where you are using more than one at the same time. |