# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.md.txt

# Ordering

# Ordering


```
@Beta
public final class Ordering
```

<br />

*** ** * ** ***

Represents an ordering criterion for sorting documents in a Firestore pipeline.

You create `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` instances using the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)` and `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)` helper methods.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion` |
| `public enum https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction extends https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html` |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Direction` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering#dir()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering#expr()` |

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on field. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering#hashCode()()` |

## Public fields

### dir

```
public final @NonNull Ordering.Direction dir
```

### expr

```
public final @NonNull Expression expr
```

## Public methods

### ascending

```
public static final @NonNull Ordering ascending(@NonNull Expression expr)
```

Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The order is based on the evaluation of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` object with ascending sort by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)`. |

### ascending

```
public static final @NonNull Ordering ascending(@NonNull String fieldName)
```

Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on field.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of field to sort documents. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` object with ascending sort by field. |

### descending

```
public static final @NonNull Ordering descending(@NonNull Expression expr)
```

Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr` | The order is based on the evaluation of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression`. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` object with descending sort by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)`. |

### descending

```
public static final @NonNull Ordering descending(@NonNull String fieldName)
```

Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on field.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName` | The name of field to sort documents. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` object with descending sort by field. |

### equals

```
public boolean equals(Object other)
```

### hashCode

```
public int hashCode()
```