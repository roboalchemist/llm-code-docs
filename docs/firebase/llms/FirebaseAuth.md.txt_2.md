# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.md.txt

# FirebaseAuth

# FirebaseAuth


```
public abstract class FirebaseAuth
```

<br />

*** ** * ** ***

The entry point of the Firebase Authentication SDK.

First, obtain an instance of this class by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getInstance()`.

Then, sign up or sign in a user with one of the following methods:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCustomToken(java.lang.String)`

Finally, call `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()` to get a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` object, which contains information about the signed-in user.

## Summary

| ### Nested types |
|---|
| `public interface https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener` Listener called when there is a change in the authentication state. |
| `public interface https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener` Listener called when the id token is changed. |

| ### Public fields |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#currentUser()` |
| `https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#customAuthDomain()` |
| `https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#languageCode()` |
| `https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#tenantId()` |

| ### Public methods |
|---|---|
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener listener)` Registers a listener to changes in the user authentication state. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener listener)` Registers a listener to changes in the token authentication state. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#applyActionCode(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html code)` Applies the given `code`, which can be any out of band code which is valid according to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#checkActionCode(java.lang.String)` that does not also pass `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#verifyPasswordResetCode(java.lang.String)`, which requires an additional parameter. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#checkActionCode(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html code)` Checks that the `code` given is valid. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#confirmPasswordReset(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html code, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html newPassword)` Changes the user's password to `newPassword` for the account for which the `code` is valid. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html password )` Tries to create a new user account with the given email address and password. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/SignInMethodQueryResult>` | `[fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String))(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email)` **This method is deprecated.** Migrating off of this method is recommended as a security best-practice. <br /> |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getApp()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance to which this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` belongs. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()()` Returns the currently signed-in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` or null if there is none. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCustomAuthDomain()()` Returns the custom auth domain previously set on this instance or `null` if none was set. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getFirebaseAuthSettings()()` Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings` instance for this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | `@https://developer.android.com/reference/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getInstance()()` Returns an instance of this class corresponding to the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` | `@https://developer.android.com/reference/androidx/annotation/Keep.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp)` Returns an instance of this class corresponding to the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getLanguageCode()()` Returns the language code set in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#setLanguageCode(java.lang.String)`. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getPendingAuthResult()()` Returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` wrapping an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult`. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getTenantId()()` Returns the Tenant ID previously set on this instance or `null` if none was set. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#initializeRecaptchaConfig()()` Initializes the reCAPTCHA Enterprise client proactively to enhance reCAPTCHA signal collection and to complete reCAPTCHA-protected flows in a single attempt. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#isSignInWithEmailLink(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html link)` Determines if the given link is a link intended for use with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)`. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener listener )` Unregisters a listener to authentication changes. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener listener)` Unregisters a listener to authentication changes. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#revokeAccessToken(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html accessToken)` Revokes the provided `accessToken`. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendPasswordResetEmail(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email)` Calls `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendPasswordResetEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)` without any ActionCodeSettings. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendPasswordResetEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings actionCodeSettings )` Triggers the Firebase Authentication backend to send a password-reset email to the given email address, which must correspond to an existing user of your app. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendSignInLinkToEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings actionCodeSettings )` Sends an email to the specified email which will contain a link to be used to sign in the user. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#setCustomAuthDomain(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html domain)` Sets the custom auth domain that is used to handle all sign-in redirects. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#setFirebaseUIVersion(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html firebaseUIVersion)` For internal use in FirebaseUI only. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#setLanguageCode(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html languageCode)` Sets the user-facing language code for auth operations that can be internationalized, such as `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#sendEmailVerification()`. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#setTenantId(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html tenantId)` Sets the Tenant ID to be passed on all future sign-in/sign-up operations and sign in or sign up users to the specified project as identified by the tenant. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()()` Signs in the user anonymously without requiring any credential. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential credential)` Tries to sign in a user with the given `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential`. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCustomToken(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html token)` Tries to sign in a user with a given Custom Token. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html password)` Tries to sign in a user with the given email address and password. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailLink(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html link)` Tries to sign in a user with the given email address and link. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signOut()()` Signs out the current user and clears it from the disk cache. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#startActivityForSignInWithProvider(android.app.Activity,com.google.firebase.auth.FederatedAuthProvider)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider federatedAuthProvider )` Signs in the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) for the given `provider`. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#updateCurrentUser(com.google.firebase.auth.FirebaseUser)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser user)` Sets the current user to a copy of the given user, but associated with this 's `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#useAppLanguage()()` Sets the user-facing language code to be the default app language. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#useEmulator(java.lang.String,int)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html host, int port)` Modifies this FirebaseAuth instance to communicate with the Firebase Authentication emulator. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#verifyPasswordResetCode(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html code)` Checks that the `code` is a valid password reset out of band code. |

