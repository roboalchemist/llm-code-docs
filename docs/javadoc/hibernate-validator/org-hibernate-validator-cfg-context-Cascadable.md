# Interface Cascadable<C extends Cascadable<C>>

Type Parameters:
`C` - The concrete type of the cascadable.

All Known Subinterfaces:
`ContainerElementConstraintMappingContext, ParameterConstraintMappingContext, PropertyConstraintMappingContext, ReturnValueConstraintMappingContext`

---

public interface Cascadable<C extends Cascadable<C>>
Facet of a constraint mapping creational context which allows to mark the underlying
element as to be validated in a cascaded way.

Author:
Gunnar Morling, Kevin Pollet <[email protected]> (C) 2011 SERLI

- 

## Method Summary

Modifier and Type
Method
Description
`GroupConversionTargetContext<C>`
`convertGroup(Class<?> from)`

Adds a group conversion for this cascadable element.

`C`
`valid()`

Marks the current element (property, parameter etc.) as cascadable.

- 

## Method Details

  - 

### valid

C valid()
Marks the current element (property, parameter etc.) as cascadable.

Returns:
The current creational context following the method chaining pattern.

  - 

### convertGroup

GroupConversionTargetContext<C> convertGroup(Class<?> from)
Adds a group conversion for this cascadable element. Several conversions may be configured for one element.

Parameters:
`from` - the source group of the conversion to be configured
Returns:
a creational context allow to set the target group of the conversion

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved