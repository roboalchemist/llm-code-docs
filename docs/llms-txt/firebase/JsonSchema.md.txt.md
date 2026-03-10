# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.md.txt

# JsonSchema

# JsonSchema


```
public final class JsonSchema<T extends Object>
```

<br />

*** ** * ** ***

Definition of a data type.

These types can be objects, but also primitives and arrays. Represents a select subset of an [JsonSchema object](https://json-schema.org/specification).

**Note:** While optional, including a `description` field in your `JsonSchema` is strongly encouraged. The more information the model has about what it's expected to generate, the better the results.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion` |

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#anyOf()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#clazz()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#description()` |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#enum()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#format()` |
| `final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#items()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#maxItems()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Double.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#maximum()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Integer.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#minItems()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Double.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#minimum()` |
| `final https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#nullable()` |
| `final https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#properties()` |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#required()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#title()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#type()` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#anyOf(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> schemas)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` representing a value that must conform to *any* (one of) the provided sub-schema. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#array(com.google.firebase.ai.type.JsonSchema,kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Int,kotlin.Int)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> items, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Integer.html minItems, https://developer.android.com/reference/kotlin/java/lang/Integer.html maxItems )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for an array. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#boolean(kotlin.String,kotlin.Boolean,kotlin.String)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` representing a boolean value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Double.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#double(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a double-precision floating-point number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for an enumeration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#enumeration(kotlin.collections.List,kotlin.reflect.KClass,kotlin.String,kotlin.Boolean,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> clazz, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for an enumeration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Float.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#float(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a single-precision floating-point number. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema#getSerializer()()` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Integer.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#integer(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a 32-bit signed integer number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Long.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#long(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a 64-bit signed integer number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> properties, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a complex data type. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T>` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#obj(kotlin.collections.Map,kotlin.reflect.KClass,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> properties, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> clazz, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a complex data type. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema.Companion#string(kotlin.String,kotlin.Boolean,com.google.firebase.ai.type.StringFormat,kotlin.String)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/StringFormat format, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a string. |

## Public fields

### anyOf

```
public final List<@NonNull JsonSchema<@NonNull ?>> anyOf
```

### clazz

```
public final @NonNull KClass<@NonNull T> clazz
```

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
public final JsonSchema<@NonNull ?> items
```

### maxItems

```
public final Integer maxItems
```

### maximum

```
public final Double maximum
```

### minItems

```
public final Integer minItems
```

### minimum

```
public final Double minimum
```

### nullable

```
public final Boolean nullable
```

### properties

```
public final Map<@NonNull String, @NonNull JsonSchema<@NonNull ?>> properties
```

### required

```
public final List<@NonNull String> required
```

### title

```
public final String title
```

### type

```
public final @NonNull String type
```

## Public methods

### anyOf

```
public static final @NonNull JsonSchema<@NonNull String> anyOf(@NonNull List<@NonNull JsonSchema<@NonNull ?>> schemas)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` representing a value that must conform to *any* (one of) the provided sub-schema.

Example: A field that can hold either a simple userID or a more detailed user object.

```
JsonSchema.anyOf( listOf( JsonSchema.integer(description = "User ID"), JsonSchema.obj( mapOf(
    "userID" to JsonSchema.integer(description = "User ID"),
    "username" to JsonSchema.string(description = "Username")
)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> schemas` | The list of valid schemas which could be here |

### array

```
public static final @NonNull JsonSchema<@NonNull List<@NonNull T>> <T extends Object> array(
    @NonNull JsonSchema<@NonNull T> items,
    String description,
    boolean nullable,
    String title,
    Integer minItems,
    Integer maxItems
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for an array.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> items` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` of the elements stored in the array. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the array represents. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### boolean

```
public static final @NonNull JsonSchema<@NonNull Boolean> boolean(String description, boolean nullable, String title)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` representing a boolean value.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the boolean should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### double

```
public static final @NonNull JsonSchema<@NonNull Double> double(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a double-precision floating-point number.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### enumeration

```
public static final @NonNull JsonSchema<@NonNull String> enumeration(
    @NonNull List<@NonNull String> values,
    String description,
    boolean nullable,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for an enumeration.

For example, the cardinal directions can be represented as:

```
JsonSchema.enumeration(listOf("north", "east", "south", "west"), "Cardinal directions")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values` | The list of valid values for this enumeration |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | The description of what the parameter should contain or represent |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### enumeration

```
public static final @NonNull JsonSchema<@NonNull T> <T extends Object> enumeration(
    @NonNull List<@NonNull String> values,
    @NonNull KClass<@NonNull T> clazz,
    String description,
    boolean nullable,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for an enumeration.

For example, the cardinal directions can be represented as:

```
JsonSchema.enumeration(
  listOf("north", "east", "south", "west"),
  Direction::class,
  "Cardinal directions"
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values` | The list of valid values for this enumeration |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> clazz` | the real class that this schema represents |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | The description of what the parameter should contain or represent |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### float

```
public static final @NonNull JsonSchema<@NonNull Float> float(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a single-precision floating-point number.

**Important:** This `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### getSerializer

```
public final @NonNull KSerializer<@NonNull T> getSerializer()
```

### integer

```
public static final @NonNull JsonSchema<@NonNull Integer> integer(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a 32-bit signed integer number.

**Important:** This `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the integer should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### long

```
public static final @NonNull JsonSchema<@NonNull Long> long(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a 64-bit signed integer number.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### obj

```
public static final @NonNull JsonSchema<@NonNull JsonObject> obj(
    @NonNull Map<@NonNull String, @NonNull JsonSchema<@NonNull ?>> properties,
    @NonNull List<@NonNull String> optionalProperties,
    String description,
    boolean nullable,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema`.

**Example:** A `city` could be represented with the following object `JsonSchema`.

```
JsonSchema.obj(mapOf(
  "name"  to JsonSchema.string(),
  "population" to JsonSchema.integer()
))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> properties` | The map of the object's property names to their `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema`s. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the object represents. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### obj

```
public static final @NonNull JsonSchema<@NonNull T> <T extends Object> obj(
    @NonNull Map<@NonNull String, @NonNull JsonSchema<@NonNull ?>> properties,
    @NonNull KClass<@NonNull T> clazz,
    @NonNull List<@NonNull String> optionalProperties,
    String description,
    boolean nullable,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema`.

**Example:** A `city` could be represented with the following object `JsonSchema`.

```
JsonSchema.obj(mapOf(
    "name"  to JsonSchema.string(),
    "population" to JsonSchema.integer()
  ),
  City::class
)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html ?>> properties` | The map of the object's property names to their `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema`s. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.reflect/-k-class/index.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html T> clazz` | the real class that this schema represents |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the object represents. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### string

```
public static final @NonNull JsonSchema<@NonNull String> string(
    String description,
    boolean nullable,
    StringFormat format,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/JsonSchema` for a string.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the string should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/StringFormat format` | An optional pattern that values need to adhere to. |