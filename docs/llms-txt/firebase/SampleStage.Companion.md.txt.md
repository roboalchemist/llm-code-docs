# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion.md.txt

# SampleStage.Companion

# SampleStage.Companion


```
public static class SampleStage.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withDocLimit(kotlin.Int)(int results)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with the specified number of results returned. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)(double percentage)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with size limited to percentage of prior stages results. |

## Public methods

### withDocLimit

```
public static final @NonNull SampleStage withDocLimit(int results)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with the specified number of results returned.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withDocLimit(kotlin.Int)` parameter represents the number of results to produce and must be a non-negative integer value. If the previous stage produces less than the specified number, the entire previous results are returned. If the previous stage produces more than the specified number, this stage samples the specified number of documents from the previous stage, with equal probability for each result.

| Parameters |
|---|---|
| `int results` | The number of documents to emit. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with specified documents. |

### withPercentage

```
public static final @NonNull SampleStage withPercentage(double percentage)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with size limited to percentage of prior stages results.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)` parameter is the target percentage (between 0.0 \& 1.0) of the number of input documents to produce. Each input document is independently selected against the given percentage. As a result the output size will be approximately documents \* `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)`.

| Parameters |
|---|---|
| `double percentage` | The percentage of the prior stages documents to emit. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage` with specified `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/SampleStage.Companion#withPercentage(kotlin.Double)`. |