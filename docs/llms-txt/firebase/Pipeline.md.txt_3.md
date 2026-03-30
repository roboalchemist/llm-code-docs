# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.md.txt

# Pipeline

# Pipeline


```
@Beta
class Pipeline
```

<br />

*** ** * ** ***

A `Pipeline` is composed of a sequence of stages. Each stage processes the output from the previous one, and the final stage's output is the result of the pipeline's execution.

**Example usage:**

```
{@code Pipeline pipeline = firestore.pipeline()
.collection("books") .where(Field("rating").isGreaterThan(4.5))
.sort(Field("rating").descending()) .limit(2); }
```

**Note on Execution:** The stages are conceptual. The Firestore backend may optimize
execution (e.g., reordering or merging stages) as long as the final result remains the same.

**Important Limitations:**

- Pipelines operate on a **request/response basis
  only**.
- They do **not** utilize or update the local SDK cache.
- They do **not** support realtime snapshot listeners.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AbstractOptions` |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions.IndexMode` |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html` A `Snapshot` contains the results of a pipeline execution. |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#addFields(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)(field: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable, vararg additionalFields: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable)` Adds new fields to outputs from previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#aggregate(com.google.firebase.firestore.pipeline.AggregateStage)(aggregateStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage)` Performs optionally grouped aggregation operations on the documents from previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#aggregate(com.google.firebase.firestore.pipeline.AliasedAggregate,kotlin.Array)( accumulator: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate, vararg additionalAccumulators: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate )` Performs aggregation operations on the documents from previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#aggregate(com.google.firebase.firestore.pipeline.AggregateStage,com.google.firebase.firestore.pipeline.AggregateOptions)(aggregateStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateOptions)` Performs optionally grouped aggregation operations on the documents from previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#distinct(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)(group: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable, vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Returns a set of distinct values from the inputs to this stage. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#distinct(kotlin.String,kotlin.Array)(groupField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Returns a set of distinct values from the inputs to this stage. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#execute()()` Executes this pipeline and returns the results as a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot`. |
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#execute(com.google.firebase.firestore.Pipeline.ExecuteOptions)(options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions)` Executes this pipeline and returns the results as a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#findNearest(com.google.firebase.firestore.pipeline.Field,kotlin.DoubleArray,com.google.firebase.firestore.pipeline.FindNearestStage.DistanceMeasure)( vectorField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field, vectorValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html, distanceMeasure: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure )` Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the full set in the order of similarity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#findNearest(kotlin.String,kotlin.DoubleArray,com.google.firebase.firestore.pipeline.FindNearestStage.DistanceMeasure)( vectorField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vectorValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html, distanceMeasure: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure )` Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the full set in the order of similarity. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#findNearest(kotlin.String,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.FindNearestStage.DistanceMeasure,com.google.firebase.firestore.pipeline.FindNearestOptions)( vectorField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vectorValue: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression, distanceMeasure: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions )` Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the first N documents (specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions#withLimit(kotlin.Long)`) in the result set. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#limit(kotlin.Int)(limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Limits the maximum number of documents returned by previous stages to `limit`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#offset(kotlin.Int)(offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Skips the first `offset` number of documents from the results of previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#rawStage(com.google.firebase.firestore.pipeline.RawStage)(rawStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage)` Adds a raw stage to the pipeline by specifying the stage name as an argument. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#removeFields(com.google.firebase.firestore.pipeline.Field,kotlin.Array)(field: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field, vararg additionalFields: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Remove fields from outputs of previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#removeFields(kotlin.String,kotlin.Array)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg additionalFields: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Remove fields from outputs of previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#replaceWith(kotlin.String)(field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Fully overwrites all fields in a document with those coming from a nested map. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#replaceWith(com.google.firebase.firestore.pipeline.Expression)(mapValue: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression)` Fully overwrites all fields in a document with those coming from a nested map. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#sample(kotlin.Int)(documents: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Performs a pseudo-random sampling of the input documents. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#sample(com.google.firebase.firestore.pipeline.SampleStage)(sample: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage)` Performs a pseudo-random sampling of the input documents. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#select(kotlin.String,kotlin.Array)(fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, vararg additionalSelections: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Selects or creates a set of fields from the outputs of previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#select(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)(selection: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable, vararg additionalSelections: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Selects or creates a set of fields from the outputs of previous stages. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#sort(com.google.firebase.firestore.pipeline.Ordering,kotlin.Array)(order: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering, vararg additionalOrders: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering)` Sorts the documents from previous stages based on one or more `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` criteria. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#union(com.google.firebase.firestore.Pipeline)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline)` Performs union of all documents from two pipelines, including duplicates. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable)(arrayWithAlias: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable)` Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.UnnestStage)(unnestStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage)` Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(kotlin.String,kotlin.String)(arrayField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, alias: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable,com.google.firebase.firestore.pipeline.UnnestOptions)(arrayWithAlias: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions)` Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#where(com.google.firebase.firestore.pipeline.BooleanExpression)(condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression)` Filters the documents from previous stages to only include those matching the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`. |

