# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser.md.txt

# FirebaseUser

# FirebaseUser


```
public abstract class FirebaseUser implements Parcelable, UserInfo
```

<br />

*** ** * ** ***

Represents a user's profile information in your Firebase project's user database. It also contains helper methods to change or retrieve profile information, as well as to manage that user's authentication state.

## Summary

|                                                   ### Public constructors                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|
| [FirebaseUser](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#FirebaseUser())`()` |

|                                                                                                                                            ### Public methods                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [delete](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#delete())`()` Deletes the user record from your Firebase project's database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `abstract @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                               | [getDisplayName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getDisplayName())`()` Returns the main display name of this user from the Firebase project's user database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `abstract @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                               | [getEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getEmail())`()` Returns the main email address of the user, as stored in the Firebase project's user database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[GetTokenResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult)`>` | [getIdToken](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getIdToken(boolean))`(boolean forceRefresh)` Fetches a Firebase Auth ID Token for the user; useful when authenticating against your own backend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `abstract @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[FirebaseUserMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata)                                                                              | [getMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getMetadata())`()` Returns the [FirebaseUserMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata) associated with this user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[MultiFactor](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor)                                                                                                  | [getMultiFactor](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getMultiFactor())`()` Returns a [MultiFactor](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor) instance which is the main entry point for multi-factor related operations on this user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `abstract @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                               | [getPhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getPhoneNumber())`()` Returns the phone number of the user, as stored in the Firebase project's user database, or `null` if none exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `abstract @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[Uri](https://developer.android.com/reference/android/net/Uri.html)                                                                                                                                   | [getPhotoUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getPhotoUrl())`()` Returns the URL of this user's main profile picture, as stored in the Firebase project's user database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/java/util/List.html)`<`[UserInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo)`>`                               | [getProviderData](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getProviderData())`()` Returns a [List](https://developer.android.com/reference/java/util/List.html) of [UserInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo) objects that represents the linked identities of the user using different authentication providers that may be linked to their account.                                                                                                                                                                                                                                                                                                                                                                               |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                 | [getProviderId](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getProviderId())`()` Always returns [PROVIDER_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthProvider#PROVIDER_ID()).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `abstract @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                               | [getTenantId](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getTenantId())`()` Returns the tenant ID of the current user or `null` if this user isn't associated with a tenant project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                 | [getUid](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#getUid())`()` Returns a string used to uniquely identify your user in your Firebase project's user database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `abstract boolean`                                                                                                                                                                                                                                                                                        | [isAnonymous](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#isAnonymous())`()` Returns true if the user is anonymous; that is, the user account was created with [signInAnonymously](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()) and has not been linked to another account with [linkWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).                                                                                                                                                                                                                                                                 |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>`         | [linkWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)` credential)` Attaches the given [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) to the user.                                                                                                                                                                                                                                                                                               |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)` credential)` Reauthenticates the user with the given credential.                                                                                                                                                                                                                                                                                                                                                                                                |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>`         | [reauthenticateAndRetrieveData](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticateAndRetrieveData(com.google.firebase.auth.AuthCredential))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)` credential)` Reauthenticates the user with the given credential, and returns the profile data for that account.                                                                                                                                                                                                                                                                                                                   |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [reload](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reload())`()` Manually refreshes the data of the current user (for example, attached providers, display name, and so on).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [sendEmailVerification](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#sendEmailVerification())`()` Calls [sendEmailVerification](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#sendEmailVerification(com.google.firebase.auth.ActionCodeSettings)) with null `actionCodeSettings`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [sendEmailVerification](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#sendEmailVerification(com.google.firebase.auth.ActionCodeSettings))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings)` actionCodeSettings)` Initiates email verification for the user.                                                                                                                                                                                                                                                                                                                                                                       |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>`         | [startActivityForLinkWithProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#startActivityForLinkWithProvider(android.app.Activity,com.google.firebase.auth.FederatedAuthProvider))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Activity](https://developer.android.com/reference/android/app/Activity.html)` activity,` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FederatedAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider)` federatedAuthProvider` `)` Links the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) to the given `provider`.                                  |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>`         | [startActivityForReauthenticateWithProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#startActivityForReauthenticateWithProvider(android.app.Activity,com.google.firebase.auth.FederatedAuthProvider))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Activity](https://developer.android.com/reference/android/app/Activity.html)` activity,` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FederatedAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider)` federatedAuthProvider` `)` Reauthenticates the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) using the given `provider`. |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>`         | [unlink](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#unlink(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` provider)` Detaches credentials from a given provider type from this user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | ~~[updateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String))~~`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` email)` **This method is deprecated.** Use [verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String)) instead. <br />                                                                                                                                                                                                                                                                                                      |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [updatePassword](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updatePassword(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` password)` Updates the password of the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [updatePhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updatePhoneNumber(com.google.firebase.auth.PhoneAuthCredential))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[PhoneAuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthCredential)` credential)` Updates the phone number of the user.                                                                                                                                                                                                                                                                                                                                                                                         |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [updateProfile](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[UserProfileChangeRequest](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest)` request)` Updates the user profile information.                                                                                                                                                                                                                                                                                                                                                                                     |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` newEmail)` Calls [verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)) without any ` actionCodeSettings`.                                                                                                                                                                                                                                             |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                          | [verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` newEmail,` ` @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings)` actionCodeSettings` `)` Sends a verification email to `newEmail`.                                                                                                                                                            |

|                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `static final int` | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `static final int` | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                                                                                                                                                                                  ### Inherited methods                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `abstract int`  | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()`                                                                                                     | | `abstract void` | [writeToParcel](https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int))`(`[Parcel](https://developer.android.com/reference/android/os/Parcel.html)` p, int p1)` | |
| From [com.google.firebase.auth.UserInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo) |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `abstract boolean` | [isEmailVerified](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo#isEmailVerified())`()` Returns `true` if the user's email is verified. |                                                                                                                                                                                                                                                                             |

## Public constructors

### FirebaseUser

```
publicÂ FirebaseUser()
```  

## Public methods

### delete

```
publicÂ @NonNull Task<Void>Â delete()
```

Deletes the user record from your Firebase project's database. If the operation is successful, the user will be signed out.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)).
Exceptions

- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException) thrown if the user's last sign-in time does not meet the security threshold. Use [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)) to resolve. This does not apply if the user is anonymous.  

### getDisplayName

```
publicÂ abstractÂ @Nullable StringÂ getDisplayName()
```

Returns the main display name of this user from the Firebase project's user database. Unlike the display name property from instances of [UserInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo) corresponding to authentication providers (like Google Sign-In), which is not modifiable, this name can be updated at any time by calling [updateProfile](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)).

This field will be automatically populated on account creation if the [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) used on [signInWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) contained such information.  

|                                                                                  See also                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [updateProfile](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)) |   |

### getEmail

```
publicÂ abstractÂ @Nullable StringÂ getEmail()
```

Returns the main email address of the user, as stored in the Firebase project's user database. Unlike the email property from instances of [UserInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo) corresponding to authentication providers (like GitHub), which is not modifiable, this email address can be updated at any time by calling [updateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String)).

This field will be automatically populated on account creation if the [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) used on [signInWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) contained such information, or if the account was created with [createUserWithEmailAndPassword](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)). However, this is not true if the setting "Multiple Accounts per Email" is enabled in the Firebase Console - in that case this will be null unless the account was created with [createUserWithEmailAndPassword](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#createUserWithEmailAndPassword(java.lang.String,java.lang.String)) or [updateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String)) has been called.

If the user also has a password, this email address can be used to sign in into the account using [signInWithEmailAndPassword](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithEmailAndPassword(java.lang.String,java.lang.String)).

This email address is displayed in the Users section of the Firebase console.  

|                                                               See also                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------|---|
| [updateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String)) |   |

### getIdToken

```
publicÂ @NonNull Task<GetTokenResult>Â getIdToken(booleanÂ forceRefresh)
```

Fetches a Firebase Auth ID Token for the user; useful when authenticating against your own backend. Use our server SDKs or follow the official documentation to securely verify the integrity and validity of this token.
Exceptions

- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) if `forceRefresh == true`, thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid

|       Parameters       |
|------------------------|--------------------------------------------------------------------------------------------------|
| `boolean forceRefresh` | force refreshes the token. Should only be set to `true` if the token is invalidated out of band. |

|                                                                                                                                                  Returns                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[GetTokenResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult)`>` | a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with the [com.google.firebase.auth.GetTokenResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult) |

### getMetadata

