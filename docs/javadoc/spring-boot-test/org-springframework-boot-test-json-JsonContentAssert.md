# Class JsonContentAssert

java.lang.Object
org.assertj.core.api.AbstractAssert<JsonContentAssert, CharSequence>
org.springframework.boot.test.json.JsonContentAssert

All Implemented Interfaces:
`org.assertj.core.api.Assert<JsonContentAssert, CharSequence>, org.assertj.core.api.Descriptable<JsonContentAssert>, org.assertj.core.api.ExtensionPoints<JsonContentAssert, CharSequence>`

---

public class JsonContentAssert
extends org.assertj.core.api.AbstractAssert<JsonContentAssert, CharSequence>
AssertJ `Assert` for `JsonContent`.

Since:
1.4.0

- 

## Field Summary

### Fields inherited from class org.assertj.core.api.AbstractAssert

`actual, info, myself, objects, throwUnsupportedExceptionOnEquals`

- 

## Constructor Summary

Constructors

Constructor
Description
`JsonContentAssert(Class<?> resourceLoadClass,
 @Nullable CharSequence json)`

Create a new `JsonContentAssert` instance that will load resources as UTF-8.

`JsonContentAssert(Class<?> resourceLoadClass,
 @Nullable Charset charset,
 @Nullable CharSequence json)`

Create a new `JsonContentAssert` instance that will load resources in the
given `charset`.

- 

## Method Summary

Modifier and Type
Method
Description
`JsonContentAssert`
`doesNotHaveEmptyJsonPathValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path does not produce an
`empty` result.

`JsonContentAssert`
`doesNotHaveJsonPath(CharSequence expression,
 Object... args)`

Verify that the JSON path is not present, even if it has a `null` value.

`JsonContentAssert`
`doesNotHaveJsonPathValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces no result.

`<E> org.assertj.core.api.ListAssert<E>`
`extractingJsonPathArrayValue(CharSequence expression,
 Object... args)`

Extract the array value at the given JSON path for further object assertions.

`org.assertj.core.api.AbstractBooleanAssert<?>`
`extractingJsonPathBooleanValue(CharSequence expression,
 Object... args)`

Extract the boolean value at the given JSON path for further object assertions.

`<K,V> org.assertj.core.api.MapAssert<K,V>`
`extractingJsonPathMapValue(CharSequence expression,
 Object... args)`

Extract the map value at the given JSON path for further object assertions.

`org.assertj.core.api.AbstractObjectAssert<?,Number>`
`extractingJsonPathNumberValue(CharSequence expression,
 Object... args)`

Extract the number value at the given JSON path for further object assertions.

`org.assertj.core.api.AbstractCharSequenceAssert<?,String>`
`extractingJsonPathStringValue(CharSequence expression,
 Object... args)`

Extract the string value at the given JSON path for further object assertions.

`org.assertj.core.api.AbstractObjectAssert<?,Object>`
`extractingJsonPathValue(CharSequence expression,
 Object... args)`

Extract the value at the given JSON path for further object assertions.

`JsonContentAssert`
`hasEmptyJsonPathValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces an
`empty` result.

`JsonContentAssert`
`hasJsonPath(CharSequence expression,
 Object... args)`

Verify that the JSON path is present without checking if it has a value.

`JsonContentAssert`
`hasJsonPathArrayValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces a non-null array
result.

`JsonContentAssert`
`hasJsonPathBooleanValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces a non-null boolean
result.

`JsonContentAssert`
`hasJsonPathMapValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces a non-null map result.

`JsonContentAssert`
`hasJsonPathNumberValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces a non-null number
result.

`JsonContentAssert`
`hasJsonPathStringValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces a non-null string
result.

`JsonContentAssert`
`hasJsonPathValue(CharSequence expression,
 Object... args)`

Verify that the actual value at the given JSON path produces a non-null result.

`JsonContentAssert`
`isEqualTo(@Nullable Object expected)`

Overridden version of `isEqualTo` to perform JSON tests based on the object
type.