## Public functions

### addFields

```
fun addFields(field: Selectable, vararg additionalFields: Selectable): Pipeline
```

Adds new fields to outputs from previous stages.

This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones.

The added fields are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable`s, which can be:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`: References an existing document field.

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression`: Represents the result of a expression with an assigned alias name using Expr.alias

Example:

```kotlin
firestore.pipeline().collection("books")
  .addFields(
    field("rating").as("bookRating"), // Rename 'rating' to 'bookRating'
    add(5, field("quantity")).as("totalCost")  // Calculate 'totalCost'
  );
```

| Parameters |
|---|---|
| `field: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The first field to add to the documents, specified as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable`. |
| `vararg additionalFields: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The fields to add to the documents, specified as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable`s. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### aggregate

```
fun aggregate(aggregateStage: AggregateStage): Pipeline
```

Performs optionally grouped aggregation operations on the documents from previous stages.

This stage allows you to calculate aggregate values over a set of documents, optionally grouped by one or more fields or functions. You can specify:

- **Grouping Fields or Expressions:** One or more fields or functions to group the documents by. For each distinct combination of values in these fields, a separate group is created. If no grouping fields are provided, a single group containing all documents is used. Not specifying groups is the same as putting the entire inputs into one group.

- **AggregateFunctions:** One or more accumulation operations to perform within each group. These are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions, which are typically created by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction#alias(kotlin.String)` on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` instances. Each aggregation calculates a value (e.g., sum, average, count) based on the documents within its group.

Example:

```kotlin
// Calculate the average rating for each genre.
firestore.pipeline().collection("books")
  .aggregate(
    Aggregate
      .withAccumulators(average("rating").as("avg_rating"))
      .withGroups("genre"));
```

| Parameters |
|---|---|
| `aggregateStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` object that specifies the grouping fields (if any) and the aggregation operations to perform. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### aggregate

```
fun aggregate(
    accumulator: AliasedAggregate,
    vararg additionalAccumulators: AliasedAggregate
): Pipeline
```

Performs aggregation operations on the documents from previous stages.

This stage allows you to calculate aggregate values over a set of documents. You define the aggregations to perform using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions which are typically results of calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction#alias(kotlin.String)` on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` instances.

Example:

```kotlin
// Calculate the average rating and the total number of books
firestore.pipeline().collection("books")
    .aggregate(
        field("rating").average().as("averageRating"),
        countAll().as("totalBooks")
    );
```

| Parameters |
|---|---|
| `accumulator: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` | The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expression, wrapping an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` with an alias for the accumulated results. |
| `vararg additionalAccumulators: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions, each wrapping an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` with an alias for the accumulated results. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### aggregate

```
fun aggregate(aggregateStage: AggregateStage, options: AggregateOptions): Pipeline
```

Performs optionally grouped aggregation operations on the documents from previous stages.

This stage allows you to calculate aggregate values over a set of documents, optionally grouped by one or more fields or functions. You can specify:

- **Grouping Fields or Expressions:** One or more fields or functions to group the documents by. For each distinct combination of values in these fields, a separate group is created. If no grouping fields are provided, a single group containing all documents is used. Not specifying groups is the same as putting the entire inputs into one group.