```
publicÂ abstractÂ @Nullable FirebaseUserMetadataÂ getMetadata()
```

Returns the [FirebaseUserMetadata](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata) associated with this user.  

### getMultiFactor

```
publicÂ abstractÂ @NonNull MultiFactorÂ getMultiFactor()
```

Returns a [MultiFactor](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor) instance which is the main entry point for multi-factor related operations on this user.  

### getPhoneNumber

```
publicÂ abstractÂ @Nullable StringÂ getPhoneNumber()
```

Returns the phone number of the user, as stored in the Firebase project's user database, or `null` if none exists. This can be updated at any time by calling [updatePhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updatePhoneNumber(com.google.firebase.auth.PhoneAuthCredential)).

This field will be automatically populated on account creation if the [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) used on [signInWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) contained such information. This phone number is displayed in the Users section of the Firebase console.  

|                                                                                   See also                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [updatePhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updatePhoneNumber(com.google.firebase.auth.PhoneAuthCredential)) |   |

### getPhotoUrl

```
publicÂ abstractÂ @Nullable UriÂ getPhotoUrl()
```

Returns the URL of this user's main profile picture, as stored in the Firebase project's user database. Unlike the profile URL property from instances of [UserInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo) corresponding to authentication providers (like Facebook Login), which is not modifiable, this URL can be updated at any time by calling [updateProfile](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)).

This field will be automatically populated on account creation if the [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) used on [signInWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) contained such information.  

|                                                                                  See also                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [updateProfile](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateProfile(com.google.firebase.auth.UserProfileChangeRequest)) |   |

### getProviderData

```
publicÂ abstractÂ @NonNull List<UserInfo>Â getProviderData()
```

Returns a [List](https://developer.android.com/reference/java/util/List.html) of [UserInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserInfo) objects that represents the linked identities of the user using different authentication providers that may be linked to their account. Use this to access, for example, your user's basic profile information retrieved from Facebook whether or not the user used Facebook Login to sign in to the current session.  

### getProviderId

```
publicÂ abstractÂ @NonNull StringÂ getProviderId()
```

Always returns [PROVIDER_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthProvider#PROVIDER_ID()).  

### getTenantId

```
publicÂ abstractÂ @Nullable StringÂ getTenantId()
```

Returns the tenant ID of the current user or `null` if this user isn't associated with a tenant project.  

### getUid

```
publicÂ abstractÂ @NonNull StringÂ getUid()
```

Returns a string used to uniquely identify your user in your Firebase project's user database. Use it when storing information in Firebase Database or Storage, or even in your own backend.

This identifier is opaque and does not correspond necessarily to the user's email address or any other field.  

### isAnonymous

```
publicÂ abstractÂ booleanÂ isAnonymous()
```

Returns true if the user is anonymous; that is, the user account was created with [signInAnonymously](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInAnonymously()) and has not been linked to another account with [linkWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).  

### linkWithCredential

```
publicÂ @NonNull Task<AuthResult>Â linkWithCredential(@NonNull AuthCredentialÂ credential)
```

Attaches the given [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) to the user. This allows the user to sign in to this account in the future with credentials for such provider.
Exceptions

- [FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException) thrown if `credential instanceof
  EmailAuthCredential` and the password is not strong enough
- [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) thrown if the `credential` is malformed or expired
- [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException) thrown if there is another user account associated with the given `credential`
- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException) thrown if `credential instanceof
  EmailAuthCredential` and if the user's last sign-in time does not meet the security threshold. Use [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)) to resolve. This does not apply if the user is anonymous.
- [FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) thrown if there is an attempt to link a provider that is already linked to this account or if an internal error occurs

|                                                                                                     Parameters                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)` credential` | a valid credential of a type not yet linked to this user |

|                                                                                                                                              Returns                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) of [AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult) |

### reauthenticate

```
publicÂ @NonNull Task<Void>Â reauthenticate(@NonNull AuthCredentialÂ credential)
```

Reauthenticates the user with the given credential. This is useful for operations that require a recent sign-in, to prevent or resolve a [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException).
Exceptions

- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled or deleted
- [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) thrown if the `credential` is malformed or has expired, or if it corresponds to another existing user's account. Inspect the error code to desambiguate.

|                                                                                                     Parameters                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)` credential` | authentication credential that must be valid for the current user. |

### reauthenticateAndRetrieveData

