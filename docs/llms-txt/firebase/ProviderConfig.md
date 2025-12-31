# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.md.txt

# ProviderConfig

public abstract class **ProviderConfig** extends Object  

|---|---|---|
| Known Direct Subclasses [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig), [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) |-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------| | [OidcProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/OidcProviderConfig) | Contains metadata associated with an OIDC Auth provider. | | [SamlProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/SamlProviderConfig) | Contains metadata associated with a SAML Auth provider.  | |||

The base class for Auth providers.  

### Nested Class Summary

|-------|---|---|-------------------------------------------------------------------|
| class | [ProviderConfig.AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T extends [AbstractCreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractCreateRequest)\<T\>\> || A base specification class for creating a new provider.           |
| class | [ProviderConfig.AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T extends [AbstractUpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig.AbstractUpdateRequest)\<T\>\> || A base class for updating the attributes of an existing provider. |

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------|
|   | [ProviderConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig#ProviderConfig())() |

### Public Method Summary

|---------|----------------------------------------------------------------------------------------------------------------------------------------------|
| String  | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig#getDisplayName())() |
| String  | [getProviderId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig#getProviderId())()   |
| boolean | [isEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/ProviderConfig#isEnabled())()           |

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
**ProviderConfig**
()

<br />

## Public Methods

#### public String
**getDisplayName**
()

<br />

#### public String
**getProviderId**
()

<br />

#### public boolean
**isEnabled**
()

<br />