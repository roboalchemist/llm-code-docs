# Interface ContainerElementTarget

All Known Subinterfaces:
`ContainerElementConstraintMappingContext, ParameterConstraintMappingContext, PropertyConstraintMappingContext, ReturnValueConstraintMappingContext`

---

@Incubating
public interface ContainerElementTarget
Facet of a constraint mapping creational context which allows to select a type argument or the component type of the
(return) type of the current property, parameter or method as target for the next operations.

Since:
6.0
Author:
Gunnar Morling

- 

## Method Summary

Modifier and Type
Method
Description
`ContainerElementConstraintMappingContext`
`containerElementType()`

Selects the single type argument of the current element's generic type as the target for the next operations.

`ContainerElementConstraintMappingContext`
`containerElementType(int index,
 int... nestedIndexes)`

Selects the single type argument of the current element's generic type as the target for the next operations.

- 

## Method Details

  - 

### containerElementType

ContainerElementConstraintMappingContext containerElementType()
Selects the single type argument of the current element's generic type as the target for the next operations.
Selects the component type if the current element is of an array type.

Returns:
A creational context representing the single type argument or the component type of the current element's
type.
Throws:
`ValidationException` - If the given element (property, return value or parameter) is not of a generic type
nor of an array type or is a generic type but has more than one type argument.

  - 

### containerElementType

ContainerElementConstraintMappingContext containerElementType(int index,
 int... nestedIndexes)
Selects the single type argument of the current element's generic type as the target for the next operations.
Selects the component type if the current element is of an array type.

Parameters:
`index` - The index of the type argument to configure. Pass 0 when navigating into an array type.
`nestedIndexes` - the nested index(es) in case the container element to configure is a generic type within
another generic type, e.g. `List<Map<String, String>>`, a multi-dimensional array or a combination of
(nested) parameterized and array types.
Returns:
A creational context representing the specified type argument.
Throws:
`ValidationException` - If the given element (property, return value or parameter) is not of a generic type
nor of an array type or is a generic type but has no type argument with the given index.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved