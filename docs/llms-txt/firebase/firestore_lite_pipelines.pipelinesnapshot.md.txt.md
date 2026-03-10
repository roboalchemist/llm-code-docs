# Source: https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipelinesnapshot.md.txt

# PipelineSnapshot class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Represents the results of a Firestore pipeline execution.

A `PipelineSnapshot` contains zero or more [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) objects representing the documents returned by a pipeline query. It provides methods to iterate over the documents and access metadata about the query results.

**Signature:**

    export declare class PipelineSnapshot 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(pipeline, results, executionTime)](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipelinesnapshot.md#pipelinesnapshotconstructor) |   | ***(Public Preview)*** Constructs a new instance of the `PipelineSnapshot` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [executionTime](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipelinesnapshot.md#pipelinesnapshotexecutiontime) |   | [Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class) | ***(Public Preview)*** The time at which the pipeline producing this result is executed. |
| [results](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipelinesnapshot.md#pipelinesnapshotresults) |   | [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipelineresult.md#pipelineresult_class)\[\] | ***(Public Preview)*** An array of all the results in the `PipelineSnapshot`. |

## PipelineSnapshot.(constructor)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Constructs a new instance of the `PipelineSnapshot` class

**Signature:**

    constructor(pipeline: Pipeline, results: PipelineResult[], executionTime?: Timestamp);

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pipeline | [Pipeline](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipeline.md#pipeline_class) |   |
| results | [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_lite_pipelines.pipelineresult.md#pipelineresult_class)\[\] |   |
| executionTime | [Timestamp](https://firebase.google.com/docs/reference/js/firestore_lite.timestamp.md#timestamp_class) |   |

## PipelineSnapshot.executionTime

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The time at which the pipeline producing this result is executed.

**Signature:**

    get executionTime(): Timestamp;

## PipelineSnapshot.results

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An array of all the results in the `PipelineSnapshot`.

**Signature:**

    get results(): PipelineResult[];

### Example

    const snapshot: PipelineSnapshot = await firestore
      .pipeline()
      .collection('myCollection')
      .where(field('value').greaterThan(10))
      .execute();

    snapshot.results.forEach(doc => {
      console.log(doc.id, '=>', doc.data());
    });