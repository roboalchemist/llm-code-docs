# Interface ContainerElementConstraintMappingContext

All Superinterfaces:
`Cascadable<ContainerElementConstraintMappingContext>, Constrainable<ContainerElementConstraintMappingContext>, ConstraintDefinitionTarget, ConstraintMappingTarget, ConstructorTarget, ContainerElementTarget, MethodTarget, ParameterTarget, PropertyTarget, ReturnValueTarget, TypeTarget`

---

public interface ContainerElementConstraintMappingContext
extends Constrainable<ContainerElementConstraintMappingContext>, ConstraintMappingTarget, PropertyTarget, ConstructorTarget, MethodTarget, ContainerElementTarget, ParameterTarget, ReturnValueTarget, Cascadable<ContainerElementConstraintMappingContext>
Constraint mapping creational context representing a type argument of a property, parameter or method return value
with a generic (return) type. Allows to place constraints on that type argument, mark it as cascadable and to
navigate to other constraint targets.

Since:
6.0
Author:
Gunnar Morling

- 

## Method Summary

### Methods inherited from interface Cascadable

`convertGroup, valid`

### Methods inherited from interface Constrainable

`constraint`

### Methods inherited from interface ConstraintDefinitionTarget

`constraintDefinition`

### Methods inherited from interface ConstructorTarget

`constructor`

### Methods inherited from interface ContainerElementTarget

`containerElementType, containerElementType`

### Methods inherited from interface MethodTarget

`method`

### Methods inherited from interface ParameterTarget

`parameter`

### Methods inherited from interface PropertyTarget

`field, getter`

### Methods inherited from interface ReturnValueTarget

`returnValue`

### Methods inherited from interface TypeTarget

`type`

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved