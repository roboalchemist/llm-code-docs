# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser.md.txt

# FirebaseUser

# FirebaseUser


```
abstract class FirebaseUser : Parcelable, UserInfo
```

<br />

*** ** * ** ***

Represents a user's profile information in your Firebase project's user database. It also contains helper methods to change or retrieve profile information, as well as to manage that user's authentication state.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#FirebaseUser()()` |

| ### Public functions |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#delete()()` Deletes the user record from your Firebase project's database. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getDisplayName()()` Returns the main display name of this user from the Firebase project's user database. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getEmail()()` Returns the main email address of the user, as stored in the Firebase project's user database. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GetTokenResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getIdToken(boolean)(forceRefresh: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Fetches a Firebase Auth ID Token for the user; useful when authenticating against your own backend. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUserMetadata?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getMetadata()()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUserMetadata` associated with this user. |
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getMultiFactor()()` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor` instance which is the main entry point for multi-factor related operations on this user. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getPhoneNumber()()` Returns the phone number of the user, as stored in the Firebase project's user database, or `null` if none exists. |
| `abstract https://developer.android.com/reference/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getPhotoUrl()()` Returns the URL of this user's main profile picture, as stored in the Firebase project's user database. |
| `abstract (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getProviderData()()` Returns a `https://developer.android.com/reference/java/util/List.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo` objects that represents the linked identities of the user using different authentication providers that may be linked to their account. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getProviderId()()` Always returns `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthProvider#PROVIDER_ID()`. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getTenantId()()` Returns the tenant ID of the current user or `null` if this user isn't associated with a tenant project. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#getUid()()` Returns a string used to uniquely identify your user in your Firebase project's user database. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#isAnonymous()()` Returns true if the user is anonymous; that is, the user account was created with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInAnonymously()` and has not been linked to another account with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)(credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)` Attaches the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` to the user. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)(credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)` Reauthenticates the user with the given credential. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticateAndRetrieveData(com.google.firebase.auth.AuthCredential)(credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)` Reauthenticates the user with the given credential, and returns the profile data for that account. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reload()()` Manually refreshes the data of the current user (for example, attached providers, display name, and so on). |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#sendEmailVerification()()` Calls `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#sendEmailVerification(com.google.firebase.auth.ActionCodeSettings)` with null `actionCodeSettings`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#sendEmailVerification(com.google.firebase.auth.ActionCodeSettings)(actionCodeSettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings)` Initiates email verification for the user. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#startActivityForLinkWithProvider(android.app.Activity,com.google.firebase.auth.FederatedAuthProvider)( activity: https://developer.android.com/reference/android/app/Activity.html, federatedAuthProvider: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider )` Links the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) to the given `provider`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#startActivityForReauthenticateWithProvider(android.app.Activity,com.google.firebase.auth.FederatedAuthProvider)( activity: https://developer.android.com/reference/android/app/Activity.html, federatedAuthProvider: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider )` Reauthenticates the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) using the given `provider`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#unlink(java.lang.String)(provider: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Detaches credentials from a given provider type from this user. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `[updateEmail](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String))(email: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` **This function is deprecated.** Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String)` instead. <br /> |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updatePassword(java.lang.String)(password: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Updates the password of the user. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updatePhoneNumber(com.google.firebase.auth.PhoneAuthCredential)(credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthCredential)` Updates the phone number of the user. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)(request: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest)` Updates the user profile information. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String)(newEmail: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Calls `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)` without any ` actionCodeSettings`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)( newEmail: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, actionCodeSettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings? )` Sends a verification email to `newEmail`. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(p: https://developer.android.com/reference/android/os/Parcel.html!, p1: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | |
| From [com.google.firebase.auth.UserInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo#isEmailVerified()()` Returns `true` if the user's email is verified. | |

## Public constructors

### FirebaseUser

```
FirebaseUser()
```

## Public functions

### delete

```
fun delete(): Task<Void!>
```

Deletes the user record from your Firebase project's database. If the operation is successful, the user will be signed out.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)`.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException` thrown if the user's last sign-in time does not meet the security threshold. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)` to resolve. This does not apply if the user is anonymous.

### getDisplayName

```
abstract fun getDisplayName(): String?
```

Returns the main display name of this user from the Firebase project's user database. Unlike the display name property from instances of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo` corresponding to authentication providers (like Google Sign-In), which is not modifiable, this name can be updated at any time by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)`.

This field will be automatically populated on account creation if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` used on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` contained such information.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)` |   |

### getEmail

```
abstract fun getEmail(): String?
```

Returns the main email address of the user, as stored in the Firebase project's user database. Unlike the email property from instances of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo` corresponding to authentication providers (like GitHub), which is not modifiable, this email address can be updated at any time by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String)`.

This field will be automatically populated on account creation if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` used on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` contained such information, or if the account was created with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)`. However, this is not true if the setting "Multiple Accounts per Email" is enabled in the Firebase Console - in that case this will be null unless the account was created with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String)` has been called.

