# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest.md.txt

# UserRecord.UpdateRequest

public static class **UserRecord.UpdateRequest** extends Object  
A class for updating the attributes of an existing user. An instance of this class can be
obtained via a [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) object, or from a user ID string. Specify the changes to be
made in the user account by calling the various setter methods available in this class.  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#UpdateRequest(java.lang.String))(String uid) Creates a new [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest), which can be used to update the attributes of the user identified by the specified user ID. |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setCustomClaims](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setCustomClaims(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> customClaims) Updates the custom claims associated with this user.                                                                                 |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setDisabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setDisabled(boolean))(boolean disabled) Enables or disables this user account.                                                                                                                                                                   |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setDisplayName(java.lang.String))(String displayName) Updates the display name of this user.                                                                                                                                                  |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setEmail(java.lang.String))(String email) Updates the email address associated with this user.                                                                                                                                                      |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setEmailVerified](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setEmailVerified(boolean))(boolean emailVerified) Updates the email verification status of this account.                                                                                                                                    |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setPassword](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setPassword(java.lang.String))(String password) Updates the password of this user.                                                                                                                                                               |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setPhoneNumber(java.lang.String))(String phone) Updates the phone number associated with this user.                                                                                                                                           |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setPhotoUrl(java.lang.String))(String photoUrl) Updates the Photo URL of this user.                                                                                                                                                              |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setProviderToLink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setProviderToLink(com.google.firebase.auth.UserProvider))([UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider) providerToLink) Links this user to the specified provider. |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [setProvidersToUnlink](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest#setProvidersToUnlink(java.lang.Iterable<java.lang.String>))(Iterable\<String\> providerIds) Unlinks this user from the specified providers.                                                                                             |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Constructors

#### public
**UpdateRequest**
(String uid)

Creates a new [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest), which can be used to update the attributes
of the user identified by the specified user ID. This method allows updating attributes of
a user account, without first having to call [getUser(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#getUser(java.lang.String)).  

##### Parameters

| uid | a non-null, non-empty user ID string. |
|-----|---------------------------------------|

##### Throws

| IllegalArgumentException | If the user ID is null or empty. |
|--------------------------|----------------------------------|

## Public Methods

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setCustomClaims**
(Map\<String, Object\> customClaims)

Updates the custom claims associated with this user. Calling this method with a null
argument removes any custom claims from the user account.  

##### Parameters

| customClaims | a Map of custom claims or null |
|--------------|--------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setDisabled**
(boolean disabled)

Enables or disables this user account.  

##### Parameters

| disabled | a boolean indicating whether this account should be disabled. |
|----------|---------------------------------------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setDisplayName**
(String displayName)

Updates the display name of this user. Calling this method with a null argument removes the
display name attribute from the user account.  

##### Parameters

| displayName | a display name string or null |
|-------------|-------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setEmail**
(String email)

Updates the email address associated with this user.  

##### Parameters

| email | a non-null, non-empty email address to be associated with the user. |
|-------|---------------------------------------------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setEmailVerified**
(boolean emailVerified)

Updates the email verification status of this account.  

##### Parameters

| emailVerified | a boolean indicating whether the email address has been verified. |
|---------------|-------------------------------------------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setPassword**
(String password)

Updates the password of this user.  

##### Parameters

| password | a new password string that is at least 6 characters long. |
|----------|-----------------------------------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setPhoneNumber**
(String phone)

Updates the phone number associated with this user. Calling this method with a null argument
removes the phone number from the user account.  

##### Parameters

| phone | a valid phone number string or null. |
|-------|--------------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setPhotoUrl**
(String photoUrl)

Updates the Photo URL of this user. Calling this method with a null argument removes
the photo URL attribute from the user account.  

##### Parameters

| photoUrl | a valid URL string or null |
|----------|----------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setProviderToLink**
([UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider) providerToLink)

Links this user to the specified provider.

Linking a provider to an existing user account does not invalidate the
refresh token of that account. In other words, the existing account
continues to be able to access resources, despite not having used
the newly linked provider to sign in. If you wish to force the user to
authenticate with this new provider, you need to (a) revoke their
refresh token (see
https://firebase.google.com/docs/auth/admin/manage-sessions#revoke_refresh_tokens),
and (b) ensure no other authentication methods are present on this
account.  

##### Parameters

| providerToLink | provider info to be linked to this user\\'s account. |
|----------------|------------------------------------------------------|

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**setProvidersToUnlink**
(Iterable\<String\> providerIds)

Unlinks this user from the specified providers.  

##### Parameters

| providerIds | list of identifiers for the identity providers. |
|-------------|-------------------------------------------------|