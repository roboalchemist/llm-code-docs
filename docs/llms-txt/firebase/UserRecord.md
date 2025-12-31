# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.md.txt

# UserRecord

public class **UserRecord** extends Object  
implements [UserInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo)  

|---|---|---|
| Known Direct Subclasses [ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord) |-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------| | [ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord) | Contains metadata associated with a Firebase user account, along with password hash and salt. | |||

Contains metadata associated with a Firebase user account. Instances of this class are immutable
and thread safe.  

### Nested Class Summary

|-------|---|---|----------------------------------------------------------|
| class | [UserRecord.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.CreateRequest) || A specification class for creating new user accounts.    |
| class | [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest) || A class for updating the attributes of an existing user. |

### Public Method Summary

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

From interface [com.google.firebase.auth.UserInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo)  

|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract String | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getDisplayName())() Returns the user's display name, if available.  |
| abstract String | [getEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getEmail())() Returns the user's email address, if available.             |
| abstract String | [getPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getPhoneNumber())() Returns the user's phone number, if available.  |
| abstract String | [getPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getPhotoUrl())() Returns the user's photo URL, if available.           |
| abstract String | [getProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getProviderId())() Returns the ID of the identity provider.          |
| abstract String | [getUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getUid())() Returns the user's unique ID assigned by the identity provider. |

## Public Methods

#### public Map\<String, Object\>
**getCustomClaims**
()

Returns custom claims set on this user.  

##### Returns

- a non-null, immutable Map of custom claims, possibly empty.  

#### public String
**getDisplayName**
()

Returns the display name of this user.  

##### Returns

- a display name string or null.  

#### public String
**getEmail**
()

Returns the email address associated with this user.  

##### Returns

- an email address string or null.  

#### public String
**getPhoneNumber**
()

Returns the phone number associated with this user.  

##### Returns

- a phone number string or null.  

#### public String
**getPhotoUrl**
()

Returns the photo URL of this user.  

##### Returns

- a URL string or null.  

#### public [UserInfo\[\]](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo)
**getProviderData**
()

Returns an array of `UserInfo` objects that represents the identities from different
identity providers that are linked to this user.  

##### Returns

- an array of [UserInfo](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo) instances, which may be empty.  

#### public String
**getProviderId**
()

Returns the provider ID of this user.  

##### Returns

- a constant provider ID value.  

#### public String
**getTenantId**
()

Returns the tenant ID associated with this user, if one exists.  

##### Returns

- a tenant ID string or null.  

#### public long
**getTokensValidAfterTimestamp**
()

Returns a timestamp in milliseconds since epoch, truncated down to the closest second.
Tokens minted before this timestamp are considered invalid.  

##### Returns

- Timestamp in milliseconds since the epoch. Tokens minted before this timestamp are considered invalid.  

#### public String
**getUid**
()

Returns the user ID of this user.  

##### Returns

- a non-null, non-empty user ID string.  

#### public [UserMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserMetadata)
**getUserMetadata**
()

Returns additional metadata associated with this user.  

##### Returns

- a non-null UserMetadata instance.  

#### public boolean
**isDisabled**
()

Returns whether this user account is disabled.  

##### Returns

- true if the user account is disabled, and false otherwise.  

#### public boolean
**isEmailVerified**
()

Returns whether the email address of this user has been verified.  

##### Returns

- true if the email has been verified, and false otherwise.  

#### public [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest)
**updateRequest**
()

Returns a new [UserRecord.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord.UpdateRequest), which can be used to update the attributes
of this user.  

##### Returns

- a non-null UserRecord.UpdateRequest instance.