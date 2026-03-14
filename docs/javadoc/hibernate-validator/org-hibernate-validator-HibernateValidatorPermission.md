# Class HibernateValidatorPermission

java.lang.Object
java.security.Permission
java.security.BasicPermission
org.hibernate.validator.HibernateValidatorPermission

All Implemented Interfaces:
`Serializable, Guard`

---

@Deprecated(forRemoval=true)
public class HibernateValidatorPermission
extends BasicPermission
Deprecated, for removal: This API element is subject to removal in a future version.
This permission will be removed in the future versions of Hibernate Validator as it does not rely on the `SecurityManager` anymore.

Our specific implementation of `BasicPermission` as we cannot define additional `RuntimePermission`.

`HibernateValidatorPermission` is thread-safe and immutable.

Author:
Guillaume Smet
See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final HibernateValidatorPermission`
`ACCESS_PRIVATE_MEMBERS`

Deprecated, for removal: This API element is subject to removal in a future version.
 

- 

## Constructor Summary

Constructors

Constructor
Description
`HibernateValidatorPermission(String name)`

Deprecated, for removal: This API element is subject to removal in a future version.
 
`HibernateValidatorPermission(String name,
 String actions)`

Deprecated, for removal: This API element is subject to removal in a future version.
 

- 

## Method Summary

### Methods inherited from class BasicPermission

`equals, getActions, hashCode, implies, newPermissionCollection`

### Methods inherited from class Permission

`checkGuard, getName, toString`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### ACCESS_PRIVATE_MEMBERS

public static final HibernateValidatorPermission ACCESS_PRIVATE_MEMBERS
Deprecated, for removal: This API element is subject to removal in a future version.

- 

## Constructor Details

  - 

### HibernateValidatorPermission

public HibernateValidatorPermission(String name)
Deprecated, for removal: This API element is subject to removal in a future version.

  - 

### HibernateValidatorPermission

public HibernateValidatorPermission(String name,
 String actions)
Deprecated, for removal: This API element is subject to removal in a future version.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved