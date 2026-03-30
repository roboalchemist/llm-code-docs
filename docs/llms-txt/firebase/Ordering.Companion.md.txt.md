# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion.md.txt

# Ordering.Companion

# Ordering.Companion


```
public static class Ordering.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#ascending(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in ascending order based on field. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression expr)` Create an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on value of `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(com.google.firebase.firestore.pipeline.Expression)`. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering.Companion#descending(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html fieldName)` Creates an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Ordering` that sorts documents in descending order based on field. |

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