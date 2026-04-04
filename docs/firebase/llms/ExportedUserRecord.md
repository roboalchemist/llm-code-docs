# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord.md.txt

# ExportedUserRecord

public class **ExportedUserRecord** extends [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)  
Contains metadata associated with a Firebase user account, along with password hash and salt.
Instances of this class are immutable and thread-safe.  

### Public Method Summary

|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String | [getPasswordHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord#getPasswordHash())() Returns the user's password hash as a base64-encoded string. |
| String | [getPasswordSalt](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord#getPasswordSalt())() Returns the user's password salt as a base64-encoded string. |

### Inherited Method Summary

From class [com.google.firebase.auth.UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord)  

|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map\<String, Object\>                                                                                                                         | [getCustomClaims](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getCustomClaims())() Returns custom claims set on this user.                                                                                                                                                                           |
| String                                                                                                                                        | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getDisplayName())() Returns the display name of this user.                                                                                                                                                                              |
| String                                                                                                                                        | [getEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getEmail())() Returns the email address associated with this user.                                                                                                                                                                            |
| String                                                                                                                                        | [getPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getPhoneNumber())() Returns the phone number associated with this user.                                                                                                                                                                 |
| String                                                                                                                                        | [getPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getPhotoUrl())() Returns the photo URL of this user.                                                                                                                                                                                       |
| [UserInfo\[\]](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo)                             | [getProviderData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getProviderData())() Returns an array of `UserInfo` objects that represents the identities from different identity providers that are linked to this user.                                                                             |
| String                                                                                                                                        | [getProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getProviderId())() Returns the provider ID of this user.                                                                                                                                                                                 |
| String                                                                                                                                        | [getTenantId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getTenantId())() Returns the tenant ID associated with this user, if one exists.                                                                                                                                                           |
| long                                                                                                                                          | [getTokensValidAfterTimestamp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getTokensValidAfterTimestamp())() Returns a timestamp in milliseconds since epoch, truncated down to the closest second.                                                                                                  |
| String                                                                                                                                        | [getUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getUid())() Returns the user ID of this user.                                                                                                                                                                                                   |
| [UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata)                         | [getUserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#getUserMetadata())() Returns additional metadata associated with this user.                                                                                                                                                            |
| boolean                                                                                                                                       | [isDisabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#isDisabled())() Returns whether this user account is disabled.                                                                                                                                                                              |
| boolean                                                                                                                                       | [isEmailVerified](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#isEmailVerified())() Returns whether the email address of this user has been verified.                                                                                                                                                 |
| [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) | [updateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord#updateRequest())() Returns a new [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest), which can be used to update the attributes of this user. |

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

From interface [com.google.firebase.auth.UserInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo)  

|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract String | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getDisplayName())() Returns the user's display name, if available.  |
| abstract String | [getEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getEmail())() Returns the user's email address, if available.             |
| abstract String | [getPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getPhoneNumber())() Returns the user's phone number, if available.  |
| abstract String | [getPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getPhotoUrl())() Returns the user's photo URL, if available.           |
| abstract String | [getProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getProviderId())() Returns the ID of the identity provider.          |
| abstract String | [getUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getUid())() Returns the user's unique ID assigned by the identity provider. |

## Public Methods

#### public String
**getPasswordHash**
()

Returns the user's password hash as a base64-encoded string.

If the Firebase Auth hashing algorithm (SCRYPT) was used to create the user account,
returns the base64-encoded password hash of the user. If a different hashing algorithm was
used to create this user, as is typical when migrating from another Auth system, returns
an empty string. Returns null if no password is set.  

##### Returns

- A base64-encoded password hash, possibly empty or null.  

#### public String
**getPasswordSalt**
()

Returns the user's password salt as a base64-encoded string.

If the Firebase Auth hashing algorithm (SCRYPT) was used to create the user account,
returns the base64-encoded password salt of the user. If a different hashing algorithm was
used to create this user, as is typical when migrating from another Auth system, returns
an empty string. Returns null if no password is set.  

##### Returns

- A base64-encoded password salt, possibly empty or null.