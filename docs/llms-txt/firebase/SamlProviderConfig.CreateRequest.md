# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest.md.txt

# SamlProviderConfig.CreateRequest

public static final class **SamlProviderConfig.CreateRequest** extends [ProviderConfig.AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T extends [AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T\>\>  
A specification class for creating a new SAML Auth provider.

Set the initial attributes of the new provider by calling various setter methods available
in this class.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#CreateRequest())() Creates a new [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest), which can be used to create a new SAML Auth provider. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | [addAllX509Certificates](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#addAllX509Certificates(java.util.Collection<java.lang.String>))(Collection\<String\> x509Certificates) Adds a collection of x509 certificates to the new provider. |
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | [addX509Certificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#addX509Certificate(java.lang.String))(String x509Certificate) Adds a x509 certificate to the new provider.                                                             |
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | [setCallbackUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#setCallbackUrl(java.lang.String))(String callbackUrl) Sets the callback URL for the new provider.                                                                          |
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | [setIdpEntityId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#setIdpEntityId(java.lang.String))(String idpEntityId) Sets the IDP entity ID for the new provider.                                                                         |
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | [setProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#setProviderId(java.lang.String))(String providerId) Sets the ID for the new provider.                                                                                       |
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | [setRpEntityId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#setRpEntityId(java.lang.String))(String rpEntityId) Sets the RP entity ID for the new provider.                                                                             |
| [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) | [setSsoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest#setSsoUrl(java.lang.String))(String ssoUrl) Sets the SSO URL for the new provider.                                                                                              |

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

Creates a new [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest), which can be used to create a new SAML Auth provider.

The returned object should be passed to
[createSamlProviderConfig(CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#createSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.CreateRequest)) to register the provider
information persistently.

## Public Methods

#### public [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest)
**addAllX509Certificates**
(Collection\<String\> x509Certificates)

Adds a collection of x509 certificates to the new provider.  

##### Parameters

| x509Certificates | A non-null, non-empty collection of x509 certificate strings. |
|------------------|---------------------------------------------------------------|

##### Throws

| IllegalArgumentException | If the collection is null or empty, or if any x509 certificates are null or empty. |
|--------------------------|------------------------------------------------------------------------------------|

#### public [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest)
**addX509Certificate**
(String x509Certificate)

Adds a x509 certificate to the new provider.  

##### Parameters

| x509Certificate | A non-null, non-empty x509 certificate string. |
|-----------------|------------------------------------------------|

##### Throws

| IllegalArgumentException | If the x509 certificate is null or empty. |
|--------------------------|-------------------------------------------|

#### public [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest)
**setCallbackUrl**
(String callbackUrl)

Sets the callback URL for the new provider.  

##### Parameters

| callbackUrl | A non-null, non-empty callback URL string. |
|-------------|--------------------------------------------|

##### Throws

| IllegalArgumentException | If the callback URL is null or empty, or if the format is invalid. |
|--------------------------|--------------------------------------------------------------------|

#### public [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest)
**setIdpEntityId**
(String idpEntityId)

Sets the IDP entity ID for the new provider.  

##### Parameters

| idpEntityId | A non-null, non-empty IDP entity ID string. |
|-------------|---------------------------------------------|

##### Throws

| IllegalArgumentException | If the IDP entity ID is null or empty. |
|--------------------------|----------------------------------------|

#### public [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest)
**setProviderId**
(String providerId)

Sets the ID for the new provider.  

##### Parameters

| providerId | A non-null, non-empty provider ID string. |
|------------|-------------------------------------------|

##### Throws

| IllegalArgumentException | If the provider ID is null or empty, or is not prefixed with 'saml.'. |
|--------------------------|-----------------------------------------------------------------------|

#### public [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest)
**setRpEntityId**
(String rpEntityId)

Sets the RP entity ID for the new provider.  

##### Parameters

| rpEntityId | A non-null, non-empty RP entity ID string. |
|------------|--------------------------------------------|

##### Throws

| IllegalArgumentException | If the RP entity ID is null or empty. |
|--------------------------|---------------------------------------|

#### public [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest)
**setSsoUrl**
(String ssoUrl)

Sets the SSO URL for the new provider.  

##### Parameters

| ssoUrl | A non-null, non-empty SSO URL string. |
|--------|---------------------------------------|

##### Throws

| IllegalArgumentException | If the SSO URL is null or empty, or if the format is invalid. |
|--------------------------|---------------------------------------------------------------|