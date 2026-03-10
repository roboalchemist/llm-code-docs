# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage.Companion.md.txt

# AggregateStage.Companion

# AggregateStage.Companion


```
public static class AggregateStage.Companion
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage.Companion#withAccumulators(com.google.firebase.firestore.pipeline.AliasedAggregate,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate accumulator, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate additionalAccumulators )` Create `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` with one or more accumulators. |

## Public methods

### withAccumulators

```
public static final @NonNull AggregateStage withAccumulators(
    @NonNull AliasedAggregate accumulator,
    @NonNull AliasedAggregate additionalAccumulators
)
```

Create `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` with one or more accumulators.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate accumulator` | The first `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate` expression, wrapping an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` with an alias for the accumulated results. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate additionalAccumulators` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions, each wrapping an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` with an alias for the accumulated results. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` with specified accumulators. |