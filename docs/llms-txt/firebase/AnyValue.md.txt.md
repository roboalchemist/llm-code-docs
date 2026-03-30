# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.md.txt

# AnyValue

# AnyValue


```
@Serializable(with = AnyValueSerializer)
class AnyValue
```

<br />

*** ** * ** ***

Represents a variable or field of the Data Connect custom scalar type `Any`.

### Valid values for `AnyValue`

`AnyValue` can encapsulate `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`, `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html`, `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html`, a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html` of one of these types, or a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` whose values are one of these types. The values can be arbitrarily nested (for example, a list that contains a map that contains other maps, and so on). The lists and maps can contain heterogeneous values; for example, a single `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html` can contain a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value, some `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` values, and some `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html` values. The values of a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html` or a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html` may be `null`. The only exception is that a variable or field declared as `[Any]` in GraphQL may *not* have `null` values in the top-level list; however, nested lists or maps *may* contain null values.

### Storing `Int` in an `AnyValue`

To store an `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` value, simply convert it to a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` and store the `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` value.

### Storing `Long` in an `AnyValue`

To store a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` value, converting it to a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` can be lossy if the value is sufficiently large (or small) to not be exactly representable by `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html`. The *largest* `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` value that can be stored in a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` with its exact value is `2^53 -- 1` (`9007199254740991`). The *smallest* `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` value that can be stored in a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` with its exact value is `-(2^53 -- 1)` (`-9007199254740991`). This limitation is exactly the same in JavaScript, which does not have a native "int" or "long" type, but rather stores all numeric values in a 64-bit floating point value. See [MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) and [MIN_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER) for more details.

### Integration with `kotlinx.serialization`

To serialize a value of this type when using Data Connect, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/AnyValueSerializer`.

### Example

For example, suppose this schema and operation is defined in the GraphQL source:

```kotlin
type Foo @table { value: Any }

mutation FooInsert($value: Any) {
  key: foo_insert(data: { value: $value })
}
```

then a serializable "Variables" type could be defined as follows:

```kotlin
@Serializable
data class FooInsertVariables(
  @Serializable(with=AnyValueSerializer::class) val value: AnyValue?
)
```

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#AnyValue(kotlin.Boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#AnyValue(kotlin.Double)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#AnyValue(kotlin.collections.List)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>)` Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#AnyValue(kotlin.collections.Map)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>)` Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#AnyValue(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`. |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#hashCode()()` Calculates and returns the hash code for this object. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#value()` The native Kotlin type of the value encapsulated in this object. |

| ### Extension functions |
|---|---|
| `T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#(com.google.firebase.dataconnect.AnyValue).decode(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)( deserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<T>, serializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Decodes the encapsulated value using the given deserializer. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue#(com.google.firebase.dataconnect.AnyValue).decode()()` Decodes the encapsulated value using the *default* serializer for the return type, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`. |

## Public constructors

### AnyValue

```
AnyValue(value: Boolean)
```

Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html`.

### AnyValue

```
AnyValue(value: Double)
```

Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html`.

### AnyValue

```
AnyValue(value: List<Any?>)
```

Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html`.

An exception is thrown if any of the values of the list, or its sub-values, are invalid for being stored in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue`; see the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` class documentation for a detailed description of valid values.

This class makes a *deep copy* of the given list; therefore, any modifications to the list or its constituent lists or maps after this object is created will have no effect on this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` object.

### AnyValue

```
AnyValue(value: Map<String, Any?>)
```

Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html`.

An exception is thrown if any of the values of the map, or its sub-values, are invalid for being stored in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue`; see the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` class documentation for a detailed description of valid values.

This class makes a *deep copy* of the given map; therefore, any modifications to the map or its constituent lists or maps after this object is created will have no effect on this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` object.

### AnyValue

```
AnyValue(value: String)
```

Creates an instance that encapsulates the given `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`.

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` whose encapsulated value compares equal using the `==` operator to the given object. |

### hashCode

```
open fun hashCode(): Int
```

Calculates and returns the hash code for this object.

The hash code is *not* guaranteed to be stable across application restarts.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object, calculated from the encapsulated value. |

### toString

```
open fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object's encapsulated value. |

## Public properties

### value

```
val value: Any
```

The native Kotlin type of the value encapsulated in this object.

Although this type is `Any` it will be one of `String`, `Boolean`, `Double`, `List<Any?>` or `Map<String, Any?>`. See the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` class documentation for a detailed description of the types of values that are supported.

## Extension functions

### decode

```
fun <T : Any?> AnyValue.decode(
    deserializer: DeserializationStrategy<T>,
    serializersModule: SerializersModule? = null
): T
```

Decodes the encapsulated value using the given deserializer.

| Parameters |
|---|---|
| `deserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<T>` | The deserializer for the decoder to use. |
| `serializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? = null` | a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use during deserialization; may be `null` (the default) to *not* use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use during deserialization. |

| Returns |
|---|---|
| `T` | the object of type `T` created by decoding the encapsulated value using the given deserializer. |

### decode

```
inline fun <T : Any?> AnyValue.decode(): T
```

Decodes the encapsulated value using the *default* serializer for the return type, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`.

| Returns |
|---|---|
| `T` | the object of type `T` created by decoding the encapsulated value using the *default* serializer for the return type, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`. |