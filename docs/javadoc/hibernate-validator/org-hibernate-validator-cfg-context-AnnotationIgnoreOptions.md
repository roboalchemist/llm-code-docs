# Interface AnnotationIgnoreOptions<C extends AnnotationIgnoreOptions<C>>

All Known Subinterfaces:
`ConstructorConstraintMappingContext, CrossParameterConstraintMappingContext, MethodConstraintMappingContext, ParameterConstraintMappingContext, PropertyConstraintMappingContext, ReturnValueConstraintMappingContext, TypeConstraintMappingContext<C>`

---

public interface AnnotationIgnoreOptions<C extends AnnotationIgnoreOptions<C>>
Facet of a constraint mapping creational context which allows to configure how existing annotation should be treated.

Author:
Gunnar Morling

- 

## Method Summary

Modifier and Type
Method
Description
`C`
`ignoreAnnotations(boolean ignoreAnnotations)`

Specifies whether annotations at the given element should be ignored or not, overriding any setting given for
parent elements.

- 

## Method Details

  - 

### ignoreAnnotations

C ignoreAnnotations(boolean ignoreAnnotations)
Specifies whether annotations at the given element should be ignored or not, overriding any setting given for
parent elements. E.g. the setting given for a method parameter overrides the setting given for the method
declaring that parameter.

Parameters:
`ignoreAnnotations` - Whether to ignore annotation-based constraints or not.
Returns:
This context for method chaining.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved