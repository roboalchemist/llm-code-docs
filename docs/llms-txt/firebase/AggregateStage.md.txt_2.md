# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage.md.txt

# AggregateStage

# AggregateStage


```
@Beta
class AggregateStage : Stage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.AggregateStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage) |

*** ** * ** ***

Performs optionally grouped aggregation operations on the documents from previous stages.

This stage allows you to calculate aggregate values over a set of documents, optionally grouped by one or more fields or functions. You can specify:

- **Grouping Fields or Expressions:** One or more fields or functions to group the documents by. For each distinct combination of values in these fields, a separate group is created. If no grouping fields are provided, a single group containing all documents is used. Not specifying groups is the same as putting the entire inputs into one group.

- **AggregateFunctions:** One or more accumulation operations to perform within each group. These are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions, which are typically created by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction#alias(kotlin.String)` on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` instances. Each aggregation calculates a value (e.g., sum, average, count) based on the documents within its group.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage.Companion#withAccumulators(com.google.firebase.firestore.pipeline.AliasedAggregate,kotlin.Array)( accumulator: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate, vararg additionalAccumulators: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate )` Create `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` with one or more accumulators. |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage#hashCode()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage#withGroups(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)(group: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable, vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Add one or more groups to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage#withGroups(kotlin.String,kotlin.Array)(groupField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Add one or more groups to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public companion functions

### withAccumulators

```
fun withAccumulators(
    accumulator: AliasedAggregate,
    vararg additionalAccumulators: AliasedAggregate
): AggregateStage
```

Create `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` with one or more accumulators.

| Parameters |
|---|---|
| `accumulator: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` | The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expression, wrapping an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` with an alias for the accumulated results. |
| `vararg additionalAccumulators: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions, each wrapping an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` with an alias for the accumulated results. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` with specified accumulators. |

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

### hashCode

```
open fun hashCode(): Int
```

### withGroups

```
fun withGroups(group: Selectable, vararg additionalGroups: Any): AggregateStage
```

Add one or more groups to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage`

| Parameters |
|---|---|
| `group: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expression to consider when determining group value combinations. |
| `vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions to consider when determining group value combinations or `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`s representing field names. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` with specified groups. |

### withGroups

```
fun withGroups(groupField: String, vararg additionalGroups: Any): AggregateStage
```

Add one or more groups to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage`

| Parameters |
|---|---|
| `groupField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` representing field name. |
| `vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions to consider when determining group value combinations or `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`s representing field names. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` with specified groups. |