```
publicÂ @NonNull Task<AuthResult>Â reauthenticateAndRetrieveData(@NonNull AuthCredentialÂ credential)
```

Reauthenticates the user with the given credential, and returns the profile data for that account. This is useful for operations that require a recent sign-in, to prevent or resolve a [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException).
Exceptions

- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled or deleted
- [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) thrown if the `credential` is malformed or has expired, or if it corresponds to another existing user's account. Inspect the error code to desambiguate.

|                                                                                                     Parameters                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential)` credential` | authentication credential that must be valid for the current user. |

|                                                                                                                                              Returns                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>` | [AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult) containing the [FirebaseUser](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser) reference and . |

### reload

```
publicÂ @NonNull Task<Void>Â reload()
```

Manually refreshes the data of the current user (for example, attached providers, display name, and so on).
Exceptions

- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid  

### sendEmailVerification

```
publicÂ @NonNull Task<Void>Â sendEmailVerification()
```

Calls [sendEmailVerification](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#sendEmailVerification(com.google.firebase.auth.ActionCodeSettings)) with null `actionCodeSettings`.  

### sendEmailVerification

```
publicÂ @NonNull Task<Void>Â sendEmailVerification(@NonNull ActionCodeSettingsÂ actionCodeSettings)
```

Initiates email verification for the user. Takes in an [ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings) to allow linking back to your app in the email.  

|                                                                                                                             Returns                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) to track completion of the sending operation. |

### startActivityForLinkWithProvider

```
publicÂ @NonNull Task<AuthResult>Â startActivityForLinkWithProvider(
Â Â Â Â @NonNull ActivityÂ activity,
Â Â Â Â @NonNull FederatedAuthProviderÂ federatedAuthProvider
)
```

Links the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) to the given `provider`. If the calling activity dies during this operation, use [getPendingAuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getPendingAuthResult()) to get the outcome of this operation.

Note: this call has a UI associated with it, unlike the majority of calls in FirebaseAuth.
Exceptions

- [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) thrown if the credential generated from the flow is malformed or expired.
- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the user has been disabled by an administrator.
- [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException) thrown if the email that keys the user that is signing in is already in use.
- [FirebaseAuthWebException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWebException) thrown if there is an operation already in progress, the pending operation was canceled, there is a problem with 3rd party cookies in the browser, or some other error in the web context has occurred.
- [FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) thrown if signing in via this method has been disabled in the Firebase Console, or if the `provider` passed is configured improperly.

|                                                                                                                 Parameters                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Activity](https://developer.android.com/reference/android/app/Activity.html)` activity`                                                           | the current [Activity](https://developer.android.com/reference/android/app/Activity.html) that you intent to launch this flow from                                                                                |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FederatedAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider)` federatedAuthProvider` | an [FederatedAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider) configured with information about the provider that you intend to link to the user. |

|                                                                                                                                              Returns                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>` | a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with a reference to an [AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult) with user information upon success |

### startActivityForReauthenticateWithProvider

```
publicÂ @NonNull Task<AuthResult>Â startActivityForReauthenticateWithProvider(
Â Â Â Â @NonNull ActivityÂ activity,
Â Â Â Â @NonNull FederatedAuthProviderÂ federatedAuthProvider
)
```

Reauthenticates the user using the mobile browser (either a Custom Chrome Tab or the device's default browser) using the given `provider`. If the calling activity dies during this operation, use [getPendingAuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#getPendingAuthResult()) to get the outcome of this operation.

Note: this call has a UI associated with it, unlike the majority of calls in FirebaseAuth.
Exceptions

- [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) thrown if the credential generated from the flow is malformed or expired.
- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the user has been disabled by an administrator.
- [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException) thrown if the email that keys the user that is signing in is already in use.
- [FirebaseAuthWebException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWebException) thrown if there is an operation already in progress, the pending operation was canceled, there is a problem with 3rd party cookies in the browser, or some other error in the web context has occurred.
- [FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) thrown if signing in via this method has been disabled in the Firebase Console, or if the `provider` passed is configured improperly.

|                                                                                                                 Parameters                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Activity](https://developer.android.com/reference/android/app/Activity.html)` activity`                                                           | the current [Activity](https://developer.android.com/reference/android/app/Activity.html) that you intent to launch this flow from                                                                         |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[FederatedAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider)` federatedAuthProvider` | an [FederatedAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FederatedAuthProvider) configured with information about how you intend the user to reauthenticate. |

|                                                                                                                                              Returns                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>` | a [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) with a reference to an [AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult) with user information upon success |

### unlink

```
publicÂ @NonNull Task<AuthResult>Â unlink(@NonNull StringÂ provider)
```

Detaches credentials from a given provider type from this user. This prevents the user from signing in to this account in the future with credentials from such provider.
Exceptions

- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid

|                                                                                 Parameters                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` provider` | a unique identifier of the type of provider to be unlinked, for example, [PROVIDER_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID()). |

|                                                                                                                                              Returns                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult)`>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) of [AuthResult](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthResult) |

