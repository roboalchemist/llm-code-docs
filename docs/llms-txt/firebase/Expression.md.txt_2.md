# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.md.txt

# Expression

# Expression


```
@Beta
abstract class Expression
```

<br />

Known direct subclasses [BooleanExpression](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression), [FunctionExpression](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FunctionExpression), [Selectable](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A class that represents a filter condition. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FunctionExpression` | This class defines the base class for Firestore `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` functions, which can be evaluated within pipeline execution. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | Expressions that have an alias are `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` |

Known indirect subclasses [AliasedExpression](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression), [Field](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression` | Represents an expression that will be given the alias in the output document. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | Represents a reference to a field in a Firestore document. |

*** ** * ** ***

Represents an expression that can be evaluated to a value within the execution of a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline`.

Expressions are the building blocks for creating complex queries and transformations in Firestore pipelines. They can represent:

- **Field references:** Access values from document fields.

- **Literals:** Represent constant values (strings, numbers, booleans).

- **Function calls:** Apply functions to one or more expressions.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` class provides a fluent API for building expressions. You can chain together method calls to create complex expressions.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#abs(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#abs(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#abs(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#abs(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#add(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that adds numeric expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#add(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that adds numeric expressions with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#add(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that adds a numeric field with a numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#add(kotlin.String,kotlin.Number)(numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that adds a numeric field with constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#and(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Array)(condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression, vararg conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression)` Creates an expression that performs a logical 'AND' operation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#array(kotlin.collections.List)(elements: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>)` Creates an expression that creates a Firestore array value from an input array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#array(kotlin.Array)(vararg elements: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Creates an expression that creates a Firestore array value from an input array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(com.google.firebase.firestore.pipeline.Expression,kotlin.Any,kotlin.Array)( firstArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, secondArray: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html )` Creates an expression that concatenates an array with other arrays. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( firstArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, secondArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html )` Creates an expression that concatenates an array with other arrays. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(kotlin.String,kotlin.Any,kotlin.Array)( firstArrayField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, secondArray: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html )` Creates an expression that concatenates a field's array value with other arrays. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( firstArrayField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, secondArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html )` Creates an expression that concatenates a field's array value with other arrays. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, element: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, element: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if the array contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,kotlin.Any)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, element: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, element: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains all elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains all the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if array field contains all elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,kotlin.collections.List)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if array field contains all the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains any elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains any of the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if array field contains any elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,kotlin.collections.List)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if array field contains any of the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, offset: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, offset: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(kotlin.String,kotlin.Int)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(com.google.firebase.firestore.pipeline.Expression)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the length of an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(com.google.firebase.firestore.pipeline.Expression)` expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(kotlin.String)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that calculates the length of an array field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(com.google.firebase.firestore.pipeline.Expression)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Reverses the order of elements in the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(kotlin.String)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Reverses the order of elements in the array field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arraySum(com.google.firebase.firestore.pipeline.Expression)(array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the sum of the elements in an array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arraySum(kotlin.String)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the sum of the elements in an array field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(com.google.firebase.firestore.pipeline.Expression,kotlin.ByteArray)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise AND operation between an expression and a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise AND operation between two expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(kotlin.String,kotlin.ByteArray)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise AND operation between an field and constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise AND operation between an field and an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that applies a bitwise left shift operation between an expression and a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise left shift operation between two expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(kotlin.String,kotlin.Int)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that applies a bitwise left shift operation between a field and a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise left shift operation between a field and an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitNot(com.google.firebase.firestore.pipeline.Expression)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise NOT operation to an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitNot(kotlin.String)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that applies a bitwise NOT operation to a field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(com.google.firebase.firestore.pipeline.Expression,kotlin.ByteArray)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise OR operation between an expression and a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise OR operation between two expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(kotlin.String,kotlin.ByteArray)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise OR operation between an field and constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise OR operation between an field and an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that applies a bitwise right shift operation between an expression and a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise right shift operation between two expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(kotlin.String,kotlin.Int)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that applies a bitwise right shift operation between a field and a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise right shift operation between a field and an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(com.google.firebase.firestore.pipeline.Expression,kotlin.ByteArray)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise XOR operation between an expression and a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise XOR operation between two expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(kotlin.String,kotlin.ByteArray)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise XOR operation between an field and constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise XOR operation between an field and an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#byteLength(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that calculates the length of a string represented by a field in UTF-8 bytes, or just the length of a Blob. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#byteLength(com.google.firebase.firestore.pipeline.Expression)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the length of a string in UTF-8 bytes, or just the length of a Blob. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#charLength(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the character length of a string expression in UTF8. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#charLength(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that calculates the character length of a string field in UTF8. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#collectionId(com.google.firebase.firestore.pipeline.Expression)(path: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the collection ID from a path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#collectionId(kotlin.String)(pathField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the collection ID from a path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#concat(com.google.firebase.firestore.pipeline.Expression,kotlin.Any,kotlin.Array)(first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates strings, arrays, or blobs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#concat(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates strings, arrays, or blobs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#concat(kotlin.String,kotlin.Any,kotlin.Array)(first: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates strings, arrays, or blobs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#concat(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(first: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates strings, arrays, or blobs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression, thenExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression )` Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if a condition is true or an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if the condition is false. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)(condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression, thenValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if a condition is true or an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if the condition is false. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.DocumentReference)(ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)` Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.Blob)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)` Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.Boolean)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.ByteArray)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Create a constant for a bytes value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(java.util.Date)(value: https://developer.android.com/reference/kotlin/java/util/Date.html)` Create a constant for a `https://developer.android.com/reference/kotlin/java/util/Date.html` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.GeoPoint)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint)` Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.Number)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.String)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.Timestamp)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)` Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.VectorValue)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(com.google.firebase.firestore.pipeline.Expression,kotlin.DoubleArray)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the Cosine distance between vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the Cosine distance between two vector expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.VectorValue)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the Cosine distance between vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(kotlin.String,kotlin.DoubleArray)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the Cosine distance between a vector field and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the Cosine distance between a vector field and a vector expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(kotlin.String,com.google.firebase.firestore.VectorValue)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the Cosine distance between a vector field and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#currentTimestamp()()` Creates an expression that evaluates to the current server timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#divide(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that divides two numeric expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#divide(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that divides a numeric expression by a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#divide(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that divides numeric field by a numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#divide(kotlin.String,kotlin.Number)(dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that divides a numeric field by a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#documentId(com.google.firebase.firestore.DocumentReference)(docRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)` Creates an expression that returns the document ID from a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#documentId(com.google.firebase.firestore.pipeline.Expression)(documentPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the document ID from a path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#documentId(kotlin.String)(documentPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the document ID from a path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(com.google.firebase.firestore.pipeline.Expression,kotlin.DoubleArray)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the dot product distance between vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the dot product distance between two vector expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.VectorValue)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the dot product distance between vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(kotlin.String,kotlin.DoubleArray)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the dot product distance between vector field and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the dot product distance between a vector field and a vector expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(kotlin.String,com.google.firebase.firestore.VectorValue)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the dot product distance between a vector field and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, suffix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, suffix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equal(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is equal to an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equal(kotlin.String,kotlin.Any)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if a field's value is equal to another value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equal(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if an expression is equal to a value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equal(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if two expressions are equal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is equal to any of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is equal to any of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is equal to any of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,kotlin.collections.List)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if a field's value is equal to any of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,kotlin.collections.List)` . |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(com.google.firebase.firestore.pipeline.Expression,kotlin.DoubleArray)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the Euclidean distance between vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the Euclidean distance between two vector expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.VectorValue)(vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the Euclidean distance between vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(kotlin.String,kotlin.DoubleArray)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the Euclidean distance between a vector field and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the Euclidean distance between a vector field and a vector expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(kotlin.String,com.google.firebase.firestore.VectorValue)(vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the Euclidean distance between a vector field and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exists(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a field exists. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exists(com.google.firebase.firestore.pipeline.Expression)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field exists. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exp(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exp(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exp(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exp(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#field(com.google.firebase.firestore.FieldPath)(fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#field(kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#floor(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#floor(com.google.firebase.firestore.pipeline.Expression)` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#floor(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#floor(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is greater than an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(kotlin.String,kotlin.Any)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if a field's value is greater than another value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if an expression is greater than a value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if the first expression is greater than the second expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is greater than or equal to an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(kotlin.String,kotlin.Any)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if a field's value is greater than or equal to another value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if an expression is greater than or equal to a value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if the first expression is greater than or equal to the second expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(ifExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(ifExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` is absent, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(ifFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the value of the field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)(ifFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` is absent, else return the value of the field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)(tryExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression, catchExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument evaluation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(tryExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, catchExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(tryExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, catchValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#isAbsent(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns true if a field is absent. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#isAbsent(com.google.firebase.firestore.pipeline.Expression)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns true if a value is absent. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#isError(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a given expression produces an error. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#join(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that joins the elements of an array into a string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#join(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, delimiterExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that joins the elements of an array into a string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#join(kotlin.String,kotlin.String)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that joins the elements of an array field into a string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#join(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, delimiterExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that joins the elements of an array field into a string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#length(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the length of a string, array, map, vector, or blob expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#length(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that calculates the length of a string, array, map, vector, or blob field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is less than an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(kotlin.String,kotlin.Any)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if a field's value is less than another value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if an expression is less than a value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if the first expression is less than the second expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is less than or equal to an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(kotlin.String,kotlin.Any)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if a field's value is less than or equal to another value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if an expression is less than or equal to a value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if the first expression is less than or equal to the second expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#like(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that performs a case-sensitive wildcard string comparison against a field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#like(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that performs a case-sensitive wildcard string comparison against a field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#like(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that performs a case-sensitive wildcard string comparison. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#like(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that performs a case-sensitive wildcard string comparison. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ln(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ln(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ln(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ln(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, base: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, base: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, base: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, base: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log10(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log10(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log10(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log10(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMaximum(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the largest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMaximum(kotlin.String,kotlin.Array)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the largest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMinimum(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the smallest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMinimum(kotlin.String,kotlin.Array)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the smallest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#map(kotlin.collections.Map)(elements: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that creates a Firestore map value from an input object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(mapExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(mapExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapMerge(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( firstMap: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, secondMap: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherMaps: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression )` Creates an expression that merges multiple maps into a single map. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapMerge(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( firstMapFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, secondMap: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherMaps: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression )` Creates an expression that merges multiple maps into a single map. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(mapExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, key: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(mapExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(mapField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, key: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(kotlin.String,kotlin.String)(mapField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mod(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the modulo (remainder) of dividing two numeric expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mod(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that calculates the modulo (remainder) of dividing a numeric expression by a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mod(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mod(kotlin.String,kotlin.Number)(dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that multiplies numeric expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that multiplies numeric expressions with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that multiplies a numeric field with a numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(kotlin.String,kotlin.Number)(numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that multiplies a numeric field with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#not(com.google.firebase.firestore.pipeline.BooleanExpression)(condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression)` Creates an expression that negates a boolean expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is not equal to an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(kotlin.String,kotlin.Any)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if a field's value is not equal to another value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if an expression is not equal to a value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if two expressions are not equal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is not equal to all the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)(expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is not equal to all the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a field's value is not equal to all of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,kotlin.collections.List)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if a field's value is not equal to all of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#nullValue()()` Constant for a null value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#or(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Array)(condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression, vararg conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression)` Creates an expression that performs a logical 'OR' operation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, exponent: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, exponent: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, exponent: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, exponent: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#rawFunction(kotlin.String,kotlin.Array)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates a 'raw' function expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string field contains a specified regular expression as a substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string field contains a specified regular expression as a substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string expression contains a specified regular expression as a substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string expression contains a specified regular expression as a substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the first substring of a string field that matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the first substring of a string field that matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the first substring of a string expression that matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the first substring of a string expression that matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string field matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string field matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string field matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string field matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#reverse(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that reverses a string value from the specified field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#reverse(com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that reverses a string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#round(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that rounds `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#round(com.google.firebase.firestore.pipeline.Expression)` to nearest integer. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#round(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that rounds `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#round(kotlin.String)` to nearest integer. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, decimalPlace: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is negative. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, decimalPlace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is negative. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, decimalPlace: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is negative. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, decimalPlace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is negative. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#split(kotlin.String,com.google.firebase.firestore.Blob)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)` Creates an expression that splits a blob field by a blob delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#split(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that splits a string or blob field by a delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#split(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that splits a string or blob field by a string delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#split(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.Blob)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)` Creates an expression that splits a blob by a blob delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#split(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that splits a string or blob by a delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#split(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that splits a string or blob by a string delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(com.google.firebase.firestore.pipeline.Expression)(numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(kotlin.String)(numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, prefix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, prefix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` ```kotlin // Check if the 'fullName' field starts with the value of the 'firstName' field startsWith(field("fullName"), field("firstName")) ``` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(kotlin.String,kotlin.Array)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg otherStrings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates string expressions together. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(kotlin.String,kotlin.Array)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg otherStrings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that concatenates string expressions together. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(firstString: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherStrings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates string expressions together. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(firstString: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherStrings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that concatenates string expressions together. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, substring: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string field contains a specified substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, substring: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string field contains a specified substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, substring: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if a string expression contains a specified substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, substring: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if a string expression contains a specified substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringReverse(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Reverses the given string field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#stringReverse(com.google.firebase.firestore.pipeline.Expression)(str: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Reverses the given string expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#substring(kotlin.String,kotlin.Int,kotlin.Int)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, length: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that returns a substring of the given string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#substring(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, index: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, length: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression )` Creates an expression that returns a substring of the given string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(minuend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, subtrahend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that subtracts two expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(minuend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, subtrahend: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that subtracts a constant value from a numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, subtrahend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that subtracts a numeric expressions from numeric field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(kotlin.String,kotlin.Number)(numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, subtrahend: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that subtracts a constant from numeric field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(kotlin.String,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that adds a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(kotlin.String,kotlin.String,kotlin.Long)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates an expression that adds a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that adds a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(com.google.firebase.firestore.pipeline.Expression,kotlin.String,kotlin.Long)(timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates an expression that adds a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(kotlin.String,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(kotlin.String,kotlin.String,kotlin.Long)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression )` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(com.google.firebase.firestore.pipeline.Expression,kotlin.String,kotlin.Long)(timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMicros(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMicros(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that converts a timestamp field to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMillis(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMillis(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that converts a timestamp field to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixSeconds(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixSeconds(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that converts a timestamp field to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that truncates a timestamp to a specified granularity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that truncates a timestamp to a specified granularity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that truncates a timestamp to a specified granularity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that truncates a timestamp to a specified granularity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.String)( fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.String)( timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,kotlin.String,kotlin.String)( timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#toLower(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that converts a string field to lowercase. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#toLower(com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that converts a string expression to lowercase. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#toUpper(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that converts a string field to uppercase. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#toUpper(com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that converts a string expression to uppercase. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#trim(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that removes leading and trailing whitespace from a string field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#trim(com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that removes leading and trailing whitespace from a string expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#trimValue(kotlin.String,kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, valueToTrim: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that removes leading and trailing characters from a string field. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#trimValue(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, valueToTrim: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that removes leading and trailing values from a expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#type(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns a string indicating the type of the value this expression evaluates to. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#type(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that returns a string indicating the type of the value this field evaluates to. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#unixMicrosToTimestamp(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that interprets an expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#unixMicrosToTimestamp(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that interprets a field's value as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#unixMillisToTimestamp(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that interprets an expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#unixMillisToTimestamp(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that interprets a field's value as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#unixSecondsToTimestamp(com.google.firebase.firestore.pipeline.Expression)(expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that interprets an expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#unixSecondsToTimestamp(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that interprets a field's value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#vector(kotlin.DoubleArray)(vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Create a vector constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#vector(com.google.firebase.firestore.VectorValue)(vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Create a vector constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#vectorLength(kotlin.String)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that calculates the length (dimension) of a Firestore Vector. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#vectorLength(com.google.firebase.firestore.pipeline.Expression)(vectorExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the length (dimension) of a Firestore Vector. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#xor(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Array)(condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression, vararg conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression)` Creates an expression that performs a logical 'XOR' operation. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#abs()()` Creates an expression that returns the absolute value of this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#add(com.google.firebase.firestore.pipeline.Expression)(second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that adds this numeric expression to another numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#add(kotlin.Number)(second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that adds this numeric expression to a constants. |
| `open https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#alias(kotlin.String)(alias: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Assigns an alias to this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayConcat(kotlin.Any,kotlin.Array)(secondArray: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates a field's array value with other arrays. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayConcat(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(secondArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates a field's array value with other arrays. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContains(kotlin.Any)(element: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if array contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContains(kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContains(com.google.firebase.firestore.pipeline.Expression)(element: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if array contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContains(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression)(arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if array contains all elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAll(kotlin.collections.List)(values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if array contains all the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAll(kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression)(arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if array contains any elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAny(kotlin.collections.List)(values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if array contains any of the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAny(kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayGet(com.google.firebase.firestore.pipeline.Expression)(offset: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayGet(kotlin.Int)(offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayLength()()` Creates an expression that calculates the length of an array expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayReverse()()` Reverses the order of elements in the array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arraySum()()` Creates an expression that returns the sum of the elements in this array expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#asBoolean()()` Casts the expression to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ascending()()` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on value of this expression |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#average()()` Creates an aggregation that calculates the average (mean) of this numeric expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitAnd(kotlin.ByteArray)(bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise AND operation with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitAnd(com.google.firebase.firestore.pipeline.Expression)(bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise AND operation with other expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitLeftShift(kotlin.Int)(number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that applies a bitwise left shift operation with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitLeftShift(com.google.firebase.firestore.pipeline.Expression)(numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise left shift operation with an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitNot()()` Creates an expression that applies a bitwise NOT operation to this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitOr(kotlin.ByteArray)(bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise OR operation with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitOr(com.google.firebase.firestore.pipeline.Expression)(bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise OR operation with other expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitRightShift(kotlin.Int)(number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that applies a bitwise right shift operation with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitRightShift(com.google.firebase.firestore.pipeline.Expression)(numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise right shift operation with an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitXor(kotlin.ByteArray)(bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates an expression that applies a bitwise XOR operation with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#bitXor(com.google.firebase.firestore.pipeline.Expression)(bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that applies a bitwise XOR operation with an expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#byteLength()()` Creates an expression that calculates the length of a string in UTF-8 bytes, or just the length of a Blob. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ceil()()` Creates an expression that returns the smallest integer that isn't less than this numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#charLength()()` Creates an expression that calculates the character length of this string expression in UTF8. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#collectionId()()` Creates an expression that returns the collection ID from this path expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#concat(kotlin.Any,kotlin.Array)(second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates this expression's value with others. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#concat(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates this expression's value with others. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#cosineDistance(kotlin.DoubleArray)(vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the Cosine distance between this vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#cosineDistance(com.google.firebase.firestore.pipeline.Expression)(vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the Cosine distance between this and another vector expressions. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#cosineDistance(com.google.firebase.firestore.VectorValue)(vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the Cosine distance between this vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#count()()` Creates an aggregation that counts the number of stage inputs with valid evaluations of the this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#countDistinct()()` Creates an aggregation that counts the number of distinct values of an expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#descending()()` Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on value of this expression |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#divide(com.google.firebase.firestore.pipeline.Expression)(divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that divides this numeric expression by another numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#divide(kotlin.Number)(divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that divides this numeric expression by a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#documentId()()` Creates an expression that returns the document ID from this path expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#dotProduct(kotlin.DoubleArray)(vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the dot product distance between this vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#dotProduct(com.google.firebase.firestore.pipeline.Expression)(vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the dot product distance between this and another vector expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#dotProduct(com.google.firebase.firestore.VectorValue)(vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the dot product distance between this vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#endsWith(com.google.firebase.firestore.pipeline.Expression)(suffix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#endsWith(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#endsWith(kotlin.String)(suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if this string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#endsWith(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equal(com.google.firebase.firestore.pipeline.Expression)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equal(com.google.firebase.firestore.pipeline.Expression)` expression are equal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equal(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if this expression is equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equal(kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equalAny(com.google.firebase.firestore.pipeline.Expression)(arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this expression, when evaluated, is equal to any of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equalAny(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equalAny(kotlin.collections.List)(values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if this expression, when evaluated, is equal to any of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equalAny(kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#euclideanDistance(kotlin.DoubleArray)(vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html)` Calculates the Euclidean distance between this vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#euclideanDistance(com.google.firebase.firestore.pipeline.Expression)(vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Calculates the Euclidean distance between this and another vector expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#euclideanDistance(com.google.firebase.firestore.VectorValue)(vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue)` Calculates the Euclidean distance between this vector expression and a vector literal. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#exists()()` Creates an expression that checks if this expression evaluates to a name of the field that exists. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#exp()()` Creates an expression that returns Euler's number e raised to the power of this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#floor()()` Creates an expression that returns the largest integer that is not greater than this numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThan(com.google.firebase.firestore.pipeline.Expression)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this expression is greater than the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThan(com.google.firebase.firestore.pipeline.Expression)` expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThan(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if this expression is greater than a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThan(kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThanOrEqual(com.google.firebase.firestore.pipeline.Expression)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this expression is greater than or equal to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThanOrEqual(com.google.firebase.firestore.pipeline.Expression)` expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThanOrEqual(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if this expression is greater than or equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThanOrEqual(kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifAbsent(com.google.firebase.firestore.pipeline.Expression)(elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifAbsent(com.google.firebase.firestore.pipeline.Expression)` argument if this expression is absent, else return the result of this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifAbsent(kotlin.Any)(elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifAbsent(kotlin.Any)` argument if this expression is absent, else return the result of this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifError(com.google.firebase.firestore.pipeline.Expression)(catchExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifError(com.google.firebase.firestore.pipeline.Expression)` argument if there is an error, else return the result of this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifError(kotlin.Any)(catchValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifError(kotlin.Any)` argument if there is an error, else return the result of this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#isAbsent()()` Creates an expression that returns true if the result of this expression is absent. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#isError()()` Creates an expression that checks if this expression produces an error. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#join(kotlin.String)(delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that joins the elements of an array into a string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#join(com.google.firebase.firestore.pipeline.Expression)(delimiterExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that joins the elements of an array into a string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#length()()` Creates an expression that calculates the length of a string, array, map, vector, or blob expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThan(com.google.firebase.firestore.pipeline.Expression)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this expression is less than the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThan(com.google.firebase.firestore.pipeline.Expression)` expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThan(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if this expression is less than a value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThanOrEqual(com.google.firebase.firestore.pipeline.Expression)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this expression is less than or equal to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThanOrEqual(com.google.firebase.firestore.pipeline.Expression)` expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThanOrEqual(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if this expression is less than or equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThanOrEqual(kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#like(com.google.firebase.firestore.pipeline.Expression)(pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that performs a case-sensitive wildcard string comparison. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#like(kotlin.String)(pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that performs a case-sensitive wildcard string comparison. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ln()()` Creates an expression that returns the natural logarithm of this numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#log10()()` Creates an expression that returns the base-10 logarithm of this numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#logicalMaximum(kotlin.Array)(vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the largest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#logicalMaximum(kotlin.Array)(vararg others: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the largest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#logicalMinimum(kotlin.Array)(vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that returns the smallest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#logicalMinimum(kotlin.Array)(vararg others: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns the smallest value between multiple input expressions or literal values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapGet(kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Accesses a map (object) value using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapGet(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapGet(com.google.firebase.firestore.pipeline.Expression)(keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Accesses a map (object) value using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapGet(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapMerge(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(mapExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, vararg otherMaps: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that merges multiple maps into a single map. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapRemove(kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that removes a key from this map expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapRemove(com.google.firebase.firestore.pipeline.Expression)(keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that removes a key from this map expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#maximum()()` Creates an aggregation that finds the maximum value of this expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#minimum()()` Creates an aggregation that finds the minimum value of this expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mod(com.google.firebase.firestore.pipeline.Expression)(divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that calculates the modulo (remainder) of dividing this numeric expressions by another numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mod(kotlin.Number)(divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that calculates the modulo (remainder) of dividing this numeric expressions by a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#multiply(com.google.firebase.firestore.pipeline.Expression)(second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that multiplies this numeric expression with another numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#multiply(kotlin.Number)(second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that multiplies this numeric expression with a constant. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqual(com.google.firebase.firestore.pipeline.Expression)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this expressions is not equal to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqual(com.google.firebase.firestore.pipeline.Expression)` expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqual(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that checks if this expression is not equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqual(kotlin.Any)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqualAny(com.google.firebase.firestore.pipeline.Expression)(arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this expression, when evaluated, is not equal to all the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqualAny(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqualAny(kotlin.collections.List)(values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>)` Creates an expression that checks if this expression, when evaluated, is not equal to all the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqualAny(kotlin.collections.List)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(com.google.firebase.firestore.pipeline.Expression)(exponent: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns this numeric expression raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(kotlin.Number)(exponent: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that returns this numeric expression raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(kotlin.Number)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#regexContains(com.google.firebase.firestore.pipeline.Expression)(pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this string expression contains a specified regular expression as a substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#regexContains(kotlin.String)(pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if this string expression contains a specified regular expression as a substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#regexMatch(com.google.firebase.firestore.pipeline.Expression)(pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this string expression matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#regexMatch(kotlin.String)(pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if this string expression matches a specified regular expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#reverse()()` Creates an expression that reverses this string expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#round()()` Creates an expression that rounds this numeric expression to nearest integer. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(com.google.firebase.firestore.pipeline.Expression)(decimalPlace: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that rounds off this numeric expression to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(com.google.firebase.firestore.pipeline.Expression)` is negative. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(kotlin.Int)(decimalPlace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that rounds off this numeric expression to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(kotlin.Int)` is negative. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#split(com.google.firebase.firestore.Blob)(delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)` Creates an expression that splits this blob expression by a blob delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#split(com.google.firebase.firestore.pipeline.Expression)(delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that splits this string or blob expression by a delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#split(kotlin.String)(delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that splits this string or blob expression by a string delimiter. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#sqrt()()` Creates an expression that returns the square root of this numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#startsWith(com.google.firebase.firestore.pipeline.Expression)(prefix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#startsWith(com.google.firebase.firestore.pipeline.Expression)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#startsWith(kotlin.String)(prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if this string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#startsWith(kotlin.String)`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#stringConcat(kotlin.Array)(vararg stringExpressions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that concatenates string expressions together. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#stringConcat(kotlin.Array)(vararg strings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates an expression that concatenates string expressions and string constants together. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#stringConcat(kotlin.Array)(vararg strings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that concatenates this string expression with string constants. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#stringContains(com.google.firebase.firestore.pipeline.Expression)(substring: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that checks if this string expression contains a specified substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#stringContains(kotlin.String)(substring: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that checks if this string expression contains a specified substring. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#stringReverse()()` Creates an expression that performs a reverse operation on this string expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#substring(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(start: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, length: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that returns a substring of the given string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#substring(kotlin.Int,kotlin.Int)(start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, length: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates an expression that returns a substring of the given string. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#subtract(com.google.firebase.firestore.pipeline.Expression)(subtrahend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that subtracts a constant from this numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#subtract(kotlin.Number)(subtrahend: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html)` Creates an expression that subtracts a numeric expressions from this numeric expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#sum()()` Creates an aggregation that calculates the sum of this numeric expression across multiple stage inputs. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampAdd(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that adds a specified amount of time to this timestamp expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampAdd(kotlin.String,kotlin.Long)(unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates an expression that adds a specified amount of time to this timestamp expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampSubtract(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that subtracts a specified amount of time to this timestamp expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampSubtract(kotlin.String,kotlin.Long)(unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Creates an expression that subtracts a specified amount of time to this timestamp expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampToUnixMicros()()` Creates an expression that converts this timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampToUnixMillis()()` Creates an expression that converts this timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampToUnixSeconds()()` Creates an expression that converts this timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampTruncate(com.google.firebase.firestore.pipeline.Expression)(granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that truncates this timestamp expression to a specified granularity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#timestampTruncate(kotlin.String)(granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that truncates this timestamp expression to a specified granularity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#toLower()()` Creates an expression that converts this string expression to lowercase. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#toUpper()()` Creates an expression that converts this string expression to uppercase. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#trim()()` Creates an expression that removes leading and trailing whitespace from this string expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#trimValue(com.google.firebase.firestore.pipeline.Expression)(valueToTrim: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Creates an expression that removes leading and trailing value from this expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#trimValue(kotlin.String)(valueToTrim: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Creates an expression that removes leading and trailing characters from this string expression. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#type()()` Creates an expression that returns a string indicating the type of the value this expression evaluates to. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#unixMicrosToTimestamp()()` Creates an expression that interprets this expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#unixMillisToTimestamp()()` Creates an expression that interprets this expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#unixSecondsToTimestamp()()` Creates an expression that interprets this expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#vectorLength()()` Creates an expression that calculates the length (dimension) of a Firestore Vector. |

## Public companion functions

### abs

```
fun abs(numericExpr: Expression): Expression
```

Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#abs(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Get the absolute value of the 'change' field.
abs(field("change"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the absolute value operation. |

### abs

```
fun abs(numericField: String): Expression
```

Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#abs(kotlin.String)`.

```kotlin
// Get the absolute value of the 'change' field.
abs("change")
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the absolute value operation. |

### add

```
fun add(first: Expression, second: Expression): Expression
```

Creates an expression that adds numeric expressions.

```kotlin
// Add the value of the 'quantity' field and the 'reserve' field.
add(field("quantity"), field("reserve"))
```

| Parameters |
|---|---|
| `first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to add. |
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### add

```
fun add(first: Expression, second: Number): Expression
```

Creates an expression that adds numeric expressions with a constant.

```kotlin
// Add 5 to the value of the 'quantity' field.
add(field("quantity"), 5)
```

| Parameters |
|---|---|
| `first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to add. |
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### add

```
fun add(numericFieldName: String, second: Expression): Expression
```

Creates an expression that adds a numeric field with a numeric expression.

```kotlin
// Add the value of the 'quantity' field and the 'reserve' field.
add("quantity", field("reserve"))
```

| Parameters |
|---|---|
| `numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Numeric field to add. |
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to add to field value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### add

```
fun add(numericFieldName: String, second: Number): Expression
```

Creates an expression that adds a numeric field with constant.

```kotlin
// Add 5 to the value of the 'quantity' field.
add("quantity", 5)
```

| Parameters |
|---|---|
| `numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Numeric field to add. |
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### and

```
fun and(condition: BooleanExpression, vararg conditions: BooleanExpression): BooleanExpression
```

Creates an expression that performs a logical 'AND' operation.

```kotlin
// Check if 'status' is "new" and 'priority' is greater than 1
and(field("status").equal("new"), field("priority").greaterThan(1))
```

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`. |
| `vararg conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | Additional `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`s. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the logical 'AND' operation. |

### array

```
fun array(elements: List<Any?>): Expression
```

Creates an expression that creates a Firestore array value from an input array.

| Parameters |
|---|---|
| `elements: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?>` | The input array to evaluate in the expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the array function. |

### array

```
fun array(vararg elements: Any?): Expression
```

Creates an expression that creates a Firestore array value from an input array.

```kotlin
// Create an array of numbers
array(1, 2, 3)

// Create an array containing a field value and a constant
array(field("quantity"), 10)
```

| Parameters |
|---|---|
| `vararg elements: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The input array to evaluate in the expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the array function. |

### arrayConcat

```
fun arrayConcat(
    firstArray: Expression,
    secondArray: Any,
    vararg otherArrays: Any
): Expression
```

Creates an expression that concatenates an array with other arrays.

```kotlin
// Combine the 'items' array with another array field.
arrayConcat(field("items"), field("otherItems"))
```

| Parameters |
|---|---|
| `firstArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first array expression to concatenate to. |
| `secondArray: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | An array expression or array literal to concatenate. |
| `vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayConcat

```
fun arrayConcat(
    firstArray: Expression,
    secondArray: Expression,
    vararg otherArrays: Any
): Expression
```

Creates an expression that concatenates an array with other arrays.

```kotlin
// Combine the 'items' array with another array field.
arrayConcat(field("items"), field("otherItems"))
```

| Parameters |
|---|---|
| `firstArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first array expression to concatenate to. |
| `secondArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to array to concatenate. |
| `vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayConcat

```
fun arrayConcat(
    firstArrayField: String,
    secondArray: Any,
    vararg otherArrays: Any
): Expression
```

Creates an expression that concatenates a field's array value with other arrays.

```kotlin
// Combine the 'items' array with a literal array.
arrayConcat("items", listOf("a", "b"))
```

| Parameters |
|---|---|
| `firstArrayField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains first array to concatenate to. |
| `secondArray: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | An array expression or array literal to concatenate. |
| `vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayConcat

```
fun arrayConcat(
    firstArrayField: String,
    secondArray: Expression,
    vararg otherArrays: Any
): Expression
```

Creates an expression that concatenates a field's array value with other arrays.

```kotlin
// Combine the 'items' array with another array field.
arrayConcat("items", field("otherItems"))
```

| Parameters |
|---|---|
| `firstArrayField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains first array to concatenate to. |
| `secondArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to array to concatenate. |
| `vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayContains

```
fun arrayContains(array: Expression, element: Any): BooleanExpression
```

Creates an expression that checks if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)`.

```kotlin
// Check if the 'sizes' array contains the value from the 'selectedSize' field
arrayContains(field("sizes"), field("selectedSize"))

// Check if the 'colors' array contains "red"
arrayContains(field("colors"), "red")
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to check. |
| `element: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The element to search for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContains

```
fun arrayContains(array: Expression, element: Expression): BooleanExpression
```

Creates an expression that checks if the array contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to check. |
| `element: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The element to search for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContains

```
fun arrayContains(arrayFieldName: String, element: Any): BooleanExpression
```

Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,kotlin.Any)`.

```kotlin
// Check if the 'colors' array contains "red"
arrayContains("colors", "red")
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains array to check. |
| `element: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The element to search for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContains

```
fun arrayContains(arrayFieldName: String, element: Expression): BooleanExpression
```

Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'sizes' array contains the value from the 'selectedSize' field
arrayContains("sizes", field("selectedSize"))
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains array to check. |
| `element: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The element to search for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContainsAll

```
fun arrayContainsAll(array: Expression, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains all elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'tags' array contains both of the values from field "tag1" and the literal value "tag2"
arrayContainsAll(field("tags"), array(field("tag1"), "tag2"))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to check. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAll

```
fun arrayContainsAll(array: Expression, values: List<Any>): BooleanExpression
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains all the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```kotlin
// Check if the 'tags' array contains both the value in field "tag1" and the literal value "tag2"
arrayContainsAll(field("tags"), listOf(field("tag1"), "tag2"))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to check. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAll

```
fun arrayContainsAll(arrayFieldName: String, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if array field contains all elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'permissions' array contains all the required permissions
arrayContainsAll("permissions", field("requiredPermissions"))
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains array to check. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAll

```
fun arrayContainsAll(arrayFieldName: String, values: List<Any>): BooleanExpression
```

Creates an expression that checks if array field contains all the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,kotlin.collections.List)`.

```kotlin
// Check if the 'tags' array contains both "internal" and "public"
arrayContainsAll("tags", listOf("internal", "public"))
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains array to check. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAny

```
fun arrayContainsAny(array: Expression, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains any elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'groups' array contains either the value from the 'userGroup' field
// or the value "guest"
arrayContainsAny(field("groups"), array(field("userGroup"), "guest"))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to check. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayContainsAny

```
fun arrayContainsAny(array: Expression, values: List<Any>): BooleanExpression
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains any of the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```kotlin
// Check if the 'categories' array contains either values from field "cate1" or "cate2"
arrayContainsAny(field("categories"), listOf(field("cate1"), field("cate2")))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to check. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayContainsAny

```
fun arrayContainsAny(arrayFieldName: String, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if array field contains any elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'userGroups' array contains any of the 'targetGroups'
arrayContainsAny("userGroups", field("targetGroups"))
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains array to check. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayContainsAny

```
fun arrayContainsAny(arrayFieldName: String, values: List<Any>): BooleanExpression
```

Creates an expression that checks if array field contains any of the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,kotlin.collections.List)`.

```kotlin
// Check if the 'roles' array contains "admin" or "editor"
arrayContainsAny("roles", listOf("admin", "editor"))
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains array to check. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayGet

```
fun arrayGet(array: Expression, offset: Expression): Expression
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```kotlin
// Return the value in the tags field array at index specified by field 'favoriteTag'.
arrayGet(field("tags"), field("favoriteTag"))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` evaluating to an array. |
| `offset: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An Expression evaluating to the index of the element to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayGet

```
fun arrayGet(array: Expression, offset: Int): Expression
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```kotlin
// Return the value in the 'tags' field array at index `1`.
arrayGet(field("tags"), 1)
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` evaluating to an array. |
| `offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The index of the element to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayGet

```
fun arrayGet(arrayFieldName: String, offset: Expression): Expression
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```kotlin
// Return the value in the tags field array at index specified by field 'favoriteTag'.
arrayGet("tags", field("favoriteTag"))
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of an array field. |
| `offset: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An Expression evaluating to the index of the element to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayGet

```
fun arrayGet(arrayFieldName: String, offset: Int): Expression
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```kotlin
// Return the value in the 'tags' field array at index `1`.
arrayGet("tags", 1)
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of an array field. |
| `offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The index of the element to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayLength

```
fun arrayLength(array: Expression): Expression
```

Creates an expression that calculates the length of an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(com.google.firebase.firestore.pipeline.Expression)` expression.

```kotlin
// Get the number of items in the 'cart' array
arrayLength(field("cart"))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to calculate the length of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length of the array. |

### arrayLength

```
fun arrayLength(arrayFieldName: String): Expression
```

Creates an expression that calculates the length of an array field.

```kotlin
// Get the number of items in the 'cart' array
arrayLength("cart")
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing an array to calculate the length of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length of the array. |

### arrayReverse

```
fun arrayReverse(array: Expression): Expression
```

Reverses the order of elements in the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Reverse the value of the 'myArray' field.
arrayReverse(field("myArray"))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to reverse. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayReverse operation. |

### arrayReverse

```
fun arrayReverse(arrayFieldName: String): Expression
```

Reverses the order of elements in the array field.

```kotlin
// Reverse the value of the 'myArray' field.
arrayReverse("myArray")
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains the array to reverse. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayReverse operation. |

### arraySum

```
fun arraySum(array: Expression): Expression
```

Creates an expression that returns the sum of the elements in an array.

```kotlin
// Get the sum of elements in the 'scores' array.
arraySum(field("scores"))
```

| Parameters |
|---|---|
| `array: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The array expression to sum. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the sum of the array elements. |

### arraySum

```
fun arraySum(arrayFieldName: String): Expression
```

Creates an expression that returns the sum of the elements in an array field.

```kotlin
// Get the sum of elements in the 'scores' array.
arraySum("scores")
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the array to sum. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the sum of the array elements. |

### bitAnd

```
fun bitAnd(bits: Expression, bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise AND operation between an expression and a constant.

```kotlin
// Bitwise AND the value of the 'flags' field with a constant mask.
bitAnd(field("flags"), byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitAnd

```
fun bitAnd(bits: Expression, bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise AND operation between two expressions.

```kotlin
// Bitwise AND the value of the 'flags' field with the value of the 'mask' field.
bitAnd(field("flags"), field("mask"))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitAnd

```
fun bitAnd(bitsFieldName: String, bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise AND operation between an field and constant.

```kotlin
// Bitwise AND the value of the 'flags' field with a constant mask.
bitAnd("flags", byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitAnd

```
fun bitAnd(bitsFieldName: String, bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise AND operation between an field and an expression.

```kotlin
// Bitwise AND the value of the 'flags' field with the value of the 'mask' field.
bitAnd("flags", field("mask"))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitLeftShift

```
fun bitLeftShift(bits: Expression, number: Int): Expression
```

Creates an expression that applies a bitwise left shift operation between an expression and a constant.

```kotlin
// Left shift the value of the 'bits' field by 2.
bitLeftShift(field("bits"), 2)
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitLeftShift

```
fun bitLeftShift(bits: Expression, numberExpr: Expression): Expression
```

Creates an expression that applies a bitwise left shift operation between two expressions.

```kotlin
// Left shift the value of the 'bits' field by the value of the 'shift' field.
bitLeftShift(field("bits"), field("shift"))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitLeftShift

```
fun bitLeftShift(bitsFieldName: String, number: Int): Expression
```

Creates an expression that applies a bitwise left shift operation between a field and a constant.

```kotlin
// Left shift the value of the 'bits' field by 2.
bitLeftShift("bits", 2)
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitLeftShift

```
fun bitLeftShift(bitsFieldName: String, numberExpr: Expression): Expression
```

Creates an expression that applies a bitwise left shift operation between a field and an expression.

```kotlin
// Left shift the value of the 'bits' field by the value of the 'shift' field.
bitLeftShift("bits", field("shift"))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitNot

```
fun bitNot(bits: Expression): Expression
```

Creates an expression that applies a bitwise NOT operation to an expression.

```kotlin
// Bitwise NOT the value of the 'flags' field.
bitNot(field("flags"))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise NOT operation. |

### bitNot

```
fun bitNot(bitsFieldName: String): Expression
```

Creates an expression that applies a bitwise NOT operation to a field.

```kotlin
// Bitwise NOT the value of the 'flags' field.
bitNot("flags")
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise NOT operation. |

### bitOr

```
fun bitOr(bits: Expression, bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise OR operation between an expression and a constant.

```kotlin
// Bitwise OR the value of the 'flags' field with a constant mask.
bitOr(field("flags"), byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitOr

```
fun bitOr(bits: Expression, bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise OR operation between two expressions.

```kotlin
// Bitwise OR the value of the 'flags' field with the value of the 'mask' field.
bitOr(field("flags"), field("mask"))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitOr

```
fun bitOr(bitsFieldName: String, bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise OR operation between an field and constant.

```kotlin
// Bitwise OR the value of the 'flags' field with a constant mask.
bitOr("flags", byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitOr

```
fun bitOr(bitsFieldName: String, bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise OR operation between an field and an expression.

```kotlin
// Bitwise OR the value of the 'flags' field with the value of the 'mask' field.
bitOr("flags", field("mask"))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitRightShift

```
fun bitRightShift(bits: Expression, number: Int): Expression
```

Creates an expression that applies a bitwise right shift operation between an expression and a constant.

```kotlin
// Right shift the value of the 'bits' field by 2.
bitRightShift(field("bits"), 2)
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitRightShift

```
fun bitRightShift(bits: Expression, numberExpr: Expression): Expression
```

Creates an expression that applies a bitwise right shift operation between two expressions.

```kotlin
// Right shift the value of the 'bits' field by the value of the 'shift' field.
bitRightShift(field("bits"), field("shift"))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitRightShift

```
fun bitRightShift(bitsFieldName: String, number: Int): Expression
```

Creates an expression that applies a bitwise right shift operation between a field and a constant.

```kotlin
// Right shift the value of the 'bits' field by 2.
bitRightShift("bits", 2)
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitRightShift

```
fun bitRightShift(bitsFieldName: String, numberExpr: Expression): Expression
```

Creates an expression that applies a bitwise right shift operation between a field and an expression.

```kotlin
// Right shift the value of the 'bits' field by the value of the 'shift' field.
bitRightShift("bits", field("shift"))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitXor

```
fun bitXor(bits: Expression, bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise XOR operation between an expression and a constant.

```kotlin
// Bitwise XOR the value of the 'flags' field with a constant mask.
bitXor(field("flags"), byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### bitXor

```
fun bitXor(bits: Expression, bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise XOR operation between two expressions.

```kotlin
// Bitwise XOR the value of the 'flags' field with the value of the 'mask' field.
bitXor(field("flags"), field("mask"))
```

| Parameters |
|---|---|
| `bits: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### bitXor

```
fun bitXor(bitsFieldName: String, bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise XOR operation between an field and constant.

```kotlin
// Bitwise XOR the value of the 'flags' field with a constant mask.
bitXor("flags", byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### bitXor

```
fun bitXor(bitsFieldName: String, bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise XOR operation between an field and an expression.

```kotlin
// Bitwise XOR the value of the 'flags' field with the value of the 'mask' field.
bitXor("flags", field("mask"))
```

| Parameters |
|---|---|
| `bitsFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that contains bits data. |
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### byteLength

```
fun byteLength(fieldName: String): Expression
```

Creates an expression that calculates the length of a string represented by a field in UTF-8 bytes, or just the length of a Blob.

```kotlin
// Calculate the length of the 'myString' field in bytes.
byteLength("myString")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length of the string in bytes. |

### byteLength

```
fun byteLength(value: Expression): Expression
```

Creates an expression that calculates the length of a string in UTF-8 bytes, or just the length of a Blob.

```kotlin
// Calculate the length of the 'myString' field in bytes.
byteLength("myString")
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length of the string in bytes. |

### ceil

```
fun ceil(numericExpr: Expression): Expression
```

Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Compute the ceiling of the 'price' field.
ceil(field("price"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the ceil operation. |

### ceil

```
fun ceil(numericField: String): Expression
```

Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(kotlin.String)`.

```kotlin
// Compute the ceiling of the 'price' field.
ceil("price")
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the ceil operation. |

### charLength

```
fun charLength(expr: Expression): Expression
```

Creates an expression that calculates the character length of a string expression in UTF8.

```kotlin
// Get the character length of the 'name' field in UTF-8.
charLength("name")
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the charLength operation. |

### charLength

```
fun charLength(fieldName: String): Expression
```

Creates an expression that calculates the character length of a string field in UTF8.

```kotlin
// Get the character length of the 'name' field in UTF-8.
charLength("name")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the charLength operation. |

### collectionId

```
fun collectionId(path: Expression): Expression
```

Creates an expression that returns the collection ID from a path.

```kotlin
// Get the collection ID from the 'path' field
collectionId(field("path"))
```

| Parameters |
|---|---|
| `path: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression the evaluates to a path. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the collectionId operation. |

### collectionId

```
fun collectionId(pathField: String): Expression
```

Creates an expression that returns the collection ID from a path.

```kotlin
// Get the collection ID from a path field
collectionId("pathField")
```

| Parameters |
|---|---|
| `pathField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string representation of the path. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the collectionId operation. |

### concat

```
fun concat(first: Expression, second: Any, vararg others: Any): Expression
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```kotlin
// Concatenate a field with a literal string.
concat(field("firstName"), "Doe")
```

| Parameters |
|---|---|
| `first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to concatenate. |
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The second value to concatenate. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Additional values to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### concat

```
fun concat(first: Expression, second: Expression, vararg others: Any): Expression
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```kotlin
// Concatenate the 'firstName' and 'lastName' fields with a space in between.
concat(field("firstName"), " ", field("lastName"))
```

| Parameters |
|---|---|
| `first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to concatenate. |
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to concatenate. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Additional expressions to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### concat

```
fun concat(first: String, second: Any, vararg others: Any): Expression
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```kotlin
// Concatenate a field name with a literal string.
concat("firstName", "Doe")
```

| Parameters |
|---|---|
| `first: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first value to concatenate. |
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The second value to concatenate. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Additional values to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### concat

```
fun concat(first: String, second: Expression, vararg others: Any): Expression
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```kotlin
// Concatenate a field name with an expression.
concat("firstName", field("lastName"))
```

| Parameters |
|---|---|
| `first: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first value to concatenate. |
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to concatenate. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Additional expressions to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### conditional

```
fun conditional(
    condition: BooleanExpression,
    thenExpr: Expression,
    elseExpr: Expression
): Expression
```

Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if a condition is true or an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if the condition is false.

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The condition to evaluate. |
| `thenExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to evaluate if the condition is true. |
| `elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to evaluate if the condition is false. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the conditional operation. |

### conditional

```
fun conditional(condition: BooleanExpression, thenValue: Any, elseValue: Any): Expression
```

Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if a condition is true or an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if the condition is false.

```kotlin
// If the 'quantity' field is greater than 10, return "High", otherwise return "Low"
conditional(field("quantity").greaterThan(10), "High", "Low")
```

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The condition to evaluate. |
| `thenValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Value if the condition is true. |
| `elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Value if the condition is false. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the conditional operation. |

### constant

```
fun constant(ref: DocumentReference): Expression
```

Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` value.

```kotlin
// val firestore = FirebaseFirestore.getInstance()
// val docRef = firestore.collection("cities").document("SF")
// constant(docRef)
```

| Parameters |
|---|---|
| `ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: Blob): Expression
```

Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` value.

```kotlin
// Create a constant with a Blob
constant(Blob.fromBytes(byteArrayOf(0x48, 0x65, 0x6c, 0x6c, 0x6f))) // "Hello"
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: Boolean): BooleanExpression
```

Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value.

```kotlin
// Create a constant with the value true
constant(true)
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` constant instance. |

### constant

```
fun constant(value: ByteArray): Expression
```

Create a constant for a bytes value.

```kotlin
// Create a constant with a byte array
constant(byteArrayOf(0x48, 0x65, 0x6c, 0x6c, 0x6f)) // "Hello"
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | The bytes value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: Date): Expression
```

Create a constant for a `https://developer.android.com/reference/kotlin/java/util/Date.html` value.

```kotlin
// Create a constant with the current date
constant(Date())
```

| Parameters |
|---|---|
| `value: https://developer.android.com/reference/kotlin/java/util/Date.html` | The `https://developer.android.com/reference/kotlin/java/util/Date.html` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: GeoPoint): Expression
```

Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint` value.

```kotlin
// Create a constant with a GeoPoint
constant(GeoPoint(37.7749, -122.4194))
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/GeoPoint` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: Number): Expression
```

Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` value.

```kotlin
// Create a constant with the value 123
constant(123)
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: String): Expression
```

Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value.

```kotlin
// Create a constant with the value "hello"
constant("hello")
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: Timestamp): Expression
```

Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` value.

```kotlin
// Create a constant with the current timestamp
constant(Timestamp.now())
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
fun constant(value: VectorValue): Expression
```

Create a constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` value.

```kotlin
// Create a constant with a VectorValue
constant(VectorValue(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### cosineDistance

```
fun cosineDistance(vector1: Expression, vector2: DoubleArray): Expression
```

Calculates the Cosine distance between vector expression and a vector literal.

```kotlin
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance(field("location"), doubleArrayOf(37.7749, -122.4194))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an Expression) to compare against. |
| `vector2: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
fun cosineDistance(vector1: Expression, vector2: Expression): Expression
```

Calculates the Cosine distance between two vector expressions.

```kotlin
// Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
cosineDistance(field("userVector"), field("itemVector"))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an Expression) to compare against. |
| `vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
fun cosineDistance(vector1: Expression, vector2: VectorValue): Expression
```

Calculates the Cosine distance between vector expression and a vector literal.

```kotlin
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance(field("location"), VectorValue.from(listOf(37.7749, -122.4194)))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression`) to compare against. |
| `vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
fun cosineDistance(vectorFieldName: String, vector: DoubleArray): Expression
```

Calculates the Cosine distance between a vector field and a vector literal.

```kotlin
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance("location", doubleArrayOf(37.7749, -122.4194))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
fun cosineDistance(vectorFieldName: String, vector: Expression): Expression
```

Calculates the Cosine distance between a vector field and a vector expression.

```kotlin
// Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
cosineDistance("userVector", field("itemVector"))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
fun cosineDistance(vectorFieldName: String, vector: VectorValue): Expression
```

Calculates the Cosine distance between a vector field and a vector literal.

```kotlin
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance("location", VectorValue.from(listOf(37.7749, -122.4194)))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### currentTimestamp

```
fun currentTimestamp(): Expression
```

Creates an expression that evaluates to the current server timestamp.

```kotlin
// Get the current server timestamp
currentTimestamp()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the current server timestamp. |

### divide

```
fun divide(dividend: Expression, divisor: Expression): Expression
```

Creates an expression that divides two numeric expressions.

```kotlin
// Divide the 'total' field by the 'count' field
divide(field("total"), field("count"))
```

| Parameters |
|---|---|
| `dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to be divided. |
| `divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the division operation. |

### divide

```
fun divide(dividend: Expression, divisor: Number): Expression
```

Creates an expression that divides a numeric expression by a constant.

```kotlin
// Divide the 'value' field by 10
divide(field("value"), 10)
```

| Parameters |
|---|---|
| `dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to be divided. |
| `divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The constant to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the division operation. |

### divide

```
fun divide(dividendFieldName: String, divisor: Expression): Expression
```

Creates an expression that divides numeric field by a numeric expression.

```kotlin
// Divide the 'total' field by the 'count' field.
divide("total", field("count"))
```

| Parameters |
|---|---|
| `dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The numeric field name to be divided. |
| `divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the divide operation. |

### divide

```
fun divide(dividendFieldName: String, divisor: Number): Expression
```

Creates an expression that divides a numeric field by a constant.

```kotlin
// Divide the 'total' field by 2.
divide("total", 2)
```

| Parameters |
|---|---|
| `dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The numeric field name to be divided. |
| `divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The constant to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the divide operation. |

### documentId

```
fun documentId(docRef: DocumentReference): Expression
```

Creates an expression that returns the document ID from a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference`.

| Parameters |
|---|---|
| `docRef: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the documentId operation. |

### documentId

```
fun documentId(documentPath: Expression): Expression
```

Creates an expression that returns the document ID from a path.

```kotlin
// Get the document ID from the 'path' field
documentId(field("path"))
```

| Parameters |
|---|---|
| `documentPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression the evaluates to document path. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the documentId operation. |

### documentId

```
fun documentId(documentPath: String): Expression
```

Creates an expression that returns the document ID from a path.

```kotlin
// Get the document ID from a path string
documentId("projects/p/databases/d/documents/c/d")
```

| Parameters |
|---|---|
| `documentPath: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string representation of the document path. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the documentId operation. |

### dotProduct

```
fun dotProduct(vector1: Expression, vector2: DoubleArray): Expression
```

Calculates the dot product distance between vector expression and a vector literal.

```kotlin
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct(field("vector"), doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an Expression) to compare against. |
| `vector2: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
fun dotProduct(vector1: Expression, vector2: Expression): Expression
```

Calculates the dot product distance between two vector expressions.

```kotlin
// Calculate the dot product between the 'userVector' field and the 'itemVector' field
dotProduct(field("userVector"), field("itemVector"))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an Expression) to compare against. |
| `vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
fun dotProduct(vector1: Expression, vector2: VectorValue): Expression
```

Calculates the dot product distance between vector expression and a vector literal.

```kotlin
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct(field("vector"), VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression`) to compare against. |
| `vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
fun dotProduct(vectorFieldName: String, vector: DoubleArray): Expression
```

Calculates the dot product distance between vector field and a vector literal.

```kotlin
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct("vector", doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
fun dotProduct(vectorFieldName: String, vector: Expression): Expression
```

Calculates the dot product distance between a vector field and a vector expression.

```kotlin
// Calculate the dot product between the 'userVector' field and the 'itemVector' field
dotProduct("userVector", field("itemVector"))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
fun dotProduct(vectorFieldName: String, vector: VectorValue): Expression
```

Calculates the dot product distance between a vector field and a vector literal.

```kotlin
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct("vector", VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### endsWith

```
fun endsWith(fieldName: String, suffix: Expression): BooleanExpression
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'url' field ends with the value of the 'extension' field
endsWith("url", field("extension"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains a string to check. |
| `suffix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The suffix string expression to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### endsWith

```
fun endsWith(fieldName: String, suffix: String): BooleanExpression
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,kotlin.String)`.

```kotlin
// Check if the 'filename' field ends with ".txt"
endsWith("filename", ".txt")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains a string to check. |
| `suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The suffix string to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### endsWith

```
fun endsWith(stringExpr: Expression, suffix: Expression): BooleanExpression
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'url' field ends with the value of the 'extension' field
endsWith(field("url"), field("extension"))
```

| Parameters |
|---|---|
| `stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check. |
| `suffix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The suffix string expression to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### endsWith

```
fun endsWith(stringExpr: Expression, suffix: String): BooleanExpression
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`.

```kotlin
// Check if the 'filename' field ends with ".txt"
endsWith(field("filename"), ".txt")
```

| Parameters |
|---|---|
| `stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check. |
| `suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The suffix string to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### equal

```
fun equal(fieldName: String, expression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is equal to an expression.

```kotlin
// Check if the 'age' field is equal to the 'limit' field
equal("age", field("limit"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equal

```
fun equal(fieldName: String, value: Any): BooleanExpression
```

Creates an expression that checks if a field's value is equal to another value.

```kotlin
// Check if the 'city' field is equal to string constant "London"
equal("city", "London")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equal

```
fun equal(left: Expression, right: Any): BooleanExpression
```

Creates an expression that checks if an expression is equal to a value.

```kotlin
// Check if the 'age' field is equal to 21
equal(field("age"), 21)
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equal

```
fun equal(left: Expression, right: Expression): BooleanExpression
```

Creates an expression that checks if two expressions are equal.

```kotlin
// Check if the 'age' field is equal to an expression
equal(field("age"), field("minAge").add(10))
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equalAny

```
fun equalAny(expression: Expression, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is equal to any of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'category' field is in the 'availableCategories' array field.
equalAny(field("category"), field("availableCategories"))
```

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression whose results to compare. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### equalAny

```
fun equalAny(expression: Expression, values: List<Any>): BooleanExpression
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is equal to any of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```kotlin
// Check if the 'category' field is either "Electronics" or the value of the 'primaryType' field.
equalAny(field("category"), listOf("Electronics", field("primaryType")))
```

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression whose results to compare. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The values to check against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### equalAny

```
fun equalAny(fieldName: String, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is equal to any of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'category' field is in the 'availableCategories' array field.
equalAny("category", field("availableCategories"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to compare. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### equalAny

```
fun equalAny(fieldName: String, values: List<Any>): BooleanExpression
```

Creates an expression that checks if a field's value is equal to any of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,kotlin.collections.List)` .

```kotlin
// Check if the 'category' field is either "Electronics" or "Apparel".
equalAny("category", listOf("Electronics", "Apparel"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to compare. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The values to check against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### euclideanDistance

```
fun euclideanDistance(vector1: Expression, vector2: DoubleArray): Expression
```

Calculates the Euclidean distance between vector expression and a vector literal.

```kotlin
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance(field("vector"), doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an Expression) to compare against. |
| `vector2: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
fun euclideanDistance(vector1: Expression, vector2: Expression): Expression
```

Calculates the Euclidean distance between two vector expressions.

```kotlin
// Calculate the Euclidean distance between the 'userVector' field and the 'itemVector' field
euclideanDistance(field("userVector"), field("itemVector"))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an Expression) to compare against. |
| `vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
fun euclideanDistance(vector1: Expression, vector2: VectorValue): Expression
```

Calculates the Euclidean distance between vector expression and a vector literal.

```kotlin
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance(field("vector"), VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `vector1: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression`) to compare against. |
| `vector2: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
fun euclideanDistance(vectorFieldName: String, vector: DoubleArray): Expression
```

Calculates the Euclidean distance between a vector field and a vector literal.

```kotlin
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance("vector", doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
fun euclideanDistance(vectorFieldName: String, vector: Expression): Expression
```

Calculates the Euclidean distance between a vector field and a vector expression.

```kotlin
// Calculate the Euclidean distance between the 'userVector' field and the 'itemVector' field
euclideanDistance("userVector", field("itemVector"))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
fun euclideanDistance(vectorFieldName: String, vector: VectorValue): Expression
```

Calculates the Euclidean distance between a vector field and a vector literal.

```kotlin
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance("vector", VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `vectorFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the first vector. |
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### exists

```
fun exists(fieldName: String): BooleanExpression
```

Creates an expression that checks if a field exists.

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to check. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the exists check. |

### exists

```
fun exists(value: Expression): BooleanExpression
```

Creates an expression that checks if a field exists.

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression evaluates to the name of the field to check. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the exists check. |

### exp

```
fun exp(numericExpr: Expression): Expression
```

Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exp(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Compute e to the power of the 'value' field.
exp(field("value"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the exponentiation. |

### exp

```
fun exp(numericField: String): Expression
```

Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#exp(kotlin.String)`.

```kotlin
// Compute e to the power of the 'value' field.
exp("value")
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the exponentiation. |

### field

```
fun field(fieldPath: FieldPath): Field
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path.

The path can be a simple field name (e.g., "name") or a dot-separated path to a nested field (e.g., "address.city").

```kotlin
// Get the 'address.city' field
field(FieldPath.of("address", "city"))
```

| Parameters |
|---|---|
| `fieldPath: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath` to the field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` instance representing the specified path. |

### field

```
fun field(name: String): Field
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path.

The path can be a simple field name (e.g., "name") or a dot-separated path to a nested field (e.g., "address.city").

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The path to the field. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` instance representing the specified path. |

### floor

```
fun floor(numericExpr: Expression): Expression
```

Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#floor(com.google.firebase.firestore.pipeline.Expression)`

```kotlin
// Compute the floor of the 'price' field.
floor(field("price"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the floor operation. |

### floor

```
fun floor(numericField: String): Expression
```

Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#floor(kotlin.String)`.

```kotlin
// Compute the floor of the 'price' field.
floor("price")
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the floor operation. |

### greaterThan

```
fun greaterThan(fieldName: String, expression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is greater than an expression.

```kotlin
// Check if the 'age' field is greater than the 'limit' field
greaterThan("age", field("limit"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThan

```
fun greaterThan(fieldName: String, value: Any): BooleanExpression
```

Creates an expression that checks if a field's value is greater than another value.

```kotlin
// Check if the 'price' field is greater than 100
greaterThan("price", 100)
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThan

```
fun greaterThan(left: Expression, right: Any): BooleanExpression
```

Creates an expression that checks if an expression is greater than a value.

```kotlin
// Check if the 'price' field is greater than 100
greaterThan(field("price"), 100)
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThan

```
fun greaterThan(left: Expression, right: Expression): BooleanExpression
```

Creates an expression that checks if the first expression is greater than the second expression.

```kotlin
// Check if the 'age' field is greater than the 'limit' field
greaterThan(field("age"), field("limit"))
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThanOrEqual

```
fun greaterThanOrEqual(fieldName: String, expression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is greater than or equal to an expression.

```kotlin
// Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
greaterThanOrEqual("quantity", field("requirement").add(1))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### greaterThanOrEqual

```
fun greaterThanOrEqual(fieldName: String, value: Any): BooleanExpression
```

Creates an expression that checks if a field's value is greater than or equal to another value.

```kotlin
// Check if the 'score' field is greater than or equal to 80
greaterThanOrEqual("score", 80)
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### greaterThanOrEqual

```
fun greaterThanOrEqual(left: Expression, right: Any): BooleanExpression
```

Creates an expression that checks if an expression is greater than or equal to a value.

```kotlin
// Check if the 'score' field is greater than or equal to 80
greaterThanOrEqual(field("score"), 80)
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### greaterThanOrEqual

```
fun greaterThanOrEqual(left: Expression, right: Expression): BooleanExpression
```

Creates an expression that checks if the first expression is greater than or equal to the second expression.

```kotlin
// Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
greaterThanOrEqual(field("quantity"), field("requirement").add(1))
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### ifAbsent

```
fun ifAbsent(ifExpr: Expression, elseExpr: Expression): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation.

```kotlin
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
ifAbsent(field("optional_field"), "default_value")
```

| Parameters |
|---|---|
| `ifExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check for absence. |
| `elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that will be evaluated and returned if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is absent. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifAbsent

```
fun ifAbsent(ifExpr: Expression, elseValue: Any): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` is absent, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation.

```kotlin
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
ifAbsent(field("optional_field"), "default_value")
```

| Parameters |
|---|---|
| `ifExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check for absence. |
| `elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value that will be returned if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` is absent. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifAbsent

```
fun ifAbsent(ifFieldName: String, elseExpr: Expression): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the value of the field.

```kotlin
// Returns the value of the optional field 'optional_field', or returns the value of
// 'default_field' if 'optional_field' is absent.
ifAbsent("optional_field", field("default_field"))
```

| Parameters |
|---|---|
| `ifFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to check for absence. |
| `elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that will be evaluated and returned if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is absent. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifAbsent

```
fun ifAbsent(ifFieldName: String, elseValue: Any): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` is absent, else return the value of the field.

```kotlin
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
ifAbsent("optional_field", "default_value")
```

| Parameters |
|---|---|
| `ifFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to check for absence. |
| `elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value that will be returned if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` is absent. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifError

```
fun ifError(tryExpr: BooleanExpression, catchExpr: BooleanExpression): BooleanExpression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument evaluation.

This overload will return `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` when both parameters are also `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`.

```kotlin
// Returns the result of the boolean expression, or false if it errors.
ifError(field("is_premium"), false)
```

| Parameters |
|---|---|
| `tryExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The try boolean expression. |
| `catchExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The catch boolean expression that will be evaluated and returned if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` produces an error. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the ifError operation. |

### ifError

```
fun ifError(tryExpr: Expression, catchExpr: Expression): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation.

```kotlin
// Returns the first item in the title field arrays, or returns
// the entire title field if the array is empty or the field is another type.
ifError(arrayGet(field("title"), 0), field("title"))
```

| Parameters |
|---|---|
| `tryExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The try expression. |
| `catchExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The catch expression that will be evaluated and returned if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` produces an error. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifError operation. |

### ifError

```
fun ifError(tryExpr: Expression, catchValue: Any): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation.

```kotlin
// Returns the first item in the title field arrays, or returns "Default Title"
ifError(arrayGet(field("title"), 0), "Default Title")
```

| Parameters |
|---|---|
| `tryExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The try expression. |
| `catchValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value that will be returned if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` produces an error. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifError operation. |

### isAbsent

```
fun isAbsent(fieldName: String): BooleanExpression
```

Creates an expression that returns true if a field is absent. Otherwise, returns false even if the field value is null.

```kotlin
// Check if the field `value` is absent.
isAbsent("value")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to check. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the isAbsent operation. |

### isAbsent

```
fun isAbsent(value: Expression): BooleanExpression
```

Creates an expression that returns true if a value is absent. Otherwise, returns false even if the value is null.

```kotlin
// Check if the field `value` is absent.
isAbsent(field("value"))
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the isAbsent operation. |

### isError

```
fun isError(expr: Expression): BooleanExpression
```

Creates an expression that checks if a given expression produces an error.

```kotlin
// Check if the result of a calculation is an error
isError(arrayContains(field("title"), 1))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the `isError` check. |

### join

```
fun join(arrayExpression: Expression, delimiter: String): Expression
```

Creates an expression that joins the elements of an array into a string.

```kotlin
// Join the elements of the 'tags' field with a comma and space.
join(field("tags"), ", ")
```

| Parameters |
|---|---|
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that evaluates to an array. |
| `delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string to use as a delimiter. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### join

```
fun join(arrayExpression: Expression, delimiterExpression: Expression): Expression
```

Creates an expression that joins the elements of an array into a string.

```kotlin
// Join the elements of the 'tags' field with the delimiter from the 'separator' field.
join(field("tags"), field("separator"))
```

| Parameters |
|---|---|
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that evaluates to an array. |
| `delimiterExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that evaluates to the delimiter string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### join

```
fun join(arrayFieldName: String, delimiter: String): Expression
```

Creates an expression that joins the elements of an array field into a string.

```kotlin
// Join the elements of the 'tags' field with a comma and space.
join("tags", ", ")
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the array. |
| `delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string to use as a delimiter. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### join

```
fun join(arrayFieldName: String, delimiterExpression: Expression): Expression
```

Creates an expression that joins the elements of an array field into a string.

```kotlin
// Join the elements of the 'tags' field with the delimiter from the 'separator' field.
join("tags", field("separator"))
```

| Parameters |
|---|---|
| `arrayFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the array. |
| `delimiterExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that evaluates to the delimiter string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### length

```
fun length(expr: Expression): Expression
```

Creates an expression that calculates the length of a string, array, map, vector, or blob expression.

```kotlin
// Get the length of the 'value' field where the value type can be any of a string, array, map, vector or blob.
length(field("value"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length operation. |

### length

```
fun length(fieldName: String): Expression
```

Creates an expression that calculates the length of a string, array, map, vector, or blob field.

```kotlin
// Get the length of the 'value' field where the value type can be any of a string, array, map, vector or blob.
charLength("value")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length operation. |

### lessThan

```
fun lessThan(fieldName: String, expression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is less than an expression.

```kotlin
// Check if the 'age' field is less than 'limit'
lessThan("age", field("limit"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThan

```
fun lessThan(fieldName: String, value: Any): BooleanExpression
```

Creates an expression that checks if a field's value is less than another value.

```kotlin
// Check if the 'price' field is less than 50
lessThan("price", 50)
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThan

```
fun lessThan(left: Expression, right: Any): BooleanExpression
```

Creates an expression that checks if an expression is less than a value.

```kotlin
// Check if the 'price' field is less than 50
lessThan(field("price"), 50)
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThan

```
fun lessThan(left: Expression, right: Expression): BooleanExpression
```

Creates an expression that checks if the first expression is less than the second expression.

```kotlin
// Check if the 'age' field is less than 'limit'
lessThan(field("age"), field("limit"))
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThanOrEqual

```
fun lessThanOrEqual(fieldName: String, expression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is less than or equal to an expression.

```kotlin
// Check if the 'quantity' field is less than or equal to 20
lessThanOrEqual("quantity", constant(20))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### lessThanOrEqual

```
fun lessThanOrEqual(fieldName: String, value: Any): BooleanExpression
```

Creates an expression that checks if a field's value is less than or equal to another value.

```kotlin
// Check if the 'score' field is less than or equal to 70
lessThanOrEqual("score", 70)
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### lessThanOrEqual

```
fun lessThanOrEqual(left: Expression, right: Any): BooleanExpression
```

Creates an expression that checks if an expression is less than or equal to a value.

```kotlin
// Check if the 'score' field is less than or equal to 70
lessThanOrEqual(field("score"), 70)
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### lessThanOrEqual

```
fun lessThanOrEqual(left: Expression, right: Expression): BooleanExpression
```

Creates an expression that checks if the first expression is less than or equal to the second expression.

```kotlin
// Check if the 'quantity' field is less than or equal to 20
lessThanOrEqual(field("quantity"), constant(20))
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### like

```
fun like(fieldName: String, pattern: Expression): BooleanExpression
```

Creates an expression that performs a case-sensitive wildcard string comparison against a field.

```kotlin
// Check if the 'title' field contains the string "guide"
like("title", "%guide%")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like comparison. |

### like

```
fun like(fieldName: String, pattern: String): BooleanExpression
```

Creates an expression that performs a case-sensitive wildcard string comparison against a field.

```kotlin
// Check if the 'title' field contains the string "guide"
like("title", "%guide%")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like comparison. |

### like

```
fun like(stringExpression: Expression, pattern: Expression): BooleanExpression
```

Creates an expression that performs a case-sensitive wildcard string comparison.

```kotlin
// Check if the 'title' field contains the string "guide"
like(field("title"), "%guide%")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to perform the comparison on. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like operation. |

### like

```
fun like(stringExpression: Expression, pattern: String): BooleanExpression
```

Creates an expression that performs a case-sensitive wildcard string comparison.

```kotlin
// Check if the 'title' field contains the string "guide"
like(field("title"), "%guide%")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to perform the comparison on. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like operation. |

### ln

```
fun ln(numericExpr: Expression): Expression
```

Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ln(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Compute the natural logarithm of the 'value' field.
ln(field("value"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the natural logarithm. |

### ln

```
fun ln(numericField: String): Expression
```

Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#ln(kotlin.String)`.

```kotlin
// Compute the natural logarithm of the 'value' field.
ln("value")
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the natural logarithm. |

### log

```
fun log(numericExpr: Expression, base: Expression): Expression
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Compute the logarithm of the 'value' field with the base in the 'base' field.
log(field("value"), field("base"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |
| `base: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The base of the logarithm. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |

### log

```
fun log(numericExpr: Expression, base: Number): Expression
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`.

```kotlin
// Compute the logarithm of the 'value' field with base 10.
log(field("value"), 10)
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |
| `base: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The base of the logarithm. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |

### log

```
fun log(numericField: String, base: Expression): Expression
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Compute the logarithm of the 'value' field with the base in the 'base' field.
log("value", field("base"))
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |
| `base: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The base of the logarithm. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |

### log

```
fun log(numericField: String, base: Number): Expression
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)`.

```kotlin
// Compute the logarithm of the 'value' field with base 10.
log("value", 10)
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |
| `base: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The base of the logarithm. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)`. |

### log10

```
fun log10(numericExpr: Expression): Expression
```

Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log10(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Compute the base 10 logarithm of the 'value' field.
log10(field("value"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the base 10 logarithm. |

### log10

```
fun log10(numericField: String): Expression
```

Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#log10(kotlin.String)`.

```kotlin
// Compute the base 10 logarithm of the 'value' field.
log10("value")
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the base 10 logarithm. |

### logicalMaximum

```
fun logicalMaximum(expr: Expression, vararg others: Any): Expression
```

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the larger value between the 'timestamp' field and the current timestamp.
logicalMaximum(field("timestamp"), currentTimestamp())
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first operand expression. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical maximum operation. |

### logicalMaximum

```
fun logicalMaximum(fieldName: String, vararg others: Any): Expression
```

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the larger value between the 'timestamp' field and the current timestamp.
logicalMaximum("timestamp", currentTimestamp())
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The first operand field name. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical maximum operation. |

### logicalMinimum

```
fun logicalMinimum(expr: Expression, vararg others: Any): Expression
```

Creates an expression that returns the smallest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the smaller value between the 'timestamp' field and the current timestamp.
logicalMinimum(field("timestamp"), currentTimestamp())
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first operand expression. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical minimum operation. |

### logicalMinimum

```
fun logicalMinimum(fieldName: String, vararg others: Any): Expression
```

Creates an expression that returns the smallest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the smaller value between the 'timestamp' field and the current timestamp.
logicalMinimum("timestamp", currentTimestamp())
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The first operand field name. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical minimum operation. |

### map

```
fun map(elements: Map<String, Any>): Expression
```

Creates an expression that creates a Firestore map value from an input object.

```kotlin
// Create a map with a constant key and a field value
map(mapOf("name" to field("productName"), "quantity" to 1))
```

| Parameters |
|---|---|
| `elements: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The input map to evaluate in the expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the map function. |

### mapGet

```
fun mapGet(fieldName: String, key: String): Expression
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,kotlin.String)`.

```kotlin
// Get the 'city' value from the 'address' map field
mapGet("address", "city")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name of the map field. |
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key to access in the map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapGet

```
fun mapGet(fieldName: String, keyExpression: Expression): Expression
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Get the value from the 'address' map field, using the key from the 'keyField' field
mapGet("address", field("keyField"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name of the map field. |
| `keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The key to access in the map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapGet

```
fun mapGet(mapExpression: Expression, key: String): Expression
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`.

```kotlin
// Get the 'city' value from the 'address' map field
mapGet(field("address"), "city")
```

| Parameters |
|---|---|
| `mapExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the map. |
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key to access in the map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapGet

```
fun mapGet(mapExpression: Expression, keyExpression: Expression): Expression
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Get the value from the 'address' map field, using the key from the 'keyField' field
mapGet(field("address"), field("keyField"))
```

| Parameters |
|---|---|
| `mapExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the map. |
| `keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The key to access in the map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapMerge

```
fun mapMerge(
    firstMap: Expression,
    secondMap: Expression,
    vararg otherMaps: Expression
): Expression
```

Creates an expression that merges multiple maps into a single map. If multiple maps have the same key, the later value is used.

```kotlin
// Merges the map in the settings field with, a map literal, and a map in
// that is conditionally returned by another expression
mapMerge(
  field("settings"),
  map(mapOf("enabled" to true)),
  conditional(
    field("isAdmin").equal(true),
    map(mapOf("admin" to true)),
    map(emptyMap<String, Any>())
  )
)
```

| Parameters |
|---|---|
| `firstMap: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | First map expression that will be merged. |
| `secondMap: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Second map expression that will be merged. |
| `vararg otherMaps: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Additional maps to merge. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the mapMerge operation. |

### mapMerge

```
fun mapMerge(
    firstMapFieldName: String,
    secondMap: Expression,
    vararg otherMaps: Expression
): Expression
```

Creates an expression that merges multiple maps into a single map. If multiple maps have the same key, the later value is used.

```kotlin
// Merges the map in the settings field with, a map literal, and a map in
// that is conditionally returned by another expression
mapMerge(
  "settings",
  map(mapOf("enabled" to true)),
  conditional(
    field("isAdmin").equal(true),
    map(mapOf("admin" to true)),
    map(emptyMap<String, Any>())
  )
)
```

| Parameters |
|---|---|
| `firstMapFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | First map field name that will be merged. |
| `secondMap: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Second map expression that will be merged. |
| `vararg otherMaps: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Additional maps to merge. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the mapMerge operation. |

### mapRemove

```
fun mapRemove(mapExpr: Expression, key: Expression): Expression
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```kotlin
// Removes the key 'baz' from the input map.
mapRemove(map(mapOf("foo" to "bar", "baz" to true)), constant("baz"))
```

| Parameters |
|---|---|
| `mapExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to a map. |
| `key: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mapRemove

```
fun mapRemove(mapExpr: Expression, key: String): Expression
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```kotlin
// Removes the key 'baz' from the input map.
mapRemove(map(mapOf("foo" to "bar", "baz" to true)), "baz")
```

| Parameters |
|---|---|
| `mapExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to a map. |
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mapRemove

```
fun mapRemove(mapField: String, key: Expression): Expression
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```kotlin
// Removes the key 'city' field from the map in the address field of the input document.
mapRemove("address", constant("city"))
```

| Parameters |
|---|---|
| `mapField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of a field containing a map value. |
| `key: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mapRemove

```
fun mapRemove(mapField: String, key: String): Expression
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```kotlin
// Removes the key 'city' field from the map in the address field of the input document.
mapRemove("address", "city")
```

| Parameters |
|---|---|
| `mapField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of a field containing a map value. |
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mod

```
fun mod(dividend: Expression, divisor: Expression): Expression
```

Creates an expression that calculates the modulo (remainder) of dividing two numeric expressions.

```kotlin
// Calculate the remainder of dividing the 'value' field by the 'divisor' field
mod(field("value"), field("divisor"))
```

| Parameters |
|---|---|
| `dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to be divided. |
| `divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### mod

```
fun mod(dividend: Expression, divisor: Number): Expression
```

Creates an expression that calculates the modulo (remainder) of dividing a numeric expression by a constant.

```kotlin
// Calculate the remainder of dividing the 'value' field by 3.
mod(field("value"), 3)
```

| Parameters |
|---|---|
| `dividend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to be divided. |
| `divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The constant to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### mod

```
fun mod(dividendFieldName: String, divisor: Expression): Expression
```

Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant.

```kotlin
// Calculate the remainder of dividing the 'value' field by the 'divisor' field.
mod("value", field("divisor"))
```

| Parameters |
|---|---|
| `dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The numeric field name to be divided. |
| `divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### mod

```
fun mod(dividendFieldName: String, divisor: Number): Expression
```

Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant.

```kotlin
// Calculate the remainder of dividing the 'value' field by 3.
mod("value", 3)
```

| Parameters |
|---|---|
| `dividendFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The numeric field name to be divided. |
| `divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The constant to divide by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### multiply

```
fun multiply(first: Expression, second: Expression): Expression
```

Creates an expression that multiplies numeric expressions.

```kotlin
// Multiply the 'quantity' field by the 'price' field
multiply(field("quantity"), field("price"))
```

| Parameters |
|---|---|
| `first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to multiply. |
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to multiply. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### multiply

```
fun multiply(first: Expression, second: Number): Expression
```

Creates an expression that multiplies numeric expressions with a constant.

```kotlin
// Multiply the 'quantity' field by 1.1.
multiply(field("quantity"), 1.1)
```

| Parameters |
|---|---|
| `first: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to multiply. |
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to multiply. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### multiply

```
fun multiply(numericFieldName: String, second: Expression): Expression
```

Creates an expression that multiplies a numeric field with a numeric expression.

```kotlin
// Multiply the 'quantity' field by the 'price' field.
multiply("quantity", field("price"))
```

| Parameters |
|---|---|
| `numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Numeric field to multiply. |
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to multiply. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### multiply

```
fun multiply(numericFieldName: String, second: Number): Expression
```

Creates an expression that multiplies a numeric field with a constant.

```kotlin
// Multiply the 'quantity' field by 1.1.
multiply("quantity", 1.1)
```

| Parameters |
|---|---|
| `numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Numeric field to multiply. |
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to multiply. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### not

```
fun not(condition: BooleanExpression): BooleanExpression
```

Creates an expression that negates a boolean expression.

```kotlin
// Check if 'is_admin' is not true
not(field("is_admin"))
```

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The boolean expression to negate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the not operation. |

### notEqual

```
fun notEqual(fieldName: String, expression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is not equal to an expression.

```kotlin
// Check if the 'status' field is not equal to the value of the 'otherStatus' field
notEqual("status", field("otherStatus"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqual

```
fun notEqual(fieldName: String, value: Any): BooleanExpression
```

Creates an expression that checks if a field's value is not equal to another value.

```kotlin
// Check if the 'status' field is not equal to "completed"
notEqual("status", "completed")

// Check if the 'country' field is not equal to "USA"
notEqual("country", "USA")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name to compare. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqual

```
fun notEqual(left: Expression, right: Any): BooleanExpression
```

Creates an expression that checks if an expression is not equal to a value.

```kotlin
// Check if the 'status' field is not equal to "completed"
notEqual(field("status"), "completed")
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqual

```
fun notEqual(left: Expression, right: Expression): BooleanExpression
```

Creates an expression that checks if two expressions are not equal.

```kotlin
// Check if the 'status' field is not equal to the value of the 'otherStatus' field
notEqual(field("status"), field("otherStatus"))
```

| Parameters |
|---|---|
| `left: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The first expression to compare. |
| `right: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqualAny

```
fun notEqualAny(expression: Expression, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is not equal to all the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'status' field is not in the 'inactiveStatuses' array field.
notEqualAny(field("status"), field("inactiveStatuses"))
```

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression whose results to compare. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### notEqualAny

```
fun notEqualAny(expression: Expression, values: List<Any>): BooleanExpression
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is not equal to all the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```kotlin
// Check if the 'status' field is neither "pending" nor the value of the 'rejectedStatus' field.
notEqualAny(field("status"), listOf("pending", field("rejectedStatus")))
```

| Parameters |
|---|---|
| `expression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression whose results to compare. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The values to check against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### notEqualAny

```
fun notEqualAny(fieldName: String, arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if a field's value is not equal to all of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'status' field is not in the 'inactiveStatuses' array field.
notEqualAny("status", field("inactiveStatuses"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to compare. |
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### notEqualAny

```
fun notEqualAny(fieldName: String, values: List<Any>): BooleanExpression
```

Creates an expression that checks if a field's value is not equal to all of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,kotlin.collections.List)`.

```kotlin
// Check if the 'status' field is not "archived" or "deleted".
notEqualAny("status", listOf("archived", "deleted"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field to compare. |
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The values to check against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### nullValue

```
fun nullValue(): Expression
```

Constant for a null value.

```kotlin
// Create a null constant
nullValue()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### or

```
fun or(condition: BooleanExpression, vararg conditions: BooleanExpression): BooleanExpression
```

Creates an expression that performs a logical 'OR' operation.

```kotlin
// Check if 'status' is "new" or "open"
or(field("status").equal("new"), field("status").equal("open"))
```

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`. |
| `vararg conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | Additional `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`s. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the logical 'OR' operation. |

### pow

```
fun pow(numericExpr: Expression, exponent: Expression): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. Returns infinity on overflow and zero on underflow.

```kotlin
// Raise the value of the 'base' field to the power of the 'exponent' field.
pow(field("base"), field("exponent"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |
| `exponent: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric power to raise the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |

### pow

```
fun pow(numericExpr: Expression, exponent: Number): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. Returns infinity on overflow and zero on underflow.

```kotlin
// Raise the value of the 'base' field to the power of 2.
pow(field("base"), 2)
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |
| `exponent: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The numeric power to raise the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |

### pow

```
fun pow(numericField: String, exponent: Expression): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. Returns infinity on overflow and zero on underflow.

```kotlin
// Raise the value of the 'base' field to the power of the 'exponent' field.
pow("base", field("exponent"))
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |
| `exponent: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric power to raise the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |

### pow

```
fun pow(numericField: String, exponent: Number): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. Returns infinity on overflow and zero on underflow.

```kotlin
// Raise the value of the 'base' field to the power of 2.
pow("base", 2)
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |
| `exponent: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The numeric power to raise the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)` to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. |

### rawFunction

```
fun rawFunction(name: String, vararg expr: Expression): Expression
```

Creates a 'raw' function expression. This is useful if the expression is available in the backend, but not yet in the current version of the SDK yet.

```kotlin
// Create a generic function call
rawFunction("my_function", field("arg1"), constant(42))
```

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the raw function. |
| `vararg expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expressions to be passed as arguments to the function. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the raw function. |

### regexContains

```
fun regexContains(fieldName: String, pattern: Expression): BooleanExpression
```

Creates an expression that checks if a string field contains a specified regular expression as a substring.

```kotlin
// Check if the 'description' field contains the regex from the 'pattern' field.
regexContains("description", field("pattern"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to use for the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexContains

```
fun regexContains(fieldName: String, pattern: String): BooleanExpression
```

Creates an expression that checks if a string field contains a specified regular expression as a substring.

```kotlin
// Check if the 'description' field contains "example" (case-insensitive)
regexContains("description", "(?i)example")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to use for the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexContains

```
fun regexContains(stringExpression: Expression, pattern: Expression): BooleanExpression
```

Creates an expression that checks if a string expression contains a specified regular expression as a substring.

```kotlin
// Check if the 'description' field contains "example" (case-insensitive)
regexContains(field("description"), "(?i)example")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to perform the comparison on. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to use for the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexContains

```
fun regexContains(stringExpression: Expression, pattern: String): BooleanExpression
```

Creates an expression that checks if a string expression contains a specified regular expression as a substring.

```kotlin
// Check if the 'description' field contains "example" (case-insensitive)
regexContains(field("description"), "(?i)example")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to perform the comparison on. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to use for the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexFind

```
fun regexFind(fieldName: String, pattern: Expression): Expression
```

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract a substring from 'email' based on a pattern stored in another field
regexFind("email", field("pattern"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to search. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFind

```
fun regexFind(fieldName: String, pattern: String): Expression
```

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract the domain name from an email field
regexFind("email", "@[A-Za-z0-9.-]+")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to search. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFind

```
fun regexFind(stringExpression: Expression, pattern: Expression): Expression
```

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract a substring based on a dynamic pattern field
regexFind(field("email"), field("pattern"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to search. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFind

```
fun regexFind(stringExpression: Expression, pattern: String): Expression
```

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract the domain from a lower-cased email address
regexFind(field("email"), "@[A-Za-z0-9.-]+")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to search. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFindAll

```
fun regexFindAll(fieldName: String, pattern: Expression): Expression
```

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract all matches from 'content' based on a pattern stored in another field
regexFindAll("content", field("pattern"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to search. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexFindAll

```
fun regexFindAll(fieldName: String, pattern: String): Expression
```

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract all hashtags from a post content field
regexFindAll("content", "#[A-Za-z0-9_]+")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to search. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexFindAll

```
fun regexFindAll(stringExpression: Expression, pattern: Expression): Expression
```

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract all matches based on a dynamic pattern expression
regexFindAll(field("comment"), field("pattern"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to search. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexFindAll

```
fun regexFindAll(stringExpression: Expression, pattern: String): Expression
```

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```kotlin
// Extract all mentions from a lower-cased comment
regexFindAll(field("comment"), "@[A-Za-z0-9_]+")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to search. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexMatch

```
fun regexMatch(fieldName: String, pattern: Expression): BooleanExpression
```

Creates an expression that checks if a string field matches a specified regular expression.

```kotlin
// Check if the 'email' field matches the regex from the 'pattern' field.
regexMatch("email", field("pattern"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to use for the match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### regexMatch

```
fun regexMatch(fieldName: String, pattern: String): BooleanExpression
```

Creates an expression that checks if a string field matches a specified regular expression.

```kotlin
// Check if the 'email' field matches a valid email pattern
regexMatch("email", "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to use for the match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### regexMatch

```
fun regexMatch(stringExpression: Expression, pattern: Expression): BooleanExpression
```

Creates an expression that checks if a string field matches a specified regular expression.

```kotlin
// Check if the 'email' field matches a valid email pattern
regexMatch(field("email"), "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to match against. |
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to use for the match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### regexMatch

```
fun regexMatch(stringExpression: Expression, pattern: String): BooleanExpression
```

Creates an expression that checks if a string field matches a specified regular expression.

```kotlin
// Check if the 'email' field matches a valid email pattern
regexMatch(field("email"), "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to match against. |
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to use for the match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### reverse

```
fun reverse(fieldName: String): Expression
```

Creates an expression that reverses a string value from the specified field.

```kotlin
// Reverse the value of the 'myString' field.
reverse("myString")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the string to reverse. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the reversed string. |

### reverse

```
fun reverse(stringExpression: Expression): Expression
```

Creates an expression that reverses a string.

```kotlin
// Reverse the value of the 'myString' field.
reverse(field("myString"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression evaluating to a string value, which will be reversed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the reversed string. |

### round

```
fun round(numericExpr: Expression): Expression
```

Creates an expression that rounds `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#round(com.google.firebase.firestore.pipeline.Expression)` to nearest integer.

```kotlin
// Round the value of the 'price' field.
round(field("price"))
```

Rounds away from zero in halfway cases.

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the round operation. |

### round

```
fun round(numericField: String): Expression
```

Creates an expression that rounds `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#round(kotlin.String)` to nearest integer.

```kotlin
// Round the value of the 'price' field.
round("price")
```

Rounds away from zero in halfway cases.

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the round operation. |

### roundToPrecision

```
fun roundToPrecision(numericExpr: Expression, decimalPlace: Expression): Expression
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is negative. Rounds away from zero in halfway cases.

```kotlin
// Round the value of the 'price' field to the number of decimal places specified in the
// 'precision' field.
roundToPrecision(field("price"), field("precision"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |
| `decimalPlace: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of decimal places to round. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### roundToPrecision

```
fun roundToPrecision(numericExpr: Expression, decimalPlace: Int): Expression
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is negative. Rounds away from zero in halfway cases.

```kotlin
// Round the value of the 'price' field to 2 decimal places.
roundToPrecision(field("price"), 2)
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |
| `decimalPlace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of decimal places to round. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### roundToPrecision

```
fun roundToPrecision(numericField: String, decimalPlace: Expression): Expression
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is negative. Rounds away from zero in halfway cases.

```kotlin
// Round the value of the 'price' field to the number of decimal places specified in the
// 'precision' field.
roundToPrecision("price", field("precision"))
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |
| `decimalPlace: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of decimal places to round. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### roundToPrecision

```
fun roundToPrecision(numericField: String, decimalPlace: Int): Expression
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is negative. Rounds away from zero in halfway cases.

```kotlin
// Round the value of the 'price' field to 2 decimal places.
roundToPrecision("price", 2)
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |
| `decimalPlace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of decimal places to round. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### split

```
fun split(fieldName: String, delimiter: Blob): Expression
```

Creates an expression that splits a blob field by a blob delimiter.

```kotlin
// Split the 'data' field by a delimiter
split("data", Blob.fromBytes(byteArrayOf(0x0a)))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the blob to be split. |
| `delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` | The blob delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
fun split(fieldName: String, delimiter: Expression): Expression
```

Creates an expression that splits a string or blob field by a delimiter.

```kotlin
// Split the 'tags' field by the value of the 'delimiter' field
split("tags", field("delimiter"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string or blob to be split. |
| `delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
fun split(fieldName: String, delimiter: String): Expression
```

Creates an expression that splits a string or blob field by a string delimiter.

```kotlin
// Split the 'tags' field by a comma
split("tags", ",")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string or blob to be split. |
| `delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
fun split(value: Expression, delimiter: Blob): Expression
```

Creates an expression that splits a blob by a blob delimiter.

```kotlin
// Split the 'data' field by a delimiter
split(field("data"), Blob.fromBytes(byteArrayOf(0x0a)))
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression evaluating to a blob to be split. |
| `delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` | The blob delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
fun split(value: Expression, delimiter: Expression): Expression
```

Creates an expression that splits a string or blob by a delimiter.

```kotlin
// Split the 'tags' field by a comma
split(field("tags"), field("delimiter"))
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression evaluating to a string or blob to be split. |
| `delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The delimiter to split by. Must be of the same type as `value`. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
fun split(value: Expression, delimiter: String): Expression
```

Creates an expression that splits a string or blob by a string delimiter.

```kotlin
// Split the 'tags' field by a comma
split(field("tags"), ",")
```

| Parameters |
|---|---|
| `value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression evaluating to a string or blob to be split. |
| `delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### sqrt

```
fun sqrt(numericExpr: Expression): Expression
```

Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Compute the square root of the 'value' field.
sqrt(field("value"))
```

| Parameters |
|---|---|
| `numericExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the square root operation. |

### sqrt

```
fun sqrt(numericField: String): Expression
```

Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(kotlin.String)`.

```kotlin
// Compute the square root of the 'value' field.
sqrt("value")
```

| Parameters |
|---|---|
| `numericField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the square root operation. |

### startsWith

```
fun startsWith(fieldName: String, prefix: Expression): BooleanExpression
```

Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'fullName' field starts with the value of the 'firstName' field
startsWith("fullName", field("firstName"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains a string to check. |
| `prefix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The prefix string expression to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### startsWith

```
fun startsWith(fieldName: String, prefix: String): BooleanExpression
```

Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,kotlin.String)`.

```kotlin
// Check if the 'name' field starts with "Mr."
startsWith("name", "Mr.")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains a string to check. |
| `prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The prefix string to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### startsWith

```
fun startsWith(stringExpr: Expression, prefix: Expression): BooleanExpression
```

```kotlin
// Check if the 'fullName' field starts with the value of the 'firstName' field
startsWith(field("fullName"), field("firstName"))
```

| Parameters |
|---|---|
| `stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check. |
| `prefix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The prefix string expression to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### startsWith

```
fun startsWith(stringExpr: Expression, prefix: String): BooleanExpression
```

Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`.

```kotlin
// Check if the 'name' field starts with "Mr."
startsWith(field("name"), "Mr.")
```

| Parameters |
|---|---|
| `stringExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to check. |
| `prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The prefix string to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### stringConcat

```
fun stringConcat(fieldName: String, vararg otherStrings: Any): Expression
```

Creates an expression that concatenates string expressions together.

```kotlin
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat("firstName", " ", "lastName")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name containing the initial string value. |
| `vararg otherStrings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional string expressions or string constants to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
fun stringConcat(fieldName: String, vararg otherStrings: Expression): Expression
```

Creates an expression that concatenates string expressions together.

```kotlin
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat("firstName", constant(" "), field("lastName"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The field name containing the initial string value. |
| `vararg otherStrings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Optional additional string expressions to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
fun stringConcat(firstString: Expression, vararg otherStrings: Any): Expression
```

Creates an expression that concatenates string expressions together.

```kotlin
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat(field("firstName"), " ", field("lastName"))
```

| Parameters |
|---|---|
| `firstString: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the initial string value. |
| `vararg otherStrings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional string expressions or string constants to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
fun stringConcat(firstString: Expression, vararg otherStrings: Expression): Expression
```

Creates an expression that concatenates string expressions together.

```kotlin
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat(field("firstName"), constant(" "), field("lastName"))
```

| Parameters |
|---|---|
| `firstString: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the initial string value. |
| `vararg otherStrings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Optional additional string expressions to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringContains

```
fun stringContains(fieldName: String, substring: Expression): BooleanExpression
```

Creates an expression that checks if a string field contains a specified substring.

```kotlin
// Check if the 'description' field contains the value of the 'keyword' field.
stringContains("description", field("keyword"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to perform the comparison on. |
| `substring: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the substring to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringContains

```
fun stringContains(fieldName: String, substring: String): BooleanExpression
```

Creates an expression that checks if a string field contains a specified substring.

```kotlin
// Check if the 'description' field contains "example".
stringContains("description", "example")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to perform the comparison on. |
| `substring: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The substring to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringContains

```
fun stringContains(stringExpression: Expression, substring: Expression): BooleanExpression
```

Creates an expression that checks if a string expression contains a specified substring.

```kotlin
// Check if the 'description' field contains the value of the 'keyword' field.
stringContains(field("description"), field("keyword"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to perform the comparison on. |
| `substring: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the substring to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringContains

```
fun stringContains(stringExpression: Expression, substring: String): BooleanExpression
```

Creates an expression that checks if a string expression contains a specified substring.

```kotlin
// Check if the 'description' field contains "example".
stringContains(field("description"), "example")
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to perform the comparison on. |
| `substring: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The substring to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringReverse

```
fun stringReverse(fieldName: String): Expression
```

Reverses the given string field.

```kotlin
// Reverse the value of the 'myString' field.
stringReverse("myString")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field that contains the string to reverse. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the stringReverse operation. |

### stringReverse

```
fun stringReverse(str: Expression): Expression
```

Reverses the given string expression.

```kotlin
// Reverse the value of the 'myString' field.
stringReverse(field("myString"))
```

| Parameters |
|---|---|
| `str: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The string expression to reverse. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the stringReverse operation. |

### substring

```
fun substring(fieldName: String, index: Int, length: Int): Expression
```

Creates an expression that returns a substring of the given string.

```kotlin
// Get a substring of the 'message' field starting at index 5 with length 10.
substring("message", 5, 10)
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to get a substring from. |
| `index: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The starting index of the substring. |
| `length: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The length of the substring. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the substring. |

### substring

```
fun substring(
    stringExpression: Expression,
    index: Expression,
    length: Expression
): Expression
```

Creates an expression that returns a substring of the given string.

```kotlin
// Get a substring of the 'message' field starting at index 5 with length 10.
substring(field("message"), constant(5), constant(10))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to get a substring from. |
| `index: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The starting index of the substring. |
| `length: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The length of the substring. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the substring. |

### subtract

```
fun subtract(minuend: Expression, subtrahend: Expression): Expression
```

Creates an expression that subtracts two expressions.

```kotlin
// Subtract the 'discount' field from the 'price' field
subtract(field("price"), field("discount"))
```

| Parameters |
|---|---|
| `minuend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to subtract from. |
| `subtrahend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### subtract

```
fun subtract(minuend: Expression, subtrahend: Number): Expression
```

Creates an expression that subtracts a constant value from a numeric expression.

```kotlin
// Subtract 10 from the 'price' field.
subtract(field("price"), 10)
```

| Parameters |
|---|---|
| `minuend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to subtract from. |
| `subtrahend: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### subtract

```
fun subtract(numericFieldName: String, subtrahend: Expression): Expression
```

Creates an expression that subtracts a numeric expressions from numeric field.

```kotlin
// Subtract the 'discount' field from the 'price' field.
subtract("price", field("discount"))
```

| Parameters |
|---|---|
| `numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Numeric field to subtract from. |
| `subtrahend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### subtract

```
fun subtract(numericFieldName: String, subtrahend: Number): Expression
```

Creates an expression that subtracts a constant from numeric field.

```kotlin
// Subtract 10 from the 'price' field.
subtract("price", 10)
```

| Parameters |
|---|---|
| `numericFieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Numeric field to subtract from. |
| `subtrahend: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### timestampAdd

```
fun timestampAdd(fieldName: String, unit: Expression, amount: Expression): Expression
```

Creates an expression that adds a specified amount of time to a timestamp.

```kotlin
// Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
timestampAdd("timestamp", field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the timestamp. |
| `unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the amount of time to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampAdd

```
fun timestampAdd(fieldName: String, unit: String, amount: Long): Expression
```

Creates an expression that adds a specified amount of time to a timestamp.

```kotlin
// Add 1 day to the 'timestamp' field.
timestampAdd("timestamp", "day", 1)
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the timestamp. |
| `unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The amount of time to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampAdd

```
fun timestampAdd(timestamp: Expression, unit: Expression, amount: Expression): Expression
```

Creates an expression that adds a specified amount of time to a timestamp.

```kotlin
// Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
timestampAdd(field("timestamp"), field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the timestamp. |
| `unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the amount of time to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampAdd

```
fun timestampAdd(timestamp: Expression, unit: String, amount: Long): Expression
```

Creates an expression that adds a specified amount of time to a timestamp.

```kotlin
// Add 1 day to the 'timestamp' field.
timestampAdd(field("timestamp"), "day", 1)
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the timestamp. |
| `unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The amount of time to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
fun timestampSubtract(fieldName: String, unit: Expression, amount: Expression): Expression
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```kotlin
// Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
timestampSubtract("timestamp", field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the timestamp. |
| `unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The amount of time to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
fun timestampSubtract(fieldName: String, unit: String, amount: Long): Expression
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```kotlin
// Subtract 1 day from the 'timestamp' field.
timestampSubtract("timestamp", "day", 1)
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the timestamp. |
| `unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The amount of time to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
fun timestampSubtract(
    timestamp: Expression,
    unit: Expression,
    amount: Expression
): Expression
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```kotlin
// Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
timestampSubtract(field("timestamp"), field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the timestamp. |
| `unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the amount of time to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
fun timestampSubtract(timestamp: Expression, unit: String, amount: Long): Expression
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```kotlin
// Subtract 1 day from the 'timestamp' field.
timestampSubtract(field("timestamp"), "day", 1)
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the timestamp. |
| `unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The amount of time to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampToUnixMicros

```
fun timestampToUnixMicros(expr: Expression): Expression
```

Creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to microseconds since epoch.
timestampToUnixMicros(field("timestamp"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the timestamp. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of microseconds since epoch. |

### timestampToUnixMicros

```
fun timestampToUnixMicros(fieldName: String): Expression
```

Creates an expression that converts a timestamp field to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to microseconds since epoch.
timestampToUnixMicros("timestamp")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the timestamp. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of microseconds since epoch. |

### timestampToUnixMillis

```
fun timestampToUnixMillis(expr: Expression): Expression
```

Creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to milliseconds since epoch.
timestampToUnixMillis(field("timestamp"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the timestamp. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of milliseconds since epoch. |

### timestampToUnixMillis

```
fun timestampToUnixMillis(fieldName: String): Expression
```

Creates an expression that converts a timestamp field to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to milliseconds since epoch.
timestampToUnixMillis("timestamp")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the timestamp. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of milliseconds since epoch. |

### timestampToUnixSeconds

```
fun timestampToUnixSeconds(expr: Expression): Expression
```

Creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to seconds since epoch.
timestampToUnixSeconds(field("timestamp"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the timestamp. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of seconds since epoch. |

### timestampToUnixSeconds

```
fun timestampToUnixSeconds(fieldName: String): Expression
```

Creates an expression that converts a timestamp field to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to seconds since epoch.
timestampToUnixSeconds("timestamp")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field that contains the timestamp. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of seconds since epoch. |

### timestampTruncate

```
fun timestampTruncate(fieldName: String, granularity: Expression): Expression
```

Creates an expression that truncates a timestamp to a specified granularity.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate("createdAt", field("granularity"))
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the timestamp. |
| `granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(fieldName: String, granularity: String): Expression
```

Creates an expression that truncates a timestamp to a specified granularity.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate("createdAt", "day")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the timestamp. |
| `granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(timestamp: Expression, granularity: Expression): Expression
```

Creates an expression that truncates a timestamp to a specified granularity.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate(field("createdAt"), field("granularity"))
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The timestamp expression. |
| `granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(timestamp: Expression, granularity: String): Expression
```

Creates an expression that truncates a timestamp to a specified granularity.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate(field("createdAt"), "day")
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The timestamp expression. |
| `granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(
    fieldName: String,
    granularity: Expression,
    timezone: String
): Expression
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate("createdAt", field("granularity"), "America/Los_Angeles")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the timestamp. |
| `granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(fieldName: String, granularity: String, timezone: String): Expression
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate("createdAt", "day", "America/Los_Angeles")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the timestamp. |
| `granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(
    timestamp: Expression,
    granularity: Expression,
    timezone: String
): Expression
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate(field("createdAt"), field("granularity"), "America/Los_Angeles")
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The timestamp expression. |
| `granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(
    timestamp: Expression,
    granularity: String,
    timezone: String
): Expression
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate(field("createdAt"), "day", "America/Los_Angeles")
```

| Parameters |
|---|---|
| `timestamp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The timestamp expression. |
| `granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `timezone: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### toLower

```
fun toLower(fieldName: String): Expression
```

Creates an expression that converts a string field to lowercase.

```kotlin
// Convert the 'name' field to lowercase
toLower("name")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to convert to lowercase. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the lowercase string. |

### toLower

```
fun toLower(stringExpression: Expression): Expression
```

Creates an expression that converts a string expression to lowercase.

```kotlin
// Convert the 'name' field to lowercase
toLower(field("name"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to convert to lowercase. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the lowercase string. |

### toUpper

```
fun toUpper(fieldName: String): Expression
```

Creates an expression that converts a string field to uppercase.

```kotlin
// Convert the 'title' field to uppercase
toUpper("title")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to convert to uppercase. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the uppercase string. |

### toUpper

```
fun toUpper(stringExpression: Expression): Expression
```

Creates an expression that converts a string expression to uppercase.

```kotlin
// Convert the 'title' field to uppercase
toUpper(field("title"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to convert to uppercase. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the uppercase string. |

### trim

```
fun trim(fieldName: String): Expression
```

Creates an expression that removes leading and trailing whitespace from a string field.

```kotlin
// Trim whitespace from the 'userInput' field
trim("userInput")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to trim. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trim

```
fun trim(stringExpression: Expression): Expression
```

Creates an expression that removes leading and trailing whitespace from a string expression.

```kotlin
// Trim whitespace from the 'userInput' field
trim(field("userInput"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to trim. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trimValue

```
fun trimValue(fieldName: String, valueToTrim: String): Expression
```

Creates an expression that removes leading and trailing characters from a string field.

```kotlin
// Trim '-', and '_' from the beginning and the end of 'userInput' field
trimValue("userInput", "-_")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the string to trim. |
| `valueToTrim: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | This parameter is treated as a set of characters or bytes that will be matched against the input from both ends. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trimValue

```
fun trimValue(stringExpression: Expression, valueToTrim: Expression): Expression
```

Creates an expression that removes leading and trailing values from a expression. The accepted values types are string and blob.

```kotlin
// Trim specified characters from the 'userInput' field
trimValue(field("userInput"), field("valueToTrim"))
```

| Parameters |
|---|---|
| `stringExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the string to trim. |
| `valueToTrim: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression evaluated to either a string or a blob. This parameter is treated as a set of characters or bytes that will be matched against the input from both ends. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string or bytes. |

### type

```
fun type(expr: Expression): Expression
```

Creates an expression that returns a string indicating the type of the value this expression evaluates to.

```kotlin
// Get the type of the 'value' field.
type(field("value"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to get the type of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the type operation. |

### type

```
fun type(fieldName: String): Expression
```

Creates an expression that returns a string indicating the type of the value this field evaluates to.

```kotlin
// Get the type of the 'field' field.
type("field")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field to get the type of. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the type operation. |

### unixMicrosToTimestamp

```
fun unixMicrosToTimestamp(expr: Expression): Expression
```

Creates an expression that interprets an expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'microseconds' field as microseconds since epoch.
unixMicrosToTimestamp(field("microseconds"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the number of microseconds since epoch. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixMicrosToTimestamp

```
fun unixMicrosToTimestamp(fieldName: String): Expression
```

Creates an expression that interprets a field's value as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'microseconds' field as microseconds since epoch.
unixMicrosToTimestamp("microseconds")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the number of microseconds since epoch. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixMillisToTimestamp

```
fun unixMillisToTimestamp(expr: Expression): Expression
```

Creates an expression that interprets an expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'milliseconds' field as milliseconds since epoch.
unixMillisToTimestamp(field("milliseconds"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the number of milliseconds since epoch. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixMillisToTimestamp

```
fun unixMillisToTimestamp(fieldName: String): Expression
```

Creates an expression that interprets a field's value as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'milliseconds' field as milliseconds since epoch.
unixMillisToTimestamp("milliseconds")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the number of milliseconds since epoch. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixSecondsToTimestamp

```
fun unixSecondsToTimestamp(expr: Expression): Expression
```

Creates an expression that interprets an expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'seconds' field as seconds since epoch.
unixSecondsToTimestamp(field("seconds"))
```

| Parameters |
|---|---|
| `expr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the number of seconds since epoch. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixSecondsToTimestamp

```
fun unixSecondsToTimestamp(fieldName: String): Expression
```

Creates an expression that interprets a field's value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'seconds' field as seconds since epoch.
unixSecondsToTimestamp("seconds")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the number of seconds since epoch. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### vector

```
fun vector(vector: DoubleArray): Expression
```

Create a vector constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` value.

```kotlin
// Create a vector constant from a DoubleArray
vector(doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### vector

```
fun vector(vector: VectorValue): Expression
```

Create a vector constant for a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` value.

```kotlin
// Create a vector constant from a VectorValue
vector(VectorValue(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` value. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### vectorLength

```
fun vectorLength(fieldName: String): Expression
```

Creates an expression that calculates the length (dimension) of a Firestore Vector.

```kotlin
// Get the vector length (dimension) of the field 'embedding'.
vectorLength("embedding")
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the Firestore Vector. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length (dimension) of the vector. |

### vectorLength

```
fun vectorLength(vectorExpression: Expression): Expression
```

Creates an expression that calculates the length (dimension) of a Firestore Vector.

```kotlin
// Get the vector length (dimension) of the field 'embedding'.
vectorLength(field("embedding"))
```

| Parameters |
|---|---|
| `vectorExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the Firestore Vector. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length (dimension) of the vector. |

### xor

```
fun xor(condition: BooleanExpression, vararg conditions: BooleanExpression): BooleanExpression
```

Creates an expression that performs a logical 'XOR' operation.

```kotlin
// Check if either 'a' is true or 'b' is true, but not both
xor(field("a"), field("b"))
```

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`. |
| `vararg conditions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | Additional `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`s. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the logical 'XOR' operation. |

## Public functions

### abs

```
fun abs(): Expression
```

Creates an expression that returns the absolute value of this expression.

```kotlin
// Get the absolute value of the 'change' field.
field("change").abs()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the absolute value operation. |

### add

```
fun add(second: Expression): Expression
```

Creates an expression that adds this numeric expression to another numeric expression.

```kotlin
// Add the value of the 'quantity' field and the 'reserve' field.
field("quantity").add(field("reserve"))
```

| Parameters |
|---|---|
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### add

```
fun add(second: Number): Expression
```

Creates an expression that adds this numeric expression to a constants.

```kotlin
// Add 5 to the value of the 'quantity' field.
field("quantity").add(5)
```

| Parameters |
|---|---|
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### alias

```
open fun alias(alias: String): AliasedExpression
```

Assigns an alias to this expression.

Aliases are useful for renaming fields in the output of a stage or for giving meaningful names to calculated values.

| Parameters |
|---|---|
| `alias: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The alias to assign to this expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression` that wraps this expression and associates it with the provided alias. |

### arrayConcat

```
fun arrayConcat(secondArray: Any, vararg otherArrays: Any): Expression
```

Creates an expression that concatenates a field's array value with other arrays.

```kotlin
// Combine the 'items' array with a literal array.
field("items").arrayConcat(listOf("a", "b"))
```

| Parameters |
|---|---|
| `secondArray: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | An array expression or array literal to concatenate. |
| `vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayConcat

```
fun arrayConcat(secondArray: Expression, vararg otherArrays: Any): Expression
```

Creates an expression that concatenates a field's array value with other arrays.

```kotlin
// Combine the 'items' array with another array field.
field("items").arrayConcat(field("otherItems"))
```

| Parameters |
|---|---|
| `secondArray: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to array to concatenate. |
| `vararg otherArrays: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayContains

```
fun arrayContains(element: Any): BooleanExpression
```

Creates an expression that checks if array contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContains(kotlin.Any)`.

```kotlin
// Check if the 'colors' array contains "red"
field("colors").arrayContains("red")
```

| Parameters |
|---|---|
| `element: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The element to search for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContains

```
fun arrayContains(element: Expression): BooleanExpression
```

Creates an expression that checks if array contains a specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContains(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'sizes' array contains the value from the 'selectedSize' field
field("sizes").arrayContains(field("selectedSize"))
```

| Parameters |
|---|---|
| `element: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The element to search for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContainsAll

```
fun arrayContainsAll(arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if array contains all elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'tags' array contains both of the values from field "tag1" and the literal value "tag2"
field("tags").arrayContainsAll(array(field("tag1"), "tag2"))
```

| Parameters |
|---|---|
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAll

```
fun arrayContainsAll(values: List<Any>): BooleanExpression
```

Creates an expression that checks if array contains all the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAll(kotlin.collections.List)`.

```kotlin
// Check if the 'tags' array contains both the value in field "tag1" and the literal value "tag2"
field("tags").arrayContainsAll(listOf(field("tag1"), "tag2"))
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAny

```
fun arrayContainsAny(arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if array contains any elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'groups' array contains either the value from the 'userGroup' field
// or the value "guest"
field("groups").arrayContainsAny(array(field("userGroup"), "guest"))
```

| Parameters |
|---|---|
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayContainsAny

```
fun arrayContainsAny(values: List<Any>): BooleanExpression
```

Creates an expression that checks if array contains any of the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#arrayContainsAny(kotlin.collections.List)`.

```kotlin
// Check if the 'categories' array contains either values from field "cate1" or "cate2"
field("categories").arrayContainsAny(listOf(field("cate1"), field("cate2")))
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The elements to check for in the array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayGet

```
fun arrayGet(offset: Expression): Expression
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```kotlin
// Return the value in the tags field array at index specified by field 'favoriteTag'.
field("tags").arrayGet(field("favoriteTag"))
```

| Parameters |
|---|---|
| `offset: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An Expression evaluating to the index of the element to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayGet

```
fun arrayGet(offset: Int): Expression
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```kotlin
// Return the value in the 'tags' field array at index `1`.
field("tags").arrayGet(1)
```

| Parameters |
|---|---|
| `offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | An Expression evaluating to the index of the element to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayLength

```
fun arrayLength(): Expression
```

Creates an expression that calculates the length of an array expression.

```kotlin
// Get the number of items in the 'cart' array
field("cart").arrayLength()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length of the array. |

### arrayReverse

```
fun arrayReverse(): Expression
```

Reverses the order of elements in the array.

```kotlin
// Reverse the value of the 'myArray' field.
field("myArray").arrayReverse()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the arrayReverse operation. |

### arraySum

```
fun arraySum(): Expression
```

Creates an expression that returns the sum of the elements in this array expression.

```kotlin
// Get the sum of elements in the 'scores' array.
field("scores").arraySum()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the sum of the array elements. |

### asBoolean

```
fun asBoolean(): BooleanExpression
```

Casts the expression to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the same expression. |

### ascending

```
fun ascending(): Ordering
```

Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on value of this expression

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` object with ascending sort by this expression. |

### average

```
fun average(): AggregateFunction
```

Creates an aggregation that calculates the average (mean) of this numeric expression across multiple stage inputs.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the average aggregation. |

### bitAnd

```
fun bitAnd(bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise AND operation with a constant.

```kotlin
// Bitwise AND the value of the 'flags' field with a constant mask.
field("flags").bitAnd(byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitAnd

```
fun bitAnd(bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise AND operation with other expression.

```kotlin
// Bitwise AND the value of the 'flags' field with the value of the 'mask' field.
field("flags").bitAnd(field("mask"))
```

| Parameters |
|---|---|
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitLeftShift

```
fun bitLeftShift(number: Int): Expression
```

Creates an expression that applies a bitwise left shift operation with a constant.

```kotlin
// Left shift the value of the 'bits' field by 2.
field("bits").bitLeftShift(2)
```

| Parameters |
|---|---|
| `number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitLeftShift

```
fun bitLeftShift(numberExpr: Expression): Expression
```

Creates an expression that applies a bitwise left shift operation with an expression.

```kotlin
// Left shift the value of the 'bits' field by the value of the 'shift' field.
field("bits").bitLeftShift(field("shift"))
```

| Parameters |
|---|---|
| `numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitNot

```
fun bitNot(): Expression
```

Creates an expression that applies a bitwise NOT operation to this expression.

```kotlin
// Bitwise NOT the value of the 'flags' field.
field("flags").bitNot()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise NOT operation. |

### bitOr

```
fun bitOr(bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise OR operation with a constant.

```kotlin
// Bitwise OR the value of the 'flags' field with a constant mask.
field("flags").bitOr(byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitOr

```
fun bitOr(bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise OR operation with other expression.

```kotlin
// Bitwise OR the value of the 'flags' field with the value of the 'mask' field.
field("flags").bitOr(field("mask"))
```

| Parameters |
|---|---|
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitRightShift

```
fun bitRightShift(number: Int): Expression
```

Creates an expression that applies a bitwise right shift operation with a constant.

```kotlin
// Right shift the value of the 'bits' field by 2.
field("bits").bitRightShift(2)
```

| Parameters |
|---|---|
| `number: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitRightShift

```
fun bitRightShift(numberExpr: Expression): Expression
```

Creates an expression that applies a bitwise right shift operation with an expression.

```kotlin
// Right shift the value of the 'bits' field by the value of the 'shift' field.
field("bits").bitRightShift(field("shift"))
```

| Parameters |
|---|---|
| `numberExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of bits to shift. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitXor

```
fun bitXor(bitsOther: ByteArray): Expression
```

Creates an expression that applies a bitwise XOR operation with a constant.

```kotlin
// Bitwise XOR the value of the 'flags' field with a constant mask.
field("flags").bitXor(byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `bitsOther: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | A constant byte array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### bitXor

```
fun bitXor(bitsOther: Expression): Expression
```

Creates an expression that applies a bitwise XOR operation with an expression.

```kotlin
// Bitwise XOR the value of the 'flags' field with the value of the 'mask' field.
field("flags").bitXor(field("mask"))
```

| Parameters |
|---|---|
| `bitsOther: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### byteLength

```
fun byteLength(): Expression
```

Creates an expression that calculates the length of a string in UTF-8 bytes, or just the length of a Blob.

```kotlin
// Calculate the length of the 'myString' field in bytes.
field("myString").byteLength()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length of the string in bytes. |

### ceil

```
fun ceil(): Expression
```

Creates an expression that returns the smallest integer that isn't less than this numeric expression.

```kotlin
// Compute the ceiling of the 'price' field.
field("price").ceil()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the ceil operation. |

### charLength

```
fun charLength(): Expression
```

Creates an expression that calculates the character length of this string expression in UTF8.

```kotlin
// Get the character length of the 'name' field in UTF-8.
field("name").charLength()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the charLength operation. |

### collectionId

```
fun collectionId(): Expression
```

Creates an expression that returns the collection ID from this path expression.

```kotlin
// Get the collection ID from the 'path' field
field("path").collectionId()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the collectionId operation. |

### concat

```
fun concat(second: Any, vararg others: Any): Expression
```

Creates an expression that concatenates this expression's value with others. The values must be all strings, all arrays, or all blobs. Types cannot be mixed.

```kotlin
// Concatenate a field with a literal string.
field("firstName").concat("lastName")
```

| Parameters |
|---|---|
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The second value to concatenate. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Additional values to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### concat

```
fun concat(second: Expression, vararg others: Any): Expression
```

Creates an expression that concatenates this expression's value with others. The values must be all strings, all arrays, or all blobs. Types cannot be mixed.

```kotlin
// Concatenate a field with another field.
field("firstName").concat(field("lastName"))
```

| Parameters |
|---|---|
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The second expression to concatenate. |
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Additional expressions to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### cosineDistance

```
fun cosineDistance(vector: DoubleArray): Expression
```

Calculates the Cosine distance between this vector expression and a vector literal.

```kotlin
// Calculate the Cosine distance between the 'location' field and a target location
field("location").cosineDistance(doubleArrayOf(37.7749, -122.4194))
```

| Parameters |
|---|---|
| `vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
fun cosineDistance(vector: Expression): Expression
```

Calculates the Cosine distance between this and another vector expressions.

```kotlin
// Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
field("userVector").cosineDistance(field("itemVector"))
```

| Parameters |
|---|---|
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
fun cosineDistance(vector: VectorValue): Expression
```

Calculates the Cosine distance between this vector expression and a vector literal.

```kotlin
// Calculate the Cosine distance between the 'location' field and a target location
field("location").cosineDistance(VectorValue.from(listOf(37.7749, -122.4194)))
```

| Parameters |
|---|---|
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### count

```
fun count(): AggregateFunction
```

Creates an aggregation that counts the number of stage inputs with valid evaluations of the this expression.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count aggregation. |

### countDistinct

```
fun countDistinct(): AggregateFunction
```

Creates an aggregation that counts the number of distinct values of an expression across multiple stage inputs.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the count distinct aggregation. |

### descending

```
fun descending(): Ordering
```

Create an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on value of this expression

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` object with descending sort by this expression. |

### divide

```
fun divide(divisor: Expression): Expression
```

Creates an expression that divides this numeric expression by another numeric expression.

```kotlin
// Divide the 'total' field by the 'count' field
field("total").divide(field("count"))
```

| Parameters |
|---|---|
| `divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to divide this numeric expression by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the division operation. |

### divide

```
fun divide(divisor: Number): Expression
```

Creates an expression that divides this numeric expression by a constant.

```kotlin
// Divide the 'value' field by 10
field("value").divide(10)
```

| Parameters |
|---|---|
| `divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to divide this expression by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the division operation. |

### documentId

```
fun documentId(): Expression
```

Creates an expression that returns the document ID from this path expression.

```kotlin
// Get the document ID from the 'path' field
field("path").documentId()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the documentId operation. |

### dotProduct

```
fun dotProduct(vector: DoubleArray): Expression
```

Calculates the dot product distance between this vector expression and a vector literal.

```kotlin
// Calculate the dot product between the 'vector' field and a constant vector
field("vector").dotProduct(doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
fun dotProduct(vector: Expression): Expression
```

Calculates the dot product distance between this and another vector expression.

```kotlin
// Calculate the dot product between the 'userVector' field and the 'itemVector' field
field("userVector").dotProduct(field("itemVector"))
```

| Parameters |
|---|---|
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
fun dotProduct(vector: VectorValue): Expression
```

Calculates the dot product distance between this vector expression and a vector literal.

```kotlin
// Calculate the dot product between the 'vector' field and a constant vector
field("vector").dotProduct(VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### endsWith

```
fun endsWith(suffix: Expression): BooleanExpression
```

Creates an expression that checks if this string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#endsWith(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'url' field ends with the value of the 'extension' field
field("url").endsWith(field("extension"))
```

| Parameters |
|---|---|
| `suffix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The suffix string expression to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### endsWith

```
fun endsWith(suffix: String): BooleanExpression
```

Creates an expression that checks if this string expression ends with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#endsWith(kotlin.String)`.

```kotlin
// Check if the 'filename' field ends with ".txt"
field("filename").endsWith(".txt")
```

| Parameters |
|---|---|
| `suffix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The suffix string to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### equal

```
fun equal(other: Expression): BooleanExpression
```

Creates an expression that checks if this and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equal(com.google.firebase.firestore.pipeline.Expression)` expression are equal.

```kotlin
// Check if the 'age' field is equal to an expression
field("age").equal(field("minAge").add(10))
```

| Parameters |
|---|---|
| `other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equal

```
fun equal(value: Any): BooleanExpression
```

Creates an expression that checks if this expression is equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equal(kotlin.Any)`.

```kotlin
// Check if the 'age' field is equal to 21
field("age").equal(21)
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equalAny

```
fun equalAny(arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if this expression, when evaluated, is equal to any of the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equalAny(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'category' field is in the 'availableCategories' array field.
field("category").equalAny(field("availableCategories"))
```

| Parameters |
|---|---|
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### equalAny

```
fun equalAny(values: List<Any>): BooleanExpression
```

Creates an expression that checks if this expression, when evaluated, is equal to any of the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#equalAny(kotlin.collections.List)`.

```kotlin
// Check if the 'category' field is either "Electronics" or the value of the 'primaryType' field.
field("category").equalAny(listOf("Electronics", field("primaryType")))
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The values to check against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### euclideanDistance

```
fun euclideanDistance(vector: DoubleArray): Expression
```

Calculates the Euclidean distance between this vector expression and a vector literal.

```kotlin
// Calculate the Euclidean distance between the 'vector' field and a constant vector
field("vector").euclideanDistance(doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `vector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
fun euclideanDistance(vector: Expression): Expression
```

Calculates the Euclidean distance between this and another vector expression.

```kotlin
// Calculate the Euclidean distance between the 'userVector' field and the 'itemVector' field
field("userVector").euclideanDistance(field("itemVector"))
```

| Parameters |
|---|---|
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
fun euclideanDistance(vector: VectorValue): Expression
```

Calculates the Euclidean distance between this vector expression and a vector literal.

```kotlin
// Calculate the Euclidean distance between the 'vector' field and a constant vector
field("vector").euclideanDistance(VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `vector: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue` | The other vector (represented as an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### exists

```
fun exists(): BooleanExpression
```

Creates an expression that checks if this expression evaluates to a name of the field that exists.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the exists check. |

### exp

```
fun exp(): Expression
```

Creates an expression that returns Euler's number e raised to the power of this expression.

```kotlin
// Compute e to the power of the 'value' field.
field("value").exp()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the exponentiation. |

### floor

```
fun floor(): Expression
```

Creates an expression that returns the largest integer that is not greater than this numeric expression.

```kotlin
// Compute the floor of the 'price' field.
field("price").floor()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the floor operation. |

### greaterThan

```
fun greaterThan(other: Expression): BooleanExpression
```

Creates an expression that checks if this expression is greater than the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThan(com.google.firebase.firestore.pipeline.Expression)` expression.

```kotlin
// Check if the 'age' field is greater than the 'limit' field
field("age").greaterThan(field("limit"))
```

| Parameters |
|---|---|
| `other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThan

```
fun greaterThan(value: Any): BooleanExpression
```

Creates an expression that checks if this expression is greater than a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThan(kotlin.Any)`.

```kotlin
// Check if the 'price' field is greater than 100
field("price").greaterThan(100)
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThanOrEqual

```
fun greaterThanOrEqual(other: Expression): BooleanExpression
```

Creates an expression that checks if this expression is greater than or equal to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThanOrEqual(com.google.firebase.firestore.pipeline.Expression)` expression.

```kotlin
// Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
field("quantity").greaterThanOrEqual(field("requirement").add(1))
```

| Parameters |
|---|---|
| `other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### greaterThanOrEqual

```
fun greaterThanOrEqual(value: Any): BooleanExpression
```

Creates an expression that checks if this expression is greater than or equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#greaterThanOrEqual(kotlin.Any)`.

```kotlin
// Check if the 'score' field is greater than or equal to 80
field("score").greaterThanOrEqual(80)
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### ifAbsent

```
fun ifAbsent(elseExpr: Expression): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifAbsent(com.google.firebase.firestore.pipeline.Expression)` argument if this expression is absent, else return the result of this expression.

```kotlin
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
field("optional_field").ifAbsent("default_value")
```

| Parameters |
|---|---|
| `elseExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that will be evaluated and returned if this expression is absent. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifAbsent

```
fun ifAbsent(elseValue: Any): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifAbsent(kotlin.Any)` argument if this expression is absent, else return the result of this expression.

```kotlin
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
field("optional_field").ifAbsent("default_value")
```

| Parameters |
|---|---|
| `elseValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value that will be returned if this expression is absent. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifError

```
fun ifError(catchExpr: Expression): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifError(com.google.firebase.firestore.pipeline.Expression)` argument if there is an error, else return the result of this expression.

```kotlin
// Returns the first item in the title field arrays, or returns
// the entire title field if the array is empty or the field is another type.
arrayGet(field("title"), 0).ifError(field("title"))
```

| Parameters |
|---|---|
| `catchExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The catch expression that will be evaluated and returned if the this expression produces an error. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifError operation. |

### ifError

```
fun ifError(catchValue: Any): Expression
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#ifError(kotlin.Any)` argument if there is an error, else return the result of this expression.

```kotlin
// Returns the first item in the title field arrays, or returns "Default Title"
arrayGet(field("title"), 0).ifError("Default Title")
```

| Parameters |
|---|---|
| `catchValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value that will be returned if this expression produces an error. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the ifError operation. |

### isAbsent

```
fun isAbsent(): BooleanExpression
```

Creates an expression that returns true if the result of this expression is absent. Otherwise, returns false even if the value is null.

```kotlin
// Check if the field `value` is absent.
field("value").isAbsent()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the isAbsent operation. |

### isError

```
fun isError(): BooleanExpression
```

Creates an expression that checks if this expression produces an error.

```kotlin
// Check if the result of a calculation is an error
arrayContains(field("title"), 1).isError()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the `isError` check. |

### join

```
fun join(delimiter: String): Expression
```

Creates an expression that joins the elements of an array into a string.

```kotlin
// Join the elements of the 'tags' field with a comma and space.
field("tags").join(", ")
```

| Parameters |
|---|---|
| `delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string to use as a delimiter. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### join

```
fun join(delimiterExpression: Expression): Expression
```

Creates an expression that joins the elements of an array into a string.

```kotlin
// Join the elements of the 'tags' field with the delimiter from the 'separator' field.
field("tags").join(field("separator"))
```

| Parameters |
|---|---|
| `delimiterExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression that evaluates to the delimiter string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### length

```
fun length(): Expression
```

Creates an expression that calculates the length of a string, array, map, vector, or blob expression.

```kotlin
// Get the length of the 'value' field where the value type can be any of a string, array, map, vector or blob.
field("value").length()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length operation. |

### lessThan

```
fun lessThan(other: Expression): BooleanExpression
```

Creates an expression that checks if this expression is less than the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThan(com.google.firebase.firestore.pipeline.Expression)` expression.

```kotlin
// Check if the 'age' field is less than 'limit'
field("age").lessThan(field("limit"))
```

| Parameters |
|---|---|
| `other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThan

```
fun lessThan(value: Any): BooleanExpression
```

Creates an expression that checks if this expression is less than a value.

```kotlin
// Check if the 'price' field is less than 50
field("price").lessThan(50)
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThanOrEqual

```
fun lessThanOrEqual(other: Expression): BooleanExpression
```

Creates an expression that checks if this expression is less than or equal to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThanOrEqual(com.google.firebase.firestore.pipeline.Expression)` expression.

```kotlin
// Check if the 'quantity' field is less than or equal to 20
field("quantity").lessThanOrEqual(constant(20))
```

| Parameters |
|---|---|
| `other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### lessThanOrEqual

```
fun lessThanOrEqual(value: Any): BooleanExpression
```

Creates an expression that checks if this expression is less than or equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#lessThanOrEqual(kotlin.Any)`.

```kotlin
// Check if the 'score' field is less than or equal to 70
field("score").lessThanOrEqual(70)
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### like

```
fun like(pattern: Expression): BooleanExpression
```

Creates an expression that performs a case-sensitive wildcard string comparison.

```kotlin
// Check if the 'title' field contains the string "guide"
field("title").like("%guide%")
```

| Parameters |
|---|---|
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like operation. |

### like

```
fun like(pattern: String): BooleanExpression
```

Creates an expression that performs a case-sensitive wildcard string comparison.

```kotlin
// Check if the 'title' field contains the string "guide"
field("title").like("%guide%")
```

| Parameters |
|---|---|
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like operation. |

### ln

```
fun ln(): Expression
```

Creates an expression that returns the natural logarithm of this numeric expression.

```kotlin
// compute the natural logarithm of the 'value' field.
field("value").ln()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the natural logarithm operation. |

### log10

```
fun log10(): Expression
```

Creates an expression that returns the base-10 logarithm of this numeric expression.

```kotlin
// compute the base-10 logarithm of the 'value' field.
field("value").log10()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the base-10 logarithm operation. |

### logicalMaximum

```
fun logicalMaximum(vararg others: Any): Expression
```

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the larger value between the 'timestamp' field and the current timestamp.
field("timestamp").logicalMaximum(currentTimestamp())
```

| Parameters |
|---|---|
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical maximum operation. |

### logicalMaximum

```
fun logicalMaximum(vararg others: Expression): Expression
```

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the larger value between the 'timestamp' field and the current timestamp.
field("timestamp").logicalMaximum(currentTimestamp())
```

| Parameters |
|---|---|
| `vararg others: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical maximum operation. |

### logicalMinimum

```
fun logicalMinimum(vararg others: Any): Expression
```

Creates an expression that returns the smallest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the smaller value between the 'timestamp' field and the current timestamp.
field("timestamp").logicalMinimum(currentTimestamp())
```

| Parameters |
|---|---|
| `vararg others: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical minimum operation. |

### logicalMinimum

```
fun logicalMinimum(vararg others: Expression): Expression
```

Creates an expression that returns the smallest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```kotlin
// Returns the smaller value between the 'timestamp' field and the current timestamp.
field("timestamp").logicalMinimum(currentTimestamp())
```

| Parameters |
|---|---|
| `vararg others: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Expressions or literals. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the logical minimum operation. |

### mapGet

```
fun mapGet(key: String): Expression
```

Accesses a map (object) value using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapGet(kotlin.String)`.

```kotlin
// Get the 'city' value from the 'address' map field
field("address").mapGet("city")
```

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key to access in the map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapGet

```
fun mapGet(keyExpression: Expression): Expression
```

Accesses a map (object) value using the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#mapGet(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Get the value from the 'address' map field, using the key from the 'keyField' field
field("address").mapGet(field("keyField"))
```

| Parameters |
|---|---|
| `keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The name of the key to remove from this map expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapMerge

```
fun mapMerge(mapExpr: Expression, vararg otherMaps: Expression): Expression
```

Creates an expression that merges multiple maps into a single map. If multiple maps have the same key, the later value is used.

```kotlin
// Merges the map in the settings field with, a map literal, and a map in
// that is conditionally returned by another expression
field("settings").mapMerge(
  map(mapOf("enabled" to true)),
  conditional(
    field("isAdmin").equal(true),
    map(mapOf("admin" to true)),
    map(emptyMap<String, Any>())
  )
)
```

| Parameters |
|---|---|
| `mapExpr: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Map expression that will be merged. |
| `vararg otherMaps: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Additional maps to merge. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the mapMerge operation. |

### mapRemove

```
fun mapRemove(key: String): Expression
```

Creates an expression that removes a key from this map expression.

```kotlin
// Removes the key 'baz' from the input map.
map(mapOf("foo" to "bar", "baz" to true)).mapRemove("baz")
```

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the key to remove from this map expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mapRemove

```
fun mapRemove(keyExpression: Expression): Expression
```

Creates an expression that removes a key from this map expression.

```kotlin
// Removes the key 'baz' from the input map.
map(mapOf("foo" to "bar", "baz" to true)).mapRemove(constant("baz"))
```

| Parameters |
|---|---|
| `keyExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The name of the key to remove from this map expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### maximum

```
fun maximum(): AggregateFunction
```

Creates an aggregation that finds the maximum value of this expression across multiple stage inputs.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the maximum aggregation. |

### minimum

```
fun minimum(): AggregateFunction
```

Creates an aggregation that finds the minimum value of this expression across multiple stage inputs.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the minimum aggregation. |

### mod

```
fun mod(divisor: Expression): Expression
```

Creates an expression that calculates the modulo (remainder) of dividing this numeric expressions by another numeric expression.

```kotlin
// Calculate the remainder of dividing the 'value' field by the 'divisor' field
field("value").mod(field("divisor"))
```

| Parameters |
|---|---|
| `divisor: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric expression to divide this expression by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### mod

```
fun mod(divisor: Number): Expression
```

Creates an expression that calculates the modulo (remainder) of dividing this numeric expressions by a constant.

```kotlin
// Calculate the remainder of dividing the 'value' field by 3.
field("value").mod(3)
```

| Parameters |
|---|---|
| `divisor: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The constant to divide this expression by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### multiply

```
fun multiply(second: Expression): Expression
```

Creates an expression that multiplies this numeric expression with another numeric expression.

```kotlin
// Multiply the 'quantity' field by the 'price' field
field("quantity").multiply(field("price"))
```

| Parameters |
|---|---|
| `second: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to multiply. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### multiply

```
fun multiply(second: Number): Expression
```

Creates an expression that multiplies this numeric expression with a constant.

```kotlin
// Multiply the 'quantity' field by 1.1.
field("quantity").multiply(1.1)
```

| Parameters |
|---|---|
| `second: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to multiply. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### notEqual

```
fun notEqual(other: Expression): BooleanExpression
```

Creates an expression that checks if this expressions is not equal to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqual(com.google.firebase.firestore.pipeline.Expression)` expression.

```kotlin
// Check if the 'status' field is not equal to the value of the 'otherStatus' field
field("status").notEqual(field("otherStatus"))
```

| Parameters |
|---|---|
| `other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqual

```
fun notEqual(value: Any): BooleanExpression
```

Creates an expression that checks if this expression is not equal to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqual(kotlin.Any)`.

```kotlin
// Check if the 'status' field is not equal to "completed"
field("status").notEqual("completed")
```

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The value to compare to. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqualAny

```
fun notEqualAny(arrayExpression: Expression): BooleanExpression
```

Creates an expression that checks if this expression, when evaluated, is not equal to all the elements of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqualAny(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'status' field is not in the 'inactiveStatuses' array field.
field("status").notEqualAny(field("inactiveStatuses"))
```

| Parameters |
|---|---|
| `arrayExpression: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### notEqualAny

```
fun notEqualAny(values: List<Any>): BooleanExpression
```

Creates an expression that checks if this expression, when evaluated, is not equal to all the provided `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#notEqualAny(kotlin.collections.List)`.

```kotlin
// Check if the 'status' field is neither "pending" nor the value of the 'rejectedStatus' field.
field("status").notEqualAny(listOf("pending", field("rejectedStatus")))
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html>` | The values to check against. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### pow

```
fun pow(exponent: Expression): Expression
```

Creates an expression that returns this numeric expression raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(com.google.firebase.firestore.pipeline.Expression)`. Returns infinity on overflow and zero on underflow.

```kotlin
// Raise the value of the 'base' field to the power of the 'exponent' field.
field("base").pow(field("exponent"))
```

| Parameters |
|---|---|
| `exponent: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The numeric power to raise this numeric expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising this numeric expression to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(com.google.firebase.firestore.pipeline.Expression)`. |

### pow

```
fun pow(exponent: Number): Expression
```

Creates an expression that returns this numeric expression raised to the power of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(kotlin.Number)`. Returns infinity on overflow and zero on underflow.

```kotlin
// Raise the value of the 'base' field to the power of 2.
field("base").pow(2)
```

| Parameters |
|---|---|
| `exponent: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | The numeric power to raise this numeric expression. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising this numeric expression to the power of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#pow(kotlin.Number)`. |

### regexContains

```
fun regexContains(pattern: Expression): BooleanExpression
```

Creates an expression that checks if this string expression contains a specified regular expression as a substring.

```kotlin
// Check if the 'description' field contains "example" (case-insensitive)
field("description").regexContains("(?i)example")
```

| Parameters |
|---|---|
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to use for the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexContains

```
fun regexContains(pattern: String): BooleanExpression
```

Creates an expression that checks if this string expression contains a specified regular expression as a substring.

```kotlin
// Check if the 'description' field contains "example" (case-insensitive)
field("description").regexContains("(?i)example")
```

| Parameters |
|---|---|
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to use for the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexMatch

```
fun regexMatch(pattern: Expression): BooleanExpression
```

Creates an expression that checks if this string expression matches a specified regular expression.

```kotlin
// Check if the 'email' field matches a valid email pattern
field("email").regexMatch("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `pattern: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The regular expression to use for the match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### regexMatch

```
fun regexMatch(pattern: String): BooleanExpression
```

Creates an expression that checks if this string expression matches a specified regular expression.

```kotlin
// Check if the 'email' field matches a valid email pattern
field("email").regexMatch("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `pattern: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The regular expression to use for the match. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### reverse

```
fun reverse(): Expression
```

Creates an expression that reverses this string expression.

```kotlin
// Reverse the value of the 'myString' field.
field("myString").reverse()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the reversed string. |

### round

```
fun round(): Expression
```

Creates an expression that rounds this numeric expression to nearest integer.

```kotlin
// Round the value of the 'price' field.
field("price").round()
```

Rounds away from zero in halfway cases.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the round operation. |

### roundToPrecision

```
fun roundToPrecision(decimalPlace: Expression): Expression
```

Creates an expression that rounds off this numeric expression to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(com.google.firebase.firestore.pipeline.Expression)` is negative. Rounds away from zero in halfway cases.

```kotlin
// Round the value of the 'price' field to the number of decimal places specified in the
// 'precision' field.
field("price").roundToPrecision(field("precision"))
```

| Parameters |
|---|---|
| `decimalPlace: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The number of decimal places to round. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### roundToPrecision

```
fun roundToPrecision(decimalPlace: Int): Expression
```

Creates an expression that rounds off this numeric expression to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#roundToPrecision(kotlin.Int)` is negative. Rounds away from zero in halfway cases.

```kotlin
// Round the value of the 'price' field to 2 decimal places.
field("price").roundToPrecision(2)
```

| Parameters |
|---|---|
| `decimalPlace: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of decimal places to round. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### split

```
fun split(delimiter: Blob): Expression
```

Creates an expression that splits this blob expression by a blob delimiter.

```kotlin
// Split the 'data' field by a delimiter
field("data").split(Blob.fromBytes(byteArrayOf(0x0a)))
```

| Parameters |
|---|---|
| `delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` | The blob delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
fun split(delimiter: Expression): Expression
```

Creates an expression that splits this string or blob expression by a delimiter.

```kotlin
// Split the 'tags' field by a comma
field("tags").split(field("delimiter"))
```

| Parameters |
|---|---|
| `delimiter: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
fun split(delimiter: String): Expression
```

Creates an expression that splits this string or blob expression by a string delimiter.

```kotlin
// Split the 'tags' field by a comma
field("tags").split(",")
```

| Parameters |
|---|---|
| `delimiter: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string delimiter to split by. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### sqrt

```
fun sqrt(): Expression
```

Creates an expression that returns the square root of this numeric expression.

```kotlin
// Compute the square root of the 'value' field.
field("value").sqrt()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the square root operation. |

### startsWith

```
fun startsWith(prefix: Expression): BooleanExpression
```

Creates an expression that checks if this string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#startsWith(com.google.firebase.firestore.pipeline.Expression)`.

```kotlin
// Check if the 'fullName' field starts with the value of the 'firstName' field
field("fullName").startsWith(field("firstName"))
```

| Parameters |
|---|---|
| `prefix: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The prefix string expression to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### startsWith

```
fun startsWith(prefix: String): BooleanExpression
```

Creates an expression that checks if this string expression starts with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression#startsWith(kotlin.String)`.

```kotlin
// Check if the 'name' field starts with "Mr."
field("name").startsWith("Mr.")
```

| Parameters |
|---|---|
| `prefix: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The prefix string to check for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### stringConcat

```
fun stringConcat(vararg stringExpressions: Expression): Expression
```

Creates an expression that concatenates string expressions together.

```kotlin
// Combine the 'firstName', " ", and 'lastName' fields into a single string
field("firstName").stringConcat(constant(" "), field("lastName"))
```

| Parameters |
|---|---|
| `vararg stringExpressions: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The string expressions to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
fun stringConcat(vararg strings: Any): Expression
```

Creates an expression that concatenates string expressions and string constants together.

```kotlin
// Combine the 'firstName', " ", and 'lastName' fields into a single string
field("firstName").stringConcat(" ", field("lastName"))
```

| Parameters |
|---|---|
| `vararg strings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The string expressions or string constants to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
fun stringConcat(vararg strings: String): Expression
```

Creates an expression that concatenates this string expression with string constants.

```kotlin
// Combine the 'firstName', " ", and 'lastName' fields into a single string
field("firstName").stringConcat(" ", "lastName")
```

| Parameters |
|---|---|
| `vararg strings: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The string constants to concatenate. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringContains

```
fun stringContains(substring: Expression): BooleanExpression
```

Creates an expression that checks if this string expression contains a specified substring.

```kotlin
// Check if the 'description' field contains the value of the 'keyword' field.
field("description").stringContains(field("keyword"))
```

| Parameters |
|---|---|
| `substring: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the substring to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringContains

```
fun stringContains(substring: String): BooleanExpression
```

Creates an expression that checks if this string expression contains a specified substring.

```kotlin
// Check if the 'description' field contains "example".
field("description").stringContains("example")
```

| Parameters |
|---|---|
| `substring: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The substring to search for. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringReverse

```
fun stringReverse(): Expression
```

Creates an expression that performs a reverse operation on this string expression.

```kotlin
// reverse the field "filename": "abc.txt" => "txt.cba"
field("filename").stringReverse()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the 'stringReverse' operation. |

### substring

```
fun substring(start: Expression, length: Expression): Expression
```

Creates an expression that returns a substring of the given string.

```kotlin
// Get a substring of the 'message' field starting at index 5 with length 10.
field("message").substring(constant(5), constant(10))
```

| Parameters |
|---|---|
| `start: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The starting index of the substring. |
| `length: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The length of the substring. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the substring. |

### substring

```
fun substring(start: Int, length: Int): Expression
```

Creates an expression that returns a substring of the given string.

```kotlin
// Get a substring of the 'message' field starting at index 5 with length 10.
field("message").substring(5, 10)
```

| Parameters |
|---|---|
| `start: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The starting index of the substring. |
| `length: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The length of the substring. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the substring. |

### subtract

```
fun subtract(subtrahend: Expression): Expression
```

Creates an expression that subtracts a constant from this numeric expression.

```kotlin
// Subtract the 'discount' field from the 'price' field
field("price").subtract(field("discount"))
```

| Parameters |
|---|---|
| `subtrahend: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | Numeric expression to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### subtract

```
fun subtract(subtrahend: Number): Expression
```

Creates an expression that subtracts a numeric expressions from this numeric expression.

```kotlin
// Subtract 10 from the 'price' field.
field("price").subtract(10)
```

| Parameters |
|---|---|
| `subtrahend: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` | Constant to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### sum

```
fun sum(): AggregateFunction
```

Creates an aggregation that calculates the sum of this numeric expression across multiple stage inputs.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` representing the sum aggregation. |

### timestampAdd

```
fun timestampAdd(unit: Expression, amount: Expression): Expression
```

Creates an expression that adds a specified amount of time to this timestamp expression.

```kotlin
// Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
field("timestamp").timestampAdd(field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the amount of time to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampAdd

```
fun timestampAdd(unit: String, amount: Long): Expression
```

Creates an expression that adds a specified amount of time to this timestamp expression.

```kotlin
// Add 1 day to the 'timestamp' field.
field("timestamp").timestampAdd("day", 1)
```

| Parameters |
|---|---|
| `unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The amount of time to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
fun timestampSubtract(unit: Expression, amount: Expression): Expression
```

Creates an expression that subtracts a specified amount of time to this timestamp expression.

```kotlin
// Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
field("timestamp").timestampSubtract(field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `unit: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the amount of time to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
fun timestampSubtract(unit: String, amount: Long): Expression
```

Creates an expression that subtracts a specified amount of time to this timestamp expression.

```kotlin
// Subtract 1 day from the 'timestamp' field.
field("timestamp").timestampSubtract("day", 1)
```

| Parameters |
|---|---|
| `unit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `amount: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The amount of time to subtract. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampToUnixMicros

```
fun timestampToUnixMicros(): Expression
```

Creates an expression that converts this timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to microseconds since epoch.
field("timestamp").timestampToUnixMicros()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of microseconds since epoch. |

### timestampToUnixMillis

```
fun timestampToUnixMillis(): Expression
```

Creates an expression that converts this timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to milliseconds since epoch.
field("timestamp").timestampToUnixMillis()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of milliseconds since epoch. |

### timestampToUnixSeconds

```
fun timestampToUnixSeconds(): Expression
```

Creates an expression that converts this timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```kotlin
// Convert the 'timestamp' field to seconds since epoch.
field("timestamp").timestampToUnixSeconds()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the number of seconds since epoch. |

### timestampTruncate

```
fun timestampTruncate(granularity: Expression): Expression
```

Creates an expression that truncates this timestamp expression to a specified granularity.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day.
field("createdAt").timestampTruncate(field("granularity"))
```

| Parameters |
|---|---|
| `granularity: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
fun timestampTruncate(granularity: String): Expression
```

Creates an expression that truncates this timestamp expression to a specified granularity.

```kotlin
// Truncate the 'createdAt' timestamp to the beginning of the day.
field("createdAt").timestampTruncate("day")
```

| Parameters |
|---|---|
| `granularity: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### toLower

```
fun toLower(): Expression
```

Creates an expression that converts this string expression to lowercase.

```kotlin
// Convert the 'name' field to lowercase
field("name").toLower()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the lowercase string. |

### toUpper

```
fun toUpper(): Expression
```

Creates an expression that converts this string expression to uppercase.

```kotlin
// Convert the 'title' field to uppercase
field("title").toUpper()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the uppercase string. |

### trim

```
fun trim(): Expression
```

Creates an expression that removes leading and trailing whitespace from this string expression.

```kotlin
// Trim whitespace from the 'userInput' field
field("userInput").trim()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trimValue

```
fun trimValue(valueToTrim: Expression): Expression
```

Creates an expression that removes leading and trailing value from this expression. The accepted types are string and blob.

```kotlin
// Trim specified characters from the 'userInput' field
field("userInput").trimValue(field("trimChars"))
```

| Parameters |
|---|---|
| `valueToTrim: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The expression representing the characters to trim from the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trimValue

```
fun trimValue(valueToTrim: String): Expression
```

Creates an expression that removes leading and trailing characters from this string expression.

```kotlin
// Trim '_' and '-' from the 'userInput' field
field("userInput").trimValue("-_")
```

| Parameters |
|---|---|
| `valueToTrim: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The characters to trim from the string. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### type

```
fun type(): Expression
```

Creates an expression that returns a string indicating the type of the value this expression evaluates to.

```kotlin
// Get the type of the 'value' field.
field("value").type()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the type operation. |

### unixMicrosToTimestamp

```
fun unixMicrosToTimestamp(): Expression
```

Creates an expression that interprets this expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'microseconds' field as microseconds since epoch.
field("microseconds").unixMicrosToTimestamp()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixMillisToTimestamp

```
fun unixMillisToTimestamp(): Expression
```

Creates an expression that interprets this expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'milliseconds' field as milliseconds since epoch.
field("milliseconds").unixMillisToTimestamp()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixSecondsToTimestamp

```
fun unixSecondsToTimestamp(): Expression
```

Creates an expression that interprets this expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```kotlin
// Interpret the 'seconds' field as seconds since epoch.
field("seconds").unixSecondsToTimestamp()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### vectorLength

```
fun vectorLength(): Expression
```

Creates an expression that calculates the length (dimension) of a Firestore Vector.

```kotlin
// Get the vector length (dimension) of the field 'embedding'.
field("embedding").vectorLength()
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` representing the length (dimension) of the vector. |