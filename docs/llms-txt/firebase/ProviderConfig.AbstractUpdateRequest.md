# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest.md.txt

# ProviderConfig.AbstractUpdateRequest

public static abstract class **ProviderConfig.AbstractUpdateRequest** extends Object  

|---|---|---|
| Known Direct Subclasses [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest), [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) |---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------| | [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | A specification class for updating an existing OIDC Auth provider. | | [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | A specification class for updating an existing SAML Auth provider. | |||

A base class for updating the attributes of an existing provider.  

### Public Method Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest#setDisplayName(java.lang.String))(String displayName) Sets the display name for the existing provider. |
| T | [setEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest#setEnabled(boolean))(boolean enabled) Sets whether to allow the user to sign in with the provider.         |

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

#### public T
**setDisplayName**
(String displayName)

Sets the display name for the existing provider.  

##### Parameters

| displayName | A non-null, non-empty display name string. |
|-------------|--------------------------------------------|

##### Throws

| IllegalArgumentException | If the display name is null or empty. |
|--------------------------|---------------------------------------|

#### public T
**setEnabled**
(boolean enabled)

Sets whether to allow the user to sign in with the provider.  

##### Parameters

| enabled | A boolean indicating whether the user can sign in with the provider. |
|---------|----------------------------------------------------------------------|