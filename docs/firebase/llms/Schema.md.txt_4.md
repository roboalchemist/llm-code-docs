# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.md.txt

# Schema

# Schema


```
class Schema
```

<br />

*** ** * ** ***

Definition of a data type.

These types can be objects, but also primitives and arrays. Represents a select subset of an [OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema).

**Note:** While optional, including a `description` field in your `Schema` is strongly encouraged. The more information the model has about what it's expected to generate, the better the results.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#anyOf(kotlin.collections.List)(schemas: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema>)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` representing a value that must conform to *any* (one of) the provided sub-schema. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#array(com.google.firebase.ai.type.Schema,kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Int,kotlin.Int)( items: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minItems: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?, maxItems: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for an array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#boolean(kotlin.String,kotlin.Boolean,kotlin.String)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` representing a boolean value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#double(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a double-precision floating-point number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for an enumeration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#float(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a single-precision floating-point number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#integer(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a 32-bit signed integer number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#long(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, minimum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?, maximum: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a 64-bit signed integer number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema>, optionalProperties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a complex data type. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#string(kotlin.String,kotlin.Boolean,com.google.firebase.ai.type.StringFormat,kotlin.String)( description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, format: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/StringFormat?, title: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a string. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#anyOf()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#description()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#enum()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#format()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#items()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#maxItems()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#maximum()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#minItems()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#minimum()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#nullable()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#properties()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#required()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#title()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#type()` |

## Public companion functions

### anyOf

```
fun anyOf(schemas: List<Schema>): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` representing a value that must conform to *any* (one of) the provided sub-schema.

Example: A field that can hold either a simple userID or a more detailed user object.

```kotlin
Schema.anyOf( listOf( Schema.integer(description = "User ID"), Schema.obj( mapOf(
    "userID" to Schema.integer(description = "User ID"),
    "username" to Schema.string(description = "Username")
)))
```

| Parameters |
|---|---|
| `schemas: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema>` | The list of valid schemas which could be here |

### array

```
fun array(
    items: Schema,
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null,
    minItems: Int? = null,
    maxItems: Int? = null
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for an array.

| Parameters |
|---|---|
| `items: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` of the elements stored in the array. |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the array represents. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### boolean

```
fun boolean(description: String? = null, nullable: Boolean = false, title: String? = null): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` representing a boolean value.

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
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a double-precision floating-point number.

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
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for an enumeration.

For example, the cardinal directions can be represented as:

```kotlin
Schema.enumeration(listOf("north", "east", "south", "west"), "Cardinal directions")
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | The list of valid values for this enumeration |
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
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a single-precision floating-point number.

**Important:** This `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.

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
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a 32-bit signed integer number.

**Important:** This `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.

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
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a 64-bit signed integer number.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the number should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### obj

```
fun obj(
    properties: Map<String, Schema>,
    optionalProperties: List<String> = emptyList(),
    description: String? = null,
    nullable: Boolean = false,
    title: String? = null
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema`.

**Example:** A `city` could be represented with the following object `Schema`.

```kotlin
Schema.obj(mapOf(
  "name"  to Schema.string(),
  "population" to Schema.integer()
))
```

| Parameters |
|---|---|
| `properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema>` | The map of the object's property names to their `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema`s. |
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
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema` for a string.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the string should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |
| `format: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/StringFormat? = null` | An optional pattern that values need to adhere to. |

## Public properties

### anyOf

```
val anyOf: List<Schema>?
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
val items: Schema?
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
val properties: Map<String, Schema>?
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