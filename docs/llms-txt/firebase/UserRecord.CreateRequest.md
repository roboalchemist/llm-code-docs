# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest.md.txt

# UserRecord.CreateRequest

public static class **UserRecord.CreateRequest** extends Object  
A specification class for creating new user accounts. Set the initial attributes of the new
user account by calling various setter methods available in this class. None of the attributes
are required.  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#CreateRequest())() Creates a new [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest), which can be used to create a new user. |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setDisabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setDisabled(boolean))(boolean disabled) Sets whether the new user account should be disabled by default or not.      |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setDisplayName(java.lang.String))(String displayName) Sets the display name for the new user.                     |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setEmail(java.lang.String))(String email) Sets an email address for the new user.                                       |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setEmailVerified](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setEmailVerified(boolean))(boolean emailVerified) Sets whether the user email address has been verified or not. |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setPassword](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setPassword(java.lang.String))(String password) Sets the password for the new user.                                  |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setPhoneNumber(java.lang.String))(String phone) Sets a phone number for the new user.                             |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setPhotoUrl(java.lang.String))(String photoUrl) Sets the photo URL for the new user.                                 |
| [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) | [setUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest#setUid(java.lang.String))(String uid) Sets a user ID for the new user.                                                    |

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
**CreateRequest**
()

Creates a new [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest), which can be used to create a new user. The returned
object should be passed to [createUser(CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createUser(com.google.firebase.auth.UserRecord.CreateRequest)) to register
the user information persistently.

## Public Methods

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setDisabled**
(boolean disabled)

Sets whether the new user account should be disabled by default or not.  

##### Parameters

| disabled | a boolean indicating whether the new account should be disabled. |
|----------|------------------------------------------------------------------|

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setDisplayName**
(String displayName)

Sets the display name for the new user.  

##### Parameters

| displayName | a non-null display name string. |
|-------------|---------------------------------|

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setEmail**
(String email)

Sets an email address for the new user.  

##### Parameters

| email | a non-null, non-empty email address string. |
|-------|---------------------------------------------|

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setEmailVerified**
(boolean emailVerified)

Sets whether the user email address has been verified or not.  

##### Parameters

| emailVerified | a boolean indicating the email verification status. |
|---------------|-----------------------------------------------------|

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setPassword**
(String password)

Sets the password for the new user.  

##### Parameters

| password | a password string that is at least 6 characters long. |
|----------|-------------------------------------------------------|

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setPhoneNumber**
(String phone)

Sets a phone number for the new user.  

##### Parameters

| phone | a non-null, non-empty phone number string. |
|-------|--------------------------------------------|

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setPhotoUrl**
(String photoUrl)

Sets the photo URL for the new user.  

##### Parameters

| photoUrl | a non-null, non-empty URL string. |
|----------|-----------------------------------|

#### public [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest)
**setUid**
(String uid)

Sets a user ID for the new user.  

##### Parameters

| uid | a non-null, non-empty user ID that uniquely identifies the new user. The user ID must not be longer than 128 characters. |
|-----|--------------------------------------------------------------------------------------------------------------------------|