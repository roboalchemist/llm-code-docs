# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.md.txt

# Tenant

public final class **Tenant** extends Object  
Contains metadata associated with a Firebase tenant.

Instances of this class are immutable and thread safe.  

### Nested Class Summary

|-------|---|---|------------------------------------------------------------|
| class | [Tenant.CreateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.CreateRequest) || A specification class for creating a new tenant.           |
| class | [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) || A class for updating the attributes of an existing tenant. |

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------|
|   | [Tenant](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant#Tenant())() |

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String                                                                                                                                             | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant#getDisplayName())()                                                                                                                                                                                                                            |
| String                                                                                                                                             | [getTenantId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant#getTenantId())()                                                                                                                                                                                                                                  |
| boolean                                                                                                                                            | [isEmailLinkSignInEnabled](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant#isEmailLinkSignInEnabled())()                                                                                                                                                                                                        |
| boolean                                                                                                                                            | [isPasswordSignInAllowed](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant#isPasswordSignInAllowed())()                                                                                                                                                                                                          |
| [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) | [updateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant#updateRequest())() Returns a new [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest), which can be used to update the attributes of this tenant. |

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
**Tenant**
()

<br />

## Public Methods

#### public String
**getDisplayName**
()

<br />

#### public String
**getTenantId**
()

<br />

#### public boolean
**isEmailLinkSignInEnabled**
()

<br />

#### public boolean
**isPasswordSignInAllowed**
()

<br />

#### public [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest)
**updateRequest**
()

Returns a new [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest), which can be used to update the attributes of this tenant.  

##### Returns

- a non-null [Tenant.UpdateRequest](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/multitenancy/Tenant.UpdateRequest) instance.