# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/Schema.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/Schema.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/Schema.md.txt

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

|                                 ### Public companion functions                                 |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [anyOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#anyOf(kotlin.collections.List))`(schemas: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) representing a value that must conform to *any* (one of) the provided sub-schema.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [array](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#array(com.google.firebase.ai.type.Schema,kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Int,kotlin.Int))`(` ` items: `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`,` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` minItems: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?,` ` maxItems: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for an array.                                                                                                                                                                                                |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [boolean](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#boolean(kotlin.String,kotlin.Boolean,kotlin.String))`(description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`, title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) representing a boolean value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [double](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#double(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` minimum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?,` ` maximum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a double-precision floating-point number.                                                                                                                                                                                                                                                                                             |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [enumeration](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String))`(` ` values: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>,` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for an enumeration.                                                                                                                                                                                                                                                                                                                        |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [float](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#float(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` minimum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?,` ` maximum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a single-precision floating-point number.                                                                                                                                                                                                                                                                                               |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [integer](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#integer(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` minimum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?,` ` maximum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a 32-bit signed integer number.                                                                                                                                                                                                                                                                                                     |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [long](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#long(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` minimum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?,` ` maximum: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a 64-bit signed integer number.                                                                                                                                                                                                                                                                                                           |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [obj](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String))`(` ` properties: `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>,` ` optionalProperties: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>,` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a complex data type. |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) | [string](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema.Companion#string(kotlin.String,kotlin.Boolean,com.google.firebase.ai.type.StringFormat,kotlin.String))`(` ` description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`,` ` format: `[StringFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/StringFormat)`?,` ` title: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` `)` Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a string.                                                                                                                                                                                                                                                                                                                                                                                        |

|                                                                                                                              ### Public properties                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>?`                                                                                   | [anyOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#anyOf())             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                             | [description](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#description()) |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>?`                                                                                                 | [enum](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#enum())               |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                             | [format](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#format())           |
| [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`?`                                                                                                                                                                               | [items](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#items())             |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                                                                                   | [maxItems](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#maxItems())       |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?`                                                                                                                                                                                             | [maximum](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#maximum())         |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`?`                                                                                                                                                                                                   | [minItems](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#minItems())       |
| [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`?`                                                                                                                                                                                             | [minimum](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#minimum())         |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`?`                                                                                                                                                                                           | [nullable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#nullable())       |
| [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>?` | [properties](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#properties())   |
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>?`                                                                                                 | [required](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#required())       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                             | [title](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#title())             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                                                                                                                                | [type](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema#type())               |

## Public companion functions

### anyOf

```
funÂ anyOf(schemas:Â List<Schema>):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) representing a value that must conform to *any* (one of) the provided sub-schema.

Example: A field that can hold either a simple userID or a more detailed user object.  

```kotlin
Schema.anyOf( listOf( Schema.integer(description = "User ID"), Schema.obj( mapOf(
    "userID" to Schema.integer(description = "User ID"),
    "username" to Schema.string(description = "Username")
)))
```  

|                                                                                               Parameters                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `schemas: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>` | The list of valid schemas which could be here |

### array

```
funÂ array(
Â Â Â Â items:Â Schema,
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â title:Â String? = null,
Â Â Â Â minItems:Â Int? = null,
Â Â Â Â maxItems:Â Int? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for an array.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `items: `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)   | The [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) of the elements stored in the array. |
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null` | An optional description of what the array represents.                                                                                   |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`  | Indicates whether the value can be `null`. Defaults to `false`.                                                                         |

### boolean

```
funÂ boolean(description:Â String? = null,Â nullable:Â Boolean = false,Â title:Â String? = null):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) representing a boolean value.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null` | An optional description of what the boolean should contain or represent. |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`  | Indicates whether the value can be `null`. Defaults to `false`.          |

### double

```
funÂ double(
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â title:Â String? = null,
Â Â Â Â minimum:Â Double? = null,
Â Â Â Â maximum:Â Double? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a double-precision floating-point number.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null` | An optional description of what the number should contain or represent. |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`  | Indicates whether the value can be `null`. Defaults to `false`.         |

### enumeration

```
funÂ enumeration(
Â Â Â Â values:Â List<String>,
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â title:Â String? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for an enumeration.

For example, the cardinal directions can be represented as:  

```kotlin
Schema.enumeration(listOf("north", "east", "south", "west"), "Cardinal directions")
```  

|                                                                                        Parameters                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| `values: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`>` | The list of valid values for this enumeration                     |
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null`                                                                                | The description of what the parameter should contain or represent |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`                                                                                 | Indicates whether the value can be `null`. Defaults to `false`.   |

### float

```
funÂ float(
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â title:Â String? = null,
Â Â Â Â minimum:Â Double? = null,
Â Â Â Â maximum:Â Double? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a single-precision floating-point number.

**Important:** This [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null` | An optional description of what the number should contain or represent. |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`  | Indicates whether the value can be `null`. Defaults to `false`.         |

### integer

```
funÂ integer(
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â title:Â String? = null,
Â Â Â Â minimum:Â Double? = null,
Â Â Â Â maximum:Â Double? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a 32-bit signed integer number.

**Important:** This [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null` | An optional description of what the integer should contain or represent. |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`  | Indicates whether the value can be `null`. Defaults to `false`.          |

### long

```
funÂ long(
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â title:Â String? = null,
Â Â Â Â minimum:Â Double? = null,
Â Â Â Â maximum:Â Double? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a 64-bit signed integer number.  

|                                                Parameters                                                 |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null` | An optional description of what the number should contain or represent. |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`  | Indicates whether the value can be `null`. Defaults to `false`.         |

### obj

```
funÂ obj(
Â Â Â Â properties:Â Map<String,Â Schema>,
Â Â Â Â optionalProperties:Â List<String> = emptyList(),
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â title:Â String? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema).

**Example:** A `city` could be represented with the following object `Schema`.  

```kotlin
Schema.obj(mapOf(
  "name"  to Schema.string(),
  "population" to Schema.integer()
))
```  

|                                                                                                                                          Parameters                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `properties: `[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, `[Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)`>` | The map of the object's property names to their [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema)s.                                       |
| `optionalProperties: `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`> = emptyList()`                                                                           | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null`                                                                                                                                                                                    | An optional description of what the object represents.                                                                                                                                 |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`                                                                                                                                                                                     | Indicates whether the value can be `null`. Defaults to `false`.                                                                                                                        |

### string

```
funÂ string(
Â Â Â Â description:Â String? = null,
Â Â Â Â nullable:Â Boolean = false,
Â Â Â Â format:Â StringFormat? = null,
Â Â Â Â title:Â String? = null
):Â Schema
```

Returns a [Schema](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Schema) for a string.  

|                                                           Parameters                                                           |
|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `description: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`? = null`                      | An optional description of what the string should contain or represent. |
| `nullable: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` = false`                       | Indicates whether the value can be `null`. Defaults to `false`.         |
| `format: `[StringFormat](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/StringFormat)`? = null` | An optional pattern that values need to adhere to.                      |

## Public properties

### anyOf

```
valÂ anyOf:Â List<Schema>?
```  

### description

```
valÂ description:Â String?
```  

### enum

```
valÂ enum:Â List<String>?
```  

### format

```
valÂ format:Â String?
```  

### items

```
valÂ items:Â Schema?
```  

### maxItems

```
valÂ maxItems:Â Int?
```  

### maximum

```
valÂ maximum:Â Double?
```  

### minItems

```
valÂ minItems:Â Int?
```  

### minimum

```
valÂ minimum:Â Double?
```  

### nullable

```
valÂ nullable:Â Boolean?
```  

### properties

```
valÂ properties:Â Map<String,Â Schema>?
```  

### required

```
valÂ required:Â List<String>?
```  

### title

```
valÂ title:Â String?
```  

### type

```
valÂ type:Â String
```