If the user also has a password, this email address can be used to sign in into the account using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)`.

This email address is displayed in the Users section of the Firebase console.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String)` |   |

### getIdToken

```
fun getIdToken(forceRefresh: Boolean): Task<GetTokenResult!>
```

Fetches a Firebase Auth ID Token for the user; useful when authenticating against your own backend. Use our server SDKs or follow the official documentation to securely verify the integrity and validity of this token.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` if `forceRefresh == true`, thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid

| Parameters |
|---|---|
| `forceRefresh: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | force refreshes the token. Should only be set to `true` if the token is invalidated out of band. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GetTokenResult!>` | a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GetTokenResult` |

### getMetadata

```
abstract fun getMetadata(): FirebaseUserMetadata?
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUserMetadata` associated with this user.

### getMultiFactor

```
abstract fun getMultiFactor(): MultiFactor
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor` instance which is the main entry point for multi-factor related operations on this user.

### getPhoneNumber

```
abstract fun getPhoneNumber(): String?
```

Returns the phone number of the user, as stored in the Firebase project's user database, or `null` if none exists. This can be updated at any time by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updatePhoneNumber(com.google.firebase.auth.PhoneAuthCredential)`.

This field will be automatically populated on account creation if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` used on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` contained such information. This phone number is displayed in the Users section of the Firebase console.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updatePhoneNumber(com.google.firebase.auth.PhoneAuthCredential)` |   |

### getPhotoUrl

```
abstract fun getPhotoUrl(): Uri?
```

Returns the URL of this user's main profile picture, as stored in the Firebase project's user database. Unlike the profile URL property from instances of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo` corresponding to authentication providers (like Facebook Login), which is not modifiable, this URL can be updated at any time by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)`.

This field will be automatically populated on account creation if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` used on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` contained such information.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)` |   |

### getProviderData

```
abstract fun getProviderData(): (Mutable)List<UserInfo!>
```

Returns a `https://developer.android.com/reference/java/util/List.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserInfo` objects that represents the linked identities of the user using different authentication providers that may be linked to their account. Use this to access, for example, your user's basic profile information retrieved from Facebook whether or not the user used Facebook Login to sign in to the current session.

### getProviderId

```
abstract fun getProviderId(): String
```

Always returns `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthProvider#PROVIDER_ID()`.

### getTenantId

```
abstract fun getTenantId(): String?
```

Returns the tenant ID of the current user or `null` if this user isn't associated with a tenant project.

### getUid

```
abstract fun getUid(): String
```

Returns a string used to uniquely identify your user in your Firebase project's user database. Use it when storing information in Firebase Database or Storage, or even in your own backend.

This identifier is opaque and does not correspond necessarily to the user's email address or any other field.

### isAnonymous

```
abstract fun isAnonymous(): Boolean
```

Returns true if the user is anonymous; that is, the user account was created with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInAnonymously()` and has not been linked to another account with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

### linkWithCredential

```
fun linkWithCredential(credential: AuthCredential): Task<AuthResult!>
```

Attaches the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` to the user. This allows the user to sign in to this account in the future with credentials for such provider.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWeakPasswordException` thrown if `credential instanceof
  EmailAuthCredential` and the password is not strong enough
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `credential` is malformed or expired
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if there is another user account associated with the given `credential`
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException` thrown if `credential instanceof
  EmailAuthCredential` and if the user's last sign-in time does not meet the security threshold. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)` to resolve. This does not apply if the user is anonymous.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException` thrown if there is an attempt to link a provider that is already linked to this account or if an internal error occurs

| Parameters |
|---|---|
| `credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | a valid credential of a type not yet linked to this user |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult` |

### reauthenticate

```
fun reauthenticate(credential: AuthCredential): Task<Void!>
```

Reauthenticates the user with the given credential. This is useful for operations that require a recent sign-in, to prevent or resolve a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException`.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled or deleted
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `credential` is malformed or has expired, or if it corresponds to another existing user's account. Inspect the error code to desambiguate.

| Parameters |
|---|---|
| `credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | authentication credential that must be valid for the current user. |

### reauthenticateAndRetrieveData

```
fun reauthenticateAndRetrieveData(credential: AuthCredential): Task<AuthResult!>
```

Reauthenticates the user with the given credential, and returns the profile data for that account. This is useful for operations that require a recent sign-in, to prevent or resolve a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException`.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled or deleted
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `credential` is malformed or has expired, or if it corresponds to another existing user's account. Inspect the error code to desambiguate.

| Parameters |
|---|---|
| `credential: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | authentication credential that must be valid for the current user. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult` containing the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser` reference and . |

### reload

```
fun reload(): Task<Void!>
```

Manually refreshes the data of the current user (for example, attached providers, display name, and so on).
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid

### sendEmailVerification

```
fun sendEmailVerification(): Task<Void!>
```

Calls `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#sendEmailVerification(com.google.firebase.auth.ActionCodeSettings)` with null `actionCodeSettings`.

### sendEmailVerification

```
fun sendEmailVerification(actionCodeSettings: ActionCodeSettings): Task<Void!>
```

