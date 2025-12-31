# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion.md.txt

# Schema.Companion

# Schema.Companion


```
public static class Schema.Companion
```

<br />

*** ** * ** ***

## Summary

|                                                                                              ### Public methods                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [anyOf](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#anyOf(kotlin.collections.List))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema)`> schemas)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) representing a value that must conform to *any* (one of) the provided sub-schema.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [array](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#array(com.google.firebase.ai.type.Schema,kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Int,kotlin.Int))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema)` items,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title,` ` `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)` minItems,` ` `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)` maxItems` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for an array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [boolean](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#boolean(kotlin.String,kotlin.Boolean,kotlin.String))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description, boolean nullable, `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) representing a boolean value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [enumeration](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`> values,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for an enumeration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [numDouble](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numDouble(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` minimum,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` maximum` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a double-precision floating-point number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [numFloat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numFloat(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` minimum,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` maximum` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a single-precision floating-point number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [numInt](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numInt(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` minimum,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` maximum` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a 32-bit signed integer number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [numLong](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numLong(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double))`(` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` minimum,` ` `[Double](https://developer.android.com/reference/kotlin/java/lang/Double.html)` maximum` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a 64-bit signed integer number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [obj](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Map](https://developer.android.com/reference/kotlin/java/util/Map.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema)`> properties,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`> optionalProperties,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a complex data type. |
| `static final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) | [str](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#str(kotlin.String,kotlin.Boolean,com.google.firebase.ai.type.StringFormat,kotlin.String))`(` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` boolean nullable,` ` `[StringFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/StringFormat)` format,` ` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` title` `)` Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Public methods

### anyOf

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ anyOf(@NonNull List<@NonNull Schema>Â schemas)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) representing a value that must conform to *any* (one of) the provided sub-schema.

Example: A field that can hold either a simple userID or a more detailed user object.  

```text
Schema.anyOf( listOf( Schema.integer(description = "User ID"), Schema.obj( mapOf(
    "userID" to Schema.integer(description = "User ID"),
    "username" to Schema.string(description = "Username")
)))
```  

|                                                                                                                                                                                      Parameters                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema)`> schemas` | The list of valid schemas which could be here |

### array

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ array(
Â Â Â Â @NonNull SchemaÂ items,
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringÂ title,
Â Â Â Â IntegerÂ minItems,
Â Â Â Â IntegerÂ maxItems
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for an array.  

|                                                                                               Parameters                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema)` items` | The [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) of the elements stored in the array. |
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description`                                                                                                            | An optional description of what the array represents.                                                                                    |
| `boolean nullable`                                                                                                                                                                                      | Indicates whether the value can be `null`. Defaults to `false`.                                                                          |

### boolean

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ boolean(StringÂ description,Â booleanÂ nullable,Â StringÂ title)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) representing a boolean value.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description` | An optional description of what the boolean should contain or represent. |
| `boolean nullable`                                                                           | Indicates whether the value can be `null`. Defaults to `false`.          |

### enumeration

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ enumeration(
Â Â Â Â @NonNull List<@NonNull String>Â values,
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringÂ title
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for an enumeration.

For example, the cardinal directions can be represented as:  

```gdscript
Schema.enumeration(listOf("north", "east", "south", "west"), "Cardinal directions")
```  

|                                                                                                                                                                             Parameters                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`> values` | The list of valid values for this enumeration                     |
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description`                                                                                                                                                                                                                                                                        | The description of what the parameter should contain or represent |
| `boolean nullable`                                                                                                                                                                                                                                                                                                                                                  | Indicates whether the value can be `null`. Defaults to `false`.   |

### numDouble

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ numDouble(
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringÂ title,
Â Â Â Â DoubleÂ minimum,
Â Â Â Â DoubleÂ maximum
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a double-precision floating-point number.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description` | An optional description of what the number should contain or represent. |
| `boolean nullable`                                                                           | Indicates whether the value can be `null`. Defaults to `false`.         |

### numFloat

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ numFloat(
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringÂ title,
Â Â Â Â DoubleÂ minimum,
Â Â Â Â DoubleÂ maximum
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a single-precision floating-point number.

**Important:** This [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description` | An optional description of what the number should contain or represent. |
| `boolean nullable`                                                                           | Indicates whether the value can be `null`. Defaults to `false`.         |

### numInt

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ numInt(
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringÂ title,
Â Â Â Â DoubleÂ minimum,
Â Â Â Â DoubleÂ maximum
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a 32-bit signed integer number.

**Important:** This [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description` | An optional description of what the integer should contain or represent. |
| `boolean nullable`                                                                           | Indicates whether the value can be `null`. Defaults to `false`.          |

### numLong

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ numLong(
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringÂ title,
Â Â Â Â DoubleÂ minimum,
Â Â Â Â DoubleÂ maximum
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a 64-bit signed integer number.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description` | An optional description of what the number should contain or represent. |
| `boolean nullable`                                                                           | Indicates whether the value can be `null`. Defaults to `false`.         |

### obj

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ obj(
Â Â Â Â @NonNull Map<@NonNull String,Â @NonNull Schema>Â properties,
Â Â Â Â @NonNull List<@NonNull String>Â optionalProperties,
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringÂ title
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema).

**Example:** A `city` could be represented with the following object `Schema`.  

```text
Schema.obj(mapOf(
  "name"  to Schema.string(),
  "population" to Schema.integer()
))
```  

|                                                                                                                                                                                                                                                                               Parameters                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Map](https://developer.android.com/reference/kotlin/java/util/Map.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema)`> properties` | The map of the object's property names to their [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema)s.                                      |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`> optionalProperties`                                                                                                                                                                                        | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | An optional description of what the object represents.                                                                                                                                 |
| `boolean nullable`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Indicates whether the value can be `null`. Defaults to `false`.                                                                                                                        |

### str

```
publicÂ staticÂ finalÂ @NonNull SchemaÂ str(
Â Â Â Â StringÂ description,
Â Â Â Â booleanÂ nullable,
Â Â Â Â StringFormatÂ format,
Â Â Â Â StringÂ title
)
```

Returns a [Schema](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema) for a string.  

|                                                      Parameters                                                      |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description`                         | An optional description of what the string should contain or represent. |
| `boolean nullable`                                                                                                   | Indicates whether the value can be `null`. Defaults to `false`.         |
| [StringFormat](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/StringFormat)` format` | An optional pattern that values need to adhere to.                      |