# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest.md.txt

# ProviderConfig.AbstractCreateRequest

public static abstract class **ProviderConfig.AbstractCreateRequest** extends Object  

|---|---|---|
| Known Direct Subclasses [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest), [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) |---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------| | [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | A specification class for creating a new OIDC Auth provider. | | [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | A specification class for creating a new SAML Auth provider. | |||

A base specification class for creating a new provider.

Set the initial attributes of the new provider by calling various setter methods available
in this class.  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest#AbstractCreateRequest())() |

### Public Method Summary

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest#setDisplayName(java.lang.String))(String displayName) Sets the display name for the new provider. |
| T | [setEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest#setEnabled(boolean))(boolean enabled) Sets whether to allow the user to sign in with the provider.    |

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
**AbstractCreateRequest**
()

<br />

## Public Methods

#### public T
**setDisplayName**
(String displayName)

Sets the display name for the new provider.  

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