# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.md.txt

# Schema

# Schema


```
class Schema
```

<br />

*** ** * ** ***

> [!CAUTION]
> **This class is deprecated.**   
> The Vertex AI in Firebase SDK (firebase-vertexai) has been replaced with the FirebaseAI SDK (firebase-ai) to accommodate the evolving set of supported features and services. For migration details, see the migration guide: https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk

Definition of a data type.

These types can be objects, but also primitives and arrays. Represents a select subset of an [OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema).

**Note:** While optional, including a `description` field in your `Schema` is strongly encouraged. The more information the model has about what it's expected to generate, the better the results.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#array(com.google.firebase.vertexai.type.Schema,kotlin.String,kotlin.Boolean)(items: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for an array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#boolean(kotlin.String,kotlin.Boolean)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` representing a boolean value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#double(kotlin.String,kotlin.Boolean)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a double-precision floating-point number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean)(values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for an enumeration. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#float(kotlin.String,kotlin.Boolean)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a single-precision floating-point number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#integer(kotlin.String,kotlin.Boolean)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a 32-bit signed integer number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#long(kotlin.String,kotlin.Boolean)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a 64-bit signed integer number. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean)( properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema>, optionalProperties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a complex data type. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.Companion#string(kotlin.String,kotlin.Boolean,com.google.firebase.vertexai.type.StringFormat)(description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?, nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html, format: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/StringFormat?)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a string. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#description()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#enum()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#format()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#items()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#nullable()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#properties()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#required()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema#type()` |

## Public companion functions

### array

```
fun array(items: Schema, description: String? = null, nullable: Boolean = false): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for an array.

| Parameters |
|---|---|
| `items: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` of the elements stored in the array. |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the array represents. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### boolean

```
fun boolean(description: String? = null, nullable: Boolean = false): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` representing a boolean value.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the boolean should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### double

```
fun double(description: String? = null, nullable: Boolean = false): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a double-precision floating-point number.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the number should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### enumeration

```
fun enumeration(
    values: List<String>,
    description: String? = null,
    nullable: Boolean = false
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for an enumeration.

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
fun float(description: String? = null, nullable: Boolean = false): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a single-precision floating-point number.

**Important:** This `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the number should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### integer

```
fun integer(description: String? = null, nullable: Boolean = false): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a 32-bit signed integer number.

**Important:** This `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the integer should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### long

```
fun long(description: String? = null, nullable: Boolean = false): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a 64-bit signed integer number.

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
    nullable: Boolean = false
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema`.

**Example:** A `city` could be represented with the following object `Schema`.

```kotlin
Schema.obj(mapOf(
  "name"  to Schema.string(),
  "population" to Schema.integer()
))
```

| Parameters |
|---|---|
| `properties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema>` | The map of the object's property names to their `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema`s. |
| `optionalProperties: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html> = emptyList()` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the object represents. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |

### string

```
fun string(
    description: String? = null,
    nullable: Boolean = false,
    format: StringFormat? = null
): Schema
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema` for a string.

| Parameters |
|---|---|
| `description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html? = null` | An optional description of what the string should contain or represent. |
| `nullable: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html = false` | Indicates whether the value can be `null`. Defaults to `false`. |
| `format: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/StringFormat? = null` | An optional pattern that values need to adhere to. |

## Public properties

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

### type

```
val type: String
```