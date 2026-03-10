# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion.md.txt

# Expression.Companion

# Expression.Companion


```
public static class Expression.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#abs(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#abs(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#abs(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#abs(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#add(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second)` Creates an expression that adds numeric expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#add(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second)` Creates an expression that adds numeric expressions with a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#add(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second)` Creates an expression that adds a numeric field with a numeric expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#add(kotlin.String,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second)` Creates an expression that adds a numeric field with constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#and(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression conditions )` Creates an expression that performs a logical 'AND' operation. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#array(kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> elements)` Creates an expression that creates a Firestore array value from an input array. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#array(kotlin.Array)(https://developer.android.com/reference/kotlin/java/lang/Object.html elements)` Creates an expression that creates a Firestore array value from an input array. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(com.google.firebase.firestore.pipeline.Expression,kotlin.Any,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstArray, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html secondArray, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays )` Creates an expression that concatenates an array with other arrays. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstArray, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondArray, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays )` Creates an expression that concatenates an array with other arrays. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(kotlin.String,kotlin.Any,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html firstArrayField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html secondArray, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays )` Creates an expression that concatenates a field's array value with other arrays. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayConcat(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html firstArrayField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondArray, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays )` Creates an expression that concatenates a field's array value with other arrays. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html element)` Creates an expression that checks if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression element)` Creates an expression that checks if the array contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html element)` Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,kotlin.Any)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression element)` Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression )` Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains all elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values )` Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains all the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression )` Creates an expression that checks if array field contains all elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values )` Creates an expression that checks if array field contains all the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression )` Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains any elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values )` Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains any of the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression )` Creates an expression that checks if array field contains any elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values )` Creates an expression that checks if array field contains any of the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression offset)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array, int offset)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression offset)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayGet(kotlin.String,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, int offset)` Creates an expression that indexes into an array from the beginning or end and return the element. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array)` Creates an expression that calculates the length of an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(com.google.firebase.firestore.pipeline.Expression)` expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName)` Creates an expression that calculates the length of an array field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array)` Reverses the order of elements in the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName)` Reverses the order of elements in the array field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arraySum(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array)` Creates an expression that returns the sum of the elements in an array. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arraySum(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName)` Creates an expression that returns the sum of the elements in an array field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(com.google.firebase.firestore.pipeline.Expression,kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther)` Creates an expression that applies a bitwise AND operation between an expression and a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther)` Creates an expression that applies a bitwise AND operation between two expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(kotlin.String,kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther)` Creates an expression that applies a bitwise AND operation between an field and constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitAnd(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther)` Creates an expression that applies a bitwise AND operation between an field and an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, int number)` Creates an expression that applies a bitwise left shift operation between an expression and a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr)` Creates an expression that applies a bitwise left shift operation between two expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(kotlin.String,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, int number)` Creates an expression that applies a bitwise left shift operation between a field and a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitLeftShift(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr)` Creates an expression that applies a bitwise left shift operation between a field and an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitNot(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits)` Creates an expression that applies a bitwise NOT operation to an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitNot(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName)` Creates an expression that applies a bitwise NOT operation to a field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(com.google.firebase.firestore.pipeline.Expression,kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther)` Creates an expression that applies a bitwise OR operation between an expression and a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther)` Creates an expression that applies a bitwise OR operation between two expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(kotlin.String,kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther)` Creates an expression that applies a bitwise OR operation between an field and constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitOr(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther)` Creates an expression that applies a bitwise OR operation between an field and an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, int number)` Creates an expression that applies a bitwise right shift operation between an expression and a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr)` Creates an expression that applies a bitwise right shift operation between two expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(kotlin.String,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, int number)` Creates an expression that applies a bitwise right shift operation between a field and a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitRightShift(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr )` Creates an expression that applies a bitwise right shift operation between a field and an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(com.google.firebase.firestore.pipeline.Expression,kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther)` Creates an expression that applies a bitwise XOR operation between an expression and a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther)` Creates an expression that applies a bitwise XOR operation between two expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(kotlin.String,kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther)` Creates an expression that applies a bitwise XOR operation between an field and constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#bitXor(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther)` Creates an expression that applies a bitwise XOR operation between an field and an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#byteLength(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that calculates the length of a string represented by a field in UTF-8 bytes, or just the length of a Blob. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#byteLength(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value)` Creates an expression that calculates the length of a string in UTF-8 bytes, or just the length of a Blob. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#charLength(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that calculates the character length of a string expression in UTF8. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#charLength(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that calculates the character length of a string field in UTF8. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#collectionId(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression path)` Creates an expression that returns the collection ID from a path. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#collectionId(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pathField)` Creates an expression that returns the collection ID from a path. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#concat(com.google.firebase.firestore.pipeline.Expression,kotlin.Any,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html second, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others )` Creates an expression that concatenates strings, arrays, or blobs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#concat(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others )` Creates an expression that concatenates strings, arrays, or blobs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#concat(kotlin.String,kotlin.Any,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html second, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others)` Creates an expression that concatenates strings, arrays, or blobs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#concat(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others )` Creates an expression that concatenates strings, arrays, or blobs. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression thenExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression elseExpr )` Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if a condition is true or an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if the condition is false. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html thenValue, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html elseValue )` Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if a condition is true or an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if the condition is false. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.DocumentReference)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference ref)` Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.Blob)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob value)` Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.Boolean)(boolean value)` Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.ByteArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] value)` Create a constant for a bytes value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(java.util.Date)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Date.html value)` Create a constant for a `https://developer.android.com/reference/kotlin/java/util/Date.html` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.GeoPoint)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint value)` Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html value)` Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.Timestamp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp value)` Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#constant(com.google.firebase.firestore.VectorValue)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue value)` Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(com.google.firebase.firestore.pipeline.Expression,kotlin.DoubleArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector2)` Calculates the Cosine distance between vector expression and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector2)` Calculates the Cosine distance between two vector expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.VectorValue)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector2)` Calculates the Cosine distance between vector expression and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(kotlin.String,kotlin.DoubleArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector)` Calculates the Cosine distance between a vector field and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector)` Calculates the Cosine distance between a vector field and a vector expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#cosineDistance(kotlin.String,com.google.firebase.firestore.VectorValue)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector )` Calculates the Cosine distance between a vector field and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#currentTimestamp()()` Creates an expression that evaluates to the current server timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#divide(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor)` Creates an expression that divides two numeric expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#divide(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor)` Creates an expression that divides a numeric expression by a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#divide(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor)` Creates an expression that divides numeric field by a numeric expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#divide(kotlin.String,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor)` Creates an expression that divides a numeric field by a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#documentId(com.google.firebase.firestore.DocumentReference)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference docRef)` Creates an expression that returns the document ID from a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#documentId(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression documentPath)` Creates an expression that returns the document ID from a path. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#documentId(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html documentPath)` Creates an expression that returns the document ID from a path. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(com.google.firebase.firestore.pipeline.Expression,kotlin.DoubleArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector2)` Calculates the dot product distance between vector expression and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector2)` Calculates the dot product distance between two vector expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.VectorValue)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector2)` Calculates the dot product distance between vector expression and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(kotlin.String,kotlin.DoubleArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector)` Calculates the dot product distance between vector field and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector)` Calculates the dot product distance between a vector field and a vector expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#dotProduct(kotlin.String,com.google.firebase.firestore.VectorValue)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector)` Calculates the dot product distance between a vector field and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression suffix)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html suffix)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression suffix)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html suffix)` Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equal(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an expression that checks if a field's value is equal to an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equal(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Creates an expression that checks if a field's value is equal to another value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equal(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right)` Creates an expression that checks if an expression is equal to a value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equal(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right)` Creates an expression that checks if two expressions are equal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression )` Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is equal to any of the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values )` Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is equal to any of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression)` Creates an expression that checks if a field's value is equal to any of the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values)` Creates an expression that checks if a field's value is equal to any of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,kotlin.collections.List)` . |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(com.google.firebase.firestore.pipeline.Expression,kotlin.DoubleArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector2)` Calculates the Euclidean distance between vector expression and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector2)` Calculates the Euclidean distance between two vector expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.VectorValue)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector2 )` Calculates the Euclidean distance between vector expression and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(kotlin.String,kotlin.DoubleArray)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector )` Calculates the Euclidean distance between a vector field and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector )` Calculates the Euclidean distance between a vector field and a vector expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#euclideanDistance(kotlin.String,com.google.firebase.firestore.VectorValue)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector )` Calculates the Euclidean distance between a vector field and a vector literal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exists(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that checks if a field exists. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exists(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value)` Creates an expression that checks if a field exists. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exp(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exp(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exp(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exp(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#field(com.google.firebase.firestore.FieldPath)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#field(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name)` Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#floor(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#floor(com.google.firebase.firestore.pipeline.Expression)` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#floor(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#floor(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an expression that checks if a field's value is greater than an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Creates an expression that checks if a field's value is greater than another value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right)` Creates an expression that checks if an expression is greater than a value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThan(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right)` Creates an expression that checks if the first expression is greater than the second expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression )` Creates an expression that checks if a field's value is greater than or equal to an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Creates an expression that checks if a field's value is greater than or equal to another value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right)` Creates an expression that checks if an expression is greater than or equal to a value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#greaterThanOrEqual(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right)` Creates an expression that checks if the first expression is greater than or equal to the second expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression ifExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression elseExpr)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression ifExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html elseValue)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` is absent, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html ifFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression elseExpr)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the value of the field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html ifFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html elseValue)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` is absent, else return the value of the field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression tryExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression catchExpr )` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument evaluation. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression tryExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression catchExpr)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression tryExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html catchValue)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#isAbsent(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that returns true if a field is absent. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#isAbsent(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value)` Creates an expression that returns true if a value is absent. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#isError(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that checks if a given expression produces an error. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#join(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter)` Creates an expression that joins the elements of an array into a string. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#join(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiterExpression )` Creates an expression that joins the elements of an array into a string. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#join(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter)` Creates an expression that joins the elements of an array field into a string. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#join(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiterExpression )` Creates an expression that joins the elements of an array field into a string. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#length(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that calculates the length of a string, array, map, vector, or blob expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#length(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that calculates the length of a string, array, map, vector, or blob field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an expression that checks if a field's value is less than an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Creates an expression that checks if a field's value is less than another value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right)` Creates an expression that checks if an expression is less than a value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThan(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right)` Creates an expression that checks if the first expression is less than the second expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an expression that checks if a field's value is less than or equal to an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Creates an expression that checks if a field's value is less than or equal to another value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right)` Creates an expression that checks if an expression is less than or equal to a value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#lessThanOrEqual(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right)` Creates an expression that checks if the first expression is less than or equal to the second expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#like(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern)` Creates an expression that performs a case-sensitive wildcard string comparison against a field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#like(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that performs a case-sensitive wildcard string comparison against a field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#like(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern)` Creates an expression that performs a case-sensitive wildcard string comparison. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#like(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that performs a case-sensitive wildcard string comparison. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ln(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ln(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ln(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ln(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression base)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html base)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression base)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html base)` Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log10(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log10(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log10(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log10(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMaximum(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others)` Creates an expression that returns the largest value between multiple input expressions or literal values. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMaximum(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others)` Creates an expression that returns the largest value between multiple input expressions or literal values. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMinimum(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others)` Creates an expression that returns the smallest value between multiple input expressions or literal values. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#logicalMinimum(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others)` Creates an expression that returns the smallest value between multiple input expressions or literal values. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#map(kotlin.collections.Map)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> elements)` Creates an expression that creates a Firestore map value from an input object. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression keyExpression)` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression keyExpression )` Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapMerge(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstMap, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondMap, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherMaps )` Creates an expression that merges multiple maps into a single map. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapMerge(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html firstMapFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondMap, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherMaps )` Creates an expression that merges multiple maps into a single map. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression key)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mapField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression key)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapRemove(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mapField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key)` Creates an expression that removes a key from the map produced by evaluating an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mod(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor)` Creates an expression that calculates the modulo (remainder) of dividing two numeric expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mod(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor)` Creates an expression that calculates the modulo (remainder) of dividing a numeric expression by a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mod(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor)` Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mod(kotlin.String,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor)` Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second)` Creates an expression that multiplies numeric expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second)` Creates an expression that multiplies numeric expressions with a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second)` Creates an expression that multiplies a numeric field with a numeric expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#multiply(kotlin.String,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second)` Creates an expression that multiplies a numeric field with a constant. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#not(com.google.firebase.firestore.pipeline.BooleanExpression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition)` Creates an expression that negates a boolean expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression)` Creates an expression that checks if a field's value is not equal to an expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(kotlin.String,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Creates an expression that checks if a field's value is not equal to another value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right)` Creates an expression that checks if an expression is not equal to a value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqual(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right)` Creates an expression that checks if two expressions are not equal. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression )` Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is not equal to all the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values )` Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is not equal to all the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression)` Creates an expression that checks if a field's value is not equal to all of the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,kotlin.collections.List)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values)` Creates an expression that checks if a field's value is not equal to all of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,kotlin.collections.List)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#nullValue()()` Constant for a null value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#or(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression conditions )` Creates an expression that performs a logical 'OR' operation. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression exponent)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html exponent)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression exponent)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html exponent)` Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#rawFunction(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates a 'raw' function expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern)` Creates an expression that checks if a string field contains a specified regular expression as a substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that checks if a string field contains a specified regular expression as a substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern )` Creates an expression that checks if a string expression contains a specified regular expression as a substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexContains(com.google.firebase.firestore.pipeline.Expression,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern )` Creates an expression that checks if a string expression contains a specified regular expression as a substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern)` Creates an expression that returns the first substring of a string field that matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that returns the first substring of a string field that matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern )` Creates an expression that returns the first substring of a string expression that matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFind(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that returns the first substring of a string expression that matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern)` Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern )` Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexFindAll(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern)` Creates an expression that checks if a string field matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that checks if a string field matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern )` Creates an expression that checks if a string field matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#regexMatch(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern)` Creates an expression that checks if a string field matches a specified regular expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#reverse(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that reverses a string value from the specified field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#reverse(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression)` Creates an expression that reverses a string. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#round(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that rounds `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#round(com.google.firebase.firestore.pipeline.Expression)` to nearest integer. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#round(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that rounds `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#round(kotlin.String)` to nearest integer. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression decimalPlace )` Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is negative. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr, int decimalPlace)` Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is negative. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression decimalPlace )` Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is negative. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField, int decimalPlace)` Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is negative. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#split(kotlin.String,com.google.firebase.firestore.Blob)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob delimiter)` Creates an expression that splits a blob field by a blob delimiter. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#split(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiter)` Creates an expression that splits a string or blob field by a delimiter. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#split(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter)` Creates an expression that splits a string or blob field by a string delimiter. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#split(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.Blob)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob delimiter)` Creates an expression that splits a blob by a blob delimiter. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#split(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiter)` Creates an expression that splits a string or blob by a delimiter. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#split(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter)` Creates an expression that splits a string or blob by a string delimiter. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr)` Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField)` Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression prefix)` Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prefix)` Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression prefix)` ``` // Check if the 'fullName' field starts with the value of the 'firstName' field startsWith(field("fullName"), field("firstName")) ``` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prefix)` Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherStrings)` Creates an expression that concatenates string expressions together. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherStrings)` Creates an expression that concatenates string expressions together. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstString, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherStrings)` Creates an expression that concatenates string expressions together. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringConcat(com.google.firebase.firestore.pipeline.Expression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstString, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherStrings )` Creates an expression that concatenates string expressions together. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression substring)` Creates an expression that checks if a string field contains a specified substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html substring)` Creates an expression that checks if a string field contains a specified substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression substring )` Creates an expression that checks if a string expression contains a specified substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringContains(com.google.firebase.firestore.pipeline.Expression,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html substring )` Creates an expression that checks if a string expression contains a specified substring. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringReverse(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Reverses the given string field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#stringReverse(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression str)` Reverses the given string expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#substring(kotlin.String,kotlin.Int,kotlin.Int)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, int index, int length)` Creates an expression that returns a substring of the given string. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#substring(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression index, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression length )` Creates an expression that returns a substring of the given string. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression minuend, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression subtrahend)` Creates an expression that subtracts two expressions. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression minuend, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html subtrahend)` Creates an expression that subtracts a constant value from a numeric expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(kotlin.String,com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression subtrahend)` Creates an expression that subtracts a numeric expressions from numeric field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#subtract(kotlin.String,kotlin.Number)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html subtrahend)` Creates an expression that subtracts a constant from numeric field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(kotlin.String,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount )` Creates an expression that adds a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(kotlin.String,kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit, long amount)` Creates an expression that adds a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount )` Creates an expression that adds a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampAdd(com.google.firebase.firestore.pipeline.Expression,kotlin.String,kotlin.Long)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit, long amount )` Creates an expression that adds a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(kotlin.String,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount )` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(kotlin.String,kotlin.String,kotlin.Long)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit, long amount )` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount )` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampSubtract(com.google.firebase.firestore.pipeline.Expression,kotlin.String,kotlin.Long)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit, long amount )` Creates an expression that subtracts a specified amount of time to a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMicros(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMicros(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that converts a timestamp field to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMillis(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixMillis(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that converts a timestamp field to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixSeconds(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampToUnixSeconds(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that converts a timestamp field to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity )` Creates an expression that truncates a timestamp to a specified granularity. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity)` Creates an expression that truncates a timestamp to a specified granularity. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity )` Creates an expression that truncates a timestamp to a specified granularity. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity )` Creates an expression that truncates a timestamp to a specified granularity. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,com.google.firebase.firestore.pipeline.Expression,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone )` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(kotlin.String,kotlin.String,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone )` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone )` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#timestampTruncate(com.google.firebase.firestore.pipeline.Expression,kotlin.String,kotlin.String)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone )` Creates an expression that truncates a timestamp to a specified granularity in a given timezone. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#toLower(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that converts a string field to lowercase. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#toLower(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression)` Creates an expression that converts a string expression to lowercase. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#toUpper(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that converts a string field to uppercase. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#toUpper(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression)` Creates an expression that converts a string expression to uppercase. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#trim(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that removes leading and trailing whitespace from a string field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#trim(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression)` Creates an expression that removes leading and trailing whitespace from a string expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#trimValue(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html valueToTrim)` Creates an expression that removes leading and trailing characters from a string field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#trimValue(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression valueToTrim )` Creates an expression that removes leading and trailing values from a expression. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#type(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that returns a string indicating the type of the value this expression evaluates to. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#type(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that returns a string indicating the type of the value this field evaluates to. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#unixMicrosToTimestamp(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that interprets an expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#unixMicrosToTimestamp(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that interprets a field's value as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#unixMillisToTimestamp(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that interprets an expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#unixMillisToTimestamp(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that interprets a field's value as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#unixSecondsToTimestamp(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates an expression that interprets an expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#unixSecondsToTimestamp(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that interprets a field's value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#vector(kotlin.DoubleArray)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector)` Create a vector constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#vector(com.google.firebase.firestore.VectorValue)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector)` Create a vector constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` value. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#vectorLength(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an expression that calculates the length (dimension) of a Firestore Vector. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#vectorLength(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vectorExpression)` Creates an expression that calculates the length (dimension) of a Firestore Vector. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#xor(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression conditions )` Creates an expression that performs a logical 'XOR' operation. |