## Public fields

### currentUser

```
public @Nullable FirebaseUser currentUser
```

### customAuthDomain

```
public String customAuthDomain
```

### languageCode

```
public String languageCode
```

### tenantId

```
public String tenantId
```

## Public methods

### addAuthStateListener

```
public void addAuthStateListener(@NonNull FirebaseAuth.AuthStateListener listener)
```

Registers a listener to changes in the user authentication state. There can be more than one listener registered at the same time for one or more `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instances.

The listeners call back in the UI thread, on the following events:

- Right after the listener has been registered
- When a user signs in
- When the current user signs out
- When the current user changes

It is a recommended practice to always listen to sign-out events, as you may want to prompt the user to sign in again and maybe restrict the information or actions they have access to.

Use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)` to unregister a listener.

See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)` if you want to listen to token refreshes.

See Also: `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`

### addIdTokenListener

```
public void addIdTokenListener(@NonNull FirebaseAuth.IdTokenListener listener)
```

Registers a listener to changes in the token authentication state. There can be more than one listener registered at the same time for one or more `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instances.

The listeners call back in the UI thread, on the following events:

- Right after the listener has been registered
- When a user signs in
- When the current user signs out
- When the current user changes
- When there is a change in the current user's token

It is a recommended practice to always listen to sign-out events, as you may want to prompt the user to sign in again and maybe restrict the information or actions they have access to.

Use `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#removeIdTokenListener(com.google.firebase.auth.FirebaseAuth.IdTokenListener)` to unregister a listener.

See `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#addAuthStateListener(com.google.firebase.auth.FirebaseAuth.AuthStateListener)` if you do not want to listen to token refreshes.

See Also: `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener`

### applyActionCode

```
public @NonNull Task<Void> applyActionCode(@NonNull String code)
```

Applies the given `code`, which can be any out of band code which is valid according to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#checkActionCode(java.lang.String)` that does not also pass `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#verifyPasswordResetCode(java.lang.String)`, which requires an additional parameter.

### checkActionCode

```
public @NonNull Task<ActionCodeResult> checkActionCode(@NonNull String code)
```

Checks that the `code` given is valid. This code will have been generated by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendPasswordResetEmail(java.lang.String)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#sendEmailVerification()` valid for a single use.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` which you can use to see the result via the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeResult`, which holds the user email for which that ActionCode is valid, as well as the which is being performed. |

### confirmPasswordReset

```
public @NonNull Task<Void> confirmPasswordReset(@NonNull String code, @NonNull String newPassword)
```

Changes the user's password to `newPassword` for the account for which the `code` is valid. Code validity can be checked with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#verifyPasswordResetCode(java.lang.String)`. This use case is only valid for signed-out users, and behavior is undefined for signed-in users. Password changes for signed-in users should be made using `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updatePassword(java.lang.String)`.
Exceptions

- `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` thrown if passed a null `code` or `
  newPassword`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthActionCodeException` thrown if the `code` is malformed or has expired.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the user corresponding to the given code has been disabled, or if there is no user corresponding to the given code.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException` thrown if the given `newPassword` is too weak.

See Also:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#verifyPasswordResetCode(java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendPasswordResetEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)`

### createUserWithEmailAndPassword

```
public @NonNull Task<AuthResult> createUserWithEmailAndPassword(
    @NonNull String email,
    @NonNull String password
)
```

Tries to create a new user account with the given email address and password. If successful, it also signs the user in into the app.

Access the signed-in user with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()`.

Upon successful completion, this operation triggers an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered s and an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`s.

**Important:** you must enable Email \&Password accounts in the Firebase console before you can use this method.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException` thrown if the password is not strong enough
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `email` address is malformed
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if there already exists an account with the given `email` address

See Also:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCustomToken(java.lang.String)`

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` with the result of the operation |

### fetchSignInMethodsForEmail

```
public @NonNull Task<SignInMethodQueryResult> [fetchSignInMethodsForEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String))(@NonNull String email)
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Migrating off of this method is recommended as a security best-practice. Learn more in the Identity Platform documentation for [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection).