### updateEmail

```
publicÂ @NonNull Task<Void>Â [updateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#updateEmail(java.lang.String))(@NonNull StringÂ email)
```
| **This method is deprecated.**   
|
| Use [verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String)) instead.

Updates the email address of the user.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)).

In addition, note that the original email address recipient will receive an email that allows them to revoke the email address change, in order to protect them from account hijacking.
Exceptions

- [FirebaseAuthInvalidCredentialsException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidCredentialsException) thrown if the `email` address is malformed
- [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException) thrown if there already exists an account with the given `email` address
- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException) thrown if the user's last sign-in time does not meet the security threshold. Use [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)) to resolve. This does not apply if the user is anonymous.
- [FirebaseAuthException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthException) thrown with code OPERATION_NOT_ALLOWED if [Email Enumeration Protection](https://cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) is enabled.  

### updatePassword

```
publicÂ @NonNull Task<Void>Â updatePassword(@NonNull StringÂ password)
```

Updates the password of the user.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)).

Anonymous users who update both their email and password will no longer be anonymous. They will be able to log in with these credentials.
Exceptions

- [FirebaseAuthWeakPasswordException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthWeakPasswordException) thrown if the password is not strong enough
- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException) thrown if the user's last sign-in time does not meet the security threshold. Use [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)) to resolve. This does not apply if the user is anonymous.  

### updatePhoneNumber

```
publicÂ @NonNull Task<Void>Â updatePhoneNumber(@NonNull PhoneAuthCredentialÂ credential)
```

Updates the phone number of the user.

**Important:** this is a security sensitive operation that requires the user to have recently signed in. If this requirement isn't met, ask the user to authenticate again and later call [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)).
Exceptions

- [FirebaseAuthUserCollisionException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthUserCollisionException) thrown if there already exists an account with the given phone number
- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid
- [FirebaseAuthRecentLoginRequiredException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthRecentLoginRequiredException) thrown if the user's last sign-in time does not meet the security threshold. Use [reauthenticate](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#reauthenticate(com.google.firebase.auth.AuthCredential)) to resolve. This does not apply if the user is anonymous.  

### updateProfile

```
publicÂ @NonNull Task<Void>Â updateProfile(@NonNull UserProfileChangeRequestÂ request)
```

Updates the user profile information. Use [UserProfileChangeRequest.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.Builder) to construct the request.
Exceptions

- [FirebaseAuthInvalidUserException](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuthInvalidUserException) thrown if the current user's account has been disabled, deleted, or its credentials are no longer valid  

### verifyBeforeUpdateEmail

```
publicÂ @NonNull Task<Void>Â verifyBeforeUpdateEmail(@NonNull StringÂ newEmail)
```

Calls [verifyBeforeUpdateEmail](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#verifyBeforeUpdateEmail(java.lang.String,com.google.firebase.auth.ActionCodeSettings)) without any `
actionCodeSettings`.  

### verifyBeforeUpdateEmail

```
publicÂ @NonNull Task<Void>Â verifyBeforeUpdateEmail(
Â Â Â Â @NonNull StringÂ newEmail,
Â Â Â Â @Nullable ActionCodeSettingsÂ actionCodeSettings
)
```

Sends a verification email to `newEmail`. Upon redemption of the link in the email, this user's email will be changed to `newEmail` and that email will be marked verified.  

|                                                                                                              Parameters                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` newEmail`                                                          | the user's new email                                                                                                                                                                    |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings)` actionCodeSettings` | the optional [ActionCodeSettings](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings) object to allow linking back to your app in the email |

|                                                                                                                             Returns                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>` | [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html) to track completion of the sending operation. |