- **AggregateFunctions:** One or more accumulation operations to perform within each group. These are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedAggregate` expressions, which are typically created by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction#alias(kotlin.String)` on `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateFunction` instances. Each aggregation calculates a value (e.g., sum, average, count) based on the documents within its group.

| Parameters |
|---|---|
| `aggregateStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateStage` object that specifies the grouping fields (if any) and the aggregation operations to perform. |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateOptions` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AggregateOptions` to use when performing the aggregation. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### distinct

```
fun distinct(group: Selectable, vararg additionalGroups: Any): Pipeline
```

Returns a set of distinct values from the inputs to this stage.

This stage runs through the results from previous stages to include only results with unique combinations of Expr values `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FunctionExpression`, etc).

The parameters to this stage are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions or strings:

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`: Name of an existing field

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`: References an existing document field.

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression`: Represents the result of a function with an assigned alias name using Expr.alias

Example:

```kotlin
// Get a list of unique author names in uppercase and genre combinations.
firestore.pipeline().collection("books")
    .distinct(toUppercase(field("author")).as("authorName"), field("genre"))
    .select("authorName");
```

| Parameters |
|---|---|
| `group: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expression to consider when determining distinct value combinations. |
| `vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions to consider when determining distinct value combinations or `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`s representing field names. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### distinct

```
fun distinct(groupField: String, vararg additionalGroups: Any): Pipeline
```

Returns a set of distinct values from the inputs to this stage.

This stage runs through the results from previous stages to include only results with unique combinations of Expr values (`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FunctionExpression`, etc).

The parameters to this stage are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions or strings:

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`: Name of an existing field

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`: References an existing document field.

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression`: Represents the result of a function with an assigned alias name using Expr.alias

Example:

```kotlin
// Get a list of unique genres.
firestore.pipeline().collection("books")
    .distinct("genre");
```

| Parameters |
|---|---|
| `groupField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` representing field name. |
| `vararg additionalGroups: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions to consider when determining distinct value combinations or `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`s representing field names. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### execute

```
fun execute(): Task<Pipeline.Snapshot>
```

Executes this pipeline and returns the results as a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot`.

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that will be resolved with the results of the pipeline. |

### execute

```
fun execute(options: Pipeline.ExecuteOptions): Task<Pipeline.Snapshot>
```

Executes this pipeline and returns the results as a `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot`.

| Parameters |
|---|---|
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.ExecuteOptions` to use to instruct Firestore backend execution. |

| Returns |
|---|---|
| `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline.Snapshot>` | A `https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html` that will be resolved with the results of the pipeline. |

### findNearest

```
fun findNearest(
    vectorField: Field,
    vectorValue: DoubleArray,
    distanceMeasure: FindNearestStage.DistanceMeasure
): Pipeline
```

Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the full set in the order of similarity.

| Parameters |
|---|---|
| `vectorField: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` that contains vector to search on. |
| `vectorValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` that is used to measure the distance from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#findNearest(com.google.firebase.firestore.pipeline.Field,kotlin.DoubleArray,com.google.firebase.firestore.pipeline.FindNearestStage.DistanceMeasure)` values in the documents. |
| `distanceMeasure: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure` | specifies what type of distance is calculated. when performing the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### findNearest

```
fun findNearest(
    vectorField: String,
    vectorValue: DoubleArray,
    distanceMeasure: FindNearestStage.DistanceMeasure
): Pipeline
```

Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the full set in the order of similarity.

| Parameters |
|---|---|
| `vectorField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` specifying the vector field to search on. |
| `vectorValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double-array/index.html` that is used to measure the distance from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#findNearest(kotlin.String,kotlin.DoubleArray,com.google.firebase.firestore.pipeline.FindNearestStage.DistanceMeasure)` values in the documents. |
| `distanceMeasure: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure` | specifies what type of distance is calculated when performing the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### findNearest

```
fun findNearest(
    vectorField: String,
    vectorValue: Expression,
    distanceMeasure: FindNearestStage.DistanceMeasure,
    options: FindNearestOptions
): Pipeline
```

Performs a vector similarity search, ordering the result set by most similar to least similar, and returning the first N documents (specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions#withLimit(kotlin.Long)`) in the result set.

Example:

```kotlin
// Find books with similar "topicVectors" to the given targetVector
firestore.pipeline().collection("books")
    .findNearest("topicVectors", targetVector, FindNearest.DistanceMeasure.COSINE,
       new FindNearestOptions()
         .withLimit(10)
         .withDistanceField("distance"));
```

| Parameters |
|---|---|
| `vectorField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A field name that contains vector to search on. |
| `vectorValue: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` that should evaluate to a vector used to measure the distance from `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#findNearest(kotlin.String,com.google.firebase.firestore.pipeline.Expression,com.google.firebase.firestore.pipeline.FindNearestStage.DistanceMeasure,com.google.firebase.firestore.pipeline.FindNearestOptions)` values in the documents. |
| `distanceMeasure: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestStage.DistanceMeasure` | specifies what type of distance is calculated when performing the search. |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/FindNearestOptions` to use when performing the search. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### limit

```
fun limit(limit: Int): Pipeline
```

Limits the maximum number of documents returned by previous stages to `limit`.

This stage is particularly useful when you want to retrieve a controlled subset of data from a potentially large result set. It's often used for:

- **Pagination:** In combination with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#offset(kotlin.Int)` to retrieve specific pages of results.

- **Limiting Data Retrieval:** To prevent excessive data transfer and improve performance, especially when dealing with large collections.

Example:

```kotlin
// Limit the results to the top 10 highest-rated books
firestore.pipeline().collection("books")
    .sort(field("rating").descending())
    .limit(10);
```

| Parameters |
|---|---|
| `limit: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The maximum number of documents to return. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### offset

```
fun offset(offset: Int): Pipeline
```

Skips the first `offset` number of documents from the results of previous stages.

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#limit(kotlin.Int)` to control the size of each page.

Example:

```kotlin
// Retrieve the second page of 20 results
firestore.pipeline().collection("books")
    .sort(field("published").descending())
    .offset(20)  // Skip the first 20 results
    .limit(20);   // Take the next 20 results
```

| Parameters |
|---|---|
| `offset: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of documents to skip. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### rawStage

```
fun rawStage(rawStage: RawStage): Pipeline
```

Adds a raw stage to the pipeline by specifying the stage name as an argument. This does not offer any type safety on the stage params and requires the caller to know the order (and optionally names) of parameters accepted by the stage.

This method provides a way to call stages that are supported by the Firestore backend but that are not implemented in the SDK version being used.

| Parameters |
|---|---|
| `rawStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` object that specifies stage name and parameters. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### removeFields

```
fun removeFields(field: Field, vararg additionalFields: Field): Pipeline
```

Remove fields from outputs of previous stages.

Example:

```kotlin
firestore.pipeline().collection("books")
  .removeFields(
    field("rating"), field("cost")
  );
```

| Parameters |
|---|---|
| `field: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` to remove. |
| `vararg additionalFields: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` | Optional additional `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`s to remove. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### removeFields

```
fun removeFields(field: String, vararg additionalFields: String): Pipeline
```

Remove fields from outputs of previous stages.

Example:

```kotlin
firestore.pipeline().collection("books")
  .removeFields(
    "rating", "cost"
  );
```

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The first `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` name of field to remove. |
| `vararg additionalFields: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Optional additional `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` name of fields to remove. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### replaceWith

```
fun replaceWith(field: String): Pipeline
```

Fully overwrites all fields in a document with those coming from a nested map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

Example:

```kotlin
// Input.
// {
//  "name": "John Doe Jr.",
//  "parents": {
//    "father": "John Doe Sr.",
//    "mother": "Jane Doe"
// }

// Emit parents as document.
firestore.pipeline().collection("people").replaceWith("parents");

// Output
// {
//  "father": "John Doe Sr.",
//  "mother": "Jane Doe"
// }
```

| Parameters |
|---|---|
| `field: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` specifying the field name containing the nested map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### replaceWith

```
fun replaceWith(mapValue: Expression): Pipeline
```

Fully overwrites all fields in a document with those coming from a nested map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

Example:

```kotlin
// Input.
// {
//  "name": "John Doe Jr.",
//  "parents": {
//    "father": "John Doe Sr.",
//    "mother": "Jane Doe"
// }

// Emit parents as document.
firestore.pipeline().collection("people").replaceWith(field("parents"));

// Output
// {
//  "father": "John Doe Sr.",
//  "mother": "Jane Doe"
// }
```

| Parameters |
|---|---|
| `mapValue: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Expression` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` containing the nested map. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### sample

```
fun sample(documents: Int): Pipeline
```

Performs a pseudo-random sampling of the input documents.

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#sample(kotlin.Int)` parameter represents the target number of documents to produce and must be a non-negative integer value. If the previous stage produces less than size documents, the entire previous results are returned. If the previous stage produces more than size, this outputs a sample of exactly size entries where any sample is equally likely.

Example:

```kotlin
// Sample 10 books, if available.
firestore.pipeline().collection("books")
    .sample(10);
```

| Parameters |
|---|---|
| `documents: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The number of documents to emit. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### sample

```
fun sample(sample: SampleStage): Pipeline
```

Performs a pseudo-random sampling of the input documents.

Examples:

```kotlin
// Sample 10 books, if available.
firestore.pipeline().collection("books")
    .sample(Sample.withDocLimit(10));

// Sample 50% of books.
firestore.pipeline().collection("books")
    .sample(Sample.withPercentage(0.5));
```

| Parameters |
|---|---|
| `sample: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/SampleStage` object that specifies how sampling is performed. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### select

```
fun select(fieldName: String, vararg additionalSelections: Any): Pipeline
```

Selects or creates a set of fields from the outputs of previous stages.

The selected fields are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions, which can be:

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`: Name of an existing field

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`: Reference to an existing field.

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression`: Represents the result of a expression with an assigned alias name using Expr.alias

If no selections are provided, the output of this stage is empty. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#addFields(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)` instead if only additions are desired.

Example:

```kotlin
firestore.collection("books")
  .select("name", "address");

// The above is a shorthand of this:
firestore.pipeline().collection("books")
   .select(field("name"), field("address"));
```

| Parameters |
|---|---|
| `fieldName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The first field to include in the output documents, specified as a string value representing a field names. |
| `vararg additionalSelections: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional fields to include in the output documents, specified as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions or string values representing field names. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### select

```
fun select(selection: Selectable, vararg additionalSelections: Any): Pipeline
```

Selects or creates a set of fields from the outputs of previous stages.

The selected fields are defined using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions or strings, which can be:

- `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html`: Name of an existing field

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field`: Reference to an existing field.

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/AliasedExpression`: Represents the result of a expression with an assigned alias name using Expr.alias

If no selections are provided, the output of this stage is empty. Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#addFields(com.google.firebase.firestore.pipeline.Selectable,kotlin.Array)` instead if only additions are desired.

Example:

```kotlin
firestore.pipeline().collection("books")
  .select(
    field("name"),
    field("address").toUppercase().as("upperAddress"),
  );
```

| Parameters |
|---|---|
| `selection: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The first field to include in the output documents, specified as a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expression. |
| `vararg additionalSelections: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | Optional additional fields to include in the output documents, specified as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` expressions or string values representing field names. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### sort

```
fun sort(order: Ordering, vararg additionalOrders: Ordering): Pipeline
```

Sorts the documents from previous stages based on one or more `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` criteria.

This stage allows you to order the results of your pipeline. You can specify multiple `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` instances to sort by multiple fields in ascending or descending order. If documents have the same value for a field used for sorting, the next specified ordering will be used. If all orderings result in equal comparison, the documents are considered equal and the order is unspecified.

Example:

```kotlin
// Sort books by rating in descending order, and then by title in ascending order for books with the same rating
firestore.pipeline().collection("books")
    .sort(
        Ordering.of("rating").descending(),
        Ordering.of("title")  // Ascending order is the default
    );
```

| Parameters |
|---|---|
| `order: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | The first `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` instance specifying the sorting criteria. |
| `vararg additionalOrders: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` | Optional additional `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Ordering` instances specifying the sorting criteria. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### union

```
fun union(other: Pipeline): Pipeline
```

Performs union of all documents from two pipelines, including duplicates.

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the `other` Pipeline given in parameter. The order of documents emitted from this stage is undefined.

Example:

```kotlin
// Emit documents from books collection and magazines collection.
firestore.pipeline().collection("books")
    .union(firestore.pipeline().collection("magazines"));
```

| Parameters |
|---|---|
| `other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | The other `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` that is part of union. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### unnest

```
fun unnest(arrayWithAlias: Selectable): Pipeline
```

Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array is found in parameter `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable)`, which can be an Expr with an alias specified via Expr.alias, or a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` that can also have alias specified. For each element of the input array, an augmented document will be produced. The element of input array will be stored in a field with name specified by the alias of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable)` parameter. If the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable)` is a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` with no alias, then the original array field will be replaced with the individual element.

| Parameters |
|---|---|
| `arrayWithAlias: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The input array with field alias to store output element of array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### unnest

