# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage.md.txt

# AggregateStage

# AggregateStage


```
@Beta
public final class AggregateStage extends Stage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.AggregateStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage) |

*** ** * ** ***

Performs optionally grouped aggregation operations on the documents from previous stages.

This stage allows you to calculate aggregate values over a set of documents, optionally grouped by one or more fields or functions. You can specify:

- **Grouping Fields or Expressions:** One or more fields or functions to group the documents by. For each distinct combination of values in these fields, a separate group is created. If no grouping fields are provided, a single group containing all documents is used. Not specifying groups is the same as putting the entire inputs into one group.

- **AggregateFunctions:** One or more accumulation operations to perform within each group. These are defined using `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions, which are typically created by calling `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction#alias(kotlin.String)` on `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateFunction` instances. Each aggregation calculates a value (e.g., sum, average, count) based on the documents within its group.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage.Companion` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage#hashCode()()` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage.Companion#withAccumulators(com.google.firebase.firestore.pipeline.AliasedAggregate,kotlin.Array)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate accumulator, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AliasedAggregate additionalAccumulators )` Create `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` with one or more accumulators. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage#withGroups(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable group, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html additionalGroups)` Add one or more groups to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage#withGroups(kotlin.String,kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html groupField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html additionalGroups)` Add one or more groups to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` |

| ### Inherited methods |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class> value )` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value)` Specify named `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public methods

### equals

```
public boolean equals(Object other)
```

### hashCode

```
public int hashCode()
```

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

### withGroups

```
public final @NonNull AggregateStage withGroups(@NonNull Selectable group, @NonNull Object additionalGroups)
```

Add one or more groups to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable group` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable` expression to consider when determining group value combinations. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html additionalGroups` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable` expressions to consider when determining group value combinations or `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`s representing field names. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` with specified groups. |

### withGroups

```
public final @NonNull AggregateStage withGroups(@NonNull String groupField, @NonNull Object additionalGroups)
```

Add one or more groups to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage`

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html groupField` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` representing field name. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Object.html additionalGroups` | The `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable` expressions to consider when determining group value combinations or `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`s representing field names. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/AggregateStage` with specified groups. |