# Source: https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user.md.txt

# Firebase.Auth.FirebaseUser Class Reference

# Firebase.Auth.FirebaseUser

[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) user account object.

## Summary

This class allows you to manipulate the profile of a user, link to and unlink from authentication providers, and refresh authentication tokens.

### Inheritance

Inherits from: [Firebase.Auth.UserInfoInterface](https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-info-interface)

|                                                                                                                                                                                                                                       ### Properties                                                                                                                                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DisplayName](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a96557dd160b049f9ece8eb8a7cfd47ad)     | `string` Gets the display name associated with the user, if any.                                                                                                                                                                                                                                       |
| [Email](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a9e720f9e532ed02c4682af1bd944b2b6)           | `string` Gets email associated with the user, if any.                                                                                                                                                                                                                                                  |
| [IsAnonymous](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a497fb5b6e375fe95818d62ca13c8a470)     | `bool` Returns true if user signed in anonymously.                                                                                                                                                                                                                                                     |
| [IsEmailVerified](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a4b529a149fc66466b8d616ea7a38abd1) | `bool` Returns true if the email address associated with this user has been verified.                                                                                                                                                                                                                  |
| [Metadata](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a8e52ed88732bf5f98e1d2830c635fee6)        | [UserMetadata](https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-metadata#class_firebase_1_1_auth_1_1_user_metadata) Gets the metadata for this user account.                                                                                                                  |
| [PhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1ab356a1dd64ae1225aa5f755f583a688d)     | `string` Gets the phone number for the user, in E.164 format.                                                                                                                                                                                                                                          |
| [PhotoUrl](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a86cf3b31b5395324a57919c006db2fb3)        | `System.Uri` The photo url associated with the user, if any.                                                                                                                                                                                                                                           |
| [ProviderData](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a7b1e550bbd0a347051263c802723c2e3)    | `System.Collections.Generic.IEnumerable< `[IUserInfo](https://firebase.google.com/docs/reference/unity/interface/firebase/auth/i-user-info#interface_firebase_1_1_auth_1_1_i_user_info)` >` Gets the third party profile data associated with this user returned by the authentication server, if any. |
| [ProviderId](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1add0beea29b9714af8249fb2435e4ce0e)      | `string` Gets the provider ID for the user (For example, "Facebook").                                                                                                                                                                                                                                  |
| [UserId](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a656c442dc88d5059100b4cf5bcfedcee)          | `string` Gets the unique [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) user ID for the user.                                                                                                                                                      |

|                                                                                                                                                                                                                                                                                                                    ### Public functions                                                                                                                                                                                                                                                                                                                     ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DeleteAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1ab73af96697c0b7f8c7f1d75f09cea50b)`()`                                                                                                                                                                                                         | `System.Threading.Tasks.Task` Deletes the user account.                                                                                                                                                                                                         |
| [IsValid](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a25aeb5ab151dadc5e01b32ee64a9e944)`()`                                                                                                                                                                                                             | `bool` Returns whether this [FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user) object represents a valid user.                                                        |
| [LinkWithCredentialAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1ac723e0d3e1c8130828e43d949827625a)`(`[Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential)` credential)`                                            | `async Task< `[AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result)` >` Associates a user account from a third-party identity provider.                                        |
| [LinkWithProviderAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a353382f71c5482aa87abea48d95df5d0)`(`[FederatedAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-auth-provider#class_firebase_1_1_auth_1_1_federated_auth_provider)` provider)`           | `async Task< `[AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result)` >` Link a user via a federated auth provider.                                                             |
| [ReauthenticateAndRetrieveDataAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1ad665e313850a54d49e4dcdd42fe9d40f)`(`[Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential)` credential)`                                 | `async Task< `[AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result)` >` Reauthenticate using a credential.                                                                     |
| [ReauthenticateAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1aafa69a00d02dce5e9b059fc62173507b)`(`[Credential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/credential#class_firebase_1_1_auth_1_1_credential)` credential)`                                                | `Task` Convenience function for ReauthenticateAndRetrieveData that discards the returned [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info) data. |
| [ReauthenticateWithProviderAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1ad6901082772c216f04f96d8455f7fdb1)`(`[FederatedAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/federated-auth-provider#class_firebase_1_1_auth_1_1_federated_auth_provider)` provider)` | `async Task< `[AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result)` >` Reauthenticate a user via a federated auth provider.                                                   |
| [ReloadAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a0b3aa0fa399fb2fc7e2ebc2ff8926c31)`()`                                                                                                                                                                                                         | `System.Threading.Tasks.Task` Refreshes the data for this user.                                                                                                                                                                                                 |
| [SendEmailVerificationAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a36b7917f2008b0a2aad2d8f9952b2e1f)`()`                                                                                                                                                                                          | `Task` Initiates email verification for the user.                                                                                                                                                                                                               |
| [SendEmailVerificationBeforeUpdatingEmailAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a9e4a57037c46ace7adf48abb7449bba9)`(string email)`                                                                                                                                                           | `Task` Send an email to verify the ownership of the account, then update to the new email.                                                                                                                                                                      |
| [TokenAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a28fec97e9ca1343ffc4c1f7a0f25b664)`(bool forceRefresh)`                                                                                                                                                                                         | `Task< string >` The Java Web Token (JWT) that can be used to identify the user to the backend.                                                                                                                                                                 |
| [UnlinkAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a4b78506f6ec9563cbd29ee330e8a3768)`(string provider)`                                                                                                                                                                                          | `async Task< `[AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result)` >` Unlinks the current user from the provider specified.                                                  |
| [UpdatePasswordAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a860a327839c3f3d00e412ecb4c8837c0)`(string password)`                                                                                                                                                                                  | `Task` Attempts to change the password for the current user.                                                                                                                                                                                                    |
| [UpdatePhoneNumberCredentialAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a3259b0f399768c858be211e9f9f66e3d)`(`[PhoneAuthCredential](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-credential#class_firebase_1_1_auth_1_1_phone_auth_credential)` credential)`    | `async Task< `[FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user)` >` Updates the currently linked phone number on the user.                                           |
| [UpdateUserProfileAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1aace3845cc6ed29facfad3ad1174c2a7c)`(`[UserProfile](https://firebase.google.com/docs/reference/unity/class/firebase/auth/user-profile#class_firebase_1_1_auth_1_1_user_profile)` profile)`                                           | `Task` Updates a subset of user profile information.                                                                                                                                                                                                            |

## Properties

### DisplayName

```c#
string DisplayName
```  
Gets the display name associated with the user, if any.  

### Email

```c#
string Email
```  
Gets email associated with the user, if any.  

### IsAnonymous

```c#
bool IsAnonymous
```  
Returns true if user signed in anonymously.  

### IsEmailVerified

```c#
bool IsEmailVerified
```  
Returns true if the email address associated with this user has been verified.  

### Metadata

```c#
UserMetadata Metadata
```  
Gets the metadata for this user account.  

### PhoneNumber

```c#
string PhoneNumber
```  
Gets the phone number for the user, in E.164 format.  

### PhotoUrl

```c#
System.Uri PhotoUrl
```  
The photo url associated with the user, if any.  

### ProviderData

```c#
System.Collections.Generic.IEnumerable< IUserInfo > ProviderData
```  
Gets the third party profile data associated with this user returned by the authentication server, if any.  

### ProviderId

```c#
string ProviderId
```  
Gets the provider ID for the user (For example, "Facebook").  

### UserId

```c#
string UserId
```  
Gets the unique [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) user ID for the user.


| **Note:** The user's ID, unique to the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) project. Do NOT use this value to authenticate with your backend server, if you have one. Use [FirebaseUser.TokenAsync](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user_1a28fec97e9ca1343ffc4c1f7a0f25b664) instead.

<br />

## Public functions

### DeleteAsync

```c#
System.Threading.Tasks.Task DeleteAsync()
```  
Deletes the user account.  

### IsValid

```c#
bool IsValid()
```  
Returns whether this [FirebaseUser](https://firebase.google.com/docs/reference/unity/class/firebase/auth/firebase-user#class_firebase_1_1_auth_1_1_firebase_user) object represents a valid user.

Could be false on FirebaseUsers contained with [AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result) structures from failed [Auth](https://firebase.google.com/docs/reference/unity/namespace/firebase/auth#namespace_firebase_1_1_auth) operations.  

### LinkWithCredentialAsync

```c#
async Task< AuthResult > LinkWithCredentialAsync(
  Credential credential
)
```  
Associates a user account from a third-party identity provider.  

### LinkWithProviderAsync

```c#
async Task< AuthResult > LinkWithProviderAsync(
  FederatedAuthProvider provider
)
```  
Link a user via a federated auth provider.


| **Note:** : This operation is supported only on iOS, tvOS and Android platforms. On other platforms this method will return a Future with a preset error code: kAuthErrorUnimplemented.

<br />

### ReauthenticateAndRetrieveDataAsync

```c#
async Task< AuthResult > ReauthenticateAndRetrieveDataAsync(
  Credential credential
)
```  
Reauthenticate using a credential.

Data from the Identity Provider used to sign-in is returned in the [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info) inside the returned [AuthResult](https://firebase.google.com/docs/reference/unity/class/firebase/auth/auth-result#class_firebase_1_1_auth_1_1_auth_result).

Returns an error if the existing credential is not for this user or if sign-in with that credential failed.


| **Note:** : The current user may be signed out if this operation fails on Android and desktop platforms.

<br />

### ReauthenticateAsync

```c#
Task ReauthenticateAsync(
  Credential credential
)
```  
Convenience function for ReauthenticateAndRetrieveData that discards the returned [AdditionalUserInfo](https://firebase.google.com/docs/reference/unity/class/firebase/auth/additional-user-info#class_firebase_1_1_auth_1_1_additional_user_info) data.  

### ReauthenticateWithProviderAsync

```c#
async Task< AuthResult > ReauthenticateWithProviderAsync(
  FederatedAuthProvider provider
)
```  
Reauthenticate a user via a federated auth provider.


| **Note:** : This operation is supported only on iOS, tvOS and Android platforms. On other platforms this method will return a Future with a preset error code: kAuthErrorUnimplemented.

<br />

### ReloadAsync

```c#
System.Threading.Tasks.Task ReloadAsync()
```  
Refreshes the data for this user.

For example, the attached providers, email address, display name, etc.  

### SendEmailVerificationAsync

```c#
Task SendEmailVerificationAsync()
```  
Initiates email verification for the user.  

### SendEmailVerificationBeforeUpdatingEmailAsync

```c#
Task SendEmailVerificationBeforeUpdatingEmailAsync(
  string email
)
```  
Send an email to verify the ownership of the account, then update to the new email.  

### TokenAsync

```c#
Task< string > TokenAsync(
  bool forceRefresh
)
```  
The Java Web Token (JWT) that can be used to identify the user to the backend.

If a current ID token is still believed to be valid (i.e. it has not yet expired), that token will be returned immediately. A developer may set the optional force_refresh flag to get a new ID token, whether or not the existing token has expired. For example, a developer may use this when they have discovered that the token is invalid for some other reason.  

### UnlinkAsync

```c#
async Task< AuthResult > UnlinkAsync(
  string provider
)
```  
Unlinks the current user from the provider specified.

Status will be an error if the user is not linked to the given provider.  

### UpdatePasswordAsync

```c#
Task UpdatePasswordAsync(
  string password
)
```  
Attempts to change the password for the current user.

For an account linked to an Identity Provider (IDP) with no password, this will result in the account becoming an email/password-based account while maintaining the IDP link. May fail if the password is invalid, if there is a conflicting email/password-based account, or if the token has expired. To retrieve fresh tokens, call ReauthenticateAsync.  

### UpdatePhoneNumberCredentialAsync

```c#
async Task< FirebaseUser > UpdatePhoneNumberCredentialAsync(
  PhoneAuthCredential credential
)
```  
Updates the currently linked phone number on the user.

This is useful when a user wants to change their phone number. It is a shortcut to calling `UnlinkAsync(phoneCredential.Provider)` and then `LinkWithCredentialAsync(phoneCredential)`. `phoneCredential` must have been created with [PhoneAuthProvider](https://firebase.google.com/docs/reference/unity/class/firebase/auth/phone-auth-provider#class_firebase_1_1_auth_1_1_phone_auth_provider).  

### UpdateUserProfileAsync

```c#
Task UpdateUserProfileAsync(
  UserProfile profile
)
```  
Updates a subset of user profile information.