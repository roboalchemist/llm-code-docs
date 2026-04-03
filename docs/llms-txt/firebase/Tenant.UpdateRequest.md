# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest.md.txt

# Tenant.UpdateRequest

public static final class **Tenant.UpdateRequest** extends Object  
A class for updating the attributes of an existing tenant.

An instance of this class can be obtained via a [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant) object, or from a tenant ID
string. Specify the changes to be made to the tenant by calling the various setter methods
available in this class.  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest#UpdateRequest(java.lang.String))(String tenantId) Creates a new [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest), which can be used to update the attributes of the of the tenant identified by the specified tenant ID. |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest#setDisplayName(java.lang.String))(String displayName) Sets the display name of the existing tenant.                                   |
| [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) | [setEmailLinkSignInEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest#setEmailLinkSignInEnabled(boolean))(boolean emailLinkSignInEnabled) Sets whether to enable email link user authentication. |
| [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) | [setPasswordSignInAllowed](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest#setPasswordSignInAllowed(boolean))(boolean passwordSignInAllowed) Sets whether to allow email/password user authentication. |

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
**UpdateRequest**
(String tenantId)

Creates a new [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest), which can be used to update the attributes of the
of the tenant identified by the specified tenant ID.

This method allows updating attributes of a tenant account, without first having to call
[getTenant(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/TenantManager#getTenant(java.lang.String)).  

##### Parameters

| tenantId | a non-null, non-empty tenant ID string. |
|----------|-----------------------------------------|

##### Throws

| IllegalArgumentException | If the tenant ID is null or empty. |
|--------------------------|------------------------------------|

## Public Methods

#### public [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest)
**setDisplayName**
(String displayName)

Sets the display name of the existing tenant.  

##### Parameters

| displayName | a non-null, non-empty display name string. |
|-------------|--------------------------------------------|

#### public [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest)
**setEmailLinkSignInEnabled**
(boolean emailLinkSignInEnabled)

Sets whether to enable email link user authentication.  

##### Parameters

| emailLinkSignInEnabled | a boolean indicating whether users can be authenticated using an email link. |
|------------------------|------------------------------------------------------------------------------|

#### public [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest)
**setPasswordSignInAllowed**
(boolean passwordSignInAllowed)

Sets whether to allow email/password user authentication.  

##### Parameters

| passwordSignInAllowed | a boolean indicating whether users can be authenticated using an email and password. |
|-----------------------|--------------------------------------------------------------------------------------|