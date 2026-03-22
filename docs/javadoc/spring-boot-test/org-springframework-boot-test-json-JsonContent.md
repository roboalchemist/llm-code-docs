# Class JsonContent<T>

java.lang.Object
org.springframework.boot.test.json.JsonContent<T>

Type Parameters:
`T` - the source type that created the content

All Implemented Interfaces:
`org.assertj.core.api.AssertProvider<JsonContentAssert>`

---

public final class JsonContent<T>
extends Object
implements org.assertj.core.api.AssertProvider<JsonContentAssert>
JSON content usually created from a JSON tester. Generally used only to
`provide` `JsonContentAssert` to AssertJ `assertThat`
calls.

Since:
1.4.0

- 

## Constructor Summary

Constructors

Constructor
Description
`JsonContent(Class<?> resourceLoadClass,
 @Nullable org.springframework.core.ResolvableType type,
 String json)`

Create a new `JsonContent` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`JsonContentAssert`
`assertThat()`

Deprecated.
to prevent accidental use.

`String`
`getJson()`

Return the actual JSON content string.

`String`
`toString()`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### JsonContent

public JsonContent(Class<?> resourceLoadClass,
 @Nullable org.springframework.core.ResolvableType type,
 String json)
Create a new `JsonContent` instance.

Parameters:
`resourceLoadClass` - the source class used to load resources
`type` - the type under test (or `null` if not known)
`json` - the actual JSON content

- 

## Method Details

  - 

### assertThat

@Deprecated(since="1.5.7",
            forRemoval=false)
public JsonContentAssert assertThat()
Deprecated.
to prevent accidental use. Prefer standard AssertJ
`assertThat(context)...` calls instead.

Use AssertJ's `assertThat`
instead.

Specified by:
`assertThat` in interface `org.assertj.core.api.AssertProvider<T>`

  - 

### getJson

public String getJson()
Return the actual JSON content string.

Returns:
the JSON content

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`