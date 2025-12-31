# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest.md.txt

# OidcProviderConfig.CreateRequest

public static final class **OidcProviderConfig.CreateRequest** extends [ProviderConfig.AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T extends [AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T\>\>  
A specification class for creating a new OIDC Auth provider.

Set the initial attributes of the new provider by calling various setter methods available
in this class.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest#CreateRequest())() Creates a new [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest), which can be used to create a new OIDC Auth provider. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | [setClientId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest#setClientId(java.lang.String))(String clientId) Sets the client ID for the new provider.                                             |
| [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | [setClientSecret](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest#setClientSecret(java.lang.String))(String clientSecret) Sets the client secret for the new provider.                             |
| [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | [setCodeResponseType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest#setCodeResponseType(boolean))(boolean enabled) Sets whether to enable the code response flow for the new provider.           |
| [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | [setIdTokenResponseType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest#setIdTokenResponseType(boolean))(boolean enabled) Sets whether to enable the ID token response flow for the new provider. |
| [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | [setIssuer](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest#setIssuer(java.lang.String))(String issuer) Sets the issuer for the new provider.                                                      |
| [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) | [setProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest#setProviderId(java.lang.String))(String providerId) Sets the ID for the new provider.                                              |

### Inherited Method Summary

From class [com.google.firebase.auth.ProviderConfig.AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)  

|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest#setDisplayName(java.lang.String))(String displayName) Sets the display name for the new provider. |
| T | [setEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest#setEnabled(boolean))(boolean enabled) Sets whether to allow the user to sign in with the provider.    |

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

Creates a new [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest), which can be used to create a new OIDC Auth provider.

The returned object should be passed to
[createOidcProviderConfig(CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createOidcProviderConfig(com.google.firebase.auth.OidcProviderConfig.CreateRequest)) to save the config.

## Public Methods

#### public [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest)
**setClientId**
(String clientId)

Sets the client ID for the new provider.  

##### Parameters

| clientId | A non-null, non-empty client ID string. |
|----------|-----------------------------------------|

##### Throws

| IllegalArgumentException | If the client ID is null or empty. |
|--------------------------|------------------------------------|

#### public [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest)
**setClientSecret**
(String clientSecret)

Sets the client secret for the new provider. This is required for the code flow.  

##### Parameters

| clientSecret | A non-null, non-empty client secret string. |
|--------------|---------------------------------------------|

##### Throws

| IllegalArgumentException | If the client secret is null or empty. |
|--------------------------|----------------------------------------|

#### public [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest)
**setCodeResponseType**
(boolean enabled)

Sets whether to enable the code response flow for the new provider. By default, this is not
enabled if no response type is specified.

A client secret must be set for this response type.

Having both the code and ID token response flows is currently not supported.  

##### Parameters

| enabled | A boolean signifying whether the code response type is supported. |
|---------|-------------------------------------------------------------------|

#### public [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest)
**setIdTokenResponseType**
(boolean enabled)

Sets whether to enable the ID token response flow for the new provider. By default, this is
enabled if no response type is specified.

Having both the code and ID token response flows is currently not supported.  

##### Parameters

| enabled | A boolean signifying whether the ID token response type is supported. |
|---------|-----------------------------------------------------------------------|

#### public [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest)
**setIssuer**
(String issuer)

Sets the issuer for the new provider.  

##### Parameters

| issuer | A non-null, non-empty issuer URL string. |
|--------|------------------------------------------|

##### Throws

| IllegalArgumentException | If the issuer URL is null or empty, or if the format is invalid. |
|--------------------------|------------------------------------------------------------------|

#### public [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest)
**setProviderId**
(String providerId)

Sets the ID for the new provider.  

##### Parameters

| providerId | A non-null, non-empty provider ID string. |
|------------|-------------------------------------------|

##### Throws

| IllegalArgumentException | If the provider ID is null or empty, or is not prefixed with 'oidc.'. |
|--------------------------|-----------------------------------------------------------------------|