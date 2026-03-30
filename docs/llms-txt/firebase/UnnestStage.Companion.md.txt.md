# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion.md.txt

# UnnestStage.Companion

# UnnestStage.Companion


```
public static class UnnestStage.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable arrayWithAlias)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html alias)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |

## Public methods

### withField

```
public static final @NonNull UnnestStage withField(@NonNull Selectable arrayWithAlias)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array is found in parameter `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)`, which can be an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` with an alias specified via `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression#alias(kotlin.String)`, or a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` that can also have alias specified. For each element of the input array, an augmented document will be produced. The element of input array will be stored in a field with name specified by the alias of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)` parameter. If the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)` is a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` with no alias, then the original array field will be replaced with the individual element.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable arrayWithAlias` | The input array with field alias to store output element of array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |

### withField

```
public static final @NonNull UnnestStage withField(@NonNull String arrayField, @NonNull String alias)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array found in the previous stage document field specified by the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)` parameter, will for each element of the input array produce an augmented document. The element of the input array will be stored in a field with name specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)` parameter on the augmented document.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |