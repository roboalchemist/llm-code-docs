# Class ObjectContent<T>

java.lang.Object
org.springframework.boot.test.json.ObjectContent<T>

Type Parameters:
`T` - the content type

All Implemented Interfaces:
`org.assertj.core.api.AssertProvider<ObjectContentAssert<T>>`

---

public final class ObjectContent<T>
extends Object
implements org.assertj.core.api.AssertProvider<ObjectContentAssert<T>>
Object content usually created from `AbstractJsonMarshalTester`. Generally used
only to `provide` `ObjectContentAssert` to AssertJ
`assertThat` calls.

Since:
1.4.0

- 

## Constructor Summary

Constructors

Constructor
Description
`ObjectContent(@Nullable org.springframework.core.ResolvableType type,
 T object)`

Create a new `ObjectContent` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`ObjectContentAssert<T>`
`assertThat()`
 
`T`
`getObject()`

Return the actual object content.

`String`
`toString()`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### ObjectContent

public ObjectContent(@Nullable org.springframework.core.ResolvableType type,
 T object)
Create a new `ObjectContent` instance.

Parameters:
`type` - the type under test (or `null` if not known)
`object` - the actual object content

- 

## Method Details

  - 

### assertThat

public ObjectContentAssert<T> assertThat()

Specified by:
`assertThat` in interface `org.assertj.core.api.AssertProvider<T>`

  - 

### getObject

public T getObject()
Return the actual object content.

Returns:
the object content

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`