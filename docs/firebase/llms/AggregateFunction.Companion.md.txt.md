# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion.md.txt

# AggregateFunction.Companion

# AggregateFunction.Companion


```
public static class AggregateFunction.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#average(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an aggregation that calculates the average (mean) of values from an expression across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#average(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an aggregation that calculates the average (mean) of a field's values across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an aggregation that counts the number of stage inputs with valid evaluations of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an aggregation that counts the number of stage inputs where the input field exists. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countAll()()` Creates an aggregation that counts the total number of stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countDistinct(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an aggregation that counts the number of distinct values of an expression across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countDistinct(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an aggregation that counts the number of distinct values of a field across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countIf(com.google.firebase.firestore.pipeline.BooleanExpression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition)` Creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#maximum(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an aggregation that finds the maximum value of an expression across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#maximum(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an aggregation that finds the maximum value of a field across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#minimum(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an aggregation that finds the minimum value of an expression across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#minimum(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an aggregation that finds the minimum value of a field across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#rawAggregate(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates a raw aggregation function. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#sum(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an aggregation that calculates the sum of values from an expression across multiple stage inputs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#sum(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an aggregation that calculates the sum of a field's values across multiple stage inputs. |

## Public methods

### average

```
public static final @NonNull AggregateFunction average(@NonNull Expression expression)
```

Creates an aggregation that calculates the average (mean) of values from an expression across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression representing the values to average. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the average aggregation. |

### average

```
public static final @NonNull AggregateFunction average(@NonNull String fieldName)
```

Creates an aggregation that calculates the average (mean) of a field's values across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing numeric values to average. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the average aggregation. |

### count

```
public static final @NonNull AggregateFunction count(@NonNull Expression expression)
```

Creates an aggregation that counts the number of stage inputs with valid evaluations of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to count. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the 'count' aggregation. |

### count

```
public static final @NonNull AggregateFunction count(@NonNull String fieldName)
```

Creates an aggregation that counts the number of stage inputs where the input field exists.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field to count. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the 'count' aggregation. |

### countAll

```
public static final @NonNull AggregateFunction countAll()
```

Creates an aggregation that counts the total number of stage inputs.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the countAll aggregation. |

### countDistinct

```
public static final @NonNull AggregateFunction countDistinct(@NonNull Expression expression)
```

Creates an aggregation that counts the number of distinct values of an expression across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to count the distinct values of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count distinct aggregation. |

### countDistinct

```
public static final @NonNull AggregateFunction countDistinct(@NonNull String fieldName)
```

Creates an aggregation that counts the number of distinct values of a field across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field to count the distinct values of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count distinct aggregation. |

### countIf

```
public static final @NonNull AggregateFunction countIf(@NonNull BooleanExpression condition)
```

Creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition` | The boolean expression to evaluate on each input. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count aggregation. |

### maximum

```
public static final @NonNull AggregateFunction maximum(@NonNull Expression expression)
```

Creates an aggregation that finds the maximum value of an expression across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to find the maximum value of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the maximum aggregation. |

### maximum

```
public static final @NonNull AggregateFunction maximum(@NonNull String fieldName)
```

Creates an aggregation that finds the maximum value of a field across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field to find the maximum value of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the maximum aggregation. |

### minimum

```
public static final @NonNull AggregateFunction minimum(@NonNull Expression expression)
```

Creates an aggregation that finds the minimum value of an expression across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to find the minimum value of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the minimum aggregation. |

### minimum

```
public static final @NonNull AggregateFunction minimum(@NonNull String fieldName)
```

Creates an aggregation that finds the minimum value of a field across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field to find the minimum value of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the minimum aggregation. |

### rawAggregate

```
public static final @NonNull AggregateFunction rawAggregate(@NonNull String name, @NonNull Expression expr)
```

Creates a raw aggregation function.

This method provides a way to call aggregation functions that are supported by the Firestore backend but that are not available as specific factory methods in this class.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the aggregation function. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expressions to pass as arguments to the function. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` for the specified function. |

### sum

```
public static final @NonNull AggregateFunction sum(@NonNull Expression expression)
```

Creates an aggregation that calculates the sum of values from an expression across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to sum up. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the sum aggregation. |

### sum

```
public static final @NonNull AggregateFunction sum(@NonNull String fieldName)
```

Creates an aggregation that calculates the sum of a field's values across multiple stage inputs.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing numeric values to sum up. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` representing the sum aggregation. |