Initiates email verification for the user. Takes in an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings` to allow linking back to your app in the email.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` to track completion of the sending operation. |

### startActivityForLinkWithProvider

```
fun startActivityForLinkWithProvider(
    activity: Activity,
    federatedAuthProvider: FederatedAuthProvider
): Task<AuthResult!>
```

Links the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) to the given `provider`. If the calling activity dies during this operation, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#getPendingAuthResult()` to get the outcome of this operation.

Note: this call has a UI associated with it, unlike the majority of calls in FirebaseAuth.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the credential generated from the flow is malformed or expired.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the user has been disabled by an administrator.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if the email that keys the user that is signing in is already in use.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWebException` thrown if there is an operation already in progress, the pending operation was canceled, there is a problem with 3rd party cookies in the browser, or some other error in the web context has occurred.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException` thrown if signing in via this method has been disabled in the Firebase Console, or if the `provider` passed is configured improperly.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/android/app/Activity.html` | the current `https://developer.android.com/reference/android/app/Activity.html` that you intent to launch this flow from |
| `federatedAuthProvider: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider` | an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider` configured with information about the provider that you intend to link to the user. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with a reference to an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult` with user information upon success |

### startActivityForReauthenticateWithProvider

```
fun startActivityForReauthenticateWithProvider(
    activity: Activity,
    federatedAuthProvider: FederatedAuthProvider
): Task<AuthResult!>
```

Reauthenticates the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) using the given `provider`. If the calling activity dies during this operation, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#getPendingAuthResult()` to get the outcome of this operation.

Note: this call has a UI associated with it, unlike the majority of calls in FirebaseAuth.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the credential generated from the flow is malformed or expired.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the user has been disabled by an administrator.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if the email that keys the user that is signing in is already in use.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWebException` thrown if there is an operation already in progress, the pending operation was canceled, there is a problem with 3rd party cookies in the browser, or some other error in the web context has occurred.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException` thrown if signing in via this method has been disabled in the Firebase Console, or if the `provider` passed is configured improperly.

| Parameters |
|---|---|
| `activity: https://developer.android.com/reference/android/app/Activity.html` | the current `https://developer.android.com/reference/android/app/Activity.html` that you intent to launch this flow from |
| `federatedAuthProvider: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider` | an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider` configured with information about how you intend the user to reauthenticate. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` with a reference to an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult` with user information upon success |

### unlink

```
fun unlink(provider: String): Task<AuthResult!>
```

Detaches credentials from a given provider type from this user. This prevents the user from signing in to this account in the future with credentials from such provider.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid

| Parameters |
|---|---|
| `provider: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a unique identifier of the type of provider to be unlinked, for example, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID()`. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthResult` |

### updateEmail

```
fun [updateEmail](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String))(email: String): Task<Void!>
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String)` instead.

Updates the email address of the user.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)`.

In addition, note that the original email address recipient will receive an email that allows them to revoke the email address change, in order to protect them from account hijacking.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException` thrown if the `email` address is malformed
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if there already exists an account with the given `email` address
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException` thrown if the user's last sign-in time does not meet the security threshold. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)` to resolve. This does not apply if the user is anonymous.
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthException` thrown with code OPERATION_NOT_ALLOWED if [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) is enabled.

### updatePassword

```
fun updatePassword(password: String): Task<Void!>
```

Updates the password of the user.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)`.

Anonymous users who update both their email and password will no longer be anonymous. They will be able to log in with these credentials.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthWeakPasswordException` thrown if the password is not strong enough
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException` thrown if the user's last sign-in time does not meet the security threshold. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)` to resolve. This does not apply if the user is anonymous.

### updatePhoneNumber

```
fun updatePhoneNumber(credential: PhoneAuthCredential): Task<Void!>
```

Updates the phone number of the user.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)`.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthUserCollisionException` thrown if there already exists an account with the given phone number
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException` thrown if the user's last sign-in time does not meet the security threshold. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)` to resolve. This does not apply if the user is anonymous.

### updateProfile

```
fun updateProfile(request: UserProfileChangeRequest): Task<Void!>
```

Updates the user profile information. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest.Builder` to construct the request.
Exceptions

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuthInvalidUserException` thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid

### verifyBeforeUpdateEmail

```
fun verifyBeforeUpdateEmail(newEmail: String): Task<Void!>
```

Calls `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)` without any `
actionCodeSettings`.

### verifyBeforeUpdateEmail

```
fun verifyBeforeUpdateEmail(
    newEmail: String,
    actionCodeSettings: ActionCodeSettings?
): Task<Void!>
```

Sends a verification email to `newEmail`. Upon redemption of the link in the email, this user's email will be changed to `newEmail` and that email will be marked verified.

| Parameters |
|---|---|
| `newEmail: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the user's new email |
| `actionCodeSettings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings?` | the optional `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/ActionCodeSettings` object to allow linking back to your app in the email |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html!>` | `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` to track completion of the sending operation. |