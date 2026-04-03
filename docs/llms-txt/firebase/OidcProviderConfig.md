# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.md.txt

# OidcProviderConfig

public final class **OidcProviderConfig** extends [ProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig)  
Contains metadata associated with an OIDC Auth provider.

Instances of this class are immutable and thread safe.  

### Nested Class Summary

|-------|---|---|--------------------------------------------------------------------|
| class | [OidcProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.CreateRequest) || A specification class for creating a new OIDC Auth provider.       |
| class | [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) || A specification class for updating an existing OIDC Auth provider. |

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig#OidcProviderConfig())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String                                                                                                                                                        | [getClientId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig#getClientId())()                                                                                                                                                                                                                                                      |
| String                                                                                                                                                        | [getClientSecret](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig#getClientSecret())()                                                                                                                                                                                                                                              |
| String                                                                                                                                                        | [getIssuer](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig#getIssuer())()                                                                                                                                                                                                                                                          |
| boolean                                                                                                                                                       | [isCodeResponseType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig#isCodeResponseType())()                                                                                                                                                                                                                                        |
| boolean                                                                                                                                                       | [isIdTokenResponseType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig#isIdTokenResponseType())()                                                                                                                                                                                                                                  |
| [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) | [updateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig#updateRequest())() Returns a new [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest), which can be used to update the attributes of this provider config. |

### Inherited Method Summary

From class [com.google.firebase.auth.ProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig)  

|---------|----------------------------------------------------------------------------------------------------------------------------------------------|
| String  | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig#getDisplayName())() |
| String  | [getProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig#getProviderId())()   |
| boolean | [isEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig#isEnabled())()           |

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
**OidcProviderConfig**
()

<br />

## Public Methods

#### public String
**getClientId**
()

<br />

#### public String
**getClientSecret**
()

<br />

#### public String
**getIssuer**
()

<br />

#### public boolean
**isCodeResponseType**
()

<br />

#### public boolean
**isIdTokenResponseType**
()

<br />

#### public [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest)
**updateRequest**
()

Returns a new [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest), which can be used to update the attributes of this
provider config.  

##### Returns

- A non-null [OidcProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig.UpdateRequest) instance.