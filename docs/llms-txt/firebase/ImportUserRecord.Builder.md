# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder.md.txt

# ImportUserRecord.Builder

public static class **ImportUserRecord.Builder** extends Object  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [addAllUserProviders](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#addAllUserProviders(java.util.List<com.google.firebase.auth.UserProvider>))(List\<[UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider)\> providers) Associates all user provider's in the given list with this user. |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [addUserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#addUserProvider(com.google.firebase.auth.UserProvider))([UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider) provider) Adds a user provider to be associated with this user.                                             |
| [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#build())() Builds a new [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord).                                                                                                                                              |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [putAllCustomClaims](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#putAllCustomClaims(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> customClaims) Sets the custom claims associated with this user.                                                                                                                           |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [putCustomClaim](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#putCustomClaim(java.lang.String, java.lang.Object))(String key, Object value) Sets the specified custom claim on this user account.                                                                                                                                                        |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setDisabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setDisabled(boolean))(boolean disabled) Sets whether the user account should be disabled by default or not.                                                                                                                                                                                   |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setDisplayName(java.lang.String))(String displayName) Sets the display name for the user.                                                                                                                                                                                                  |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setEmail(java.lang.String))(String email) Sets an email address for the user.                                                                                                                                                                                                                    |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setEmailVerified](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setEmailVerified(boolean))(boolean emailVerified) Sets whether the user email address has been verified or not.                                                                                                                                                                          |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setPasswordHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setPasswordHash(byte[]))(byte\[\] passwordHash) Sets a byte array representing the user's hashed password.                                                                                                                                                                                |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setPasswordSalt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setPasswordSalt(byte[]))(byte\[\] passwordSalt) Sets a byte array representing the user's password salt.                                                                                                                                                                                  |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setPhoneNumber(java.lang.String))(String phoneNumber) Sets the phone number associated with this user.                                                                                                                                                                                     |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setPhotoUrl(java.lang.String))(String photoUrl) Sets the photo URL for the user.                                                                                                                                                                                                              |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setUid(java.lang.String))(String uid) Sets a user ID for the user.                                                                                                                                                                                                                                 |
| [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder) | [setUserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder#setUserMetadata(com.google.firebase.auth.UserMetadata))([UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata) userMetadata) Sets additional metadata about the user.                                                      |

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

## Public Methods

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**addAllUserProviders**
(List\<[UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider)\> providers)

Associates all user provider's in the given list with this user.  

##### Parameters

| providers | A list of [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider) instances. |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**addUserProvider**
([UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider) provider)

Adds a user provider to be associated with this user.

A [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider) represents the identity of the user as specified by an
identity provider that is linked to this user account. The identity provider can specify
its own values for common user attributes like email, display name and photo URL.  

##### Parameters

| provider | A non-null [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider). |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord)
**build**
()

Builds a new [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord).  

##### Returns

- A non-null [ImportUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord).  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**putAllCustomClaims**
(Map\<String, Object\> customClaims)

Sets the custom claims associated with this user.  

##### Parameters

| customClaims | a Map of custom claims |
|--------------|------------------------|

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**putCustomClaim**
(String key, Object value)

Sets the specified custom claim on this user account.  

##### Parameters

|  key  | Name of the claim.  |
| value | Value of the claim. |
|-------|---------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setDisabled**
(boolean disabled)

Sets whether the user account should be disabled by default or not.  

##### Parameters

| disabled | a boolean indicating whether the account should be disabled. |
|----------|--------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setDisplayName**
(String displayName)

Sets the display name for the user.  

##### Parameters

| displayName | a non-null, non-empty display name string. |
|-------------|--------------------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setEmail**
(String email)

Sets an email address for the user.  

##### Parameters

| email | a non-null, non-empty email address string. |
|-------|---------------------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setEmailVerified**
(boolean emailVerified)

Sets whether the user email address has been verified or not.  

##### Parameters

| emailVerified | a boolean indicating the email verification status. |
|---------------|-----------------------------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setPasswordHash**
(byte\[\] passwordHash)

Sets a byte array representing the user's hashed password. If at least one user account
carries a password hash, a [UserImportHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportHash) must be specified when calling the
[importUsersAsync(List, UserImportOptions)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#importUsersAsync(java.util.List<com.google.firebase.auth.ImportUserRecord>, com.google.firebase.auth.UserImportOptions)) method. See
[setHash(UserImportHash)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserImportOptions.Builder#setHash(com.google.firebase.auth.UserImportHash)).  

##### Parameters

| passwordHash | A byte array. |
|--------------|---------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setPasswordSalt**
(byte\[\] passwordSalt)

Sets a byte array representing the user's password salt.  

##### Parameters

| passwordSalt | A byte array. |
|--------------|---------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setPhoneNumber**
(String phoneNumber)

Sets the phone number associated with this user.  

##### Parameters

| phoneNumber | a valid phone number string. |
|-------------|------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setPhotoUrl**
(String photoUrl)

Sets the photo URL for the user.  

##### Parameters

| photoUrl | a non-null, non-empty URL string. |
|----------|-----------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setUid**
(String uid)

Sets a user ID for the user.  

##### Parameters

| uid | a non-null, non-empty user ID that uniquely identifies the user. The user ID must not be longer than 128 characters. |
|-----|----------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ImportUserRecord.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ImportUserRecord.Builder)
**setUserMetadata**
([UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata) userMetadata)

Sets additional metadata about the user.  

##### Parameters

| userMetadata | A [UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata) instance. |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.