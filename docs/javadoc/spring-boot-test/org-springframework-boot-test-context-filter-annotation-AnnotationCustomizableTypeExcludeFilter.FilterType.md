# Enum Class AnnotationCustomizableTypeExcludeFilter.FilterType

java.lang.Object
java.lang.Enum<AnnotationCustomizableTypeExcludeFilter.FilterType>
org.springframework.boot.test.context.filter.annotation.AnnotationCustomizableTypeExcludeFilter.FilterType

All Implemented Interfaces:
`Serializable, Comparable<AnnotationCustomizableTypeExcludeFilter.FilterType>, Constable`

Enclosing class:
`AnnotationCustomizableTypeExcludeFilter`

---

protected static enum AnnotationCustomizableTypeExcludeFilter.FilterType
extends Enum<AnnotationCustomizableTypeExcludeFilter.FilterType>

Since:
4.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class Enum

`Enum.EnumDesc<E>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`EXCLUDE`
 
`INCLUDE`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static AnnotationCustomizableTypeExcludeFilter.FilterType`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static AnnotationCustomizableTypeExcludeFilter.FilterType[]`
`values()`

Returns an array containing the constants of this enum class, in
the order they are declared.

### Methods inherited from class Enum

`clone, compareTo, describeConstable, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

### Methods inherited from class Object

`getClass, notify, notifyAll, wait, wait, wait`

- 

## Enum Constant Details

  - 

### INCLUDE

public static final AnnotationCustomizableTypeExcludeFilter.FilterType INCLUDE

  - 

### EXCLUDE

public static final AnnotationCustomizableTypeExcludeFilter.FilterType EXCLUDE

- 

## Method Details

  - 

### values

public static AnnotationCustomizableTypeExcludeFilter.FilterType[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static AnnotationCustomizableTypeExcludeFilter.FilterType valueOf(String name)
Returns the enum constant of this class with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum class has no constant with the specified name
`NullPointerException` - if the argument is null