# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.md.txt

# Schema

# Schema


```
public final class Schema
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

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#description()` |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#enum()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#format()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#items()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#nullable()` |
| `final https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#properties()` |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#required()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema#type()` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#array(com.google.firebase.vertexai.type.Schema,kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema items, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for an array. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#boolean(kotlin.String,kotlin.Boolean)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` representing a boolean value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#double(kotlin.String,kotlin.Boolean)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a double-precision floating-point number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for an enumeration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#float(kotlin.String,kotlin.Boolean)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a single-precision floating-point number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#integer(kotlin.String,kotlin.Boolean)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a 32-bit signed integer number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#long(kotlin.String,kotlin.Boolean)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a 64-bit signed integer number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema> properties, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a complex data type. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema.Companion#string(kotlin.String,kotlin.Boolean,com.google.firebase.vertexai.type.StringFormat)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/StringFormat format)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a string. |

## Public fields

### description

```
public final String description
```

### enum

```
public final List<@NonNull String> enum
```

### format

```
public final String format
```

### items

```
public final Schema items
```

### nullable

```
public final Boolean nullable
```

### properties

```
public final Map<@NonNull String, @NonNull Schema> properties
```

### required

```
public final List<@NonNull String> required
```

### type

```
public final @NonNull String type
```

## Public methods

### array

```
public static final @NonNull Schema array(@NonNull Schema items, String description, boolean nullable)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for an array.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema items` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` of the elements stored in the array. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the array represents. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### boolean

```
public static final @NonNull Schema boolean(String description, boolean nullable)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` representing a boolean value.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the boolean should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### double

```
public static final @NonNull Schema double(String description, boolean nullable)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a double-precision floating-point number.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### enumeration

```
public static final @NonNull Schema enumeration(
    @NonNull List<@NonNull String> values,
    String description,
    boolean nullable
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for an enumeration.

For example, the cardinal directions can be represented as:

```
Schema.enumeration(listOf("north", "east", "south", "west"), "Cardinal directions")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values` | The list of valid values for this enumeration |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | The description of what the parameter should contain or represent |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### float

```
public static final @NonNull Schema float(String description, boolean nullable)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a single-precision floating-point number.

**Important:** This `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### integer

```
public static final @NonNull Schema integer(String description, boolean nullable)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a 32-bit signed integer number.

**Important:** This `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the integer should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### long

```
public static final @NonNull Schema long(String description, boolean nullable)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a 64-bit signed integer number.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### obj

```
public static final @NonNull Schema obj(
    @NonNull Map<@NonNull String, @NonNull Schema> properties,
    @NonNull List<@NonNull String> optionalProperties,
    String description,
    boolean nullable
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema`.

**Example:** A `city` could be represented with the following object `Schema`.

```
Schema.obj(mapOf(
  "name"  to Schema.string(),
  "population" to Schema.integer()
))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema> properties` | The map of the object's property names to their `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema`s. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the object represents. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### string

```
public static final @NonNull Schema string(String description, boolean nullable, StringFormat format)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Schema` for a string.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the string should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/StringFormat format` | An optional pattern that values need to adhere to. |