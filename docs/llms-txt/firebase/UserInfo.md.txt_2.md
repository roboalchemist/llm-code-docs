# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo.md.txt

# UserInfo

public interface **UserInfo**

|---|---|---|
| Known Indirect Subclasses [ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord), [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) |---|---| | [ExportedUserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ExportedUserRecord) | Contains metadata associated with a Firebase user account, along with password hash and salt. | | [UserRecord](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord) | Contains metadata associated with a Firebase user account. | |||

A collection of standard profile information for a user. Used to expose profile information
returned by an identity provider.

### Public Method Summary

|---|---|
| abstract String | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getDisplayName())() Returns the user's display name, if available. |
| abstract String | [getEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getEmail())() Returns the user's email address, if available. |
| abstract String | [getPhoneNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getPhoneNumber())() Returns the user's phone number, if available. |
| abstract String | [getPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getPhotoUrl())() Returns the user's photo URL, if available. |
| abstract String | [getProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getProviderId())() Returns the ID of the identity provider. |
| abstract String | [getUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserInfo#getUid())() Returns the user's unique ID assigned by the identity provider. |

## Public Methods

#### public abstract String
**getDisplayName**
()

Returns the user's display name, if available.

##### Returns

- a display name string or null.

#### public abstract String
**getEmail**
()

Returns the user's email address, if available.

##### Returns

- an email address string or null.

#### public abstract String
**getPhoneNumber**
()

Returns the user's phone number, if available.

##### Returns

- a phone number string or null.

#### public abstract String
**getPhotoUrl**
()

Returns the user's photo URL, if available.

##### Returns

- a URL string or null.

#### public abstract String
**getProviderId**
()

Returns the ID of the identity provider. This can be a short domain name (e.g. google.com) or
the identifier of an OpenID identity provider.

##### Returns

- an ID string that uniquely identifies the identity provider.

#### public abstract String
**getUid**
()

Returns the user's unique ID assigned by the identity provider.

##### Returns

- a user ID string.