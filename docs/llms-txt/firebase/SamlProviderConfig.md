# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.md.txt

# SamlProviderConfig

public final class **SamlProviderConfig** extends [ProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig)  
Contains metadata associated with a SAML Auth provider.

Instances of this class are immutable and thread safe.  

### Nested Class Summary

|-------|---|---|--------------------------------------------------------------------|
| class | [SamlProviderConfig.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.CreateRequest) || A specification class for creating a new SAML Auth provider.       |
| class | [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) || A specification class for updating an existing SAML Auth provider. |

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig#SamlProviderConfig())() |

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String                                                                                                                                                        | [getCallbackUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig#getCallbackUrl())()                                                                                                                                                                                                                                                |
| String                                                                                                                                                        | [getIdpEntityId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig#getIdpEntityId())()                                                                                                                                                                                                                                                |
| String                                                                                                                                                        | [getRpEntityId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig#getRpEntityId())()                                                                                                                                                                                                                                                  |
| String                                                                                                                                                        | [getSsoUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig#getSsoUrl())()                                                                                                                                                                                                                                                          |
| List\<String\>                                                                                                                                                | [getX509Certificates](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig#getX509Certificates())()                                                                                                                                                                                                                                      |
| [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) | [updateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig#updateRequest())() Returns a new [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest), which can be used to update the attributes of this provider config. |

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
**SamlProviderConfig**
()

<br />

## Public Methods

#### public String
**getCallbackUrl**
()

<br />

#### public String
**getIdpEntityId**
()

<br />

#### public String
**getRpEntityId**
()

<br />

#### public String
**getSsoUrl**
()

<br />

#### public List\<String\>
**getX509Certificates**
()

<br />

#### public [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest)
**updateRequest**
()

Returns a new [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest), which can be used to update the attributes of this
provider config.  

##### Returns

- a non-null [SamlProviderConfig.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig.UpdateRequest) instance.