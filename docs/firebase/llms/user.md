# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user.md.txt

# firebase::auth::User Class Reference

# firebase::auth::User


`#include <user.h>`

Firebase user account object.

## Summary

This class allows you to manipulate the profile of a user, link to and unlink from authentication providers, and refresh authentication tokens.

### Inheritance

Inherits from: [firebase::auth::UserInfoInterface](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface)

| ### Constructors and Destructors ||
|---|---|
| [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a359b14bc4d9a397eeae997ff1414a495)`()` ||
| [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1abc3154a55ebc56240edbebe8240340c8)`(const `[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user)` &)` Copy constructor. ||
| [~User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1af3ddbd47ef7f5b6725289b3692af8197)`()` ||

|                                                                                                                                                                                                                                                                                                                                                             ### Public functions                                                                                                                                                                                                                                                                                                                                                              ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Delete](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ab025baf16a575581c7be262650b504fb)`()`                                                                                                                                                                                                             | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Deletes the user account.                                                                                                                                                                                                                              |
| [DeleteLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a5b9baf5b55e4e21aafd609e0d4422b30)`() const `                                                                                                                                                                                            | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get results of the most recent call to Delete.                                                                                                                                                                                                         |
| [GetToken](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a2214a2f314fd251bad6f318ec9eab22d)`(bool force_refresh)`                                                                                                                                                                                         | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< std::string >` The Java Web Token (JWT) that can be used to identify the user to the backend.                                                                                                                                                                  |
| [GetTokenLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1acd83b244deab7d1ac11785a3846e4e34)`() const `                                                                                                                                                                                          | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< std::string >` Get results of the most recent call to GetToken.                                                                                                                                                                                                |
| [LinkWithCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ac19c2856d0f0678109d9883dda58bc13)`(const `[Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential)` & credential)`                                            | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >` Links the user with the given 3rd party credentials.                                                                 |
| [LinkWithCredentialLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1aebf302d5f35d82a69164c807e8cf1f49)`() const `                                                                                                                                                                                | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >` Get results of the most recent call to LinkWithCredential.                                                           |
| [LinkWithProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a21ac8cf2e5b915dfd426c4fd707707c2)`(`[FederatedAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider#classfirebase_1_1auth_1_1_federated_auth_provider)` *provider) const `           | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >`                                                                                                                      |
| [Reauthenticate](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ad27c68266217f7c8ef56f969d482d2a5)`(const `[Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential)` & credential)`                                                | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Convenience function for ReauthenticateAndRetrieveData that discards the returned [AdditionalUserInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info) data. |
| [ReauthenticateAndRetrieveData](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a2570b91301f6785a9195e5d08fcc6127)`(const `[Credential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/credential#classfirebase_1_1auth_1_1_credential)` & credential)`                                 | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >` Reauthenticate using a credential.                                                                                   |
| [ReauthenticateAndRetrieveDataLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1abfe9775cfc3a497ee641095a5c99ffa8)`() const `                                                                                                                                                                     | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >` Get results of the most recent call to ReauthenticateAndRetrieveData.                                                |
| [ReauthenticateLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ae6f5ac19125a5748dc7f452de4248813)`() const `                                                                                                                                                                                    | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get results of the most recent call to Reauthenticate.                                                                                                                                                                                                 |
| [ReauthenticateWithProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ad7501eae0b2c22c96edabacb13176bf6)`(`[FederatedAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/federated-auth-provider#classfirebase_1_1auth_1_1_federated_auth_provider)` *provider) const ` | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >` Re-authenticates the user with a federated auth provider.                                                            |
| [Reload](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a9e1e90b228576a46c04c8b080ffcaa5b)`()`                                                                                                                                                                                                             | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Refreshes the data for this user.                                                                                                                                                                                                                      |
| [ReloadLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a977eec44388c398b2712bf3b5906a87d)`() const `                                                                                                                                                                                            | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get results of the most recent call to Reload.                                                                                                                                                                                                         |
| [SendEmailVerification](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a358f5f231e9d5a27dabb706db2dd59f0)`()`                                                                                                                                                                                              | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Initiates email verification for the user.                                                                                                                                                                                                             |
| [SendEmailVerificationBeforeUpdatingEmail](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a75d92f3aa48644796c7cff891bad363b)`(const char *email)`                                                                                                                                                          | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Send an email to verify the ownership of the account, then update to the new email.                                                                                                                                                                    |
| [SendEmailVerificationBeforeUpdatingEmailLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a9d3e6a1b6e088825745dfbdc1635cbdd)`() const `                                                                                                                                                          | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get results of the most recent call to SendEmailVerificationBeforeUpdatingEmail.                                                                                                                                                                       |
| [SendEmailVerificationLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a51c7728af6484560be5b823e1d078768)`() const `                                                                                                                                                                             | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get results of the most recent call to SendEmailVerification.                                                                                                                                                                                          |
| [Unlink](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a98e6cdc33039cbea4d80aa23bd9c6091)`(const char *provider)`                                                                                                                                                                                         | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >` Unlinks the current user from the provider specified.                                                                |
| [UnlinkLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1aca6bb736ffd4659ada882ed0d677a087)`() const `                                                                                                                                                                                            | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result)` >` Get results of the most recent call to Unlink.                                                                       |
| [UpdatePassword](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a53aa1dc77b04ddee678c8163142b6ee0)`(const char *password)`                                                                                                                                                                                 | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Attempts to change the password for the current user.                                                                                                                                                                                                  |
| [UpdatePasswordLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ac955f02f29f453b6ff5cde53d298c0cb)`() const `                                                                                                                                                                                    | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get results of the most recent call to UpdatePassword.                                                                                                                                                                                                 |
| [UpdatePhoneNumberCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1aa794baa1e56ac55ed59c0ee348cc5ee1)`(const `[PhoneAuthCredential](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-credential#classfirebase_1_1auth_1_1_phone_auth_credential)` & credential)`    | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user)` >` Updates the currently linked phone number on the user.                                                                                     |
| [UpdatePhoneNumberCredentialLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a9055caed6899a2a58bddf512ad5f934c)`() const `                                                                                                                                                                       | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< `[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user)` >` Get results of the most recent call to UpdatePhoneNumberCredential.                                                                        |
| [UpdateUserProfile](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a28ff1771991dbcee97a6d99e84ba0f6d)`(const `[UserProfile](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile#structfirebase_1_1auth_1_1_user_1_1_user_profile)` & profile)`                           | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Updates a subset of user profile information.                                                                                                                                                                                                          |
| [UpdateUserProfileLastResult](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a0bfa29b3ea21a74caf10173ffc2c7ae5)`() const `                                                                                                                                                                                 | [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get results of the most recent call to UpdateUserProfile.                                                                                                                                                                                              |
| [display_name](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a3ac9fa0112f381ed06d358eef133a443)`() const `                                                                                                                                                                                                | `virtual std::string` Gets the display name associated with the user, if any.                                                                                                                                                                                                                                                                                            |
| [email](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1af38240e6531dfcde92e0b53319e608e6)`() const `                                                                                                                                                                                                       | `virtual std::string` Gets email associated with the user, if any.                                                                                                                                                                                                                                                                                                       |
| [is_anonymous](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a951d793cf52d5c838361ea83a635f474)`() const `                                                                                                                                                                                                | `bool` Returns true if user signed in anonymously.                                                                                                                                                                                                                                                                                                                       |
| [is_email_verified](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1add2594ac1bd5389f57cb94bd46960621)`() const `                                                                                                                                                                                           | `bool` Returns true if the email address associated with this user has been verified.                                                                                                                                                                                                                                                                                    |
| [is_valid](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ae18ea22f23bba968c3b204051607df69)`() const `                                                                                                                                                                                                    | `bool` Returns whether this [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) object represents a valid user.                                                                                                                                                                                               |
| [metadata](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a878521381152ae73b443f44bc37c638c)`() const `                                                                                                                                                                                                    | [UserMetadata](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user-metadata#structfirebase_1_1auth_1_1_user_metadata) Gets the metadata for this user account.                                                                                                                                                                                      |
| [operator!=](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ab4045c8dcf89c0895be0a0d1b60a7a60)`(const `[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user)` &) const `                                                                          | `bool` Inequality operator.                                                                                                                                                                                                                                                                                                                                              |
| [operator=](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ae40f97e5b7d1d2cc329390ad2a6a2837)`(const `[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user)` &)`                                                                                  | [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user)` &` Assignment operator.                                                                                                                                                                                                                                  |
| [operator==](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1aaf02545c702a07fbaefc4e11a58dbee6)`(const `[User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user)` &) const `                                                                          | `bool` Equality operator.                                                                                                                                                                                                                                                                                                                                                |
| [phone_number](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1ab2b543b3e4334285ab5e45d72183ca4f)`() const `                                                                                                                                                                                                | `virtual std::string` Gets the phone number for the user, in E.164 format.                                                                                                                                                                                                                                                                                               |
| [photo_url](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1af34b736efb83f096e19c39ef7522f896)`() const `                                                                                                                                                                                                   | `virtual std::string` Gets the photo url associated with the user, if any.                                                                                                                                                                                                                                                                                               |
| [provider_data](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a86445f575082892f47393f3bef209a89)`() const `                                                                                                                                                                                               | `std::vector< `[UserInfoInterface](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user-info-interface#classfirebase_1_1auth_1_1_user_info_interface)` >` Gets the third party profile data associated with this user returned by the authentication server, if any.                                                                                  |
| [provider_id](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1abec5fa1ee6f4a95a5eab1d2e427a2870)`() const `                                                                                                                                                                                                 | `virtual std::string` Gets the provider ID for the user (For example, "Facebook").                                                                                                                                                                                                                                                                                       |
| [uid](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1aebcd5ae2fab90c792721ea32071107db)`() const `                                                                                                                                                                                                         | `virtual std::string` Gets the unique Firebase user ID for the user.                                                                                                                                                                                                                                                                                                     |

|                                                                                                                                                       ### Structs                                                                                                                                                        ||
|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [firebase::auth::User::UserProfile](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/user/user-profile) | Parameters to the [UpdateUserProfile()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a28ff1771991dbcee97a6d99e84ba0f6d) function. |

## Public functions

### Delete

```c++
Future< void > Delete()
```  
Deletes the user account.  

### DeleteLastResult

```c++
Future< void > DeleteLastResult() const 
```  
Get results of the most recent call to Delete.  

### GetToken

```c++
Future< std::string > GetToken(
  bool force_refresh
)
```  
The Java Web Token (JWT) that can be used to identify the user to the backend.

If a current ID token is still believed to be valid (i.e. it has not yet expired), that token will be returned immediately. A developer may set the optional force_refresh flag to get a new ID token, whether or not the existing token has expired. For example, a developer may use this when they have discovered that the token is invalid for some other reason.  

### GetTokenLastResult

```c++
Future< std::string > GetTokenLastResult() const 
```  
Get results of the most recent call to GetToken.  

### LinkWithCredential

```c++
Future< AuthResult > LinkWithCredential(
  const Credential & credential
)
```  
Links the user with the given 3rd party credentials.

For example, a Facebook login access token, a Twitter token/token-secret pair.

Status will be an error if the token is invalid, expired, or otherwise not accepted by the server as well as if the given 3rd party user id is already linked with another user account or if the current user is already linked with another id from the same provider.

Data from the Identity Provider used to sign-in is returned in the [AdditionalUserInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info) inside [AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result).  

### LinkWithCredentialLastResult

```c++
Future< AuthResult > LinkWithCredentialLastResult() const 
```  
Get results of the most recent call to LinkWithCredential.  

### LinkWithProvider

```c++
Future< AuthResult > LinkWithProvider(
  FederatedAuthProvider *provider
) const 
```  

| **Note:** : This operation is supported only on iOS, tvOS and Android platforms. On other platforms this method will return a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) with a preset error code: kAuthErrorUnimplemented.

<br />

|                                                                            Details                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|---------------------------------------------------------| | `provider` | Contains information on the auth provider to link with. | |
| **Returns** | A Future with the user data result of the link request.                                                                                           |

### Reauthenticate

```c++
Future< void > Reauthenticate(
  const Credential & credential
)
```  
Convenience function for ReauthenticateAndRetrieveData that discards the returned [AdditionalUserInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info) data.  

### ReauthenticateAndRetrieveData

```c++
Future< AuthResult > ReauthenticateAndRetrieveData(
  const Credential & credential
)
```  
Reauthenticate using a credential.

Some APIs (for example, UpdatePassword, Delete) require that the token used to invoke them be from a recent login attempt. This API takes an existing credential for the user and retrieves fresh tokens, ensuring that the operation can proceed. Developers can call this method prior to calling [UpdatePassword()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a53aa1dc77b04ddee678c8163142b6ee0) to ensure success.

Data from the Identity Provider used to sign-in is returned in the [AdditionalUserInfo](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/additional-user-info#structfirebase_1_1auth_1_1_additional_user_info) inside the returned [AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result).

Returns an error if the existing credential is not for this user or if sign-in with that credential failed.


| **Note:** : The current user may be signed out if this operation fails on Android and desktop platforms.

<br />

### ReauthenticateAndRetrieveDataLastResult

```c++
Future< AuthResult > ReauthenticateAndRetrieveDataLastResult() const 
```  
Get results of the most recent call to ReauthenticateAndRetrieveData.  

### ReauthenticateLastResult

```c++
Future< void > ReauthenticateLastResult() const 
```  
Get results of the most recent call to Reauthenticate.  

### ReauthenticateWithProvider

```c++
Future< AuthResult > ReauthenticateWithProvider(
  FederatedAuthProvider *provider
) const 
```  
Re-authenticates the user with a federated auth provider.


| **Note:** : This operation is supported only on iOS, tvOS and Android platforms. On other platforms this method will return a [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) with a preset error code: kAuthErrorUnimplemented.

<br />

|                                                                                    Details                                                                                     ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|-----------------------------------------------------------------| | `provider` | Contains information on the auth provider to authenticate with. | |
| **Returns** | A Future with the result of the re-authentication request.                                                                                                        |

### Reload

```c++
Future< void > Reload()
```  
Refreshes the data for this user.

For example, the attached providers, email address, display name, etc.  

### ReloadLastResult

```c++
Future< void > ReloadLastResult() const 
```  
Get results of the most recent call to Reload.  

### SendEmailVerification

```c++
Future< void > SendEmailVerification()
```  
Initiates email verification for the user.  

### SendEmailVerificationBeforeUpdatingEmail

```c++
Future< void > SendEmailVerificationBeforeUpdatingEmail(
  const char *email
)
```  
Send an email to verify the ownership of the account, then update to the new email.  

### SendEmailVerificationBeforeUpdatingEmailLastResult

```c++
Future< void > SendEmailVerificationBeforeUpdatingEmailLastResult() const 
```  
Get results of the most recent call to SendEmailVerificationBeforeUpdatingEmail.  

### SendEmailVerificationLastResult

```c++
Future< void > SendEmailVerificationLastResult() const 
```  
Get results of the most recent call to SendEmailVerification.  

### Unlink

```c++
Future< AuthResult > Unlink(
  const char *provider
)
```  
Unlinks the current user from the provider specified.

Status will be an error if the user is not linked to the given provider.  

### UnlinkLastResult

```c++
Future< AuthResult > UnlinkLastResult() const 
```  
Get results of the most recent call to Unlink.  

### UpdatePassword

```c++
Future< void > UpdatePassword(
  const char *password
)
```  
Attempts to change the password for the current user.

For an account linked to an Identity Provider (IDP) with no password, this will result in the account becoming an email/password-based account while maintaining the IDP link. May fail if the password is invalid, if there is a conflicting email/password-based account, or if the token has expired. To retrieve fresh tokens, call Reauthenticate.  

### UpdatePasswordLastResult

```c++
Future< void > UpdatePasswordLastResult() const 
```  
Get results of the most recent call to UpdatePassword.  

### UpdatePhoneNumberCredential

```c++
Future< User > UpdatePhoneNumberCredential(
  const PhoneAuthCredential & credential
)
```  
Updates the currently linked phone number on the user.

This is useful when a user wants to change their phone number. It is a shortcut to calling Unlink(phone_credential.provider().c_str()) and then LinkWithCredential(phone_credential). `credential` must have been created with [PhoneAuthProvider](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/phone-auth-provider#classfirebase_1_1auth_1_1_phone_auth_provider).  

### UpdatePhoneNumberCredentialLastResult

```c++
Future< User > UpdatePhoneNumberCredentialLastResult() const 
```  
Get results of the most recent call to UpdatePhoneNumberCredential.  

### UpdateUserProfile

```c++
Future< void > UpdateUserProfile(
  const UserProfile & profile
)
```  
Updates a subset of user profile information.  

### UpdateUserProfileLastResult

```c++
Future< void > UpdateUserProfileLastResult() const 
```  
Get results of the most recent call to UpdateUserProfile.  

### User

```c++
 User()
```  

### User

```c++
 User(
  const User &
)
```  
Copy constructor.  

### display_name

```c++
virtual std::string display_name() const 
```  
Gets the display name associated with the user, if any.  

### email

```c++
virtual std::string email() const 
```  
Gets email associated with the user, if any.  

### is_anonymous

```c++
bool is_anonymous() const 
```  
Returns true if user signed in anonymously.  

### is_email_verified

```c++
bool is_email_verified() const 
```  
Returns true if the email address associated with this user has been verified.  

### is_valid

```c++
bool is_valid() const 
```  
Returns whether this [User](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user) object represents a valid user.

Could be false on Users contained with [AuthResult](https://firebase.google.com/docs/reference/cpp/struct/firebase/auth/auth-result#structfirebase_1_1auth_1_1_auth_result) structures from failed [Auth](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/auth#classfirebase_1_1auth_1_1_auth) operations.  

### metadata

```c++
UserMetadata metadata() const 
```  
Gets the metadata for this user account.  

### operator!=

```c++
bool operator!=(
  const User &
) const 
```  
Inequality operator.  

### operator=

```c++
User & operator=(
  const User &
)
```  
Assignment operator.  

### operator==

```c++
bool operator==(
  const User &
) const 
```  
Equality operator.  

### phone_number

```c++
virtual std::string phone_number() const 
```  
Gets the phone number for the user, in E.164 format.  

### photo_url

```c++
virtual std::string photo_url() const 
```  
Gets the photo url associated with the user, if any.  

### provider_data

```c++
std::vector< UserInfoInterface > provider_data() const 
```  
Gets the third party profile data associated with this user returned by the authentication server, if any.  

### provider_id

```c++
virtual std::string provider_id() const 
```  
Gets the provider ID for the user (For example, "Facebook").  

### uid

```c++
virtual std::string uid() const 
```  
Gets the unique Firebase user ID for the user.


| **Note:** The user's ID, unique to the Firebase project. Do NOT use this value to authenticate with your backend server, if you have one. Use [User::GetToken()](https://firebase.google.com/docs/reference/cpp/class/firebase/auth/user#classfirebase_1_1auth_1_1_user_1a2214a2f314fd251bad6f318ec9eab22d) instead.

<br />

### \~User

```c++
 ~User()
```