```
fun unnest(unnestStage: UnnestStage): Pipeline
```

Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array specified in the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.UnnestStage)` parameter will for each element of the input array produce an augmented document. The element of the input array will be stored in a field with a name specified by the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.UnnestStage)` parameter.

Optionally, an index field can also be added to emitted documents. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` for further information.

| Parameters |
|---|---|
| `unnestStage: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` | An `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestStage` object that specifies the search parameters. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### unnest

```
fun unnest(arrayField: String, alias: String): Pipeline
```

Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array found in the previous stage document field specified by the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(kotlin.String,kotlin.String)` parameter, will for each element of the input array produce an augmented document. The element of the input array will be stored in a field with name specified by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(kotlin.String,kotlin.String)` parameter on the augmented document.

Example:

```kotlin
// Input:
// { "title": "The Hitchhiker's Guide to the Galaxy", "tags": [ "comedy", "space", "adventure" ], ... }

// Emit a book document for each tag of the book.
firestore.pipeline().collection("books")
    .unnest("tags", "tag");

// Output:
// { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "comedy", ... }
// { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "space", ... }
// { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "adventure", ... }
```

| Parameters |
|---|---|
| `arrayField: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of the field containing the array. |
| `alias: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The name of field to store emitted element of array. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### unnest

```
fun unnest(arrayWithAlias: Selectable, options: UnnestOptions): Pipeline
```

Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array is found in parameter `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable,com.google.firebase.firestore.pipeline.UnnestOptions)`, which can be an Expr with an alias specified via Expr.alias, or a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` that can also have alias specified. For each element of the input array, an augmented document will be produced. The element of input array will be stored in a field with name specified by the alias of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable,com.google.firebase.firestore.pipeline.UnnestOptions)` parameter. If the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline#unnest(com.google.firebase.firestore.pipeline.Selectable,com.google.firebase.firestore.pipeline.UnnestOptions)` is a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` with no alias, then the original array field will be replaced with the individual element.

Example:

```kotlin
// Input:
// { "title": "The Hitchhiker's Guide to the Galaxy", "tags": [ "comedy", "space", "adventure" ], ... }

// Emit a book document for each tag of the book.
firestore.pipeline().collection("books")
    .unnest("tags", "tag", new UnnestOptions().withIndexField("tagIndex"));

// Output:
// { "title": "The Hitchhiker's Guide to the Galaxy", "tagIndex": 0, "tag": "comedy", ... }
// { "title": "The Hitchhiker's Guide to the Galaxy", "tagIndex": 1, "tag": "space", ... }
// { "title": "The Hitchhiker's Guide to the Galaxy", "tagIndex": 2, "tag": "adventure", ... }
```

| Parameters |
|---|---|
| `arrayWithAlias: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Selectable` | The input array with field alias to store output element of array. |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/UnnestOptions` to use when performing the unnest. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |

### where

```
fun where(condition: BooleanExpression): Pipeline
```

Filters the documents from previous stages to only include those matching the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`.

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL.

You can filter documents based on their field values, using implementations of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression`, typically including but not limited to:

- field comparators: Expr.equal, Expr.lessThan, Expr.greaterThan, etc.

- logical operators: Expr.and, Expr.or, Expr.not, etc.

- advanced functions: Expr.regexMatch, Expr.arrayContains, etc.

Example:

```kotlin
firestore.pipeline().collection("books")
  .where(
    and(
        gt("rating", 4.0),   // Filter for ratings greater than 4.0
        field("genre").equal("Science Fiction") // Equivalent to equal("genre", "Science Fiction")
    )
  );
```

| Parameters |
|---|---|
| `condition: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/BooleanExpression` to apply. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with this stage appended to the stage list. |