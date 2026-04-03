# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest.md.txt

# SamlProviderConfig.UpdateRequest

public static final class **SamlProviderConfig.UpdateRequest** extends [ProviderConfig.AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T extends [AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T\>\>  
A specification class for updating an existing SAML Auth provider.

An instance of this class can be obtained via a [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) object, or from
a provider ID string. Specify the changes to be made to the provider config by calling the
various setter methods available in this class.  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest#UpdateRequest(java.lang.String))(String providerId) Creates a new [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest), which can be used to updates an existing SAML Auth provider. |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | [addAllX509Certificates](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest#addAllX509Certificates(java.util.Collection<java.lang.String>))(Collection\<String\> x509Certificates) Adds a collection of x509 certificates to the existing provider. |
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | [addX509Certificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest#addX509Certificate(java.lang.String))(String x509Certificate) Adds a x509 certificate to the existing provider.                                                             |
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | [setCallbackUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest#setCallbackUrl(java.lang.String))(String callbackUrl) Sets the callback URL for the exising provider.                                                                           |
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | [setIdpEntityId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest#setIdpEntityId(java.lang.String))(String idpEntityId) Sets the IDP entity ID for the existing provider.                                                                         |
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | [setRpEntityId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest#setRpEntityId(java.lang.String))(String rpEntityId) Sets the RP entity ID for the existing provider.                                                                             |
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | [setSsoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest#setSsoUrl(java.lang.String))(String ssoUrl) Sets the SSO URL for the existing provider.                                                                                              |

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

Creates a new [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest), which can be used to updates an existing SAML Auth
provider.

The returned object should be passed to
[updateSamlProviderConfig(UpdateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/AbstractFirebaseAuth#updateSamlProviderConfig(com.google.firebase.auth.SamlProviderConfig.UpdateRequest)) to update the provider
information persistently.  

##### Parameters

| providerId | a non-null, non-empty provider ID string. |
|------------|-------------------------------------------|

##### Throws

| IllegalArgumentException | If the provider ID is null or empty, or is not prefixed with 'saml.'. |
|--------------------------|-----------------------------------------------------------------------|

## Public Methods

#### public [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest)
**addAllX509Certificates**
(Collection\<String\> x509Certificates)

Adds a collection of x509 certificates to the existing provider.  

##### Parameters

| x509Certificates | A non-null, non-empty collection of x509 certificate strings. |
|------------------|---------------------------------------------------------------|

##### Throws

| IllegalArgumentException | If the collection is null or empty, or if any x509 certificates are null or empty. |
|--------------------------|------------------------------------------------------------------------------------|

#### public [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest)
**addX509Certificate**
(String x509Certificate)

Adds a x509 certificate to the existing provider.  

##### Parameters

| x509Certificate | A non-null, non-empty x509 certificate string. |
|-----------------|------------------------------------------------|

##### Throws

| IllegalArgumentException | If the x509 certificate is null or empty. |
|--------------------------|-------------------------------------------|

#### public [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest)
**setCallbackUrl**
(String callbackUrl)

Sets the callback URL for the exising provider.  

##### Parameters

| callbackUrl | A non-null, non-empty callback URL string. |
|-------------|--------------------------------------------|

##### Throws

| IllegalArgumentException | If the callback URL is null or empty, or if the format is invalid. |
|--------------------------|--------------------------------------------------------------------|

#### public [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest)
**setIdpEntityId**
(String idpEntityId)

Sets the IDP entity ID for the existing provider.  

##### Parameters

| idpEntityId | A non-null, non-empty IDP entity ID string. |
|-------------|---------------------------------------------|

##### Throws

| IllegalArgumentException | If the IDP entity ID is null or empty. |
|--------------------------|----------------------------------------|

#### public [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest)
**setRpEntityId**
(String rpEntityId)

Sets the RP entity ID for the existing provider.  

##### Parameters

| rpEntityId | A non-null, non-empty RP entity ID string. |
|------------|--------------------------------------------|

##### Throws

| IllegalArgumentException | If the RP entity ID is null or empty. |
|--------------------------|---------------------------------------|

#### public [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest)
**setSsoUrl**
(String ssoUrl)

Sets the SSO URL for the existing provider.  

##### Parameters

| ssoUrl | A non-null, non-empty SSO URL string. |
|--------|---------------------------------------|

##### Throws

| IllegalArgumentException | If the SSO URL is null or empty, or if the format is invalid. |
|--------------------------|---------------------------------------------------------------|