## Public methods

### abs

```
public static final @NonNull Expression abs(@NonNull Expression numericExpr)
```

Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#abs(com.google.firebase.firestore.pipeline.Expression)`.

```
// Get the absolute value of the 'change' field.
abs(field("change"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the absolute value operation. |

### abs

```
public static final @NonNull Expression abs(@NonNull String numericField)
```

Creates an expression that returns the absolute value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#abs(kotlin.String)`.

```
// Get the absolute value of the 'change' field.
abs("change")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the absolute value operation. |

### add

```
public static final @NonNull Expression add(@NonNull Expression first, @NonNull Expression second)
```

Creates an expression that adds numeric expressions.

```
// Add the value of the 'quantity' field and the 'reserve' field.
add(field("quantity"), field("reserve"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first` | Numeric expression to add. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second` | Numeric expression to add. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### add

```
public static final @NonNull Expression add(@NonNull Expression first, @NonNull Number second)
```

Creates an expression that adds numeric expressions with a constant.

```
// Add 5 to the value of the 'quantity' field.
add(field("quantity"), 5)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first` | Numeric expression to add. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second` | Constant to add. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### add

```
public static final @NonNull Expression add(@NonNull String numericFieldName, @NonNull Expression second)
```

Creates an expression that adds a numeric field with a numeric expression.

```
// Add the value of the 'quantity' field and the 'reserve' field.
add("quantity", field("reserve"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName` | Numeric field to add. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second` | Numeric expression to add to field value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### add

```
public static final @NonNull Expression add(@NonNull String numericFieldName, @NonNull Number second)
```

Creates an expression that adds a numeric field with constant.

```
// Add 5 to the value of the 'quantity' field.
add("quantity", 5)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName` | Numeric field to add. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second` | Constant to add. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the addition operation. |

### and

```
public static final @NonNull BooleanExpression and(
    @NonNull BooleanExpression condition,
    @NonNull BooleanExpression conditions
)
```

Creates an expression that performs a logical 'AND' operation.

```
// Check if 'status' is "new" and 'priority' is greater than 1
and(field("status").equal("new"), field("priority").greaterThan(1))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition` | The first `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression conditions` | Additional `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression`s. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the logical 'AND' operation. |

### array

```
public static final @NonNull Expression array(@NonNull List<Object> elements)
```

Creates an expression that creates a Firestore array value from an input array.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://developer.android.com/reference/kotlin/java/lang/Object.html> elements` | The input array to evaluate in the expression. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the array function. |

### array

```
public static final @NonNull Expression array(Object elements)
```

Creates an expression that creates a Firestore array value from an input array.

```
// Create an array of numbers
array(1, 2, 3)

// Create an array containing a field value and a constant
array(field("quantity"), 10)
```

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/Object.html elements` | The input array to evaluate in the expression. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the array function. |

### arrayConcat

```
public static final @NonNull Expression arrayConcat(
    @NonNull Expression firstArray,
    @NonNull Object secondArray,
    @NonNull Object otherArrays
)
```

Creates an expression that concatenates an array with other arrays.

```
// Combine the 'items' array with another array field.
arrayConcat(field("items"), field("otherItems"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstArray` | The first array expression to concatenate to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html secondArray` | An array expression or array literal to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayConcat

```
public static final @NonNull Expression arrayConcat(
    @NonNull Expression firstArray,
    @NonNull Expression secondArray,
    @NonNull Object otherArrays
)
```

Creates an expression that concatenates an array with other arrays.

```
// Combine the 'items' array with another array field.
arrayConcat(field("items"), field("otherItems"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstArray` | The first array expression to concatenate to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondArray` | An expression that evaluates to array to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayConcat

```
public static final @NonNull Expression arrayConcat(
    @NonNull String firstArrayField,
    @NonNull Object secondArray,
    @NonNull Object otherArrays
)
```

Creates an expression that concatenates a field's array value with other arrays.

```
// Combine the 'items' array with a literal array.
arrayConcat("items", listOf("a", "b"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html firstArrayField` | The name of field that contains first array to concatenate to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html secondArray` | An array expression or array literal to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayConcat

```
public static final @NonNull Expression arrayConcat(
    @NonNull String firstArrayField,
    @NonNull Expression secondArray,
    @NonNull Object otherArrays
)
```

Creates an expression that concatenates a field's array value with other arrays.

```
// Combine the 'items' array with another array field.
arrayConcat("items", field("otherItems"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html firstArrayField` | The name of field that contains first array to concatenate to. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondArray` | An expression that evaluates to array to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherArrays` | Optional additional array expressions or array literals to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayConcat operation. |

### arrayContains

```
public static final @NonNull BooleanExpression arrayContains(@NonNull Expression array, @NonNull Object element)
```

Creates an expression that checks if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)`.

```
// Check if the 'sizes' array contains the value from the 'selectedSize' field
arrayContains(field("sizes"), field("selectedSize"))

// Check if the 'colors' array contains "red"
arrayContains(field("colors"), "red")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html element` | The element to search for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContains

```
public static final @NonNull BooleanExpression arrayContains(@NonNull Expression array, @NonNull Expression element)
```

Creates an expression that checks if the array contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression element` | The element to search for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContains

```
public static final @NonNull BooleanExpression arrayContains(@NonNull String arrayFieldName, @NonNull Object element)
```

Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,kotlin.Any)`.

```
// Check if the 'colors' array contains "red"
arrayContains("colors", "red")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of field that contains array to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html element` | The element to search for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContains

```
public static final @NonNull BooleanExpression arrayContains(@NonNull String arrayFieldName, @NonNull Expression element)
```

Creates an expression that checks if the array field contains a specific `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContains(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'sizes' array contains the value from the 'selectedSize' field
arrayContains("sizes", field("selectedSize"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of field that contains array to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression element` | The element to search for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContains operation. |

### arrayContainsAll

```
public static final @NonNull BooleanExpression arrayContainsAll(
    @NonNull Expression array,
    @NonNull Expression arrayExpression
)
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains all elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'tags' array contains both of the values from field "tag1" and the literal value "tag2"
arrayContainsAll(field("tags"), array(field("tag1"), "tag2"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAll

```
public static final @NonNull BooleanExpression arrayContainsAll(
    @NonNull Expression array,
    @NonNull List<@NonNull Object> values
)
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains all the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```
// Check if the 'tags' array contains both the value in field "tag1" and the literal value "tag2"
arrayContainsAll(field("tags"), listOf(field("tag1"), "tag2"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAll

```
public static final @NonNull BooleanExpression arrayContainsAll(
    @NonNull String arrayFieldName,
    @NonNull Expression arrayExpression
)
```

Creates an expression that checks if array field contains all elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'permissions' array contains all the required permissions
arrayContainsAll("permissions", field("requiredPermissions"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of field that contains array to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAll

```
public static final @NonNull BooleanExpression arrayContainsAll(
    @NonNull String arrayFieldName,
    @NonNull List<@NonNull Object> values
)
```

Creates an expression that checks if array field contains all the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAll(kotlin.String,kotlin.collections.List)`.

```
// Check if the 'tags' array contains both "internal" and "public"
arrayContainsAll("tags", listOf("internal", "public"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of field that contains array to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAll operation. |

### arrayContainsAny

```
public static final @NonNull BooleanExpression arrayContainsAny(
    @NonNull Expression array,
    @NonNull Expression arrayExpression
)
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` contains any elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'groups' array contains either the value from the 'userGroup' field
// or the value "guest"
arrayContainsAny(field("groups"), array(field("userGroup"), "guest"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayContainsAny

```
public static final @NonNull BooleanExpression arrayContainsAny(
    @NonNull Expression array,
    @NonNull List<@NonNull Object> values
)
```

Creates an expression that checks if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)` contains any of the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```
// Check if the 'categories' array contains either values from field "cate1" or "cate2"
arrayContainsAny(field("categories"), listOf(field("cate1"), field("cate2")))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayContainsAny

```
public static final @NonNull BooleanExpression arrayContainsAny(
    @NonNull String arrayFieldName,
    @NonNull Expression arrayExpression
)
```

Creates an expression that checks if array field contains any elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'userGroups' array contains any of the 'targetGroups'
arrayContainsAny("userGroups", field("targetGroups"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of field that contains array to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayContainsAny

```
public static final @NonNull BooleanExpression arrayContainsAny(
    @NonNull String arrayFieldName,
    @NonNull List<@NonNull Object> values
)
```

Creates an expression that checks if array field contains any of the specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayContainsAny(kotlin.String,kotlin.collections.List)`.

```
// Check if the 'roles' array contains "admin" or "editor"
arrayContainsAny("roles", listOf("admin", "editor"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of field that contains array to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The elements to check for in the array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the arrayContainsAny operation. |

### arrayGet

```
public static final @NonNull Expression arrayGet(@NonNull Expression array, @NonNull Expression offset)
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```
// Return the value in the tags field array at index specified by field 'favoriteTag'.
arrayGet(field("tags"), field("favoriteTag"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | An `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` evaluating to an array. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression offset` | An Expression evaluating to the index of the element to return. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayGet

```
public static final @NonNull Expression arrayGet(@NonNull Expression array, int offset)
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```
// Return the value in the 'tags' field array at index `1`.
arrayGet(field("tags"), 1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | An `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` evaluating to an array. |
| `int offset` | The index of the element to return. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayGet

```
public static final @NonNull Expression arrayGet(@NonNull String arrayFieldName, @NonNull Expression offset)
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```
// Return the value in the tags field array at index specified by field 'favoriteTag'.
arrayGet("tags", field("favoriteTag"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of an array field. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression offset` | An Expression evaluating to the index of the element to return. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayGet

```
public static final @NonNull Expression arrayGet(@NonNull String arrayFieldName, int offset)
```

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

```
// Return the value in the 'tags' field array at index `1`.
arrayGet("tags", 1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of an array field. |
| `int offset` | The index of the element to return. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayOffset operation. |

### arrayLength

```
public static final @NonNull Expression arrayLength(@NonNull Expression array)
```

Creates an expression that calculates the length of an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayLength(com.google.firebase.firestore.pipeline.Expression)` expression.

```
// Get the number of items in the 'cart' array
arrayLength(field("cart"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to calculate the length of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length of the array. |

### arrayLength

```
public static final @NonNull Expression arrayLength(@NonNull String arrayFieldName)
```

Creates an expression that calculates the length of an array field.

```
// Get the number of items in the 'cart' array
arrayLength("cart")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of the field containing an array to calculate the length of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length of the array. |

### arrayReverse

```
public static final @NonNull Expression arrayReverse(@NonNull Expression array)
```

Reverses the order of elements in the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#arrayReverse(com.google.firebase.firestore.pipeline.Expression)`.

```
// Reverse the value of the 'myArray' field.
arrayReverse(field("myArray"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to reverse. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayReverse operation. |

### arrayReverse

```
public static final @NonNull Expression arrayReverse(@NonNull String arrayFieldName)
```

Reverses the order of elements in the array field.

```
// Reverse the value of the 'myArray' field.
arrayReverse("myArray")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of field that contains the array to reverse. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the arrayReverse operation. |

### arraySum

```
public static final @NonNull Expression arraySum(@NonNull Expression array)
```

Creates an expression that returns the sum of the elements in an array.

```
// Get the sum of elements in the 'scores' array.
arraySum(field("scores"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression array` | The array expression to sum. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the sum of the array elements. |

### arraySum

```
public static final @NonNull Expression arraySum(@NonNull String arrayFieldName)
```

Creates an expression that returns the sum of the elements in an array field.

```
// Get the sum of elements in the 'scores' array.
arraySum("scores")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of the field containing the array to sum. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the sum of the array elements. |

### bitAnd

```
public static final @NonNull Expression bitAnd(@NonNull Expression bits, @NonNull byte[] bitsOther)
```

Creates an expression that applies a bitwise AND operation between an expression and a constant.

```
// Bitwise AND the value of the 'flags' field with a constant mask.
bitAnd(field("flags"), byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther` | A constant byte array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitAnd

```
public static final @NonNull Expression bitAnd(@NonNull Expression bits, @NonNull Expression bitsOther)
```

Creates an expression that applies a bitwise AND operation between two expressions.

```
// Bitwise AND the value of the 'flags' field with the value of the 'mask' field.
bitAnd(field("flags"), field("mask"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitAnd

```
public static final @NonNull Expression bitAnd(@NonNull String bitsFieldName, @NonNull byte[] bitsOther)
```

Creates an expression that applies a bitwise AND operation between an field and constant.

```
// Bitwise AND the value of the 'flags' field with a constant mask.
bitAnd("flags", byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther` | A constant byte array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitAnd

```
public static final @NonNull Expression bitAnd(@NonNull String bitsFieldName, @NonNull Expression bitsOther)
```

Creates an expression that applies a bitwise AND operation between an field and an expression.

```
// Bitwise AND the value of the 'flags' field with the value of the 'mask' field.
bitAnd("flags", field("mask"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise AND operation. |

### bitLeftShift

```
public static final @NonNull Expression bitLeftShift(@NonNull Expression bits, int number)
```

Creates an expression that applies a bitwise left shift operation between an expression and a constant.

```
// Left shift the value of the 'bits' field by 2.
bitLeftShift(field("bits"), 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `int number` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitLeftShift

```
public static final @NonNull Expression bitLeftShift(@NonNull Expression bits, @NonNull Expression numberExpr)
```

Creates an expression that applies a bitwise left shift operation between two expressions.

```
// Left shift the value of the 'bits' field by the value of the 'shift' field.
bitLeftShift(field("bits"), field("shift"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitLeftShift

```
public static final @NonNull Expression bitLeftShift(@NonNull String bitsFieldName, int number)
```

Creates an expression that applies a bitwise left shift operation between a field and a constant.

```
// Left shift the value of the 'bits' field by 2.
bitLeftShift("bits", 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `int number` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitLeftShift

```
public static final @NonNull Expression bitLeftShift(@NonNull String bitsFieldName, @NonNull Expression numberExpr)
```

Creates an expression that applies a bitwise left shift operation between a field and an expression.

```
// Left shift the value of the 'bits' field by the value of the 'shift' field.
bitLeftShift("bits", field("shift"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise left shift operation. |

### bitNot

```
public static final @NonNull Expression bitNot(@NonNull Expression bits)
```

Creates an expression that applies a bitwise NOT operation to an expression.

```
// Bitwise NOT the value of the 'flags' field.
bitNot(field("flags"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise NOT operation. |

### bitNot

```
public static final @NonNull Expression bitNot(@NonNull String bitsFieldName)
```

Creates an expression that applies a bitwise NOT operation to a field.

```
// Bitwise NOT the value of the 'flags' field.
bitNot("flags")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise NOT operation. |

### bitOr

```
public static final @NonNull Expression bitOr(@NonNull Expression bits, @NonNull byte[] bitsOther)
```

Creates an expression that applies a bitwise OR operation between an expression and a constant.

```
// Bitwise OR the value of the 'flags' field with a constant mask.
bitOr(field("flags"), byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther` | A constant byte array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitOr

```
public static final @NonNull Expression bitOr(@NonNull Expression bits, @NonNull Expression bitsOther)
```

Creates an expression that applies a bitwise OR operation between two expressions.

```
// Bitwise OR the value of the 'flags' field with the value of the 'mask' field.
bitOr(field("flags"), field("mask"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitOr

```
public static final @NonNull Expression bitOr(@NonNull String bitsFieldName, @NonNull byte[] bitsOther)
```

Creates an expression that applies a bitwise OR operation between an field and constant.

```
// Bitwise OR the value of the 'flags' field with a constant mask.
bitOr("flags", byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther` | A constant byte array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitOr

```
public static final @NonNull Expression bitOr(@NonNull String bitsFieldName, @NonNull Expression bitsOther)
```

Creates an expression that applies a bitwise OR operation between an field and an expression.

```
// Bitwise OR the value of the 'flags' field with the value of the 'mask' field.
bitOr("flags", field("mask"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise OR operation. |

### bitRightShift

```
public static final @NonNull Expression bitRightShift(@NonNull Expression bits, int number)
```

Creates an expression that applies a bitwise right shift operation between an expression and a constant.

```
// Right shift the value of the 'bits' field by 2.
bitRightShift(field("bits"), 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `int number` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitRightShift

```
public static final @NonNull Expression bitRightShift(@NonNull Expression bits, @NonNull Expression numberExpr)
```

Creates an expression that applies a bitwise right shift operation between two expressions.

```
// Right shift the value of the 'bits' field by the value of the 'shift' field.
bitRightShift(field("bits"), field("shift"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitRightShift

```
public static final @NonNull Expression bitRightShift(@NonNull String bitsFieldName, int number)
```

Creates an expression that applies a bitwise right shift operation between a field and a constant.

```
// Right shift the value of the 'bits' field by 2.
bitRightShift("bits", 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `int number` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitRightShift

```
public static final @NonNull Expression bitRightShift(
    @NonNull String bitsFieldName,
    @NonNull Expression numberExpr
)
```

Creates an expression that applies a bitwise right shift operation between a field and an expression.

```
// Right shift the value of the 'bits' field by the value of the 'shift' field.
bitRightShift("bits", field("shift"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numberExpr` | The number of bits to shift. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise right shift operation. |

### bitXor

```
public static final @NonNull Expression bitXor(@NonNull Expression bits, @NonNull byte[] bitsOther)
```

Creates an expression that applies a bitwise XOR operation between an expression and a constant.

```
// Bitwise XOR the value of the 'flags' field with a constant mask.
bitXor(field("flags"), byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther` | A constant byte array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### bitXor

```
public static final @NonNull Expression bitXor(@NonNull Expression bits, @NonNull Expression bitsOther)
```

Creates an expression that applies a bitwise XOR operation between two expressions.

```
// Bitwise XOR the value of the 'flags' field with the value of the 'mask' field.
bitXor(field("flags"), field("mask"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bits` | An expression that returns bits when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### bitXor

```
public static final @NonNull Expression bitXor(@NonNull String bitsFieldName, @NonNull byte[] bitsOther)
```

Creates an expression that applies a bitwise XOR operation between an field and constant.

```
// Bitwise XOR the value of the 'flags' field with a constant mask.
bitXor("flags", byteArrayOf(0b00001111))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] bitsOther` | A constant byte array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### bitXor

```
public static final @NonNull Expression bitXor(@NonNull String bitsFieldName, @NonNull Expression bitsOther)
```

Creates an expression that applies a bitwise XOR operation between an field and an expression.

```
// Bitwise XOR the value of the 'flags' field with the value of the 'mask' field.
bitXor("flags", field("mask"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html bitsFieldName` | Name of field that contains bits data. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression bitsOther` | An expression that returns bits when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the bitwise XOR operation. |

### byteLength

```
public static final @NonNull Expression byteLength(@NonNull String fieldName)
```

Creates an expression that calculates the length of a string represented by a field in UTF-8 bytes, or just the length of a Blob.

```
// Calculate the length of the 'myString' field in bytes.
byteLength("myString")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length of the string in bytes. |

### byteLength

```
public static final @NonNull Expression byteLength(@NonNull Expression value)
```

Creates an expression that calculates the length of a string in UTF-8 bytes, or just the length of a Blob.

```
// Calculate the length of the 'myString' field in bytes.
byteLength("myString")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value` | The expression representing the string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length of the string in bytes. |

### ceil

```
public static final @NonNull Expression ceil(@NonNull Expression numericExpr)
```

Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(com.google.firebase.firestore.pipeline.Expression)`.

```
// Compute the ceiling of the 'price' field.
ceil(field("price"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the ceil operation. |

### ceil

```
public static final @NonNull Expression ceil(@NonNull String numericField)
```

Creates an expression that returns the smallest integer that isn't less than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ceil(kotlin.String)`.

```
// Compute the ceiling of the 'price' field.
ceil("price")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the ceil operation. |

### charLength

```
public static final @NonNull Expression charLength(@NonNull Expression expr)
```

Creates an expression that calculates the character length of a string expression in UTF8.

```
// Get the character length of the 'name' field in UTF-8.
charLength("name")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the charLength operation. |

### charLength

```
public static final @NonNull Expression charLength(@NonNull String fieldName)
```

Creates an expression that calculates the character length of a string field in UTF8.

```
// Get the character length of the 'name' field in UTF-8.
charLength("name")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the charLength operation. |

### collectionId

```
public static final @NonNull Expression collectionId(@NonNull Expression path)
```

Creates an expression that returns the collection ID from a path.

```
// Get the collection ID from the 'path' field
collectionId(field("path"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression path` | An expression the evaluates to a path. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the collectionId operation. |

### collectionId

```
public static final @NonNull Expression collectionId(@NonNull String pathField)
```

Creates an expression that returns the collection ID from a path.

```
// Get the collection ID from a path field
collectionId("pathField")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pathField` | The string representation of the path. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the collectionId operation. |

### concat

```
public static final @NonNull Expression concat(
    @NonNull Expression first,
    @NonNull Object second,
    @NonNull Object others
)
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```
// Concatenate a field with a literal string.
concat(field("firstName"), "Doe")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first` | The first expression to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html second` | The second value to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Additional values to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### concat

```
public static final @NonNull Expression concat(
    @NonNull Expression first,
    @NonNull Expression second,
    @NonNull Object others
)
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```
// Concatenate the 'firstName' and 'lastName' fields with a space in between.
concat(field("firstName"), " ", field("lastName"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first` | The first expression to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second` | The second expression to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Additional expressions to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### concat

```
public static final @NonNull Expression concat(@NonNull String first, @NonNull Object second, @NonNull Object others)
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```
// Concatenate a field name with a literal string.
concat("firstName", "Doe")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html first` | The name of the field containing the first value to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html second` | The second value to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Additional values to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### concat

```
public static final @NonNull Expression concat(
    @NonNull String first,
    @NonNull Expression second,
    @NonNull Object others
)
```

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

```
// Concatenate a field name with an expression.
concat("firstName", field("lastName"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html first` | The name of the field containing the first value to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second` | The second expression to concatenate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Additional expressions to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenation. |

### conditional

```
public static final @NonNull Expression conditional(
    @NonNull BooleanExpression condition,
    @NonNull Expression thenExpr,
    @NonNull Expression elseExpr
)
```

Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if a condition is true or an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` expression if the condition is false.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition` | The condition to evaluate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression thenExpr` | The expression to evaluate if the condition is true. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression elseExpr` | The expression to evaluate if the condition is false. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the conditional operation. |

### conditional

```
public static final @NonNull Expression conditional(
    @NonNull BooleanExpression condition,
    @NonNull Object thenValue,
    @NonNull Object elseValue
)
```

Creates a conditional expression that evaluates to a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if a condition is true or an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#conditional(com.google.firebase.firestore.pipeline.BooleanExpression,kotlin.Any,kotlin.Any)` if the condition is false.

```
// If the 'quantity' field is greater than 10, return "High", otherwise return "Low"
conditional(field("quantity").greaterThan(10), "High", "Low")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition` | The condition to evaluate. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html thenValue` | Value if the condition is true. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html elseValue` | Value if the condition is false. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the conditional operation. |

### constant

```
public static final @NonNull Expression constant(@NonNull DocumentReference ref)
```

Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` value.

```
// val firestore = FirebaseFirestore.getInstance()
// val docRef = firestore.collection("cities").document("SF")
// constant(docRef)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference ref` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull Blob value)
```

Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob` value.

```
// Create a constant with a Blob
constant(Blob.fromBytes(byteArrayOf(0x48, 0x65, 0x6c, 0x6c, 0x6f))) // "Hello"
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob value` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull BooleanExpression constant(boolean value)
```

Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value.

```
// Create a constant with the value true
constant(true)
```

| Parameters |
|---|---|
| `boolean value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull byte[] value)
```

Create a constant for a bytes value.

```
// Create a constant with a byte array
constant(byteArrayOf(0x48, 0x65, 0x6c, 0x6c, 0x6f)) // "Hello"
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html byte[] value` | The bytes value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull Date value)
```

Create a constant for a `https://developer.android.com/reference/kotlin/java/util/Date.html` value.

```
// Create a constant with the current date
constant(Date())
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Date.html value` | The `https://developer.android.com/reference/kotlin/java/util/Date.html` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull GeoPoint value)
```

Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint` value.

```
// Create a constant with a GeoPoint
constant(GeoPoint(37.7749, -122.4194))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint value` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/GeoPoint` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull Number value)
```

Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` value.

```
// Create a constant with the value 123
constant(123)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-number/index.html` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull String value)
```

Create a constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value.

```
// Create a constant with the value "hello"
constant("hello")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull Timestamp value)
```

Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` value.

```
// Create a constant with the current timestamp
constant(Timestamp.now())
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp value` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/Timestamp` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### constant

```
public static final @NonNull Expression constant(@NonNull VectorValue value)
```

Create a constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` value.

```
// Create a constant with a VectorValue
constant(VectorValue(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue value` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### cosineDistance

```
public static final @NonNull Expression cosineDistance(@NonNull Expression vector1, @NonNull double[] vector2)
```

Calculates the Cosine distance between vector expression and a vector literal.

```
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance(field("location"), doubleArrayOf(37.7749, -122.4194))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an Expression) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector2` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
public static final @NonNull Expression cosineDistance(@NonNull Expression vector1, @NonNull Expression vector2)
```

Calculates the Cosine distance between two vector expressions.

```
// Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
cosineDistance(field("userVector"), field("itemVector"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an Expression) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector2` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
public static final @NonNull Expression cosineDistance(@NonNull Expression vector1, @NonNull VectorValue vector2)
```

Calculates the Cosine distance between vector expression and a vector literal.

```
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance(field("location"), VectorValue.from(listOf(37.7749, -122.4194)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression`) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector2` | The other vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
public static final @NonNull Expression cosineDistance(@NonNull String vectorFieldName, @NonNull double[] vector)
```

Calculates the Cosine distance between a vector field and a vector literal.

```
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance("location", doubleArrayOf(37.7749, -122.4194))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
public static final @NonNull Expression cosineDistance(@NonNull String vectorFieldName, @NonNull Expression vector)
```

Calculates the Cosine distance between a vector field and a vector expression.

```
// Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
cosineDistance("userVector", field("itemVector"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### cosineDistance

```
public static final @NonNull Expression cosineDistance(
    @NonNull String vectorFieldName,
    @NonNull VectorValue vector
)
```

Calculates the Cosine distance between a vector field and a vector literal.

```
// Calculate the Cosine distance between the 'location' field and a target location
cosineDistance("location", VectorValue.from(listOf(37.7749, -122.4194)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector` | The other vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the cosine distance between the two vectors. |

### currentTimestamp

```
public static final @NonNull Expression currentTimestamp()
```

Creates an expression that evaluates to the current server timestamp.

```
// Get the current server timestamp
currentTimestamp()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the current server timestamp. |

### divide

```
public static final @NonNull Expression divide(@NonNull Expression dividend, @NonNull Expression divisor)
```

Creates an expression that divides two numeric expressions.

```
// Divide the 'total' field by the 'count' field
divide(field("total"), field("count"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend` | The numeric expression to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor` | The numeric expression to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the division operation. |

### divide

```
public static final @NonNull Expression divide(@NonNull Expression dividend, @NonNull Number divisor)
```

Creates an expression that divides a numeric expression by a constant.

```
// Divide the 'value' field by 10
divide(field("value"), 10)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend` | The numeric expression to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor` | The constant to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the division operation. |

### divide

```
public static final @NonNull Expression divide(@NonNull String dividendFieldName, @NonNull Expression divisor)
```

Creates an expression that divides numeric field by a numeric expression.

```
// Divide the 'total' field by the 'count' field.
divide("total", field("count"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName` | The numeric field name to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor` | The numeric expression to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the divide operation. |

### divide

```
public static final @NonNull Expression divide(@NonNull String dividendFieldName, @NonNull Number divisor)
```

Creates an expression that divides a numeric field by a constant.

```
// Divide the 'total' field by 2.
divide("total", 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName` | The numeric field name to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor` | The constant to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the divide operation. |

### documentId

```
public static final @NonNull Expression documentId(@NonNull DocumentReference docRef)
```

Creates an expression that returns the document ID from a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference docRef` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the documentId operation. |

### documentId

```
public static final @NonNull Expression documentId(@NonNull Expression documentPath)
```

Creates an expression that returns the document ID from a path.

```
// Get the document ID from the 'path' field
documentId(field("path"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression documentPath` | An expression the evaluates to document path. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the documentId operation. |

### documentId

```
public static final @NonNull Expression documentId(@NonNull String documentPath)
```

Creates an expression that returns the document ID from a path.

```
// Get the document ID from a path string
documentId("projects/p/databases/d/documents/c/d")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html documentPath` | The string representation of the document path. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the documentId operation. |

### dotProduct

```
public static final @NonNull Expression dotProduct(@NonNull Expression vector1, @NonNull double[] vector2)
```

Calculates the dot product distance between vector expression and a vector literal.

```
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct(field("vector"), doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an Expression) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector2` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
public static final @NonNull Expression dotProduct(@NonNull Expression vector1, @NonNull Expression vector2)
```

Calculates the dot product distance between two vector expressions.

```
// Calculate the dot product between the 'userVector' field and the 'itemVector' field
dotProduct(field("userVector"), field("itemVector"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an Expression) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector2` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
public static final @NonNull Expression dotProduct(@NonNull Expression vector1, @NonNull VectorValue vector2)
```

Calculates the dot product distance between vector expression and a vector literal.

```
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct(field("vector"), VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression`) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector2` | The other vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
public static final @NonNull Expression dotProduct(@NonNull String vectorFieldName, @NonNull double[] vector)
```

Calculates the dot product distance between vector field and a vector literal.

```
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct("vector", doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
public static final @NonNull Expression dotProduct(@NonNull String vectorFieldName, @NonNull Expression vector)
```

Calculates the dot product distance between a vector field and a vector expression.

```
// Calculate the dot product between the 'userVector' field and the 'itemVector' field
dotProduct("userVector", field("itemVector"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### dotProduct

```
public static final @NonNull Expression dotProduct(@NonNull String vectorFieldName, @NonNull VectorValue vector)
```

Calculates the dot product distance between a vector field and a vector literal.

```
// Calculate the dot product between the 'vector' field and a constant vector
dotProduct("vector", VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector` | The other vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the dot product distance between the two vectors. |

### endsWith

```
public static final @NonNull BooleanExpression endsWith(@NonNull String fieldName, @NonNull Expression suffix)
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'url' field ends with the value of the 'extension' field
endsWith("url", field("extension"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of field that contains a string to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression suffix` | The suffix string expression to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### endsWith

```
public static final @NonNull BooleanExpression endsWith(@NonNull String fieldName, @NonNull String suffix)
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(kotlin.String,kotlin.String)`.

```
// Check if the 'filename' field ends with ".txt"
endsWith("filename", ".txt")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of field that contains a string to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html suffix` | The suffix string to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### endsWith

```
public static final @NonNull BooleanExpression endsWith(@NonNull Expression stringExpr, @NonNull Expression suffix)
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'url' field ends with the value of the 'extension' field
endsWith(field("url"), field("extension"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr` | The expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression suffix` | The suffix string expression to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### endsWith

```
public static final @NonNull BooleanExpression endsWith(@NonNull Expression stringExpr, @NonNull String suffix)
```

Creates an expression that checks if a string expression ends with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#endsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`.

```
// Check if the 'filename' field ends with ".txt"
endsWith(field("filename"), ".txt")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr` | The expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html suffix` | The suffix string to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'ends with' comparison. |

### equal

```
public static final @NonNull BooleanExpression equal(@NonNull String fieldName, @NonNull Expression expression)
```

Creates an expression that checks if a field's value is equal to an expression.

```
// Check if the 'age' field is equal to the 'limit' field
equal("age", field("limit"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equal

```
public static final @NonNull BooleanExpression equal(@NonNull String fieldName, @NonNull Object value)
```

Creates an expression that checks if a field's value is equal to another value.

```
// Check if the 'city' field is equal to string constant "London"
equal("city", "London")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equal

```
public static final @NonNull BooleanExpression equal(@NonNull Expression left, @NonNull Object right)
```

Creates an expression that checks if an expression is equal to a value.

```
// Check if the 'age' field is equal to 21
equal(field("age"), 21)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equal

```
public static final @NonNull BooleanExpression equal(@NonNull Expression left, @NonNull Expression right)
```

Creates an expression that checks if two expressions are equal.

```
// Check if the 'age' field is equal to an expression
equal(field("age"), field("minAge").add(10))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right` | The second expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the equality comparison. |

### equalAny

```
public static final @NonNull BooleanExpression equalAny(
    @NonNull Expression expression,
    @NonNull Expression arrayExpression
)
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is equal to any of the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'category' field is in the 'availableCategories' array field.
equalAny(field("category"), field("availableCategories"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression whose results to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### equalAny

```
public static final @NonNull BooleanExpression equalAny(
    @NonNull Expression expression,
    @NonNull List<@NonNull Object> values
)
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is equal to any of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```
// Check if the 'category' field is either "Electronics" or the value of the 'primaryType' field.
equalAny(field("category"), listOf("Electronics", field("primaryType")))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression whose results to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The values to check against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### equalAny

```
public static final @NonNull BooleanExpression equalAny(@NonNull String fieldName, @NonNull Expression arrayExpression)
```

Creates an expression that checks if a field's value is equal to any of the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'category' field is in the 'availableCategories' array field.
equalAny("category", field("availableCategories"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### equalAny

```
public static final @NonNull BooleanExpression equalAny(@NonNull String fieldName, @NonNull List<@NonNull Object> values)
```

Creates an expression that checks if a field's value is equal to any of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#equalAny(kotlin.String,kotlin.collections.List)` .

```
// Check if the 'category' field is either "Electronics" or "Apparel".
equalAny("category", listOf("Electronics", "Apparel"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The values to check against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'IN' comparison. |

### euclideanDistance

```
public static final @NonNull Expression euclideanDistance(@NonNull Expression vector1, @NonNull double[] vector2)
```

Calculates the Euclidean distance between vector expression and a vector literal.

```
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance(field("vector"), doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an Expression) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector2` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
public static final @NonNull Expression euclideanDistance(@NonNull Expression vector1, @NonNull Expression vector2)
```

Calculates the Euclidean distance between two vector expressions.

```
// Calculate the Euclidean distance between the 'userVector' field and the 'itemVector' field
euclideanDistance(field("userVector"), field("itemVector"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an Expression) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector2` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
public static final @NonNull Expression euclideanDistance(
    @NonNull Expression vector1,
    @NonNull VectorValue vector2
)
```

Calculates the Euclidean distance between vector expression and a vector literal.

```
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance(field("vector"), VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector1` | The first vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression`) to compare against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector2` | The other vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
public static final @NonNull Expression euclideanDistance(
    @NonNull String vectorFieldName,
    @NonNull double[] vector
)
```

Calculates the Euclidean distance between a vector field and a vector literal.

```
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance("vector", doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector` | The other vector (as an array of doubles) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
public static final @NonNull Expression euclideanDistance(
    @NonNull String vectorFieldName,
    @NonNull Expression vector
)
```

Calculates the Euclidean distance between a vector field and a vector expression.

```
// Calculate the Euclidean distance between the 'userVector' field and the 'itemVector' field
euclideanDistance("userVector", field("itemVector"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vector` | The other vector (represented as an Expression) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### euclideanDistance

```
public static final @NonNull Expression euclideanDistance(
    @NonNull String vectorFieldName,
    @NonNull VectorValue vector
)
```

Calculates the Euclidean distance between a vector field and a vector literal.

```
// Calculate the Euclidean distance between the 'vector' field and a constant vector
euclideanDistance("vector", VectorValue.from(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html vectorFieldName` | The name of the field containing the first vector. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector` | The other vector (represented as an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue`) to compare against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the Euclidean distance between the two vectors. |

### exists

```
public static final @NonNull BooleanExpression exists(@NonNull String fieldName)
```

Creates an expression that checks if a field exists.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to check. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the exists check. |

### exists

```
public static final @NonNull BooleanExpression exists(@NonNull Expression value)
```

Creates an expression that checks if a field exists.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value` | An expression evaluates to the name of the field to check. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the exists check. |

### exp

```
public static final @NonNull Expression exp(@NonNull Expression numericExpr)
```

Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exp(com.google.firebase.firestore.pipeline.Expression)`.

```
// Compute e to the power of the 'value' field.
exp(field("value"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the exponentiation. |

### exp

```
public static final @NonNull Expression exp(@NonNull String numericField)
```

Creates an expression that returns Euler's number e raised to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#exp(kotlin.String)`.

```
// Compute e to the power of the 'value' field.
exp("value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the exponentiation. |

### field

```
public static final @NonNull Field field(@NonNull FieldPath fieldPath)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path.

The path can be a simple field name (e.g., "name") or a dot-separated path to a nested field (e.g., "address.city").

```
// Get the 'address.city' field
field(FieldPath.of("address", "city"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath fieldPath` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath` to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` instance representing the specified path. |

### field

```
public static final @NonNull Field field(@NonNull String name)
```

Creates a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` instance representing the field at the given path.

The path can be a simple field name (e.g., "name") or a dot-separated path to a nested field (e.g., "address.city").

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The path to the field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` instance representing the specified path. |

### floor

```
public static final @NonNull Expression floor(@NonNull Expression numericExpr)
```

Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#floor(com.google.firebase.firestore.pipeline.Expression)`

```
// Compute the floor of the 'price' field.
floor(field("price"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the floor operation. |

### floor

```
public static final @NonNull Expression floor(@NonNull String numericField)
```

Creates an expression that returns the largest integer that is not greater than `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#floor(kotlin.String)`.

```
// Compute the floor of the 'price' field.
floor("price")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the floor operation. |

### greaterThan

```
public static final @NonNull BooleanExpression greaterThan(@NonNull String fieldName, @NonNull Expression expression)
```

Creates an expression that checks if a field's value is greater than an expression.

```
// Check if the 'age' field is greater than the 'limit' field
greaterThan("age", field("limit"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThan

```
public static final @NonNull BooleanExpression greaterThan(@NonNull String fieldName, @NonNull Object value)
```

Creates an expression that checks if a field's value is greater than another value.

```
// Check if the 'price' field is greater than 100
greaterThan("price", 100)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThan

```
public static final @NonNull BooleanExpression greaterThan(@NonNull Expression left, @NonNull Object right)
```

Creates an expression that checks if an expression is greater than a value.

```
// Check if the 'price' field is greater than 100
greaterThan(field("price"), 100)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThan

```
public static final @NonNull BooleanExpression greaterThan(@NonNull Expression left, @NonNull Expression right)
```

Creates an expression that checks if the first expression is greater than the second expression.

```
// Check if the 'age' field is greater than the 'limit' field
greaterThan(field("age"), field("limit"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right` | The second expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than comparison. |

### greaterThanOrEqual

```
public static final @NonNull BooleanExpression greaterThanOrEqual(
    @NonNull String fieldName,
    @NonNull Expression expression
)
```

Creates an expression that checks if a field's value is greater than or equal to an expression.

```
// Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
greaterThanOrEqual("quantity", field("requirement").add(1))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### greaterThanOrEqual

```
public static final @NonNull BooleanExpression greaterThanOrEqual(@NonNull String fieldName, @NonNull Object value)
```

Creates an expression that checks if a field's value is greater than or equal to another value.

```
// Check if the 'score' field is greater than or equal to 80
greaterThanOrEqual("score", 80)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### greaterThanOrEqual

```
public static final @NonNull BooleanExpression greaterThanOrEqual(@NonNull Expression left, @NonNull Object right)
```

Creates an expression that checks if an expression is greater than or equal to a value.

```
// Check if the 'score' field is greater than or equal to 80
greaterThanOrEqual(field("score"), 80)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### greaterThanOrEqual

```
public static final @NonNull BooleanExpression greaterThanOrEqual(@NonNull Expression left, @NonNull Expression right)
```

Creates an expression that checks if the first expression is greater than or equal to the second expression.

```
// Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
greaterThanOrEqual(field("quantity"), field("requirement").add(1))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right` | The second expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the greater than or equal to comparison. |

### ifAbsent

```
public static final @NonNull Expression ifAbsent(@NonNull Expression ifExpr, @NonNull Expression elseExpr)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation.

```
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
ifAbsent(field("optional_field"), "default_value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression ifExpr` | The expression to check for absence. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression elseExpr` | The expression that will be evaluated and returned if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is absent. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifAbsent

```
public static final @NonNull Expression ifAbsent(@NonNull Expression ifExpr, @NonNull Object elseValue)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` is absent, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation.

```
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
ifAbsent(field("optional_field"), "default_value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression ifExpr` | The expression to check for absence. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html elseValue` | The value that will be returned if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` is absent. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifAbsent

```
public static final @NonNull Expression ifAbsent(@NonNull String ifFieldName, @NonNull Expression elseExpr)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is absent, else return the value of the field.

```
// Returns the value of the optional field 'optional_field', or returns the value of
// 'default_field' if 'optional_field' is absent.
ifAbsent("optional_field", field("default_field"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html ifFieldName` | The field to check for absence. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression elseExpr` | The expression that will be evaluated and returned if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is absent. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifAbsent

```
public static final @NonNull Expression ifAbsent(@NonNull String ifFieldName, @NonNull Object elseValue)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` argument if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` is absent, else return the value of the field.

```
// Returns the value of the optional field 'optional_field', or returns 'default_value'
// if the field is absent.
ifAbsent("optional_field", "default_value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html ifFieldName` | The field to check for absence. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html elseValue` | The value that will be returned if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifAbsent(kotlin.String,kotlin.Any)` is absent. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the ifAbsent operation. |

### ifError

```
public static final @NonNull BooleanExpression ifError(
    @NonNull BooleanExpression tryExpr,
    @NonNull BooleanExpression catchExpr
)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` argument evaluation.

This overload will return `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` when both parameters are also `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression`.

```
// Returns the result of the boolean expression, or false if it errors.
ifError(field("is_premium"), false)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression tryExpr` | The try boolean expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression catchExpr` | The catch boolean expression that will be evaluated and returned if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.BooleanExpression,com.google.firebase.firestore.pipeline.BooleanExpression)` produces an error. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the ifError operation. |

### ifError

```
public static final @NonNull Expression ifError(@NonNull Expression tryExpr, @NonNull Expression catchExpr)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` argument evaluation.

```
// Returns the first item in the title field arrays, or returns
// the entire title field if the array is empty or the field is another type.
ifError(arrayGet(field("title"), 0), field("title"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression tryExpr` | The try expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression catchExpr` | The catch expression that will be evaluated and returned if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` produces an error. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the ifError operation. |

### ifError

```
public static final @NonNull Expression ifError(@NonNull Expression tryExpr, @NonNull Object catchValue)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument if there is an error, else return the result of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` argument evaluation.

```
// Returns the first item in the title field arrays, or returns "Default Title"
ifError(arrayGet(field("title"), 0), "Default Title")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression tryExpr` | The try expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html catchValue` | The value that will be returned if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ifError(com.google.firebase.firestore.pipeline.Expression,kotlin.Any)` produces an error. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the ifError operation. |

### isAbsent

```
public static final @NonNull BooleanExpression isAbsent(@NonNull String fieldName)
```

Creates an expression that returns true if a field is absent. Otherwise, returns false even if the field value is null.

```
// Check if the field `value` is absent.
isAbsent("value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field to check. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the isAbsent operation. |

### isAbsent

```
public static final @NonNull BooleanExpression isAbsent(@NonNull Expression value)
```

Creates an expression that returns true if a value is absent. Otherwise, returns false even if the value is null.

```
// Check if the field `value` is absent.
isAbsent(field("value"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value` | The expression to check. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the isAbsent operation. |

### isError

```
public static final @NonNull BooleanExpression isError(@NonNull Expression expr)
```

Creates an expression that checks if a given expression produces an error.

```
// Check if the result of a calculation is an error
isError(arrayContains(field("title"), 1))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression to check. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the `isError` check. |

### join

```
public static final @NonNull Expression join(@NonNull Expression arrayExpression, @NonNull String delimiter)
```

Creates an expression that joins the elements of an array into a string.

```
// Join the elements of the 'tags' field with a comma and space.
join(field("tags"), ", ")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | The expression that evaluates to an array. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter` | The string to use as a delimiter. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### join

```
public static final @NonNull Expression join(
    @NonNull Expression arrayExpression,
    @NonNull Expression delimiterExpression
)
```

Creates an expression that joins the elements of an array into a string.

```
// Join the elements of the 'tags' field with the delimiter from the 'separator' field.
join(field("tags"), field("separator"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | The expression that evaluates to an array. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiterExpression` | The expression that evaluates to the delimiter string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### join

```
public static final @NonNull Expression join(@NonNull String arrayFieldName, @NonNull String delimiter)
```

Creates an expression that joins the elements of an array field into a string.

```
// Join the elements of the 'tags' field with a comma and space.
join("tags", ", ")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of the field containing the array. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter` | The string to use as a delimiter. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### join

```
public static final @NonNull Expression join(
    @NonNull String arrayFieldName,
    @NonNull Expression delimiterExpression
)
```

Creates an expression that joins the elements of an array field into a string.

```
// Join the elements of the 'tags' field with the delimiter from the 'separator' field.
join("tags", field("separator"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayFieldName` | The name of the field containing the array. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiterExpression` | The expression that evaluates to the delimiter string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the join operation. |

### length

```
public static final @NonNull Expression length(@NonNull Expression expr)
```

Creates an expression that calculates the length of a string, array, map, vector, or blob expression.

```
// Get the length of the 'value' field where the value type can be any of a string, array, map, vector or blob.
length(field("value"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length operation. |

### length

```
public static final @NonNull Expression length(@NonNull String fieldName)
```

Creates an expression that calculates the length of a string, array, map, vector, or blob field.

```
// Get the length of the 'value' field where the value type can be any of a string, array, map, vector or blob.
charLength("value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length operation. |

### lessThan

```
public static final @NonNull BooleanExpression lessThan(@NonNull String fieldName, @NonNull Expression expression)
```

Creates an expression that checks if a field's value is less than an expression.

```
// Check if the 'age' field is less than 'limit'
lessThan("age", field("limit"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThan

```
public static final @NonNull BooleanExpression lessThan(@NonNull String fieldName, @NonNull Object value)
```

Creates an expression that checks if a field's value is less than another value.

```
// Check if the 'price' field is less than 50
lessThan("price", 50)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThan

```
public static final @NonNull BooleanExpression lessThan(@NonNull Expression left, @NonNull Object right)
```

Creates an expression that checks if an expression is less than a value.

```
// Check if the 'price' field is less than 50
lessThan(field("price"), 50)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThan

```
public static final @NonNull BooleanExpression lessThan(@NonNull Expression left, @NonNull Expression right)
```

Creates an expression that checks if the first expression is less than the second expression.

```
// Check if the 'age' field is less than 'limit'
lessThan(field("age"), field("limit"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right` | The second expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than comparison. |

### lessThanOrEqual

```
public static final @NonNull BooleanExpression lessThanOrEqual(@NonNull String fieldName, @NonNull Expression expression)
```

Creates an expression that checks if a field's value is less than or equal to an expression.

```
// Check if the 'quantity' field is less than or equal to 20
lessThanOrEqual("quantity", constant(20))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### lessThanOrEqual

```
public static final @NonNull BooleanExpression lessThanOrEqual(@NonNull String fieldName, @NonNull Object value)
```

Creates an expression that checks if a field's value is less than or equal to another value.

```
// Check if the 'score' field is less than or equal to 70
lessThanOrEqual("score", 70)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### lessThanOrEqual

```
public static final @NonNull BooleanExpression lessThanOrEqual(@NonNull Expression left, @NonNull Object right)
```

Creates an expression that checks if an expression is less than or equal to a value.

```
// Check if the 'score' field is less than or equal to 70
lessThanOrEqual(field("score"), 70)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### lessThanOrEqual

```
public static final @NonNull BooleanExpression lessThanOrEqual(@NonNull Expression left, @NonNull Expression right)
```

Creates an expression that checks if the first expression is less than or equal to the second expression.

```
// Check if the 'quantity' field is less than or equal to 20
lessThanOrEqual(field("quantity"), constant(20))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right` | The second expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the less than or equal to comparison. |

### like

```
public static final @NonNull BooleanExpression like(@NonNull String fieldName, @NonNull Expression pattern)
```

Creates an expression that performs a case-sensitive wildcard string comparison against a field.

```
// Check if the 'title' field contains the string "guide"
like("title", "%guide%")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like comparison. |

### like

```
public static final @NonNull BooleanExpression like(@NonNull String fieldName, @NonNull String pattern)
```

Creates an expression that performs a case-sensitive wildcard string comparison against a field.

```
// Check if the 'title' field contains the string "guide"
like("title", "%guide%")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like comparison. |

### like

```
public static final @NonNull BooleanExpression like(@NonNull Expression stringExpression, @NonNull Expression pattern)
```

Creates an expression that performs a case-sensitive wildcard string comparison.

```
// Check if the 'title' field contains the string "guide"
like(field("title"), "%guide%")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like operation. |

### like

```
public static final @NonNull BooleanExpression like(@NonNull Expression stringExpression, @NonNull String pattern)
```

Creates an expression that performs a case-sensitive wildcard string comparison.

```
// Check if the 'title' field contains the string "guide"
like(field("title"), "%guide%")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The pattern to search for. You can use "%" as a wildcard character. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the like operation. |

### ln

```
public static final @NonNull Expression ln(@NonNull Expression numericExpr)
```

Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ln(com.google.firebase.firestore.pipeline.Expression)`.

```
// Compute the natural logarithm of the 'value' field.
ln(field("value"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the natural logarithm. |

### ln

```
public static final @NonNull Expression ln(@NonNull String numericField)
```

Creates an expression that returns the natural logarithm (base e) of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#ln(kotlin.String)`.

```
// Compute the natural logarithm of the 'value' field.
ln("value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the natural logarithm. |

### log

```
public static final @NonNull Expression log(@NonNull Expression numericExpr, @NonNull Expression base)
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```
// Compute the logarithm of the 'value' field with the base in the 'base' field.
log(field("value"), field("base"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression base` | The base of the logarithm. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |

### log

```
public static final @NonNull Expression log(@NonNull Expression numericExpr, @NonNull Number base)
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`.

```
// Compute the logarithm of the 'value' field with base 10.
log(field("value"), 10)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html base` | The base of the logarithm. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |

### log

```
public static final @NonNull Expression log(@NonNull String numericField, @NonNull Expression base)
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Compute the logarithm of the 'value' field with the base in the 'base' field.
log("value", field("base"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression base` | The base of the logarithm. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |

### log

```
public static final @NonNull Expression log(@NonNull String numericField, @NonNull Number base)
```

Creates an expression that returns the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)`.

```
// Compute the logarithm of the 'value' field with base 10.
log("value", 10)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html base` | The base of the logarithm. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from the logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)` with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log(kotlin.String,kotlin.Number)`. |

### log10

```
public static final @NonNull Expression log10(@NonNull Expression numericExpr)
```

Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log10(com.google.firebase.firestore.pipeline.Expression)`.

```
// Compute the base 10 logarithm of the 'value' field.
log10(field("value"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the base 10 logarithm. |

### log10

```
public static final @NonNull Expression log10(@NonNull String numericField)
```

Creates an expression that returns the base 10 logarithm of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#log10(kotlin.String)`.

```
// Compute the base 10 logarithm of the 'value' field.
log10("value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the base 10 logarithm. |

### logicalMaximum

```
public static final @NonNull Expression logicalMaximum(@NonNull Expression expr, @NonNull Object others)
```

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```
// Returns the larger value between the 'timestamp' field and the current timestamp.
logicalMaximum(field("timestamp"), currentTimestamp())
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The first operand expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the logical maximum operation. |

### logicalMaximum

```
public static final @NonNull Expression logicalMaximum(@NonNull String fieldName, @NonNull Object others)
```

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```
// Returns the larger value between the 'timestamp' field and the current timestamp.
logicalMaximum("timestamp", currentTimestamp())
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The first operand field name. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the logical maximum operation. |

### logicalMinimum

```
public static final @NonNull Expression logicalMinimum(@NonNull Expression expr, @NonNull Object others)
```

Creates an expression that returns the smallest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```
// Returns the smaller value between the 'timestamp' field and the current timestamp.
logicalMinimum(field("timestamp"), currentTimestamp())
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The first operand expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the logical minimum operation. |

### logicalMinimum

```
public static final @NonNull Expression logicalMinimum(@NonNull String fieldName, @NonNull Object others)
```

Creates an expression that returns the smallest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

```
// Returns the smaller value between the 'timestamp' field and the current timestamp.
logicalMinimum("timestamp", currentTimestamp())
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The first operand field name. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html others` | Optional additional expressions or literals. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the logical minimum operation. |

### map

```
public static final @NonNull Expression map(@NonNull Map<@NonNull String, @NonNull Object> elements)
```

Creates an expression that creates a Firestore map value from an input object.

```
// Create a map with a constant key and a field value
map(mapOf("name" to field("productName"), "quantity" to 1))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/Map.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> elements` | The input map to evaluate in the expression. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the map function. |

### mapGet

```
public static final @NonNull Expression mapGet(@NonNull String fieldName, @NonNull String key)
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,kotlin.String)`.

```
// Get the 'city' value from the 'address' map field
mapGet("address", "city")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name of the map field. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The key to access in the map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapGet

```
public static final @NonNull Expression mapGet(@NonNull String fieldName, @NonNull Expression keyExpression)
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Get the value from the 'address' map field, using the key from the 'keyField' field
mapGet("address", field("keyField"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name of the map field. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression keyExpression` | The key to access in the map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapGet

```
public static final @NonNull Expression mapGet(@NonNull Expression mapExpression, @NonNull String key)
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`.

```
// Get the 'city' value from the 'address' map field
mapGet(field("address"), "city")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpression` | The expression representing the map. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The key to access in the map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapGet

```
public static final @NonNull Expression mapGet(
    @NonNull Expression mapExpression,
    @NonNull Expression keyExpression
)
```

Accesses a value from a map (object) field using the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#mapGet(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```
// Get the value from the 'address' map field, using the key from the 'keyField' field
mapGet(field("address"), field("keyField"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpression` | The expression representing the map. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression keyExpression` | The key to access in the map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the value associated with the given key in the map. |

### mapMerge

```
public static final @NonNull Expression mapMerge(
    @NonNull Expression firstMap,
    @NonNull Expression secondMap,
    @NonNull Expression otherMaps
)
```

Creates an expression that merges multiple maps into a single map. If multiple maps have the same key, the later value is used.

```
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstMap` | First map expression that will be merged. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondMap` | Second map expression that will be merged. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherMaps` | Additional maps to merge. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the mapMerge operation. |

### mapMerge

```
public static final @NonNull Expression mapMerge(
    @NonNull String firstMapFieldName,
    @NonNull Expression secondMap,
    @NonNull Expression otherMaps
)
```

Creates an expression that merges multiple maps into a single map. If multiple maps have the same key, the later value is used.

```
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html firstMapFieldName` | First map field name that will be merged. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression secondMap` | Second map expression that will be merged. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherMaps` | Additional maps to merge. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the mapMerge operation. |

### mapRemove

```
public static final @NonNull Expression mapRemove(@NonNull Expression mapExpr, @NonNull Expression key)
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```
// Removes the key 'baz' from the input map.
mapRemove(map(mapOf("foo" to "bar", "baz" to true)), constant("baz"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpr` | An expression that evaluates to a map. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression key` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mapRemove

```
public static final @NonNull Expression mapRemove(@NonNull Expression mapExpr, @NonNull String key)
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```
// Removes the key 'baz' from the input map.
mapRemove(map(mapOf("foo" to "bar", "baz" to true)), "baz")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression mapExpr` | An expression that evaluates to a map. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mapRemove

```
public static final @NonNull Expression mapRemove(@NonNull String mapField, @NonNull Expression key)
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```
// Removes the key 'city' field from the map in the address field of the input document.
mapRemove("address", constant("city"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mapField` | The name of a field containing a map value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression key` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mapRemove

```
public static final @NonNull Expression mapRemove(@NonNull String mapField, @NonNull String key)
```

Creates an expression that removes a key from the map produced by evaluating an expression.

```
// Removes the key 'city' field from the map in the address field of the input document.
mapRemove("address", "city")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html mapField` | The name of a field containing a map value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key` | The name of the key to remove from the input map. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a modified map. |

### mod

```
public static final @NonNull Expression mod(@NonNull Expression dividend, @NonNull Expression divisor)
```

Creates an expression that calculates the modulo (remainder) of dividing two numeric expressions.

```
// Calculate the remainder of dividing the 'value' field by the 'divisor' field
mod(field("value"), field("divisor"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend` | The numeric expression to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor` | The numeric expression to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### mod

```
public static final @NonNull Expression mod(@NonNull Expression dividend, @NonNull Number divisor)
```

Creates an expression that calculates the modulo (remainder) of dividing a numeric expression by a constant.

```
// Calculate the remainder of dividing the 'value' field by 3.
mod(field("value"), 3)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression dividend` | The numeric expression to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor` | The constant to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### mod

```
public static final @NonNull Expression mod(@NonNull String dividendFieldName, @NonNull Expression divisor)
```

Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant.

```
// Calculate the remainder of dividing the 'value' field by the 'divisor' field.
mod("value", field("divisor"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName` | The numeric field name to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression divisor` | The numeric expression to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### mod

```
public static final @NonNull Expression mod(@NonNull String dividendFieldName, @NonNull Number divisor)
```

Creates an expression that calculates the modulo (remainder) of dividing a numeric field by a constant.

```
// Calculate the remainder of dividing the 'value' field by 3.
mod("value", 3)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html dividendFieldName` | The numeric field name to be divided. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html divisor` | The constant to divide by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the modulo operation. |

### multiply

```
public static final @NonNull Expression multiply(@NonNull Expression first, @NonNull Expression second)
```

Creates an expression that multiplies numeric expressions.

```
// Multiply the 'quantity' field by the 'price' field
multiply(field("quantity"), field("price"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first` | Numeric expression to multiply. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second` | Numeric expression to multiply. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### multiply

```
public static final @NonNull Expression multiply(@NonNull Expression first, @NonNull Number second)
```

Creates an expression that multiplies numeric expressions with a constant.

```
// Multiply the 'quantity' field by 1.1.
multiply(field("quantity"), 1.1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression first` | Numeric expression to multiply. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second` | Constant to multiply. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### multiply

```
public static final @NonNull Expression multiply(@NonNull String numericFieldName, @NonNull Expression second)
```

Creates an expression that multiplies a numeric field with a numeric expression.

```
// Multiply the 'quantity' field by the 'price' field.
multiply("quantity", field("price"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName` | Numeric field to multiply. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression second` | Numeric expression to multiply. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### multiply

```
public static final @NonNull Expression multiply(@NonNull String numericFieldName, @NonNull Number second)
```

Creates an expression that multiplies a numeric field with a constant.

```
// Multiply the 'quantity' field by 1.1.
multiply("quantity", 1.1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName` | Numeric field to multiply. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html second` | Constant to multiply. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the multiplication operation. |

### not

```
public static final @NonNull BooleanExpression not(@NonNull BooleanExpression condition)
```

Creates an expression that negates a boolean expression.

```
// Check if 'is_admin' is not true
not(field("is_admin"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition` | The boolean expression to negate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the not operation. |

### notEqual

```
public static final @NonNull BooleanExpression notEqual(@NonNull String fieldName, @NonNull Expression expression)
```

Creates an expression that checks if a field's value is not equal to an expression.

```
// Check if the 'status' field is not equal to the value of the 'otherStatus' field
notEqual("status", field("otherStatus"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqual

```
public static final @NonNull BooleanExpression notEqual(@NonNull String fieldName, @NonNull Object value)
```

Creates an expression that checks if a field's value is not equal to another value.

```
// Check if the 'status' field is not equal to "completed"
notEqual("status", "completed")

// Check if the 'country' field is not equal to "USA"
notEqual("country", "USA")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqual

```
public static final @NonNull BooleanExpression notEqual(@NonNull Expression left, @NonNull Object right)
```

Creates an expression that checks if an expression is not equal to a value.

```
// Check if the 'status' field is not equal to "completed"
notEqual(field("status"), "completed")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html right` | The value to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqual

```
public static final @NonNull BooleanExpression notEqual(@NonNull Expression left, @NonNull Expression right)
```

Creates an expression that checks if two expressions are not equal.

```
// Check if the 'status' field is not equal to the value of the 'otherStatus' field
notEqual(field("status"), field("otherStatus"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression left` | The first expression to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression right` | The second expression to compare to. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the inequality comparison. |

### notEqualAny

```
public static final @NonNull BooleanExpression notEqualAny(
    @NonNull Expression expression,
    @NonNull Expression arrayExpression
)
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`, when evaluated, is not equal to all the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'status' field is not in the 'inactiveStatuses' array field.
notEqualAny(field("status"), field("inactiveStatuses"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression whose results to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### notEqualAny

```
public static final @NonNull BooleanExpression notEqualAny(
    @NonNull Expression expression,
    @NonNull List<@NonNull Object> values
)
```

Creates an expression that checks if an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`, when evaluated, is not equal to all the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(com.google.firebase.firestore.pipeline.Expression,kotlin.collections.List)`.

```
// Check if the 'status' field is neither "pending" nor the value of the 'rejectedStatus' field.
notEqualAny(field("status"), listOf("pending", field("rejectedStatus")))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expression` | The expression whose results to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The values to check against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### notEqualAny

```
public static final @NonNull BooleanExpression notEqualAny(@NonNull String fieldName, @NonNull Expression arrayExpression)
```

Creates an expression that checks if a field's value is not equal to all of the elements of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'status' field is not in the 'inactiveStatuses' array field.
notEqualAny("status", field("inactiveStatuses"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression arrayExpression` | An expression that evaluates to an array, whose elements to check for equality to the input. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### notEqualAny

```
public static final @NonNull BooleanExpression notEqualAny(@NonNull String fieldName, @NonNull List<@NonNull Object> values)
```

Creates an expression that checks if a field's value is not equal to all of the provided `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#notEqualAny(kotlin.String,kotlin.collections.List)`.

```
// Check if the 'status' field is not "archived" or "deleted".
notEqualAny("status", listOf("archived", "deleted"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field to compare. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html> values` | The values to check against. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'NOT IN' comparison. |

### nullValue

```
public static final @NonNull Expression nullValue()
```

Constant for a null value.

```
// Create a null constant
nullValue()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### or

```
public static final @NonNull BooleanExpression or(
    @NonNull BooleanExpression condition,
    @NonNull BooleanExpression conditions
)
```

Creates an expression that performs a logical 'OR' operation.

```
// Check if 'status' is "new" or "open"
or(field("status").equal("new"), field("status").equal("open"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition` | The first `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression conditions` | Additional `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression`s. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the logical 'OR' operation. |

### pow

```
public static final @NonNull Expression pow(@NonNull Expression numericExpr, @NonNull Expression exponent)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. Returns infinity on overflow and zero on underflow.

```
// Raise the value of the 'base' field to the power of the 'exponent' field.
pow(field("base"), field("exponent"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression exponent` | The numeric power to raise the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)`. |

### pow

```
public static final @NonNull Expression pow(@NonNull Expression numericExpr, @NonNull Number exponent)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. Returns infinity on overflow and zero on underflow.

```
// Raise the value of the 'base' field to the power of 2.
pow(field("base"), 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html exponent` | The numeric power to raise the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)` to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(com.google.firebase.firestore.pipeline.Expression,kotlin.Number)`. |

### pow

```
public static final @NonNull Expression pow(@NonNull String numericField, @NonNull Expression exponent)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. Returns infinity on overflow and zero on underflow.

```
// Raise the value of the 'base' field to the power of the 'exponent' field.
pow("base", field("exponent"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression exponent` | The numeric power to raise the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`. |

### pow

```
public static final @NonNull Expression pow(@NonNull String numericField, @NonNull Number exponent)
```

Creates an expression that returns the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)` raised to the power of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. Returns infinity on overflow and zero on underflow.

```
// Raise the value of the 'base' field to the power of 2.
pow("base", 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html exponent` | The numeric power to raise the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing a numeric result from raising `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)` to the power of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#pow(kotlin.String,kotlin.Number)`. |

### rawFunction

```
public static final @NonNull Expression rawFunction(@NonNull String name, @NonNull Expression expr)
```

Creates a 'raw' function expression. This is useful if the expression is available in the backend, but not yet in the current version of the SDK yet.

```
// Create a generic function call
rawFunction("my_function", field("arg1"), constant(42))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the raw function. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expressions to be passed as arguments to the function. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the raw function. |

### regexContains

```
public static final @NonNull BooleanExpression regexContains(@NonNull String fieldName, @NonNull Expression pattern)
```

Creates an expression that checks if a string field contains a specified regular expression as a substring.

```
// Check if the 'description' field contains the regex from the 'pattern' field.
regexContains("description", field("pattern"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to use for the search. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexContains

```
public static final @NonNull BooleanExpression regexContains(@NonNull String fieldName, @NonNull String pattern)
```

Creates an expression that checks if a string field contains a specified regular expression as a substring.

```
// Check if the 'description' field contains "example" (case-insensitive)
regexContains("description", "(?i)example")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to use for the search. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexContains

```
public static final @NonNull BooleanExpression regexContains(
    @NonNull Expression stringExpression,
    @NonNull Expression pattern
)
```

Creates an expression that checks if a string expression contains a specified regular expression as a substring.

```
// Check if the 'description' field contains "example" (case-insensitive)
regexContains(field("description"), "(?i)example")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to use for the search. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexContains

```
public static final @NonNull BooleanExpression regexContains(
    @NonNull Expression stringExpression,
    @NonNull String pattern
)
```

Creates an expression that checks if a string expression contains a specified regular expression as a substring.

```
// Check if the 'description' field contains "example" (case-insensitive)
regexContains(field("description"), "(?i)example")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to use for the search. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains regular expression comparison. |

### regexFind

```
public static final @NonNull Expression regexFind(@NonNull String fieldName, @NonNull Expression pattern)
```

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract a substring from 'email' based on a pattern stored in another field
regexFind("email", field("pattern"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFind

```
public static final @NonNull Expression regexFind(@NonNull String fieldName, @NonNull String pattern)
```

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract the domain name from an email field
regexFind("email", "@[A-Za-z0-9.-]+")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFind

```
public static final @NonNull Expression regexFind(
    @NonNull Expression stringExpression,
    @NonNull Expression pattern
)
```

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract a substring based on a dynamic pattern field
regexFind(field("email"), field("pattern"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFind

```
public static final @NonNull Expression regexFind(@NonNull Expression stringExpression, @NonNull String pattern)
```

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract the domain from a lower-cased email address
regexFind(field("email"), "@[A-Za-z0-9.-]+")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the regular expression find function. |

### regexFindAll

```
public static final @NonNull Expression regexFindAll(@NonNull String fieldName, @NonNull Expression pattern)
```

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract all matches from 'content' based on a pattern stored in another field
regexFindAll("content", field("pattern"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexFindAll

```
public static final @NonNull Expression regexFindAll(@NonNull String fieldName, @NonNull String pattern)
```

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract all hashtags from a post content field
regexFindAll("content", "#[A-Za-z0-9_]+")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexFindAll

```
public static final @NonNull Expression regexFindAll(
    @NonNull Expression stringExpression,
    @NonNull Expression pattern
)
```

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract all matches based on a dynamic pattern expression
regexFindAll(field("comment"), field("pattern"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexFindAll

```
public static final @NonNull Expression regexFindAll(@NonNull Expression stringExpression, @NonNull String pattern)
```

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

```
// Extract all mentions from a lower-cased comment
regexFindAll(field("comment"), "@[A-Za-z0-9_]+")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to search. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to a list of matched substrings. |

### regexMatch

```
public static final @NonNull BooleanExpression regexMatch(@NonNull String fieldName, @NonNull Expression pattern)
```

Creates an expression that checks if a string field matches a specified regular expression.

```
// Check if the 'email' field matches the regex from the 'pattern' field.
regexMatch("email", field("pattern"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to use for the match. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### regexMatch

```
public static final @NonNull BooleanExpression regexMatch(@NonNull String fieldName, @NonNull String pattern)
```

Creates an expression that checks if a string field matches a specified regular expression.

```
// Check if the 'email' field matches a valid email pattern
regexMatch("email", "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to use for the match. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### regexMatch

```
public static final @NonNull BooleanExpression regexMatch(
    @NonNull Expression stringExpression,
    @NonNull Expression pattern
)
```

Creates an expression that checks if a string field matches a specified regular expression.

```
// Check if the 'email' field matches a valid email pattern
regexMatch(field("email"), "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to match against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression pattern` | The regular expression to use for the match. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### regexMatch

```
public static final @NonNull BooleanExpression regexMatch(@NonNull Expression stringExpression, @NonNull String pattern)
```

Creates an expression that checks if a string field matches a specified regular expression.

```
// Check if the 'email' field matches a valid email pattern
regexMatch(field("email"), "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to match against. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html pattern` | The regular expression to use for the match. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the regular expression match comparison. |

### reverse

```
public static final @NonNull Expression reverse(@NonNull String fieldName)
```

Creates an expression that reverses a string value from the specified field.

```
// Reverse the value of the 'myString' field.
reverse("myString")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the string to reverse. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the reversed string. |

### reverse

```
public static final @NonNull Expression reverse(@NonNull Expression stringExpression)
```

Creates an expression that reverses a string.

```
// Reverse the value of the 'myString' field.
reverse(field("myString"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | An expression evaluating to a string value, which will be reversed. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the reversed string. |

### round

```
public static final @NonNull Expression round(@NonNull Expression numericExpr)
```

Creates an expression that rounds `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#round(com.google.firebase.firestore.pipeline.Expression)` to nearest integer.

```
// Round the value of the 'price' field.
round(field("price"))
```

Rounds away from zero in halfway cases.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the round operation. |

### round

```
public static final @NonNull Expression round(@NonNull String numericField)
```

Creates an expression that rounds `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#round(kotlin.String)` to nearest integer.

```
// Round the value of the 'price' field.
round("price")
```

Rounds away from zero in halfway cases.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing an integer result from the round operation. |

### roundToPrecision

```
public static final @NonNull Expression roundToPrecision(
    @NonNull Expression numericExpr,
    @NonNull Expression decimalPlace
)
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.Expression)` is negative. Rounds away from zero in halfway cases.

```
// Round the value of the 'price' field to the number of decimal places specified in the
// 'precision' field.
roundToPrecision(field("price"), field("precision"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression decimalPlace` | The number of decimal places to round. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### roundToPrecision

```
public static final @NonNull Expression roundToPrecision(@NonNull Expression numericExpr, int decimalPlace)
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(com.google.firebase.firestore.pipeline.Expression,kotlin.Int)` is negative. Rounds away from zero in halfway cases.

```
// Round the value of the 'price' field to 2 decimal places.
roundToPrecision(field("price"), 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |
| `int decimalPlace` | The number of decimal places to round. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### roundToPrecision

```
public static final @NonNull Expression roundToPrecision(
    @NonNull String numericField,
    @NonNull Expression decimalPlace
)
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,com.google.firebase.firestore.pipeline.Expression)` is negative. Rounds away from zero in halfway cases.

```
// Round the value of the 'price' field to the number of decimal places specified in the
// 'precision' field.
roundToPrecision("price", field("precision"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression decimalPlace` | The number of decimal places to round. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### roundToPrecision

```
public static final @NonNull Expression roundToPrecision(@NonNull String numericField, int decimalPlace)
```

Creates an expression that rounds off `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` decimal places if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is positive, rounds off digits to the left of the decimal point if `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#roundToPrecision(kotlin.String,kotlin.Int)` is negative. Rounds away from zero in halfway cases.

```
// Round the value of the 'price' field to 2 decimal places.
roundToPrecision("price", 2)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |
| `int decimalPlace` | The number of decimal places to round. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the round operation. |

### split

```
public static final @NonNull Expression split(@NonNull String fieldName, @NonNull Blob delimiter)
```

Creates an expression that splits a blob field by a blob delimiter.

```
// Split the 'data' field by a delimiter
split("data", Blob.fromBytes(byteArrayOf(0x0a)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the blob to be split. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob delimiter` | The blob delimiter to split by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
public static final @NonNull Expression split(@NonNull String fieldName, @NonNull Expression delimiter)
```

Creates an expression that splits a string or blob field by a delimiter.

```
// Split the 'tags' field by the value of the 'delimiter' field
split("tags", field("delimiter"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string or blob to be split. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiter` | The delimiter to split by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
public static final @NonNull Expression split(@NonNull String fieldName, @NonNull String delimiter)
```

Creates an expression that splits a string or blob field by a string delimiter.

```
// Split the 'tags' field by a comma
split("tags", ",")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string or blob to be split. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter` | The string delimiter to split by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
public static final @NonNull Expression split(@NonNull Expression value, @NonNull Blob delimiter)
```

Creates an expression that splits a blob by a blob delimiter.

```
// Split the 'data' field by a delimiter
split(field("data"), Blob.fromBytes(byteArrayOf(0x0a)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value` | The expression evaluating to a blob to be split. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob delimiter` | The blob delimiter to split by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
public static final @NonNull Expression split(@NonNull Expression value, @NonNull Expression delimiter)
```

Creates an expression that splits a string or blob by a delimiter.

```
// Split the 'tags' field by a comma
split(field("tags"), field("delimiter"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value` | The expression evaluating to a string or blob to be split. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression delimiter` | The delimiter to split by. Must be of the same type as `value`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### split

```
public static final @NonNull Expression split(@NonNull Expression value, @NonNull String delimiter)
```

Creates an expression that splits a string or blob by a string delimiter.

```
// Split the 'tags' field by a comma
split(field("tags"), ",")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression value` | The expression evaluating to a string or blob to be split. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html delimiter` | The string delimiter to split by. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` that evaluates to an array of segments. |

### sqrt

```
public static final @NonNull Expression sqrt(@NonNull Expression numericExpr)
```

Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(com.google.firebase.firestore.pipeline.Expression)`.

```
// Compute the square root of the 'value' field.
sqrt(field("value"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression numericExpr` | An expression that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the square root operation. |

### sqrt

```
public static final @NonNull Expression sqrt(@NonNull String numericField)
```

Creates an expression that returns the square root of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#sqrt(kotlin.String)`.

```
// Compute the square root of the 'value' field.
sqrt("value")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericField` | Name of field that returns number when evaluated. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the numeric result of the square root operation. |

### startsWith

```
public static final @NonNull BooleanExpression startsWith(@NonNull String fieldName, @NonNull Expression prefix)
```

Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,com.google.firebase.firestore.pipeline.Expression)`.

```
// Check if the 'fullName' field starts with the value of the 'firstName' field
startsWith("fullName", field("firstName"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of field that contains a string to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression prefix` | The prefix string expression to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### startsWith

```
public static final @NonNull BooleanExpression startsWith(@NonNull String fieldName, @NonNull String prefix)
```

Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(kotlin.String,kotlin.String)`.

```
// Check if the 'name' field starts with "Mr."
startsWith("name", "Mr.")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of field that contains a string to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prefix` | The prefix string to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### startsWith

```
public static final @NonNull BooleanExpression startsWith(@NonNull Expression stringExpr, @NonNull Expression prefix)
```

```
// Check if the 'fullName' field starts with the value of the 'firstName' field
startsWith(field("fullName"), field("firstName"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr` | The expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression prefix` | The prefix string expression to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### startsWith

```
public static final @NonNull BooleanExpression startsWith(@NonNull Expression stringExpr, @NonNull String prefix)
```

Creates an expression that checks if a string expression starts with a given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression.Companion#startsWith(com.google.firebase.firestore.pipeline.Expression,kotlin.String)`.

```
// Check if the 'name' field starts with "Mr."
startsWith(field("name"), "Mr.")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpr` | The expression to check. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html prefix` | The prefix string to check for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the 'starts with' comparison. |

### stringConcat

```
public static final @NonNull Expression stringConcat(@NonNull String fieldName, @NonNull Object otherStrings)
```

Creates an expression that concatenates string expressions together.

```
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat("firstName", " ", "lastName")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name containing the initial string value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherStrings` | Optional additional string expressions or string constants to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
public static final @NonNull Expression stringConcat(@NonNull String fieldName, @NonNull Expression otherStrings)
```

Creates an expression that concatenates string expressions together.

```
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat("firstName", constant(" "), field("lastName"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The field name containing the initial string value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherStrings` | Optional additional string expressions to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
public static final @NonNull Expression stringConcat(@NonNull Expression firstString, @NonNull Object otherStrings)
```

Creates an expression that concatenates string expressions together.

```
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat(field("firstName"), " ", field("lastName"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstString` | The expression representing the initial string value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html otherStrings` | Optional additional string expressions or string constants to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringConcat

```
public static final @NonNull Expression stringConcat(
    @NonNull Expression firstString,
    @NonNull Expression otherStrings
)
```

Creates an expression that concatenates string expressions together.

```
// Combine the 'firstName', " ", and 'lastName' fields into a single string
stringConcat(field("firstName"), constant(" "), field("lastName"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression firstString` | The expression representing the initial string value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression otherStrings` | Optional additional string expressions to concatenate. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the concatenated string. |

### stringContains

```
public static final @NonNull BooleanExpression stringContains(@NonNull String fieldName, @NonNull Expression substring)
```

Creates an expression that checks if a string field contains a specified substring.

```
// Check if the 'description' field contains the value of the 'keyword' field.
stringContains("description", field("keyword"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression substring` | The expression representing the substring to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringContains

```
public static final @NonNull BooleanExpression stringContains(@NonNull String fieldName, @NonNull String substring)
```

Creates an expression that checks if a string field contains a specified substring.

```
// Check if the 'description' field contains "example".
stringContains("description", "example")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html substring` | The substring to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringContains

```
public static final @NonNull BooleanExpression stringContains(
    @NonNull Expression stringExpression,
    @NonNull Expression substring
)
```

Creates an expression that checks if a string expression contains a specified substring.

```
// Check if the 'description' field contains the value of the 'keyword' field.
stringContains(field("description"), field("keyword"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression substring` | The expression representing the substring to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringContains

```
public static final @NonNull BooleanExpression stringContains(
    @NonNull Expression stringExpression,
    @NonNull String substring
)
```

Creates an expression that checks if a string expression contains a specified substring.

```
// Check if the 'description' field contains "example".
stringContains(field("description"), "example")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to perform the comparison on. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html substring` | The substring to search for. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the contains comparison. |

### stringReverse

```
public static final @NonNull Expression stringReverse(@NonNull String fieldName)
```

Reverses the given string field.

```
// Reverse the value of the 'myString' field.
stringReverse("myString")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of field that contains the string to reverse. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the stringReverse operation. |

### stringReverse

```
public static final @NonNull Expression stringReverse(@NonNull Expression str)
```

Reverses the given string expression.

```
// Reverse the value of the 'myString' field.
stringReverse(field("myString"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression str` | The string expression to reverse. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the stringReverse operation. |

### substring

```
public static final @NonNull Expression substring(@NonNull String fieldName, int index, int length)
```

Creates an expression that returns a substring of the given string.

```
// Get a substring of the 'message' field starting at index 5 with length 10.
substring("message", 5, 10)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to get a substring from. |
| `int index` | The starting index of the substring. |
| `int length` | The length of the substring. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the substring. |

### substring

```
public static final @NonNull Expression substring(
    @NonNull Expression stringExpression,
    @NonNull Expression index,
    @NonNull Expression length
)
```

Creates an expression that returns a substring of the given string.

```
// Get a substring of the 'message' field starting at index 5 with length 10.
substring(field("message"), constant(5), constant(10))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to get a substring from. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression index` | The starting index of the substring. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression length` | The length of the substring. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the substring. |

### subtract

```
public static final @NonNull Expression subtract(@NonNull Expression minuend, @NonNull Expression subtrahend)
```

Creates an expression that subtracts two expressions.

```
// Subtract the 'discount' field from the 'price' field
subtract(field("price"), field("discount"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression minuend` | Numeric expression to subtract from. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression subtrahend` | Numeric expression to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### subtract

```
public static final @NonNull Expression subtract(@NonNull Expression minuend, @NonNull Number subtrahend)
```

Creates an expression that subtracts a constant value from a numeric expression.

```
// Subtract 10 from the 'price' field.
subtract(field("price"), 10)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression minuend` | Numeric expression to subtract from. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html subtrahend` | Constant to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### subtract

```
public static final @NonNull Expression subtract(@NonNull String numericFieldName, @NonNull Expression subtrahend)
```

Creates an expression that subtracts a numeric expressions from numeric field.

```
// Subtract the 'discount' field from the 'price' field.
subtract("price", field("discount"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName` | Numeric field to subtract from. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression subtrahend` | Numeric expression to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### subtract

```
public static final @NonNull Expression subtract(@NonNull String numericFieldName, @NonNull Number subtrahend)
```

Creates an expression that subtracts a constant from numeric field.

```
// Subtract 10 from the 'price' field.
subtract("price", 10)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html numericFieldName` | Numeric field to subtract from. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Number.html subtrahend` | Constant to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the subtract operation. |

### timestampAdd

```
public static final @NonNull Expression timestampAdd(
    @NonNull String fieldName,
    @NonNull Expression unit,
    @NonNull Expression amount
)
```

Creates an expression that adds a specified amount of time to a timestamp.

```
// Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
timestampAdd("timestamp", field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit` | The expression representing the unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount` | The expression representing the amount of time to add. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampAdd

```
public static final @NonNull Expression timestampAdd(@NonNull String fieldName, @NonNull String unit, long amount)
```

Creates an expression that adds a specified amount of time to a timestamp.

```
// Add 1 day to the 'timestamp' field.
timestampAdd("timestamp", "day", 1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit` | The unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `long amount` | The amount of time to add. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampAdd

```
public static final @NonNull Expression timestampAdd(
    @NonNull Expression timestamp,
    @NonNull Expression unit,
    @NonNull Expression amount
)
```

Creates an expression that adds a specified amount of time to a timestamp.

```
// Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
timestampAdd(field("timestamp"), field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The expression representing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit` | The expression representing the unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount` | The expression representing the amount of time to add. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampAdd

```
public static final @NonNull Expression timestampAdd(
    @NonNull Expression timestamp,
    @NonNull String unit,
    long amount
)
```

Creates an expression that adds a specified amount of time to a timestamp.

```
// Add 1 day to the 'timestamp' field.
timestampAdd(field("timestamp"), "day", 1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The expression representing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit` | The unit of time to add. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `long amount` | The amount of time to add. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
public static final @NonNull Expression timestampSubtract(
    @NonNull String fieldName,
    @NonNull Expression unit,
    @NonNull Expression amount
)
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```
// Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
timestampSubtract("timestamp", field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit` | The unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount` | The amount of time to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
public static final @NonNull Expression timestampSubtract(
    @NonNull String fieldName,
    @NonNull String unit,
    long amount
)
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```
// Subtract 1 day from the 'timestamp' field.
timestampSubtract("timestamp", "day", 1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit` | The unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `long amount` | The amount of time to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
public static final @NonNull Expression timestampSubtract(
    @NonNull Expression timestamp,
    @NonNull Expression unit,
    @NonNull Expression amount
)
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```
// Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
timestampSubtract(field("timestamp"), field("unit"), field("amount"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The expression representing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression unit` | The expression representing the unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression amount` | The expression representing the amount of time to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampSubtract

```
public static final @NonNull Expression timestampSubtract(
    @NonNull Expression timestamp,
    @NonNull String unit,
    long amount
)
```

Creates an expression that subtracts a specified amount of time to a timestamp.

```
// Subtract 1 day from the 'timestamp' field.
timestampSubtract(field("timestamp"), "day", 1)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The expression representing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html unit` | The unit of time to subtract. Valid units include "microsecond", "millisecond", "second", "minute", "hour" and "day". |
| `long amount` | The amount of time to subtract. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the resulting timestamp. |

### timestampToUnixMicros

```
public static final @NonNull Expression timestampToUnixMicros(@NonNull Expression expr)
```

Creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```
// Convert the 'timestamp' field to microseconds since epoch.
timestampToUnixMicros(field("timestamp"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the timestamp. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the number of microseconds since epoch. |

### timestampToUnixMicros

```
public static final @NonNull Expression timestampToUnixMicros(@NonNull String fieldName)
```

Creates an expression that converts a timestamp field to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```
// Convert the 'timestamp' field to microseconds since epoch.
timestampToUnixMicros("timestamp")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the timestamp. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the number of microseconds since epoch. |

### timestampToUnixMillis

```
public static final @NonNull Expression timestampToUnixMillis(@NonNull Expression expr)
```

Creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```
// Convert the 'timestamp' field to milliseconds since epoch.
timestampToUnixMillis(field("timestamp"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the timestamp. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the number of milliseconds since epoch. |

### timestampToUnixMillis

```
public static final @NonNull Expression timestampToUnixMillis(@NonNull String fieldName)
```

Creates an expression that converts a timestamp field to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```
// Convert the 'timestamp' field to milliseconds since epoch.
timestampToUnixMillis("timestamp")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the timestamp. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the number of milliseconds since epoch. |

### timestampToUnixSeconds

```
public static final @NonNull Expression timestampToUnixSeconds(@NonNull Expression expr)
```

Creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```
// Convert the 'timestamp' field to seconds since epoch.
timestampToUnixSeconds(field("timestamp"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the timestamp. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the number of seconds since epoch. |

### timestampToUnixSeconds

```
public static final @NonNull Expression timestampToUnixSeconds(@NonNull String fieldName)
```

Creates an expression that converts a timestamp field to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

```
// Convert the 'timestamp' field to seconds since epoch.
timestampToUnixSeconds("timestamp")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field that contains the timestamp. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the number of seconds since epoch. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(
    @NonNull String fieldName,
    @NonNull Expression granularity
)
```

Creates an expression that truncates a timestamp to a specified granularity.

```
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate("createdAt", field("granularity"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(@NonNull String fieldName, @NonNull String granularity)
```

Creates an expression that truncates a timestamp to a specified granularity.

```
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate("createdAt", "day")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(
    @NonNull Expression timestamp,
    @NonNull Expression granularity
)
```

Creates an expression that truncates a timestamp to a specified granularity.

```
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate(field("createdAt"), field("granularity"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The timestamp expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(
    @NonNull Expression timestamp,
    @NonNull String granularity
)
```

Creates an expression that truncates a timestamp to a specified granularity.

```
// Truncate the 'createdAt' timestamp to the beginning of the day.
timestampTruncate(field("createdAt"), "day")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The timestamp expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(
    @NonNull String fieldName,
    @NonNull Expression granularity,
    @NonNull String timezone
)
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate("createdAt", field("granularity"), "America/Los_Angeles")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(
    @NonNull String fieldName,
    @NonNull String granularity,
    @NonNull String timezone
)
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate("createdAt", "day", "America/Los_Angeles")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the timestamp. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(
    @NonNull Expression timestamp,
    @NonNull Expression granularity,
    @NonNull String timezone
)
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate(field("createdAt"), field("granularity"), "America/Los_Angeles")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The timestamp expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression granularity` | The granularity expression to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### timestampTruncate

```
public static final @NonNull Expression timestampTruncate(
    @NonNull Expression timestamp,
    @NonNull String granularity,
    @NonNull String timezone
)
```

Creates an expression that truncates a timestamp to a specified granularity in a given timezone.

```
// Truncate the 'createdAt' timestamp to the beginning of the day in "America/Los_Angeles"
// timezone.
timestampTruncate(field("createdAt"), "day", "America/Los_Angeles")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression timestamp` | The timestamp expression. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html granularity` | The granularity to truncate to. Valid values are "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "week(monday)", "week(tuesday)", "week(wednesday)", "week(thursday)", "week(friday)", "week(saturday)", "week(sunday)", "isoweek", "month", "quarter", "year", and "isoyear". |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html timezone` | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the truncated timestamp. |

### toLower

```
public static final @NonNull Expression toLower(@NonNull String fieldName)
```

Creates an expression that converts a string field to lowercase.

```
// Convert the 'name' field to lowercase
toLower("name")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to convert to lowercase. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the lowercase string. |

### toLower

```
public static final @NonNull Expression toLower(@NonNull Expression stringExpression)
```

Creates an expression that converts a string expression to lowercase.

```
// Convert the 'name' field to lowercase
toLower(field("name"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to convert to lowercase. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the lowercase string. |

### toUpper

```
public static final @NonNull Expression toUpper(@NonNull String fieldName)
```

Creates an expression that converts a string field to uppercase.

```
// Convert the 'title' field to uppercase
toUpper("title")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to convert to uppercase. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the uppercase string. |

### toUpper

```
public static final @NonNull Expression toUpper(@NonNull Expression stringExpression)
```

Creates an expression that converts a string expression to uppercase.

```
// Convert the 'title' field to uppercase
toUpper(field("title"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to convert to uppercase. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the uppercase string. |

### trim

```
public static final @NonNull Expression trim(@NonNull String fieldName)
```

Creates an expression that removes leading and trailing whitespace from a string field.

```
// Trim whitespace from the 'userInput' field
trim("userInput")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to trim. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trim

```
public static final @NonNull Expression trim(@NonNull Expression stringExpression)
```

Creates an expression that removes leading and trailing whitespace from a string expression.

```
// Trim whitespace from the 'userInput' field
trim(field("userInput"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to trim. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trimValue

```
public static final @NonNull Expression trimValue(@NonNull String fieldName, @NonNull String valueToTrim)
```

Creates an expression that removes leading and trailing characters from a string field.

```
// Trim '-', and '_' from the beginning and the end of 'userInput' field
trimValue("userInput", "-_")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the string to trim. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html valueToTrim` | This parameter is treated as a set of characters or bytes that will be matched against the input from both ends. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string. |

### trimValue

```
public static final @NonNull Expression trimValue(
    @NonNull Expression stringExpression,
    @NonNull Expression valueToTrim
)
```

Creates an expression that removes leading and trailing values from a expression. The accepted values types are string and blob.

```
// Trim specified characters from the 'userInput' field
trimValue(field("userInput"), field("valueToTrim"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression stringExpression` | The expression representing the string to trim. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression valueToTrim` | The expression evaluated to either a string or a blob. This parameter is treated as a set of characters or bytes that will be matched against the input from both ends. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the trimmed string or bytes. |

### type

```
public static final @NonNull Expression type(@NonNull Expression expr)
```

Creates an expression that returns a string indicating the type of the value this expression evaluates to.

```
// Get the type of the 'value' field.
type(field("value"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression to get the type of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the type operation. |

### type

```
public static final @NonNull Expression type(@NonNull String fieldName)
```

Creates an expression that returns a string indicating the type of the value this field evaluates to.

```
// Get the type of the 'field' field.
type("field")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field to get the type of. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the type operation. |

### unixMicrosToTimestamp

```
public static final @NonNull Expression unixMicrosToTimestamp(@NonNull Expression expr)
```

Creates an expression that interprets an expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```
// Interpret the 'microseconds' field as microseconds since epoch.
unixMicrosToTimestamp(field("microseconds"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the number of microseconds since epoch. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixMicrosToTimestamp

```
public static final @NonNull Expression unixMicrosToTimestamp(@NonNull String fieldName)
```

Creates an expression that interprets a field's value as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```
// Interpret the 'microseconds' field as microseconds since epoch.
unixMicrosToTimestamp("microseconds")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the number of microseconds since epoch. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixMillisToTimestamp

```
public static final @NonNull Expression unixMillisToTimestamp(@NonNull Expression expr)
```

Creates an expression that interprets an expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```
// Interpret the 'milliseconds' field as milliseconds since epoch.
unixMillisToTimestamp(field("milliseconds"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the number of milliseconds since epoch. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixMillisToTimestamp

```
public static final @NonNull Expression unixMillisToTimestamp(@NonNull String fieldName)
```

Creates an expression that interprets a field's value as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```
// Interpret the 'milliseconds' field as milliseconds since epoch.
unixMillisToTimestamp("milliseconds")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the number of milliseconds since epoch. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixSecondsToTimestamp

```
public static final @NonNull Expression unixSecondsToTimestamp(@NonNull Expression expr)
```

Creates an expression that interprets an expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```
// Interpret the 'seconds' field as seconds since epoch.
unixSecondsToTimestamp(field("seconds"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expression representing the number of seconds since epoch. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### unixSecondsToTimestamp

```
public static final @NonNull Expression unixSecondsToTimestamp(@NonNull String fieldName)
```

Creates an expression that interprets a field's value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

```
// Interpret the 'seconds' field as seconds since epoch.
unixSecondsToTimestamp("seconds")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the number of seconds since epoch. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the timestamp. |

### vector

```
public static final @NonNull Expression vector(@NonNull double[] vector)
```

Create a vector constant for a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` value.

```
// Create a vector constant from a DoubleArray
vector(doubleArrayOf(1.0, 2.0, 3.0))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html double[] vector` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### vector

```
public static final @NonNull Expression vector(@NonNull VectorValue vector)
```

Create a vector constant for a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` value.

```
// Create a vector constant from a VectorValue
vector(VectorValue(listOf(1.0, 2.0, 3.0)))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue vector` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/VectorValue` value. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` constant instance. |

### vectorLength

```
public static final @NonNull Expression vectorLength(@NonNull String fieldName)
```

Creates an expression that calculates the length (dimension) of a Firestore Vector.

```
// Get the vector length (dimension) of the field 'embedding'.
vectorLength("embedding")
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of the field containing the Firestore Vector. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length (dimension) of the vector. |

### vectorLength

```
public static final @NonNull Expression vectorLength(@NonNull Expression vectorExpression)
```

Creates an expression that calculates the length (dimension) of a Firestore Vector.

```
// Get the vector length (dimension) of the field 'embedding'.
vectorLength(field("embedding"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression vectorExpression` | The expression representing the Firestore Vector. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` representing the length (dimension) of the vector. |

### xor

```
public static final @NonNull BooleanExpression xor(
    @NonNull BooleanExpression condition,
    @NonNull BooleanExpression conditions
)
```

Creates an expression that performs a logical 'XOR' operation.

```
// Check if either 'a' is true or 'b' is true, but not both
xor(field("a"), field("b"))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression condition` | The first `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression conditions` | Additional `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression`s. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the logical 'XOR' operation. |