# Interface Constrainable<C extends Constrainable<C>>

All Known Subinterfaces:
`ContainerElementConstraintMappingContext, CrossParameterConstraintMappingContext, ParameterConstraintMappingContext, PropertyConstraintMappingContext, ReturnValueConstraintMappingContext, TypeConstraintMappingContext<C>`

---

public interface Constrainable<C extends Constrainable<C>>
Facet of a constraint mapping creational context which allows to place
constraints on the underlying element.

Author:
Gunnar Morling, Kevin Pollet <[email protected]> (C) 2011 SERLI

- 

## Method Summary

Modifier and Type
Method
Description
`C`
`constraint(ConstraintDef<?,?> definition)`

Adds a new constraint.

- 

## Method Details

  - 

### constraint

C constraint(ConstraintDef<?,?> definition)
Adds a new constraint.

Parameters:
`definition` - The constraint to add.
Returns:
The current creational context following the method chaining pattern.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved