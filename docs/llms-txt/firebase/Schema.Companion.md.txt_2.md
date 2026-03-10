# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion.md.txt

# Schema.Companion

# Schema.Companion


```
public static class Schema.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#anyOf(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema> schemas)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` representing a value that must conform to *any* (one of) the provided sub-schema. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#array(com.google.firebase.ai.type.Schema,kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Int,kotlin.Int)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema items, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Integer.html minItems, https://developer.android.com/reference/kotlin/java/lang/Integer.html maxItems )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for an array. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#boolean(kotlin.String,kotlin.Boolean,kotlin.String)(https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title)` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` representing a boolean value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#enumeration(kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for an enumeration. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numDouble(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a double-precision floating-point number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numFloat(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a single-precision floating-point number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numInt(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a 32-bit signed integer number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#numLong(kotlin.String,kotlin.Boolean,kotlin.String,kotlin.Double,kotlin.Double)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title, https://developer.android.com/reference/kotlin/java/lang/Double.html minimum, https://developer.android.com/reference/kotlin/java/lang/Double.html maximum )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a 64-bit signed integer number. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#obj(kotlin.collections.Map,kotlin.collections.List,kotlin.String,kotlin.Boolean,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema> properties, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties, https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a complex data type. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema.Companion#str(kotlin.String,kotlin.Boolean,com.google.firebase.ai.type.StringFormat,kotlin.String)( https://developer.android.com/reference/kotlin/java/lang/String.html description, boolean nullable, https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/StringFormat format, https://developer.android.com/reference/kotlin/java/lang/String.html title )` Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a string. |

## Public methods

### anyOf

```
public static final @NonNull Schema anyOf(@NonNull List<@NonNull Schema> schemas)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` representing a value that must conform to *any* (one of) the provided sub-schema.

Example: A field that can hold either a simple userID or a more detailed user object.

```
Schema.anyOf( listOf( Schema.integer(description = "User ID"), Schema.obj( mapOf(
    "userID" to Schema.integer(description = "User ID"),
    "username" to Schema.string(description = "Username")
)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema> schemas` | The list of valid schemas which could be here |

### array

```
public static final @NonNull Schema array(
    @NonNull Schema items,
    String description,
    boolean nullable,
    String title,
    Integer minItems,
    Integer maxItems
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for an array.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema items` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` of the elements stored in the array. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the array represents. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### boolean

```
public static final @NonNull Schema boolean(String description, boolean nullable, String title)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` representing a boolean value.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the boolean should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### enumeration

```
public static final @NonNull Schema enumeration(
    @NonNull List<@NonNull String> values,
    String description,
    boolean nullable,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for an enumeration.

For example, the cardinal directions can be represented as:

```
Schema.enumeration(listOf("north", "east", "south", "west"), "Cardinal directions")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> values` | The list of valid values for this enumeration |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | The description of what the parameter should contain or represent |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### numDouble

```
public static final @NonNull Schema numDouble(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a double-precision floating-point number.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### numFloat

```
public static final @NonNull Schema numFloat(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a single-precision floating-point number.

**Important:** This `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` provides a hint to the model that it should generate a single-precision floating-point number, but only guarantees that the value will be a number. Therefore it's *possible* that decoding it as a `Float` variable (or `float` in Java) could overflow.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the number should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### numInt

```
public static final @NonNull Schema numInt(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a 32-bit signed integer number.

**Important:** This `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` provides a hint to the model that it should generate a 32-bit integer, but only guarantees that the value will be an integer. Therefore it's *possible* that decoding it as an `Int` variable (or `int` in Java) could overflow.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the integer should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### numLong

```
public static final @NonNull Schema numLong(
    String description,
    boolean nullable,
    String title,
    Double minimum,
    Double maximum
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a 64-bit signed integer number.

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
    boolean nullable,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a complex data type.

This schema instructs the model to produce data of type object, which has keys of type `String` and values of type `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema`.

**Example:** A `city` could be represented with the following object `Schema`.

```
Schema.obj(mapOf(
  "name"  to Schema.string(),
  "population" to Schema.integer()
))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema> properties` | The map of the object's property names to their `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema`s. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html> optionalProperties` | The list of optional properties. They must correspond to the keys provided in the `properties` map. By default it's empty, signaling the model that all properties are to be included. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the object represents. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |

### str

```
public static final @NonNull Schema str(
    String description,
    boolean nullable,
    StringFormat format,
    String title
)
```

Returns a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Schema` for a string.

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html description` | An optional description of what the string should contain or represent. |
| `boolean nullable` | Indicates whether the value can be `null`. Defaults to `false`. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/StringFormat format` | An optional pattern that values need to adhere to. |