# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest.md.txt

# OidcProviderConfig.UpdateRequest

public static final class **OidcProviderConfig.UpdateRequest** extends [ProviderConfig.AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T extends [AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T\>\>  
A specification class for updating an existing OIDC Auth provider.

An instance of this class can be obtained via a [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) object, or from
a provider ID string. Specify the changes to be made to the provider config by calling the
various setter methods available in this class.  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest#UpdateRequest(java.lang.String))(String providerId) Creates a new [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest), which can be used to updates an existing OIDC Auth provider. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | [setClientId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest#setClientId(java.lang.String))(String clientId) Sets the client ID for the exsting provider.                                         |
| [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | [setClientSecret](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest#setClientSecret(java.lang.String))(String clientSecret) Sets the client secret for the new provider.                             |
| [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | [setCodeResponseType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest#setCodeResponseType(boolean))(boolean enabled) Sets whether to enable the code response flow for the new provider.           |
| [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | [setIdTokenResponseType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest#setIdTokenResponseType(boolean))(boolean enabled) Sets whether to enable the ID token response flow for the new provider. |
| [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | [setIssuer](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest#setIssuer(java.lang.String))(String issuer) Sets the issuer for the existing provider.                                                 |

### Inherited Method Summary

From class [com.google.firebase.auth.ProviderConfig.AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)  

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest#setDisplayName(java.lang.String))(String displayName) Sets the display name for the existing provider. |
| T | [setEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest#setEnabled(boolean))(boolean enabled) Sets whether to allow the user to sign in with the provider.         |

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
(String providerId)

Creates a new [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest), which can be used to updates an existing OIDC Auth
provider.

The returned object should be passed to
[updateOidcProviderConfig(UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.UpdateRequest)) to save the updated
config.  

##### Parameters

| providerId | A non-null, non-empty provider ID string. |
|------------|-------------------------------------------|

##### Throws

| IllegalArgumentException | If the provider ID is null or empty, or is not prefixed with "oidc.". |
|--------------------------|-----------------------------------------------------------------------|

## Public Methods

#### public [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest)
**setClientId**
(String clientId)

Sets the client ID for the exsting provider.  

##### Parameters

| clientId | A non-null, non-empty client ID string. |
|----------|-----------------------------------------|

##### Throws

| IllegalArgumentException | If the client ID is null or empty. |
|--------------------------|------------------------------------|

#### public [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest)
**setClientSecret**
(String clientSecret)

Sets the client secret for the new provider. This is required for the code flow.  

##### Parameters

| clientSecret | A non-null, non-empty client secret string. |
|--------------|---------------------------------------------|

##### Throws

| IllegalArgumentException | If the client secret is null or empty. |
|--------------------------|----------------------------------------|

#### public [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest)
**setCodeResponseType**
(boolean enabled)

Sets whether to enable the code response flow for the new provider. By default, this is not
enabled if no response type is specified.

A client secret must be set for this response type.

Having both the code and ID token response flows is currently not supported.  

##### Parameters

| enabled | A boolean signifying whether the code response type is supported. |
|---------|-------------------------------------------------------------------|

#### public [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest)
**setIdTokenResponseType**
(boolean enabled)

Sets whether to enable the ID token response flow for the new provider. By default, this is
enabled if no response type is specified.

Having both the code and ID token response flows is currently not supported.  

##### Parameters

| enabled | A boolean signifying whether the ID token response type is supported. |
|---------|-----------------------------------------------------------------------|

#### public [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest)
**setIssuer**
(String issuer)

Sets the issuer for the existing provider.  

##### Parameters

| issuer | A non-null, non-empty issuer URL string. |
|--------|------------------------------------------|

##### Throws

| IllegalArgumentException | If the issuer URL is null or empty, or if the format is invalid. |
|--------------------------|------------------------------------------------------------------|