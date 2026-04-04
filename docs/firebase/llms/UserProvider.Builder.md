# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder.md.txt

# UserProvider.Builder

public static class **UserProvider.Builder** extends Object  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder#build())() Builds a new [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider). |
| [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder) | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder#setDisplayName(java.lang.String))(String displayName) Sets the user's display name.                                                   |
| [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder) | [setEmail](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder#setEmail(java.lang.String))(String email) Sets the user's email address.                                                                    |
| [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder) | [setPhotoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder#setPhotoUrl(java.lang.String))(String photoUrl) Sets the photo URl of the user.                                                          |
| [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder) | [setProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder#setProviderId(java.lang.String))(String providerId) Sets the ID of the identity provider.                                              |
| [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder) | [setUid](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder#setUid(java.lang.String))(String uid) Sets the user's unique ID assigned by the identity provider.                                            |

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

#### public [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider)
**build**
()

Builds a new [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider).  

##### Returns

- A non-null [UserProvider](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider).  

#### public [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder)
**setDisplayName**
(String displayName)

Sets the user's display name.  

##### Parameters

| displayName | display name of the user. |
|-------------|---------------------------|

##### Returns

- This builder.  

#### public [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder)
**setEmail**
(String email)

Sets the user's email address.  

##### Parameters

| email | an email address string. |
|-------|--------------------------|

##### Returns

- This builder.  

#### public [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder)
**setPhotoUrl**
(String photoUrl)

Sets the photo URl of the user.  

##### Parameters

| photoUrl | a photo URL string. |
|----------|---------------------|

##### Returns

- This builder.  

#### public [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder)
**setProviderId**
(String providerId)

Sets the ID of the identity provider. This can be a short domain name (e.g. google.com) or
the identifier of an OpenID identity provider. This field is required.  

##### Parameters

| providerId | an ID string that uniquely identifies the identity provider. |
|------------|--------------------------------------------------------------|

##### Returns

- This builder.  

#### public [UserProvider.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserProvider.Builder)
**setUid**
(String uid)

Sets the user's unique ID assigned by the identity provider. This field is required.  

##### Parameters

| uid | a user ID string. |
|-----|-------------------|

##### Returns

- This builder.