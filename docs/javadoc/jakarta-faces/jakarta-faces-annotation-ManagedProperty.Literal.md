Package jakarta.faces.annotation

# Class ManagedProperty.Literal

java.lang.Object
jakarta.enterprise.util.AnnotationLiteral<ManagedProperty>
jakarta.faces.annotation.ManagedProperty.Literal

All Implemented Interfaces:
`Annotation`

Enclosing class:
ManagedProperty

---

public static final class ManagedProperty.Literal
extends jakarta.enterprise.util.AnnotationLiteral<ManagedProperty>
implements ManagedProperty

 Supports inline instantiation of the `ManagedProperty` qualifier.

Since:
4.0
See Also:

- Serialized Form

-

## Nested Class Summary

## Nested classes/interfaces inherited from class jakarta.faces.annotation.ManagedProperty

`ManagedProperty.Literal`

-

## Field Summary

Fields

Modifier and Type
Field
Description
`static final ManagedProperty.Literal`
`INSTANCE`

Instance of the `ManagedProperty` qualifier.

-

## Method Summary

Modifier and Type
Method
Description
`static ManagedProperty.Literal`
`of(String value)`

`String`
`value()`

### Methods inherited from class jakarta.enterprise.util.AnnotationLiteral

`annotationType, equals, hashCode, toString`

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

-

## Field Details

-

### INSTANCE

public static final ManagedProperty.Literal INSTANCE
Instance of the `ManagedProperty` qualifier.

-

## Method Details

-

### of

public static ManagedProperty.Literal of(String value)

-

### value

public String value()