Returns a list of signin methods that can be used to sign in a given user (identified by its main email address). This will match the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential#getSignInMethod()` for the credential you would generate for the appropriate signin mechanism.

This method is useful when you support multiple authentication mechanisms if you want to implement an email-first authentication flow. It is also useful to resolve a thrown on `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)`.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `email` address is malformed

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email` | the email address that identifies the user to fetch the providers from |

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/SignInMethodQueryResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/SignInMethodQueryResult` with the result of the operation. An empty list is returned when [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) is enabled, irrespective of the number of authentication methods available for the given email. |

### getApp

```
public @NonNull FirebaseApp getApp()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance to which this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` belongs.

### getCurrentUser

```
public @Nullable FirebaseUser getCurrentUser()
```

Returns the currently signed-in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` or null if there is none.

Use `getCurrentUser() != null` to check if a user is signed in.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser` | the signed-in user or null |

### getCustomAuthDomain

```
public @Nullable String getCustomAuthDomain()
```

Returns the custom auth domain previously set on this instance or `null` if none was set.

### getFirebaseAuthSettings

```
public @NonNull FirebaseAuthSettings getFirebaseAuthSettings()
```

Returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthSettings` instance for this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth` instance.

### getInstance

```
@Keep
public static @NonNull FirebaseAuth getInstance()
```

Returns an instance of this class corresponding to the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance.

Note: Firebase Authentication does not currently support Android Direct Boot.

For Applications that use Direct Boot, check if `
android.content.Context.isDeviceProtectedStorage` is `false` before you call `FirebaseAuth.getInstance()`.

### getInstance

```
@Keep
public static @NonNull FirebaseAuth getInstance(@NonNull FirebaseApp firebaseApp)
```

Returns an instance of this class corresponding to the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance.

Note: Firebase Authentication does not currently support Android Direct Boot.

For Applications that use Direct Boot, check if `
android.content.Context.isDeviceProtectedStorage` is `false` before you call `FirebaseAuth.getInstance(firebaseApp)`.

### getLanguageCode

```
public @Nullable String getLanguageCode()
```

Returns the language code set in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#setLanguageCode(java.lang.String)`.

### getPendingAuthResult

```
public @Nullable Task<AuthResult> getPendingAuthResult()
```

Returns a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` wrapping an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult`. This will return a non-null value if your app launches a web sign-in flow and the OS cleans up your hosting `https://developer.android.com/reference/android/app/Activity.html` while in the background (likely due to a low-memory event). The returned result is the value that `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#startActivityForSignInWithProvider(android.app.Activity,com.google.firebase.auth.FederatedAuthProvider)` would have returned, which includes any Exceptions thrown. Otherwise, returns null.

This method will only return a non-null result for a sign-in once. A non-null value will only be present for suitably recent sign-ins to help prevent false positive sign-ins.

### getTenantId

```
public @Nullable String getTenantId()
```

Returns the Tenant ID previously set on this instance or `null` if none was set.

### initializeRecaptchaConfig

```
public @NonNull Task<Void> initializeRecaptchaConfig()
```

Initializes the reCAPTCHA Enterprise client proactively to enhance reCAPTCHA signal collection and to complete reCAPTCHA-protected flows in a single attempt.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException` thrown on initialization failures. Common reasons are:
  - running on an unsupported API version (\< 19, KITKAT).
  - the reCAPTCHA config fetch API call failed.
  - network errors causing other API call/download failures.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` indicating if initialization was successful. |

### isSignInWithEmailLink

```
public boolean isSignInWithEmailLink(@NonNull String link)
```

Determines if the given link is a link intended for use with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)`. These links are generated by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendSignInLinkToEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)`.

### removeAuthStateListener

```
public void removeAuthStateListener(
    @NonNull FirebaseAuth.AuthStateListener listener
)
```

Unregisters a listener to authentication changes.

See Also: `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`

### removeIdTokenListener

```
public void removeIdTokenListener(@NonNull FirebaseAuth.IdTokenListener listener)
```

Unregisters a listener to authentication changes.

See Also: `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener`

### revokeAccessToken

```
public @NonNull Task<Void> revokeAccessToken(@NonNull String accessToken)
```

Revokes the provided `accessToken`. Currently supports revoking Apple-issued `
accessToken` only.

### sendPasswordResetEmail

```
public @NonNull Task<Void> sendPasswordResetEmail(@NonNull String email)
```

