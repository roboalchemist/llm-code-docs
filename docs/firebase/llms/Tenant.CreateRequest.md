# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest.md.txt

# Tenant.CreateRequest

public static final class **Tenant.CreateRequest** extends Object  
A specification class for creating a new tenant.

Set the initial attributes of the new tenant by calling various setter methods available in
this class. None of the attributes are required.  

### Public Constructor Summary

|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest#CreateRequest())() Creates a new [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest), which can be used to create a new tenant. |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest#setDisplayName(java.lang.String))(String displayName) Sets the display name for the new tenant.                                       |
| [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) | [setEmailLinkSignInEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest#setEmailLinkSignInEnabled(boolean))(boolean emailLinkSignInEnabled) Sets whether to enable email link user authentication. |
| [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) | [setPasswordSignInAllowed](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest#setPasswordSignInAllowed(boolean))(boolean passwordSignInAllowed) Sets whether to allow email/password user authentication. |

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
**CreateRequest**
()

Creates a new [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest), which can be used to create a new tenant.

The returned object should be passed to [createTenant(CreateRequest)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#createTenant(com.google.firebase.auth.multitenancy.Tenant.CreateRequest))
to register the tenant information persistently.

## Public Methods

#### public [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest)
**setDisplayName**
(String displayName)

Sets the display name for the new tenant.  

##### Parameters

| displayName | a non-null, non-empty display name string. |
|-------------|--------------------------------------------|

#### public [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest)
**setEmailLinkSignInEnabled**
(boolean emailLinkSignInEnabled)

Sets whether to enable email link user authentication.  

##### Parameters

| emailLinkSignInEnabled | a boolean indicating whether users can be authenticated using an email link. |
|------------------------|------------------------------------------------------------------------------|

#### public [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest)
**setPasswordSignInAllowed**
(boolean passwordSignInAllowed)

Sets whether to allow email/password user authentication.  

##### Parameters

| passwordSignInAllowed | a boolean indicating whether users can be authenticated using an email and password. |
|-----------------------|--------------------------------------------------------------------------------------|