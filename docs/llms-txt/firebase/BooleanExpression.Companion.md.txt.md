# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression.Companion.md.txt

# BooleanExpression.Companion

# BooleanExpression.Companion


```
public static class BooleanExpression.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression.Companion#rawFunction(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Creates a 'raw' boolean function expression. |

## Public methods

### rawFunction

```
public static final @NonNull BooleanExpression rawFunction(@NonNull String name, @NonNull Expression expr)
```

Creates a 'raw' boolean function expression. This is useful if the expression is available in the backend, but not yet in the current version of the SDK yet.

```
// Create a raw boolean function call
BooleanExpression.rawFunction("my_boolean_function", field("arg1"), constant(true))
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html name` | The name of the raw function. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The expressions to be passed as arguments to the function. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/BooleanExpression` representing the raw function. |