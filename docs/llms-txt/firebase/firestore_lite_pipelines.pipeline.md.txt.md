# Source: https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md.txt

# Pipeline class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The Pipeline class provides a flexible and expressive framework for building complex data transformation and query pipelines for Firestore.

A pipeline takes data sources, such as Firestore collections or collection groups, and applies a series of stages that are chained together. Each stage takes the output from the previous stage (or the data source) and produces an output for the next stage (or as the final output of the pipeline).

Expressions can be used within each stage to filter and transform data through the stage.

NOTE: The chained stages do not prescribe exactly how Firestore will execute the pipeline. Instead, Firestore only guarantees that the result is the same as if the chained stages were executed in order.

Usage Examples:

**Signature:**

    export declare class Pipeline 

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [addFields(field, additionalFields)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineaddfields) |   | ***(Public Preview)*** Adds new fields to outputs from previous stages.This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones (if there is name overlaps).The added fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)s, which can be:- [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class): Either a literal value (see [constant()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_0c00f91)) or a computed value with an assigned alias using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).Example: |
| [addFields(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineaddfields) |   | ***(Public Preview)*** Adds new fields to outputs from previous stages.This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones (if there is name overlaps).The added fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)s, which can be:- [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class): Either a literal value (see [constant()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_0c00f91)) or a computed value with an assigned alias using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).Example: |
| [aggregate(accumulator, additionalAccumulators)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineaggregate) |   | ***(Public Preview)*** Performs aggregation operations on the documents from previous stages. This stage allows you to calculate aggregate values over a set of documents. You define the aggregations to perform using [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class) expressions which are typically results of calling [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas) on [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) instances. Example: |
| [aggregate(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineaggregate) |   | ***(Public Preview)*** Performs optionally grouped aggregation operations on the documents from previous stages. This stage allows you to calculate aggregate values over a set of documents, optionally grouped by one or more fields or functions. You can specify: - \*\*Grouping Fields or Functions:\*\* One or more fields or functions to group the documents by. For each distinct combination of values in these fields, a separate group is created. If no grouping fields are provided, a single group containing all documents is used. Not specifying groups is the same as putting the entire inputs into one group. - \*\*Accumulators:\*\* One or more accumulation operations to perform within each group. These are defined using [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class) expressions, which are typically created by calling [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas) on [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) instances. Each aggregation calculates a value (e.g., sum, average, count) based on the documents within its group. Example: |
| [distinct(group, additionalGroups)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinedistinct) |   | ***(Public Preview)*** Returns a set of distinct values from the inputs to this stage.This stage runs through the results from previous stages to include only results with unique combinations of [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) values ([Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class), [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class), etc).The parameters to this stage are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions or strings:- `string`: Name of an existing field - [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).Example: |
| [distinct(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinedistinct) |   | ***(Public Preview)*** Returns a set of distinct values from the inputs to this stage.This stage runs through the results from previous stages to include only results with unique combinations of [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) values ([Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class), [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class), etc).The parameters to this stage are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions or strings:- `string`: Name of an existing field - [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).Example: |
| [findNearest(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinefindnearest) |   | ***(Public Preview)*** Performs a vector proximity search on the documents from the previous stage, returning the K-nearest documents based on the specified query `vectorValue` and `distanceMeasure`. The returned documents will be sorted in order from nearest to furthest from the query `vectorValue`. Example: |

    // Find the 10 most similar books based on the book description.
    const bookDescription = "Lorem ipsum...";
    const queryVector: number[] = ...; // compute embedding of `bookDescription`

    firestore.pipeline().collection("books")
        .findNearest({
          field: 'embedding',
          vectorValue: queryVector,
          distanceMeasure: 'euclidean',
          limit: 10,                        // optional
          distanceField: 'computedDistance' // optional
        });

\|
\| [limit(limit)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinelimit) \| \| ***(Public Preview)*** Limits the maximum number of documents returned by previous stages to `limit`.

This stage is particularly useful when you want to retrieve a controlled subset of data from a potentially large result set. It's often used for:

- \*\*Pagination:\*\* In combination with to retrieve specific pages of results.
- \*\*Limiting Data Retrieval:\*\* To prevent excessive data transfer and improve performance, especially when dealing with large collections.

Example: \|
\| [limit(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinelimit) \| \| ***(Public Preview)*** Limits the maximum number of documents returned by previous stages to `limit`.

This stage is particularly useful when you want to retrieve a controlled subset of data from a potentially large result set. It's often used for:

- \*\*Pagination:\*\* In combination with to retrieve specific pages of results.
- \*\*Limiting Data Retrieval:\*\* To prevent excessive data transfer and improve performance, especially when dealing with large collections.

Example: \|
\| [offset(offset)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineoffset) \| \| ***(Public Preview)*** Skips the first `offset` number of documents from the results of previous stages.

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with to control the size of each page.

Example: \|
\| [offset(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineoffset) \| \| ***(Public Preview)*** Skips the first `offset` number of documents from the results of previous stages.

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with to control the size of each page.

Example: \|
\| [rawStage(name, params, options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinerawstage) \| \| ***(Public Preview)*** Adds a raw stage to the pipeline.

This method provides a flexible way to extend the pipeline's functionality by adding custom stages. Each raw stage is defined by a unique `name` and a set of `params` that control its behavior.

Example (Assuming there is no 'where' stage available in SDK): \|
\| [removeFields(fieldValue, additionalFields)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineremovefields) \| \| ***(Public Preview)*** Remove fields from outputs of previous stages.Example: \|
\| [removeFields(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineremovefields) \| \| ***(Public Preview)*** Remove fields from outputs of previous stages.Example: \|
\| [replaceWith(fieldName)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinereplacewith) \| \| ***(Public Preview)*** Fully overwrites all fields in a document with those coming from a nested map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

Example: \|
\| [replaceWith(expr)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinereplacewith) \| \| ***(Public Preview)*** Fully overwrites all fields in a document with those coming from a map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

Example: \|
\| [replaceWith(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinereplacewith) \| \| ***(Public Preview)*** Fully overwrites all fields in a document with those coming from a map.

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

Example: \|
\| [sample(documents)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinesample) \| \| ***(Public Preview)*** Performs a pseudo-random sampling of the documents from the previous stage.

This stage will filter documents pseudo-randomly. The parameter specifies how number of documents to be returned.

Examples: \|
\| [sample(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinesample) \| \| ***(Public Preview)*** Performs a pseudo-random sampling of the documents from the previous stage.

This stage will filter documents pseudo-randomly. The 'options' parameter specifies how sampling will be performed. See [SampleStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#samplestageoptions) for more information. \|
\| [select(selection, additionalSelections)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineselect) \| \| ***(Public Preview)*** Selects or creates a set of fields from the outputs of previous stages.

The selected fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions, which can be:

- `string` : Name of an existing field
- [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing field.
- [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas)

If no selections are provided, the output of this stage is empty. Use [Pipeline.addFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields) instead if only additions are desired.

Example: \|
\| [select(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineselect) \| \| ***(Public Preview)*** Selects or creates a set of fields from the outputs of previous stages.

The selected fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions, which can be:

- `string`: Name of an existing field
- [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing field.
- [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas)

If no selections are provided, the output of this stage is empty. Use [Pipeline.addFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields) instead if only additions are desired.

Example: \|
\| [sort(ordering, additionalOrderings)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinesort) \| \| ***(Public Preview)*** Sorts the documents from previous stages based on one or more [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) criteria.

This stage allows you to order the results of your pipeline. You can specify multiple [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) instances to sort by multiple fields in ascending or descending order. If documents have the same value for a field used for sorting, the next specified ordering will be used. If all orderings result in equal comparison, the documents are considered equal and the order is unspecified.

Example: \|
\| [sort(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinesort) \| \| ***(Public Preview)*** Sorts the documents from previous stages based on one or more [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) criteria.

This stage allows you to order the results of your pipeline. You can specify multiple [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) instances to sort by multiple fields in ascending or descending order. If documents have the same value for a field used for sorting, the next specified ordering will be used. If all orderings result in equal comparison, the documents are considered equal and the order is unspecified.

Example: \|
\| [union(other)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineunion) \| \| ***(Public Preview)*** Performs union of all documents from two pipelines, including duplicates.

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the `other` [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) given in parameter. The order of documents emitted from this stage is undefined.

Example: \|
\| [union(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineunion) \| \| ***(Public Preview)*** Performs union of all documents from two pipelines, including duplicates.

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the `other` [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) given in parameter. The order of documents emitted from this stage is undefined.

Example: \|
\| [unnest(selectable, indexField)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineunnest) \| \| ***(Public Preview)*** Produces a document for each element in an input array.For each previous stage document, this stage will emit zero or more augmented documents. The input array specified by the `selectable` parameter, will emit an augmented document for each input array element. The input array element will augment the previous stage document by setting the `alias` field with the array element value.When `selectable` evaluates to a non-array value (ex: number, null, absent), then the stage becomes a no-op for the current input document, returning it as is with the `alias` field absent.No documents are emitted when `selectable` evaluates to an empty array.Example: \|
\| [unnest(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelineunnest) \| \| ***(Public Preview)*** Produces a document for each element in an input array.For each previous stage document, this stage will emit zero or more augmented documents. The input array specified by the `selectable` parameter, will emit an augmented document for each input array element. The input array element will augment the previous stage document by setting the `alias` field with the array element value.When `selectable` evaluates to a non-array value (ex: number, null, absent), then the stage becomes a no-op for the current input document, returning it as is with the `alias` field absent.No documents are emitted when `selectable` evaluates to an empty array.Example: \|
\| [where(condition)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinewhere) \| \| ***(Public Preview)*** Filters the documents from previous stages to only include those matching the specified [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class).

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL. You can filter documents based on their field values, using implementations of [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class), typically including but not limited to:

- field comparators: [Expression.equal()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionequal), [Expression.lessThan()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlessthan), [Expression.greaterThan()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiongreaterthan), etc.
- logical operators: , , , etc.
- advanced functions: [Expression.regexMatch()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexmatch), [Expression.arrayContains()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontains), etc.

Example: \|
\| [where(options)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipelinewhere) \| \| ***(Public Preview)*** Filters the documents from previous stages to only include those matching the specified [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class).

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL. You can filter documents based on their field values, using implementations of [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class), typically including but not limited to:

- field comparators: , (less than), [Expression.greaterThan()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiongreaterthan), etc.
- logical operators: , , , etc.
- advanced functions: [Expression.regexMatch()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexmatch), [Expression.arrayContains()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontains), etc.

Example: \|

## Pipeline.addFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Adds new fields to outputs from previous stages.

This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones (if there is name overlaps).

The added fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)s, which can be:

- [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class): Either a literal value (see [constant()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_0c00f91)) or a computed value with an assigned alias using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).

Example:

**Signature:**

    addFields(field: Selectable, ...additionalFields: Selectable[]): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| field | [Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface) | The first field to add to the documents, specified as a [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface). |
| additionalFields | [Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface)\[\] | Optional additional fields to add to the documents, specified as [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)s. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    firestore.pipeline().collection("books")
      .addFields(
        field("rating").as("bookRating"), // Rename 'rating' to 'bookRating'
        add(5, field("quantity")).as("totalCost")  // Calculate 'totalCost'
      );

## Pipeline.addFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Adds new fields to outputs from previous stages.

This stage allows you to compute values on-the-fly based on existing data from previous stages or constants. You can use this to create new fields or overwrite existing ones (if there is name overlaps).

The added fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)s, which can be:

- [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class): Either a literal value (see [constant()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_0c00f91)) or a computed value with an assigned alias using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).

Example:

**Signature:**

    addFields(options: AddFieldsStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [AddFieldsStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#addfieldsstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    firestore.pipeline().collection("books")
      .addFields(
        field("rating").as("bookRating"), // Rename 'rating' to 'bookRating'
        add(5, field("quantity")).as("totalCost")  // Calculate 'totalCost'
      );

## Pipeline.aggregate()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Performs aggregation operations on the documents from previous stages.

<br />

This stage allows you to calculate aggregate values over a set of documents. You define the aggregations to perform using [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class) expressions which are typically results of calling [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas) on [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) instances.

<br />

Example:

**Signature:**

    aggregate(accumulator: AliasedAggregate, ...additionalAccumulators: AliasedAggregate[]): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| accumulator | [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedaggregate.md#aliasedaggregate_class) | The first [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class), wrapping an [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) and providing a name for the accumulated results. |
| additionalAccumulators | [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.aliasedaggregate.md#aliasedaggregate_class)\[\] | Optional additional [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class), each wrapping an [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) and providing a name for the accumulated results. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    // Calculate the average rating and the total number of books
    firestore.pipeline().collection("books")
        .aggregate(
            field("rating").avg().as("averageRating"),
            countAll().as("totalBooks")
        );

## Pipeline.aggregate()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Performs optionally grouped aggregation operations on the documents from previous stages.

<br />

This stage allows you to calculate aggregate values over a set of documents, optionally grouped by one or more fields or functions. You can specify:

- \\\*\\\*Grouping Fields or Functions:\\\*\\\* One or more fields or functions to group the documents by. For each distinct combination of values in these fields, a separate group is created. If no grouping fields are provided, a single group containing all documents is used. Not specifying groups is the same as putting the entire inputs into one group.
- \\\*\\\*Accumulators:\\\*\\\* One or more accumulation operations to perform within each group. These are defined using \[AliasedAggregate\](./firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class) expressions, which are typically created by calling \[Expression.as()\](./firestore_pipelines.expression.md#expressionas) on \[AggregateFunction\](./firestore_pipelines.aggregatefunction.md#aggregatefunction_class) instances. Each aggregation calculates a value (e.g., sum, average, count) based on the documents within its group.

<br />

Example:

**Signature:**

    aggregate(options: AggregateStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [AggregateStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#aggregatestageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Calculate the average rating for each genre.
    firestore.pipeline().collection("books")
      .aggregate({
          accumulators: [avg(field("rating")).as("avg_rating")]
          groups: ["genre"]
          });

## Pipeline.distinct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns a set of distinct values from the inputs to this stage.

This stage runs through the results from previous stages to include only results with unique combinations of [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) values ([Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class), [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class), etc).

The parameters to this stage are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions or strings:

- `string`: Name of an existing field - [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).

Example:

**Signature:**

    distinct(group: string | Selectable, ...additionalGroups: Array<string | Selectable>): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| group | string \| [Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface) | The [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expression or field name to consider when determining distinct value combinations. |
| additionalGroups | Array\<string \| [Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface)\> | Optional additional [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions to consider when determining distinct value combinations or strings representing field names. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Get a list of unique author names in uppercase and genre combinations.
    firestore.pipeline().collection("books")
        .distinct(toUppercase(field("author")).as("authorName"), field("genre"), "publishedAt")
        .select("authorName");

## Pipeline.distinct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns a set of distinct values from the inputs to this stage.

This stage runs through the results from previous stages to include only results with unique combinations of [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) values ([Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class), [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class), etc).

The parameters to this stage are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions or strings:

- `string`: Name of an existing field - [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class): References an existing document field. - [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using [Expression.as()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas).

Example:

**Signature:**

    distinct(options: DistinctStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [DistinctStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#distinctstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Get a list of unique author names in uppercase and genre combinations.
    firestore.pipeline().collection("books")
        .distinct(toUppercase(field("author")).as("authorName"), field("genre"), "publishedAt")
        .select("authorName");

## Pipeline.findNearest()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Performs a vector proximity search on the documents from the previous stage, returning the K-nearest documents based on the specified query `vectorValue` and `distanceMeasure`. The returned documents will be sorted in order from nearest to furthest from the query `vectorValue`.

<br />

Example:

    // Find the 10 most similar books based on the book description.
    const bookDescription = "Lorem ipsum...";
    const queryVector: number[] = ...; // compute embedding of `bookDescription`

    firestore.pipeline().collection("books")
        .findNearest({
          field: 'embedding',
          vectorValue: queryVector,
          distanceMeasure: 'euclidean',
          limit: 10,                        // optional
          distanceField: 'computedDistance' // optional
        });

**Signature:**

    findNearest(options: FindNearestStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [FindNearestStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#findneareststageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

## Pipeline.limit()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Limits the maximum number of documents returned by previous stages to `limit`.

<br />

This stage is particularly useful when you want to retrieve a controlled subset of data from a potentially large result set. It's often used for:

- \\\*\\\*Pagination:\\\*\\\* In combination with to retrieve specific pages of results.
- \\\*\\\*Limiting Data Retrieval:\\\*\\\* To prevent excessive data transfer and improve performance, especially when dealing with large collections.

<br />

Example:

**Signature:**

    limit(limit: number): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| limit | number | The maximum number of documents to return. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    // Limit the results to the top 10 highest-rated books
    firestore.pipeline().collection('books')
        .sort(field('rating').descending())
        .limit(10);

## Pipeline.limit()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Limits the maximum number of documents returned by previous stages to `limit`.

<br />

This stage is particularly useful when you want to retrieve a controlled subset of data from a potentially large result set. It's often used for:

- \\\*\\\*Pagination:\\\*\\\* In combination with to retrieve specific pages of results.
- \\\*\\\*Limiting Data Retrieval:\\\*\\\* To prevent excessive data transfer and improve performance, especially when dealing with large collections.

<br />

Example:

**Signature:**

    limit(options: LimitStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [LimitStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#limitstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    // Limit the results to the top 10 highest-rated books
    firestore.pipeline().collection('books')
        .sort(field('rating').descending())
        .limit(10);

## Pipeline.offset()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Skips the first `offset` number of documents from the results of previous stages.

<br />

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with to control the size of each page.

<br />

Example:

**Signature:**

    offset(offset: number): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| offset | number | The number of documents to skip. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    // Retrieve the second page of 20 results
    firestore.pipeline().collection('books')
        .sort(field('published').descending())
        .offset(20)  // Skip the first 20 results
        .limit(20);   // Take the next 20 results

## Pipeline.offset()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Skips the first `offset` number of documents from the results of previous stages.

<br />

This stage is useful for implementing pagination in your pipelines, allowing you to retrieve results in chunks. It is typically used in conjunction with to control the size of each page.

<br />

Example:

**Signature:**

    offset(options: OffsetStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [OffsetStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#offsetstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    // Retrieve the second page of 20 results
    firestore.pipeline().collection('books')
        .sort(field('published').descending())
        .offset(20)  // Skip the first 20 results
        .limit(20);   // Take the next 20 results

## Pipeline.rawStage()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Adds a raw stage to the pipeline.

<br />

This method provides a flexible way to extend the pipeline's functionality by adding custom stages. Each raw stage is defined by a unique `name` and a set of `params` that control its behavior.

<br />

Example (Assuming there is no 'where' stage available in SDK):

**Signature:**

    rawStage(name: string, params: unknown[], options?: {
            [key: string]: Expression | unknown;
        }): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string | The unique name of the raw stage to add. |
| params | unknown\[\] | A list of parameters to configure the raw stage's behavior. |
| options | { \[key: string\]: [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) \| unknown; } | An object of key value pairs that specifies optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Assume we don't have a built-in 'where' stage
    firestore.pipeline().collection('books')
        .rawStage('where', [field('published').lt(1900)]) // Custom 'where' stage
        .select('title', 'author');

## Pipeline.removeFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Remove fields from outputs of previous stages.

Example:

**Signature:**

    removeFields(fieldValue: Field | string, ...additionalFields: Array<Field | string>): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldValue | [Field](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.field.md#field_class) \| string | The first field to remove. |
| additionalFields | Array\<[Field](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.field.md#field_class) \| string\> | Optional additional fields to remove. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    firestore.pipeline().collection('books')
      // removes field 'rating' and 'cost' from the previous stage outputs.
      .removeFields(
        field('rating'),
        'cost'
      );

## Pipeline.removeFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Remove fields from outputs of previous stages.

Example:

**Signature:**

    removeFields(options: RemoveFieldsStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [RemoveFieldsStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#removefieldsstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    firestore.pipeline().collection('books')
      // removes field 'rating' and 'cost' from the previous stage outputs.
      .removeFields(
        field('rating'),
        'cost'
      );

## Pipeline.replaceWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Fully overwrites all fields in a document with those coming from a nested map.

<br />

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

<br />

Example:

**Signature:**

    replaceWith(fieldName: string): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) field containing the nested map. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Input.
    // {
    //  'name': 'John Doe Jr.',
    //  'parents': {
    //    'father': 'John Doe Sr.',
    //    'mother': 'Jane Doe'
    //   }
    // }

    // Emit parents as document.
    firestore.pipeline().collection('people').replaceWith('parents');

    // Output
    // {
    //  'father': 'John Doe Sr.',
    //  'mother': 'Jane Doe'
    // }

## Pipeline.replaceWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Fully overwrites all fields in a document with those coming from a map.

<br />

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

<br />

Example:

**Signature:**

    replaceWith(expr: Expression): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.expression.md#expression_class) | An [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) that when returned evaluates to a map. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Input.
    // {
    //  'name': 'John Doe Jr.',
    //  'parents': {
    //    'father': 'John Doe Sr.',
    //    'mother': 'Jane Doe'
    //   }
    // }

    // Emit parents as document.
    firestore.pipeline().collection('people').replaceWith(map({
      foo: 'bar',
      info: {
        name: field('name')
      }
    }));

    // Output
    // {
    //  'father': 'John Doe Sr.',
    //  'mother': 'Jane Doe'
    // }

## Pipeline.replaceWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Fully overwrites all fields in a document with those coming from a map.

<br />

This stage allows you to emit a map value as a document. Each key of the map becomes a field on the document that contains the corresponding value.

<br />

Example:

**Signature:**

    replaceWith(options: ReplaceWithStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [ReplaceWithStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#replacewithstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Input.
    // {
    //  'name': 'John Doe Jr.',
    //  'parents': {
    //    'father': 'John Doe Sr.',
    //    'mother': 'Jane Doe'
    //   }
    // }

    // Emit parents as document.
    firestore.pipeline().collection('people').replaceWith(map({
      foo: 'bar',
      info: {
        name: field('name')
      }
    }));

    // Output
    // {
    //  'father': 'John Doe Sr.',
    //  'mother': 'Jane Doe'
    // }

## Pipeline.sample()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Performs a pseudo-random sampling of the documents from the previous stage.

<br />

This stage will filter documents pseudo-randomly. The parameter specifies how number of documents to be returned.

<br />

Examples:

**Signature:**

    sample(documents: number): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| documents | number | The number of documents to sample. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Sample 25 books, if available.
    firestore.pipeline().collection('books')
        .sample(25);

## Pipeline.sample()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Performs a pseudo-random sampling of the documents from the previous stage.

<br />

This stage will filter documents pseudo-randomly. The 'options' parameter specifies how sampling will be performed. See [SampleStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#samplestageoptions) for more information.

**Signature:**

    sample(options: SampleStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [SampleStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#samplestageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Sample 10 books, if available.
    firestore.pipeline().collection("books")
        .sample({ documents: 10 });

    // Sample 50% of books.
    firestore.pipeline().collection("books")
        .sample({ percentage: 0.5 });

## Pipeline.select()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Selects or creates a set of fields from the outputs of previous stages.

<br />

The selected fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions, which can be:

- \`string\` : Name of an existing field
- \[Field\](./firestore_pipelines.field.md#field_class): References an existing field.
- \[AliasedExpression\](./firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using \[Expression.as()\](./firestore_pipelines.expression.md#expressionas)

<br />

If no selections are provided, the output of this stage is empty. Use [Pipeline.addFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields) instead if only additions are desired.

<br />

Example:

**Signature:**

    select(selection: Selectable | string, ...additionalSelections: Array<Selectable | string>): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| selection | [Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface) \| string | The first field to include in the output documents, specified as [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expression or string value representing the field name. |
| additionalSelections | Array\<[Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface) \| string\> | Optional additional fields to include in the output documents, specified as [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions or `string` values representing field names. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    db.pipeline().collection("books")
      .select(
        "firstName",
        field("lastName"),
        field("address").toUppercase().as("upperAddress"),
      );

## Pipeline.select()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Selects or creates a set of fields from the outputs of previous stages.

<br />

The selected fields are defined using [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) expressions, which can be:

- \`string\`: Name of an existing field
- \[Field\](./firestore_pipelines.field.md#field_class): References an existing field.
- \[AliasedExpression\](./firestore_pipelines.aliasedexpression.md#aliasedexpression_class): Represents the result of a function with an assigned alias name using \[Expression.as()\](./firestore_pipelines.expression.md#expressionas)

<br />

If no selections are provided, the output of this stage is empty. Use [Pipeline.addFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields) instead if only additions are desired.

<br />

Example:

**Signature:**

    select(options: SelectStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [SelectStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#selectstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    db.pipeline().collection("books")
      .select(
        "firstName",
        field("lastName"),
        field("address").toUppercase().as("upperAddress"),
      );

## Pipeline.sort()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Sorts the documents from previous stages based on one or more [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) criteria.

<br />

This stage allows you to order the results of your pipeline. You can specify multiple [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) instances to sort by multiple fields in ascending or descending order. If documents have the same value for a field used for sorting, the next specified ordering will be used. If all orderings result in equal comparison, the documents are considered equal and the order is unspecified.

<br />

Example:

**Signature:**

    sort(ordering: Ordering, ...additionalOrderings: Ordering[]): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ordering | [Ordering](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.ordering.md#ordering_class) | The first [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) instance specifying the sorting criteria. |
| additionalOrderings | [Ordering](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.ordering.md#ordering_class)\[\] | Optional additional [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) instances specifying the additional sorting criteria. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Sort books by rating in descending order, and then by title in ascending order for books
    // with the same rating
    firestore.pipeline().collection("books")
        .sort(
            Ordering.of(field("rating")).descending(),
            Ordering.of(field("title"))  // Ascending order is the default
        );

## Pipeline.sort()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Sorts the documents from previous stages based on one or more [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) criteria.

<br />

This stage allows you to order the results of your pipeline. You can specify multiple [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) instances to sort by multiple fields in ascending or descending order. If documents have the same value for a field used for sorting, the next specified ordering will be used. If all orderings result in equal comparison, the documents are considered equal and the order is unspecified.

<br />

Example:

**Signature:**

    sort(options: SortStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [SortStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#sortstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Sort books by rating in descending order, and then by title in ascending order for books
    // with the same rating
    firestore.pipeline().collection("books")
        .sort(
            Ordering.of(field("rating")).descending(),
            Ordering.of(field("title"))  // Ascending order is the default
        );

## Pipeline.union()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Performs union of all documents from two pipelines, including duplicates.

<br />

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the `other` [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) given in parameter. The order of documents emitted from this stage is undefined.

<br />

Example:

**Signature:**

    union(other: Pipeline): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| other | [Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class) | The other [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) that is part of union. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Emit documents from books collection and magazines collection.
    firestore.pipeline().collection('books')
        .union(firestore.pipeline().collection('magazines'));

## Pipeline.union()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Performs union of all documents from two pipelines, including duplicates.

<br />

This stage will pass through documents from previous stage, and also pass through documents from previous stage of the `other` [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) given in parameter. The order of documents emitted from this stage is undefined.

<br />

Example:

**Signature:**

    union(options: UnionStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [UnionStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#unionstageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Emit documents from books collection and magazines collection.
    firestore.pipeline().collection('books')
        .union(firestore.pipeline().collection('magazines'));

## Pipeline.unnest()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Produces a document for each element in an input array.

For each previous stage document, this stage will emit zero or more augmented documents. The input array specified by the `selectable` parameter, will emit an augmented document for each input array element. The input array element will augment the previous stage document by setting the `alias` field with the array element value.

When `selectable` evaluates to a non-array value (ex: number, null, absent), then the stage becomes a no-op for the current input document, returning it as is with the `alias` field absent.

No documents are emitted when `selectable` evaluates to an empty array.

Example:

**Signature:**

    unnest(selectable: Selectable, indexField?: string): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| selectable | [Selectable](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.selectable.md#selectable_interface) | A selectable expression defining the field to unnest and the alias to use for each un-nested element in the output documents. |
| indexField | string | An optional string value specifying the field path to write the offset (starting at zero) into the array the un-nested element is from |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Input:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tags": [ "comedy", "space", "adventure" ], ... }

    // Emit a book document for each tag of the book.
    firestore.pipeline().collection("books")
        .unnest(field("tags").as('tag'), 'tagIndex');

    // Output:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "comedy", "tagIndex": 0, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "space", "tagIndex": 1, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "adventure", "tagIndex": 2, ... }

## Pipeline.unnest()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Produces a document for each element in an input array.

For each previous stage document, this stage will emit zero or more augmented documents. The input array specified by the `selectable` parameter, will emit an augmented document for each input array element. The input array element will augment the previous stage document by setting the `alias` field with the array element value.

When `selectable` evaluates to a non-array value (ex: number, null, absent), then the stage becomes a no-op for the current input document, returning it as is with the `alias` field absent.

No documents are emitted when `selectable` evaluates to an empty array.

Example:

**Signature:**

    unnest(options: UnnestStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [UnnestStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#unneststageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) object with this stage appended to the stage list.

### Example

    // Input:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tags": [ "comedy", "space", "adventure" ], ... }

    // Emit a book document for each tag of the book.
    firestore.pipeline().collection("books")
        .unnest(field("tags").as('tag'), 'tagIndex');

    // Output:
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "comedy", "tagIndex": 0, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "space", "tagIndex": 1, ... }
    // { "title": "The Hitchhiker's Guide to the Galaxy", "tag": "adventure", "tagIndex": 2, ... }

## Pipeline.where()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Filters the documents from previous stages to only include those matching the specified [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class).

<br />

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL. You can filter documents based on their field values, using implementations of [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class), typically including but not limited to:

- field comparators: \[Expression.equal()\](./firestore_pipelines.expression.md#expressionequal), \[Expression.lessThan()\](./firestore_pipelines.expression.md#expressionlessthan), \[Expression.greaterThan()\](./firestore_pipelines.expression.md#expressiongreaterthan), etc.
- logical operators: , , , etc.
- advanced functions: \[Expression.regexMatch()\](./firestore_pipelines.expression.md#expressionregexmatch), \[Expression.arrayContains()\](./firestore_pipelines.expression.md#expressionarraycontains), etc.

<br />

Example:

**Signature:**

    where(condition: BooleanExpression): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| condition | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.booleanexpression.md#booleanexpression_class) | The [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) to apply. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    firestore.pipeline().collection("books")
      .where(
        and(
            gt(field("rating"), 4.0),   // Filter for ratings greater than 4.0
            field("genre").eq("Science Fiction") // Equivalent to gt("genre", "Science Fiction")
        )
      );

## Pipeline.where()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Filters the documents from previous stages to only include those matching the specified [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class).

<br />

This stage allows you to apply conditions to the data, similar to a "WHERE" clause in SQL. You can filter documents based on their field values, using implementations of [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class), typically including but not limited to:

- field comparators: , (less than), \[Expression.greaterThan()\](./firestore_pipelines.expression.md#expressiongreaterthan), etc.
- logical operators: , , , etc.
- advanced functions: \[Expression.regexMatch()\](./firestore_pipelines.expression.md#expressionregexmatch), \[Expression.arrayContains()\](./firestore_pipelines.expression.md#expressionarraycontains), etc.

<br />

Example:

**Signature:**

    where(options: WhereStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [WhereStageOptions](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.md#wherestageoptions) | An object that specifies required and optional parameters for the stage. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class)

A new Pipeline object with this stage appended to the stage list.

### Example

    firestore.pipeline().collection("books")
      .where(
        and(
            gt(field("rating"), 4.0),   // Filter for ratings greater than 4.0
            field("genre").eq("Science Fiction") // Equivalent to gt("genre", "Science Fiction")
        )
      );

### Example

    const db: Firestore; // Assumes a valid firestore instance.

    // Example 1: Select specific fields and rename 'rating' to 'bookRating'
    const results1 = await execute(db.pipeline()
        .collection("books")
        .select("title", "author", field("rating").as("bookRating")));

    // Example 2: Filter documents where 'genre' is "Science Fiction" and 'published' is after 1950
    const results2 = await execute(db.pipeline()
        .collection("books")
        .where(and(field("genre").eq("Science Fiction"), field("published").gt(1950))));

    // Example 3: Calculate the average rating of books published after 1980
    const results3 = await execute(db.pipeline()
        .collection("books")
        .where(field("published").gt(1980))
        .aggregate(avg(field("rating")).as("averageRating")));