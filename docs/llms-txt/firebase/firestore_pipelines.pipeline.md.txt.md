# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md.txt

# Pipeline class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    export declare class Pipeline 

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [addFields(field, additionalFields)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields) |   | ***(Public Preview)*** |
| [addFields(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields) |   | ***(Public Preview)*** |
| [aggregate(accumulator, additionalAccumulators)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaggregate) |   | ***(Public Preview)*** |
| [aggregate(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaggregate) |   | ***(Public Preview)*** |
| [distinct(group, additionalGroups)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinedistinct) |   | ***(Public Preview)*** |
| [distinct(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinedistinct) |   | ***(Public Preview)*** |
| [findNearest(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinefindnearest) |   | ***(Public Preview)*** |
| [limit(limit)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinelimit) |   | ***(Public Preview)*** |
| [limit(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinelimit) |   | ***(Public Preview)*** |
| [offset(offset)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineoffset) |   | ***(Public Preview)*** |
| [offset(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineoffset) |   | ***(Public Preview)*** |
| [rawStage(name, params, options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinerawstage) |   | ***(Public Preview)*** |
| [removeFields(fieldValue, additionalFields)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineremovefields) |   | ***(Public Preview)*** |
| [removeFields(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineremovefields) |   | ***(Public Preview)*** |
| [replaceWith(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinereplacewith) |   | ***(Public Preview)*** |
| [replaceWith(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinereplacewith) |   | ***(Public Preview)*** |
| [replaceWith(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinereplacewith) |   | ***(Public Preview)*** |
| [sample(documents)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesample) |   | ***(Public Preview)*** |
| [sample(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesample) |   | ***(Public Preview)*** |
| [select(selection, additionalSelections)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineselect) |   | ***(Public Preview)*** |
| [select(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineselect) |   | ***(Public Preview)*** |
| [sort(ordering, additionalOrderings)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesort) |   | ***(Public Preview)*** |
| [sort(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesort) |   | ***(Public Preview)*** |
| [union(other)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineunion) |   | ***(Public Preview)*** |
| [union(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineunion) |   | ***(Public Preview)*** |
| [unnest(selectable, indexField)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineunnest) |   | ***(Public Preview)*** |
| [unnest(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineunnest) |   | ***(Public Preview)*** |
| [where(condition)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinewhere) |   | ***(Public Preview)*** |
| [where(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinewhere) |   | ***(Public Preview)*** |

## Pipeline.addFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    addFields(field: Selectable, ...additionalFields: Selectable[]): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| field | [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) |   |
| additionalFields | [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)\[\] |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.addFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    addFields(options: AddFieldsStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [AddFieldsStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#addfieldsstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.aggregate()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    aggregate(accumulator: AliasedAggregate, ...additionalAccumulators: AliasedAggregate[]): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| accumulator | [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class) |   |
| additionalAccumulators | [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class)\[\] |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.aggregate()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    aggregate(options: AggregateStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [AggregateStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#aggregatestageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.distinct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    distinct(group: string | Selectable, ...additionalGroups: Array<string | Selectable>): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| group | string \| [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) |   |
| additionalGroups | Array\<string \| [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)\> |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.distinct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    distinct(options: DistinctStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [DistinctStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#distinctstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.findNearest()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    findNearest(options: FindNearestStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [FindNearestStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#findneareststageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.limit()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    limit(limit: number): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| limit | number |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.limit()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    limit(options: LimitStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [LimitStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#limitstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.offset()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    offset(offset: number): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| offset | number |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.offset()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    offset(options: OffsetStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [OffsetStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#offsetstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.rawStage()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    rawStage(name: string, params: unknown[], options?: { [key: string]: Expression | unknown; }): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string |   |
| params | unknown\[\] |   |
| options | { \[key: string\]: [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown; } |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.removeFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    removeFields(fieldValue: Field | string, ...additionalFields: Array<Field | string>): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldValue | [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) \| string |   |
| additionalFields | Array\<[Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) \| string\> |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.removeFields()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    removeFields(options: RemoveFieldsStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [RemoveFieldsStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#removefieldsstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.replaceWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    replaceWith(fieldName: string): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.replaceWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    replaceWith(expr: Expression): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.replaceWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    replaceWith(options: ReplaceWithStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [ReplaceWithStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#replacewithstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.sample()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    sample(documents: number): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| documents | number |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.sample()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    sample(options: SampleStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [SampleStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#samplestageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.select()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    select(selection: Selectable | string, ...additionalSelections: Array<Selectable | string>): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| selection | [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) \| string |   |
| additionalSelections | Array\<[Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) \| string\> |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.select()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    select(options: SelectStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [SelectStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#selectstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.sort()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    sort(ordering: Ordering, ...additionalOrderings: Ordering[]): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ordering | [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) |   |
| additionalOrderings | [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class)\[\] |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.sort()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    sort(options: SortStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [SortStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#sortstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.union()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    union(other: Pipeline): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| other | [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.union()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    union(options: UnionStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [UnionStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unionstageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.unnest()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    unnest(selectable: Selectable, indexField?: string): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| selectable | [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) |   |
| indexField | string |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.unnest()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    unnest(options: UnnestStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [UnnestStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unneststageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.where()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    where(condition: BooleanExpression): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| condition | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

## Pipeline.where()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    where(options: WhereStageOptions): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [WhereStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#wherestageoptions) |   |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)