Calls `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendPasswordResetEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)` without any ActionCodeSettings.

### sendPasswordResetEmail

```
public @NonNull Task<Void> sendPasswordResetEmail(
    @NonNull String email,
    @Nullable ActionCodeSettings actionCodeSettings
)
```

Triggers the Firebase Authentication backend to send a password-reset email to the given email address, which must correspond to an existing user of your app. Takes in an which allows linking back to your app from the sent email.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if there is no user corresponding to the given `email` address
- No exception will be thrown in the above case, when [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) is enabled.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html email` | the email of the account to which you wish to issue an account reset email |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings actionCodeSettings` | the settings used to allow your app to handle the link sent in the email on iOS, web, and Android. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` to track completion of the sending operation |

### sendSignInLinkToEmail

```
public @NonNull Task<Void> sendSignInLinkToEmail(
    @NonNull String email,
    @NonNull ActionCodeSettings actionCodeSettings
)
```

Sends an email to the specified email which will contain a link to be used to sign in the user.

| Throws |
|---|---|
| `https://developer.android.com/reference/java/lang/IllegalArgumentException.html` | when given an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings` that does not have `canHandleCodeInApp` set to true. See also `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)` |

### setCustomAuthDomain

```
public void setCustomAuthDomain(@NonNull String domain)
```

Sets the custom auth domain that is used to handle all sign-in redirects. End-users will see this domain when signing in.

The domain must be allowlisted in the Firebase Console. If the domain contains a scheme ( `https://` or `http://`) or trailing slashes, they will be stripped off.

### setFirebaseUIVersion

```
public @NonNull Task<Void> setFirebaseUIVersion(@Nullable String firebaseUIVersion)
```

For internal use in FirebaseUI only.

### setLanguageCode

```
public void setLanguageCode(@NonNull String languageCode)
```

Sets the user-facing language code for auth operations that can be internationalized, such as `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#sendEmailVerification()`. This language code should follow the conventions defined by the IETF in BCP47.

### setTenantId

```
public void setTenantId(@NonNull String tenantId)
```

Sets the Tenant ID to be passed on all future sign-in/sign-up operations and sign in or sign up users to the specified project as identified by the tenant. If you change this field, future sign-in/sign-ups will contain the new value.

This is set to null as default and users are signed into the agent project.

Note: this is different from what the current user's Tenant ID is; you can change this instance's Tenant ID without affecting the current user.

### signInAnonymously

```
public @NonNull Task<AuthResult> signInAnonymously()
```

Signs in the user anonymously without requiring any credential.

This method creates a new account in your Firebase Authentication system, except in the case where there was already an anonymous user signed in into this app. Access the signed-in user with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()`.

Upon successful completion, this operation triggers an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered s and an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`s.

Anonymous users do not require any credential, and are useful in situations where you want to persist information about your users before asking them to sign in. For example, they may be useful when implementing a signed-out shopping cart in an e-commerce application.

Due to the unauthenticated nature of this kind of user, they are not transferrable across devices. In order to allow your app's users to keep their information, ask them to provide some other authentication credentials, and link them to the current user with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

**Important:** you must enable Anonymous accounts in the Firebase console before being able to use them.

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCustomToken(java.lang.String)`

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` with the result of the operation |

### signInWithCredential

```
public @NonNull Task<AuthResult> signInWithCredential(@NonNull AuthCredential credential)
```

Tries to sign in a user with the given `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential`.

Use this method to sign in a user into your Firebase Authentication system. First retrieve the `credential` either directly from the user, in case of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential`, or from a supported authentication SDK, such as Google Sign-In or Facebook. Later access the signed-in user with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()`.

For all `AuthCredential` types except `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthCredential`, this method will create an account for the user in the case that it didn't exist before.

**Important:** you must configure the authentication providers in the Firebase console before you can use them.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the user account you are trying to sign in to has been disabled. Also thrown if `credential` is an `
  EmailAuthCredential` with an email address that does not correspond to an existing user.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `credential` is malformed or has expired. If `credential instanceof EmailAuthCredential` it will be thrown if the password is incorrect.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if there already exists an account with the email address asserted by the `credential`. Resolve this case by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#fetchSignInMethodsForEmail(java.lang.String)` and then asking the user to sign in using one of them.

See Also:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCustomToken(java.lang.String)`

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` with the result of the operation |

### signInWithCustomToken

```
public @NonNull Task<AuthResult> signInWithCustomToken(@NonNull String token)
```