`JsonContentAssert`
`isEqualToJson(byte[] expected)`

Verifies that the actual value is `leniently` equal
to the specified JSON bytes.

`JsonContentAssert`
`isEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is equal to the specified JSON bytes.

`JsonContentAssert`
`isEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is equal to the specified JSON bytes.

`JsonContentAssert`
`isEqualToJson(File expected)`

Verifies that the actual value is `leniently` equal
to the specified JSON file.

`JsonContentAssert`
`isEqualToJson(File expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is equal to the specified JSON file.

`JsonContentAssert`
`isEqualToJson(File expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is equal to the specified JSON file.

`JsonContentAssert`
`isEqualToJson(InputStream expected)`

Verifies that the actual value is `leniently` equal
to the specified JSON input stream.

`JsonContentAssert`
`isEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is equal to the specified JSON input stream.

`JsonContentAssert`
`isEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is equal to the specified JSON input stream.

`JsonContentAssert`
`isEqualToJson(@Nullable CharSequence expected)`

Verifies that the actual value is `leniently` equal
to the specified JSON.

`JsonContentAssert`
`isEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is equal to the specified JSON.

`JsonContentAssert`
`isEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is equal to the specified JSON.

`JsonContentAssert`
`isEqualToJson(String path,
 Class<?> resourceLoadClass)`

Verifies that the actual value is `leniently` equal
to the specified JSON resource.

`JsonContentAssert`
`isEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is equal to the specified JSON resource.

`JsonContentAssert`
`isEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is equal to the specified JSON resource.

`JsonContentAssert`
`isEqualToJson(org.springframework.core.io.Resource expected)`

Verifies that the actual value is `leniently` equal
to the specified JSON resource.

`JsonContentAssert`
`isEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is equal to the specified JSON resource.

`JsonContentAssert`
`isEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is equal to the specified JSON resource.

`JsonContentAssert`
`isNotEqualTo(@Nullable Object expected)`

Overridden version of `isNotEqualTo` to perform JSON tests based on the
object type.

`JsonContentAssert`
`isNotEqualToJson(byte[] expected)`

Verifies that the actual value is not `leniently`
equal to the specified JSON bytes.

`JsonContentAssert`
`isNotEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is not equal to the specified JSON bytes.

`JsonContentAssert`
`isNotEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is not equal to the specified JSON bytes.

`JsonContentAssert`
`isNotEqualToJson(File expected)`

Verifies that the actual value is not `leniently`
equal to the specified JSON file.

`JsonContentAssert`
`isNotEqualToJson(File expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is not equal to the specified JSON file.

`JsonContentAssert`
`isNotEqualToJson(File expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is not equal to the specified JSON file.

`JsonContentAssert`
`isNotEqualToJson(InputStream expected)`

Verifies that the actual value is not `leniently`
equal to the specified JSON input stream.

`JsonContentAssert`
`isNotEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is not equal to the specified JSON input stream.

`JsonContentAssert`
`isNotEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is not equal to the specified JSON input stream.

`JsonContentAssert`
`isNotEqualToJson(@Nullable CharSequence expected)`

Verifies that the actual value is not `leniently`
equal to the specified JSON.

`JsonContentAssert`
`isNotEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is not equal to the specified JSON.

`JsonContentAssert`
`isNotEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is not equal to the specified JSON.

`JsonContentAssert`
`isNotEqualToJson(String path,
 Class<?> resourceLoadClass)`

Verifies that the actual value is not `leniently`
equal to the specified JSON resource.

`JsonContentAssert`
`isNotEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is not equal to the specified JSON resource.

`JsonContentAssert`
`isNotEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is not equal to the specified JSON resource.

`JsonContentAssert`
`isNotEqualToJson(org.springframework.core.io.Resource expected)`

Verifies that the actual value is not `leniently`
equal to the specified JSON resource.

`JsonContentAssert`
`isNotEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)`

Verifies that the actual value is not equal to the specified JSON resource.

`JsonContentAssert`
`isNotEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)`

Verifies that the actual value is not equal to the specified JSON resource.

`JsonContentAssert`
`isNotStrictlyEqualToJson(byte[] expected)`

Verifies that the actual value is not `strictly` equal
to the specified JSON bytes.

`JsonContentAssert`
`isNotStrictlyEqualToJson(File expected)`

Verifies that the actual value is not `strictly` equal
to the specified JSON file.

`JsonContentAssert`
`isNotStrictlyEqualToJson(InputStream expected)`

Verifies that the actual value is not `strictly` equal
to the specified JSON input stream.

`JsonContentAssert`
`isNotStrictlyEqualToJson(CharSequence expected)`

Verifies that the actual value is not `strictly` equal
to the specified JSON.

`JsonContentAssert`
`isNotStrictlyEqualToJson(String path,
 Class<?> resourceLoadClass)`

Verifies that the actual value is not `strictly` equal
to the specified JSON resource.

`JsonContentAssert`
`isNotStrictlyEqualToJson(org.springframework.core.io.Resource expected)`

Verifies that the actual value is not `strictly` equal
to the specified JSON resource.

`JsonContentAssert`
`isStrictlyEqualToJson(byte[] expected)`

Verifies that the actual value is `strictly` equal to
the specified JSON bytes.

`JsonContentAssert`
`isStrictlyEqualToJson(File expected)`

Verifies that the actual value is `strictly` equal to
the specified JSON file.

`JsonContentAssert`
`isStrictlyEqualToJson(InputStream expected)`

Verifies that the actual value is `strictly` equal to
the specified JSON input stream.

`JsonContentAssert`
`isStrictlyEqualToJson(CharSequence expected)`

Verifies that the actual value is `strictly` equal to
the specified JSON.

`JsonContentAssert`
`isStrictlyEqualToJson(String path,
 Class<?> resourceLoadClass)`

Verifies that the actual value is `strictly` equal to
the specified JSON resource.

`JsonContentAssert`
`isStrictlyEqualToJson(org.springframework.core.io.Resource expected)`

Verifies that the actual value is `strictly` equal to
the specified JSON resource.

### Methods inherited from class org.assertj.core.api.AbstractAssert

`actual, areEqual, asInstanceOf, asList, assertionError, asString, describedAs, descriptionText, doesNotHave, doesNotHaveSameClassAs, doesNotHaveSameHashCodeAs, doesNotHaveToString, doesNotHaveToString, doesNotMatch, doesNotMatch, equals, extracting, extracting, failure, failureWithActualExpected, failWithActualExpectedAndMessage, failWithMessage, getWritableAssertionInfo, has, hashCode, hasSameClassAs, hasSameHashCodeAs, hasToString, hasToString, inBinary, inHexadecimal, is, isElementOfCustomAssert, isExactlyInstanceOf, isIn, isIn, isInstanceOf, isInstanceOfAny, isInstanceOfSatisfying, isNot, isNotExactlyInstanceOf, isNotIn, isNotIn, isNotInstanceOf, isNotInstanceOfAny, isNotNull, isNotOfAnyClassIn, isNotSameAs, isNull, isOfAnyClassIn, isSameAs, matches, matches, newListAssertInstance, overridingErrorMessage, overridingErrorMessage, satisfies, satisfies, satisfies, satisfiesAnyOf, satisfiesAnyOf, satisfiesAnyOfForProxy, satisfiesForProxy, setCustomRepresentation, setDescriptionConsumer, setPrintAssertionsDescription, throwAssertionError, usingComparator, usingComparator, usingDefaultComparator, usingEquals, usingEquals, usingRecursiveAssertion, usingRecursiveAssertion, usingRecursiveComparison, usingRecursiveComparison, withFailMessage, withFailMessage, withRepresentation, withThreadDumpOnError`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.assertj.core.api.Descriptable

`as, as, as, describedAs, describedAs`

- 

## Constructor Details

  - 

### JsonContentAssert

public JsonContentAssert(Class<?> resourceLoadClass,
 @Nullable CharSequence json)
Create a new `JsonContentAssert` instance that will load resources as UTF-8.

Parameters:
`resourceLoadClass` - the source class used to load resources
`json` - the actual JSON content

  - 

### JsonContentAssert

public JsonContentAssert(Class<?> resourceLoadClass,
 @Nullable Charset charset,
 @Nullable CharSequence json)
Create a new `JsonContentAssert` instance that will load resources in the
given `charset`.

Parameters:
`resourceLoadClass` - the source class used to load resources
`charset` - the charset of the JSON resources
`json` - the actual JSON content
Since:
1.4.1

- 

## Method Details

  - 

### isEqualTo

public JsonContentAssert isEqualTo(@Nullable Object expected)
Overridden version of `isEqualTo` to perform JSON tests based on the object
type.

Specified by:
`isEqualTo` in interface `org.assertj.core.api.Assert<JsonContentAssert, CharSequence>`
Overrides:
`isEqualTo` in class `org.assertj.core.api.AbstractAssert<JsonContentAssert, CharSequence>`
See Also:

    - `AbstractAssert.isEqualTo(java.lang.Object)`

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(@Nullable CharSequence expected)
Verifies that the actual value is `leniently` equal
to the specified JSON. The `expected` value can contain the JSON itself or,
if it ends with `.json`, the name of a resource to be loaded using
`resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(String path,
 Class<?> resourceLoadClass)
Verifies that the actual value is `leniently` equal
to the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(byte[] expected)
Verifies that the actual value is `leniently` equal
to the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(File expected)
Verifies that the actual value is `leniently` equal
to the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(InputStream expected)
Verifies that the actual value is `leniently` equal
to the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(org.springframework.core.io.Resource expected)
Verifies that the actual value is `leniently` equal
to the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isStrictlyEqualToJson

public JsonContentAssert isStrictlyEqualToJson(CharSequence expected)
Verifies that the actual value is `strictly` equal to
the specified JSON. The `expected` value can contain the JSON itself or, if
it ends with `.json`, the name of a resource to be loaded using
`resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isStrictlyEqualToJson

public JsonContentAssert isStrictlyEqualToJson(String path,
 Class<?> resourceLoadClass)
Verifies that the actual value is `strictly` equal to
the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isStrictlyEqualToJson

public JsonContentAssert isStrictlyEqualToJson(byte[] expected)
Verifies that the actual value is `strictly` equal to
the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isStrictlyEqualToJson

public JsonContentAssert isStrictlyEqualToJson(File expected)
Verifies that the actual value is `strictly` equal to
the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isStrictlyEqualToJson

public JsonContentAssert isStrictlyEqualToJson(InputStream expected)
Verifies that the actual value is `strictly` equal to
the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isStrictlyEqualToJson

public JsonContentAssert isStrictlyEqualToJson(org.springframework.core.io.Resource expected)
Verifies that the actual value is `strictly` equal to
the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is equal to the specified JSON. The `expected`
value can contain the JSON itself or, if it ends with `.json`, the name of a
resource to be loaded using `resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is equal to the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is equal to the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(File expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is equal to the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is equal to the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is equal to the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is equal to the specified JSON. The `expected`
value can contain the JSON itself or, if it ends with `.json`, the name of a
resource to be loaded using `resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is equal to the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is equal to the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(File expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is equal to the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is equal to the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isEqualToJson

public JsonContentAssert isEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is equal to the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is not equal to the given one

  - 

### isNotEqualTo

public JsonContentAssert isNotEqualTo(@Nullable Object expected)
Overridden version of `isNotEqualTo` to perform JSON tests based on the
object type.

Specified by:
`isNotEqualTo` in interface `org.assertj.core.api.Assert<JsonContentAssert, CharSequence>`
Overrides:
`isNotEqualTo` in class `org.assertj.core.api.AbstractAssert<JsonContentAssert, CharSequence>`
See Also:

    - `AbstractAssert.isEqualTo(java.lang.Object)`

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(@Nullable CharSequence expected)
Verifies that the actual value is not `leniently`
equal to the specified JSON. The `expected` value can contain the JSON itself
or, if it ends with `.json`, the name of a resource to be loaded using
`resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(String path,
 Class<?> resourceLoadClass)
Verifies that the actual value is not `leniently`
equal to the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(byte[] expected)
Verifies that the actual value is not `leniently`
equal to the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(File expected)
Verifies that the actual value is not `leniently`
equal to the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(InputStream expected)
Verifies that the actual value is not `leniently`
equal to the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(org.springframework.core.io.Resource expected)
Verifies that the actual value is not `leniently`
equal to the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotStrictlyEqualToJson

public JsonContentAssert isNotStrictlyEqualToJson(CharSequence expected)
Verifies that the actual value is not `strictly` equal
to the specified JSON. The `expected` value can contain the JSON itself or,
if it ends with `.json`, the name of a resource to be loaded using
`resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotStrictlyEqualToJson

public JsonContentAssert isNotStrictlyEqualToJson(String path,
 Class<?> resourceLoadClass)
Verifies that the actual value is not `strictly` equal
to the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotStrictlyEqualToJson

public JsonContentAssert isNotStrictlyEqualToJson(byte[] expected)
Verifies that the actual value is not `strictly` equal
to the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotStrictlyEqualToJson

public JsonContentAssert isNotStrictlyEqualToJson(File expected)
Verifies that the actual value is not `strictly` equal
to the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotStrictlyEqualToJson

public JsonContentAssert isNotStrictlyEqualToJson(InputStream expected)
Verifies that the actual value is not `strictly` equal
to the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotStrictlyEqualToJson

public JsonContentAssert isNotStrictlyEqualToJson(org.springframework.core.io.Resource expected)
Verifies that the actual value is not `strictly` equal
to the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is not equal to the specified JSON. The
`expected` value can contain the JSON itself or, if it ends with
`.json`, the name of a resource to be loaded using `resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is not equal to the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is not equal to the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(File expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is not equal to the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is not equal to the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.JSONCompareMode compareMode)
Verifies that the actual value is not equal to the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
`compareMode` - the compare mode used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(CharSequence expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is not equal to the specified JSON. The
`expected` value can contain the JSON itself or, if it ends with
`.json`, the name of a resource to be loaded using `resourceLoadClass`.

Parameters:
`expected` - the expected JSON or the name of a resource containing the expected
JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(String path,
 Class<?> resourceLoadClass,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is not equal to the specified JSON resource.

Parameters:
`path` - the name of a resource containing the expected JSON
`resourceLoadClass` - the source class used to load the resource
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(byte[] expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is not equal to the specified JSON bytes.

Parameters:
`expected` - the expected JSON bytes
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(File expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is not equal to the specified JSON file.

Parameters:
`expected` - a file containing the expected JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(InputStream expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is not equal to the specified JSON input stream.

Parameters:
`expected` - an input stream containing the expected JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### isNotEqualToJson

public JsonContentAssert isNotEqualToJson(org.springframework.core.io.Resource expected,
 org.skyscreamer.jsonassert.comparator.JSONComparator comparator)
Verifies that the actual value is not equal to the specified JSON resource.

Parameters:
`expected` - a resource containing the expected JSON
`comparator` - the comparator used when checking
Returns:
`this` assertion object
Throws:
`AssertionError` - if the actual JSON value is equal to the given one

  - 

### hasJsonPath

public JsonContentAssert hasJsonPath(CharSequence expression,
 Object... args)
Verify that the JSON path is present without checking if it has a value.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is missing
Since:
2.2.0
See Also:

    - `hasJsonPathValue(CharSequence, Object...)`

  - 

### hasJsonPathValue

public JsonContentAssert hasJsonPathValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces a non-null result. If
the JSON path expression is not definite, this
method verifies that the value at the given path is not *empty*.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is missing

  - 

### hasJsonPathStringValue

public JsonContentAssert hasJsonPathStringValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces a non-null string
result.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is missing or not a string

  - 

### hasJsonPathNumberValue

public JsonContentAssert hasJsonPathNumberValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces a non-null number
result.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is missing or not a number

  - 

### hasJsonPathBooleanValue

public JsonContentAssert hasJsonPathBooleanValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces a non-null boolean
result.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is missing or not a boolean

  - 

### hasJsonPathArrayValue

public JsonContentAssert hasJsonPathArrayValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces a non-null array
result.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is missing or not an array

  - 

### hasJsonPathMapValue

public JsonContentAssert hasJsonPathMapValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces a non-null map result.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is missing or not a map

  - 

### hasEmptyJsonPathValue

public JsonContentAssert hasEmptyJsonPathValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces an
`empty` result.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is not empty

  - 

### doesNotHaveJsonPath

public JsonContentAssert doesNotHaveJsonPath(CharSequence expression,
 Object... args)
Verify that the JSON path is not present, even if it has a `null` value.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is not missing
Since:
2.2.0
See Also:

    - `doesNotHaveJsonPathValue(CharSequence, Object...)`

  - 

### doesNotHaveJsonPathValue

public JsonContentAssert doesNotHaveJsonPathValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path produces no result. If the JSON
path expression is not definite, this method
verifies that the value at the given path is *empty*.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is not missing

  - 

### doesNotHaveEmptyJsonPathValue

public JsonContentAssert doesNotHaveEmptyJsonPathValue(CharSequence expression,
 Object... args)
Verify that the actual value at the given JSON path does not produce an
`empty` result.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
`this` assertion object
Throws:
`AssertionError` - if the value at the given path is empty

  - 

### extractingJsonPathValue

@CheckReturnValue
public org.assertj.core.api.AbstractObjectAssert<?,Object> extractingJsonPathValue(CharSequence expression,
 Object... args)
Extract the value at the given JSON path for further object assertions.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
a new assertion object whose object under test is the extracted item
Throws:
`AssertionError` - if the path is not valid

  - 

### extractingJsonPathStringValue

@CheckReturnValue
public org.assertj.core.api.AbstractCharSequenceAssert<?,String> extractingJsonPathStringValue(CharSequence expression,
 Object... args)
Extract the string value at the given JSON path for further object assertions.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
a new assertion object whose object under test is the extracted item
Throws:
`AssertionError` - if the path is not valid or does not result in a string

  - 

### extractingJsonPathNumberValue

@CheckReturnValue
public org.assertj.core.api.AbstractObjectAssert<?,Number> extractingJsonPathNumberValue(CharSequence expression,
 Object... args)
Extract the number value at the given JSON path for further object assertions.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
a new assertion object whose object under test is the extracted item
Throws:
`AssertionError` - if the path is not valid or does not result in a number

  - 

### extractingJsonPathBooleanValue

@CheckReturnValue
public org.assertj.core.api.AbstractBooleanAssert<?> extractingJsonPathBooleanValue(CharSequence expression,
 Object... args)
Extract the boolean value at the given JSON path for further object assertions.

Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
a new assertion object whose object under test is the extracted item
Throws:
`AssertionError` - if the path is not valid or does not result in a boolean

  - 

### extractingJsonPathArrayValue

@CheckReturnValue
public <E> org.assertj.core.api.ListAssert<E> extractingJsonPathArrayValue(CharSequence expression,
 Object... args)
Extract the array value at the given JSON path for further object assertions.

Type Parameters:
`E` - element type
Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
a new assertion object whose object under test is the extracted item
Throws:
`AssertionError` - if the path is not valid or does not result in an array

  - 

### extractingJsonPathMapValue

@CheckReturnValue
public <K,V> org.assertj.core.api.MapAssert<K,V> extractingJsonPathMapValue(CharSequence expression,
 Object... args)
Extract the map value at the given JSON path for further object assertions.

Type Parameters:
`K` - key type
`V` - value type
Parameters:
`expression` - the `JsonPath` expression
`args` - arguments to parameterize the `JsonPath` expression with, using
formatting specifiers defined in `String.format(String, Object...)`
Returns:
a new assertion object whose object under test is the extracted item
Throws:
`AssertionError` - if the path is not valid or does not result in a map