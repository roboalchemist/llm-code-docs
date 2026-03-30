# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.md.txt

# JsonSchema

# JsonSchema


```
class JsonSchema<T : Any>
```

<br />

*** ** * ** ***

Definition of a data type.

These types can be objects, but also primitives and arrays. Represents a select subset of an [JsonSchema object](https://json-schema.org/specification).

**Note:** While optional, including a `description` field in your `JsonSchema` is strongly encouraged. The more information the model has about what it's expected to generate, the better the results.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#anyOf(kotlin.collections.List)(schemas: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` representing a value that must conform to *any* (one of) the provided sub-schema. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<T>>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#array(com.google.firebase.ai.type.JsonSchema,kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Int,kotlin.Int)( items: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minItems: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, maxItems: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for an array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#boolean(kotlin.String,kotlin.Boolean,kotlin.String)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` representing a boolean value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#double(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a double-precision floating-point number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for an enumeration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#enumeration(kotlin.collections.List,kotlin.reflect.KClass,kotlin.String,kotlin.Boolean,kotlin.String)( values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, clazz: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<T>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for an enumeration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-float/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#float(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a single-precision floating-point number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#integer(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a 32-bit signed integer number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#long(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a 64-bit signed integer number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>, optionalProperties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a complex data type. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#obj(kotlin.collections.Map,kotlin.reflect.KClass,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>, clazz: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<T>, optionalProperties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a complex data type. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema.Companion#string(kotlin.String,kotlin.Boolean,com.google.firebase.ai.type.StringFormat,kotlin.String)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, format: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/StringFormat?, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a string. |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#getSerializer()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#anyOf()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#clazz()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#description()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#enum()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#format()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#items()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#maxItems()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#maximum()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#minItems()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#minimum()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#nullable()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#properties()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#required()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#title()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema#type()` |

## Public companion functions

### anyOf

```
fun anyOf(schemas: List<JsonSchema<*>>): JsonSchema<String>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` representing a value that must conform to *any* (one of) the provided sub-schema.

Example: A field that can hold either a simple userID or a more detailed user object.

```kotlin
JsonSchema.anyOf( listOf( JsonSchema.integer(description = "User ID"), JsonSchema.obj( mapOf(
    "userID" to JsonSchema.integer(description = "User ID"),
    "username" to JsonSchema.string(description = "Username")
)))
```

| Parameters |
|---|---|
| `schemas: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>` | The list of valid schemas which could be here |

### array

```
fun <T : Any> array(
    items: JsonSchema<T>,
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null,
    minItems: Int? = null,
    maxItems: Int? = null
): JsonSchema<List<T>>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for an array.

| Parameters |
|---|---|
| `items: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<T>` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` of the elements stored in the array. |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the array represents. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### boolean

```
fun boolean(description: String? = null, nullable: Boolean = false, title: String? = null): JsonSchema<Boolean>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` representing a boolean value.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the boolean should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### double

```
fun double(
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null,
    minimum: Double? = null,
    maximum: Double? = null
): JsonSchema<Double>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a double-precision floating-point number.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the number should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### enumeration

```
fun enumeration(
    values: List<String>,
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null
): JsonSchema<String>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for an enumeration.

For example, the cardinal directions can be represented as:

```kotlin
JsonSchema.enumeration(listOf("north", "east", "south", "west"), "Cardinal directions")
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | The list of valid values for this enumeration |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | The description of what the parameter should contain or represent |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### enumeration

```
fun <T : Any> enumeration(
    values: List<String>,
    clazz: KClass<T>,
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null
): JsonSchema<T>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for an enumeration.

For example, the cardinal directions can be represented as:

```kotlin
JsonSchema.enumeration(
  listOf("north", "east", "south", "west"),
  Direction::class,
  "Cardinal directions"
)
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | The list of valid values for this enumeration |
| `clazz: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<T>` | the real class that this schema represents |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | The description of what the parameter should contain or represent |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### float

```
fun float(
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null,
    minimum: Double? = null,
    maximum: Double? = null
): JsonSchema<Float>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a single-precision floating-point number.

**Important:** This `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the number should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### integer

```
fun integer(
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null,
    minimum: Double? = null,
    maximum: Double? = null
): JsonSchema<Int>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a 32-bit signed integer number.

**Important:** This `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the integer should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### long

```
fun long(
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null,
    minimum: Double? = null,
    maximum: Double? = null
): JsonSchema<Long>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a 64-bit signed integer number.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the number should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### obj

```
fun obj(
    properties: Map<String, JsonSchema<*>>,
    optionalProperties: List<String> = emptyList(),
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null
): JsonSchema<JsonObject>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema`.

**Example:** A `city` could be represented with the following object `JsonSchema`.

```kotlin
JsonSchema.obj(mapOf(
  "name"  to JsonSchema.string(),
  "population" to JsonSchema.integer()
))
```

| Parameters |
|---|---|
| `properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>` | The map of the object's property names to their `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema`s. |
| `optionalProperties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList()` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the object represents. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### obj

```
fun <T : Any> obj(
    properties: Map<String, JsonSchema<*>>,
    clazz: KClass<T>,
    optionalProperties: List<String> = emptyList(),
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null
): JsonSchema<T>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema`.

**Example:** A `city` could be represented with the following object `JsonSchema`.

```kotlin
JsonSchema.obj(mapOf(
    "name"  to JsonSchema.string(),
    "population" to JsonSchema.integer()
  ),
  City::class
)
```

| Parameters |
|---|---|
| `properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema<*>>` | The map of the object's property names to their `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema`s. |
| `clazz: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<T>` | the real class that this schema represents |
| `optionalProperties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList()` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the object represents. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### string

```
fun string(
    description: String? = null,
    nullable: Boolean = false,
    format: StringFormat? = null,
    title: String? = null
): JsonSchema<String>
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/JsonSchema` for a string.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the string should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |
| `format: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/StringFormat? = null` | An optional pattern that values need to adhere to. |

## Public functions

### getSerializer

```
fun getSerializer(): KSerializer<T>
```

## Public properties

### anyOf

```
val anyOf: List<JsonSchema<*>>?
```

### clazz

```
val clazz: KClass<T>
```

### description

```
val description: String?
```

### enum

```
val enum: List<String>?
```

### format

```
val format: String?
```

### items

```
val items: JsonSchema<*>?
```

### maxItems

```
val maxItems: Int?
```

### maximum

```
val maximum: Double?
```

### minItems

```
val minItems: Int?
```

### minimum

```
val minimum: Double?
```

### nullable

```
val nullable: Boolean?
```

### properties

```
val properties: Map<String, JsonSchema<*>>?
```

### required

```
val required: List<String>?
```

### title

```
val title: String?
```

### type

```
val type: String
```