Tries to sign in a user with a given Custom Token.

Use this method after you retrieve a Firebase Auth Custom Token from your server, to sign in a user into your Firebase Authentication system. Access the signed-in user with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()`.

Upon successful completion, this operation triggers an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered s and an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`s.

This operation might create an account if the `uid` specified in the token corresponds to a user without a record in the system.

Read how to use Custom Token authentication and the cases where it is useful in [the guides](https://firebase.google.com/docs/auth/android/custom-auth).
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `token` format is incorrect or if it corresponds to a different Firebase App

<!-- -->

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()`

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` with the result of the operation |

### signInWithEmailAndPassword

```
public @NonNull Task<AuthResult> signInWithEmailAndPassword(@NonNull String email, @NonNull String password)
```

Tries to sign in a user with the given email address and password.

Access the signed-in user with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()`.

Upon successful completion, this operation triggers an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered s and an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`s.

This is equivalent to calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` with an generated by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredential(java.lang.String,java.lang.String)`.

**Important:** you must enable Email \&Password accounts in the Firebase console before being able to use this method.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the user account corresponding to `email` does not exist or has been disabled
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `password` is wrong
- When [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) is enabled, `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` is thrown if the `email` or `password` is invalid.

See also:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCustomToken(java.lang.String)`

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` with the result of the operation |

### signInWithEmailLink

```
public @NonNull Task<AuthResult> signInWithEmailLink(@NonNull String email, @NonNull String link)
```

Tries to sign in a user with the given email address and link. This link should be generated by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendSignInLinkToEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)`.

Access the signed-in user with `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getCurrentUser()`.

Upon successful completion, this operation triggers an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered s and an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`s.

This is equivalent to calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` with an generated by `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/EmailAuthProvider#getCredentialWithLink(java.lang.String,java.lang.String)`.

**Important:** you must enable Passwordless sign-in in the Firebase console before being able to use this method.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the user account corresponding to `email` does not exist or has been disabled
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `password` is wrong

See also:

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()`
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCustomToken(java.lang.String)`

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` with the result of the operation |

### signOut

```
public void signOut()
```

Signs out the current user and clears it from the disk cache.

Upon successful completion, this operation triggers an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.IdTokenListener#onIdTokenChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered s and an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener#onAuthStateChanged(com.google.firebase.auth.FirebaseAuth)` event in all registered `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth.AuthStateListener`s.

### startActivityForSignInWithProvider

```
public @NonNull Task<AuthResult> startActivityForSignInWithProvider(
    @NonNull Activity activity,
    @NonNull FederatedAuthProvider federatedAuthProvider
)
```

Signs in the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) for the given `provider`.

Note: this call has a UI associated with it, unlike the majority of calls in FirebaseAuth.
Exceptions

- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the credential generated from the flow is malformed or expired.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the user has been disabled by an administrator.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if the email that keys the user that is signing in is already in use.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWebException` thrown if there is an operation already in progress, the pending operation was canceled, there is a problem with 3rd party cookies in the browser, or some other error in the web context has occurred.
- `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException` thrown if signing in via this method has been disabled in the Firebase Console, or if the `provider` passed is configured improperly.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/app/Activity.html activity` | the current `https://developer.android.com/reference/android/app/Activity.html` from which you intend to launch this flow. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider federatedAuthProvider` | an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider` configured with information about how you intend the user to sign in. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult>` | a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with a reference to an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult` with user information upon success |

### updateCurrentUser

```
public @NonNull Task<Void> updateCurrentUser(@NonNull FirebaseUser user)
```

Sets the current user to a copy of the given user, but associated with this 's `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`. If the given user isn't for this project, then a will be returned via the Task.

### useAppLanguage

```
public void useAppLanguage()
```

Sets the user-facing language code to be the default app language.

### useEmulator

```
public void useEmulator(@NonNull String host, int port)
```

Modifies this FirebaseAuth instance to communicate with the Firebase Authentication emulator.

Note: this must be called before this instance has been used to do any operations.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html host` | the emulator host (e.g. 10.0.2.2) |
| `int port` | the emulator port (e.g. 8080) |

### verifyPasswordResetCode

```
public @NonNull Task<String> verifyPasswordResetCode(@NonNull String code)
```

Checks that the `code` is a valid password reset out of band code. This code will have been generated by a call to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#sendPasswordResetEmail(java.lang.String)`, and is valid for a single use.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/String.html>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` which holds the email for which this code is applicable. |