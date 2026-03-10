# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.md.txt

# AggregateFunction

# AggregateFunction


```
class AggregateFunction
```

<br />

*** ** * ** ***

A class that represents an aggregate function.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#average(com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an aggregation that calculates the average (mean) of values from an expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#average(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an aggregation that calculates the average (mean) of a field's values across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an aggregation that counts the number of stage inputs with valid evaluations of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an aggregation that counts the number of stage inputs where the input field exists. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countAll()()` Creates an aggregation that counts the total number of stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countDistinct(com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an aggregation that counts the number of distinct values of an expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countDistinct(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an aggregation that counts the number of distinct values of a field across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#countIf(com.google.firebase.firestore.pipeline.BooleanExpression)(condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression)` Creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#maximum(com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an aggregation that finds the maximum value of an expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#maximum(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an aggregation that finds the maximum value of a field across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#minimum(com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an aggregation that finds the minimum value of an expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#minimum(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an aggregation that finds the minimum value of a field across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#rawAggregate(kotlin.String,kotlin.Array)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates a raw aggregation function. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#sum(com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an aggregation that calculates the sum of values from an expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#sum(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an aggregation that calculates the sum of a field's values across multiple stage inputs. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction#alias(kotlin.String)(alias: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Assigns an alias to this aggregate. |

## Public companion functions

### average

```
fun average(expression: Expression): AggregateFunction
```

Creates an aggregation that calculates the average (mean) of values from an expression across multiple stage inputs.

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the values to average. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the average aggregation. |

### average

```
fun average(fieldName: String): AggregateFunction
```

Creates an aggregation that calculates the average (mean) of a field's values across multiple stage inputs.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing numeric values to average. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the average aggregation. |

### count

```
fun count(expression: Expression): AggregateFunction
```

Creates an aggregation that counts the number of stage inputs with valid evaluations of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction.Companion#count(com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to count. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the 'count' aggregation. |

### count

```
fun count(fieldName: String): AggregateFunction
```

Creates an aggregation that counts the number of stage inputs where the input field exists.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to count. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the 'count' aggregation. |

### countAll

```
fun countAll(): AggregateFunction
```

Creates an aggregation that counts the total number of stage inputs.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the countAll aggregation. |

### countDistinct

```
fun countDistinct(expression: Expression): AggregateFunction
```

Creates an aggregation that counts the number of distinct values of an expression across multiple stage inputs.

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to count the distinct values of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count distinct aggregation. |

### countDistinct

```
fun countDistinct(fieldName: String): AggregateFunction
```

Creates an aggregation that counts the number of distinct values of a field across multiple stage inputs.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to count the distinct values of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count distinct aggregation. |

### countIf

```
fun countIf(condition: BooleanExpression): AggregateFunction
```

Creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true.

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The boolean expression to evaluate on each input. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count aggregation. |

### maximum

```
fun maximum(expression: Expression): AggregateFunction
```

Creates an aggregation that finds the maximum value of an expression across multiple stage inputs.

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to find the maximum value of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the maximum aggregation. |

### maximum

```
fun maximum(fieldName: String): AggregateFunction
```

Creates an aggregation that finds the maximum value of a field across multiple stage inputs.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to find the maximum value of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the maximum aggregation. |

### minimum

```
fun minimum(expression: Expression): AggregateFunction
```

Creates an aggregation that finds the minimum value of an expression across multiple stage inputs.

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to find the minimum value of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the minimum aggregation. |

### minimum

```
fun minimum(fieldName: String): AggregateFunction
```

Creates an aggregation that finds the minimum value of a field across multiple stage inputs.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to find the minimum value of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the minimum aggregation. |

### rawAggregate

```
fun rawAggregate(name: String, vararg expr: Expression): AggregateFunction
```

Creates a raw aggregation function.

This method provides a way to call aggregation functions that are supported by the Firestore backend but that are not available as specific factory methods in this class.

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the aggregation function. |
| `vararg expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expressions to pass as arguments to the function. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` for the specified function. |

### sum

```
fun sum(expression: Expression): AggregateFunction
```

Creates an aggregation that calculates the sum of values from an expression across multiple stage inputs.

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to sum up. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the sum aggregation. |

### sum

```
fun sum(fieldName: String): AggregateFunction
```

Creates an aggregation that calculates the sum of a field's values across multiple stage inputs.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing numeric values to sum up. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the sum aggregation. |

## Public functions

### alias

```
fun alias(alias: String): AliasedAggregate
```

Assigns an alias to this aggregate.

| Parameters |
|---|---|
| `alias: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The alias to assign to this aggregate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` that wraps this aggregate and associates it with the provided alias. |