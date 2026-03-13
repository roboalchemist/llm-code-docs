# Interface ConstructorTarget

All Known Subinterfaces:
`ContainerElementConstraintMappingContext, CrossParameterConstraintMappingContext, ParameterConstraintMappingContext, PropertyConstraintMappingContext, ReturnValueConstraintMappingContext, TypeConstraintMappingContext<C>`

---

public interface ConstructorTarget
Facet of a constraint mapping creational context which allows to select the bean
constructor to which the next operations shall apply.

Author:
Gunnar Morling

- 

## Method Summary

Modifier and Type
Method
Description
`ConstructorConstraintMappingContext`
`constructor(Class<?>... parameterTypes)`

Selects a constructor to which the next operations shall apply.

- 

## Method Details

  - 

### constructor

ConstructorConstraintMappingContext constructor(Class<?>... parameterTypes)
Selects a constructor to which the next operations shall apply.

Until this method is called constraints apply on class level. After calling this method constraints
apply to the specified constructor.

A given constructor may only be configured once.

Parameters:
`parameterTypes` - The constructor parameter types.
Returns:
A creational context representing the selected constructor.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved