# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md.txt

# PipelineSource class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Provides the entry point for defining the data source of a Firestore [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class).

Use the methods of this class (e.g., [PipelineSource.collection()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollection), [PipelineSource.collectionGroup()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollectiongroup), [PipelineSource.database()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedatabase), or [PipelineSource.documents()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedocuments)) to specify the initial data for your pipeline, such as a collection, a collection group, the entire database, or a set of specific documents.

**Signature:**

    export declare class PipelineSource<PipelineType> 

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [collection(collection)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollection) |   | ***(Public Preview)*** Returns all documents from the entire collection. The collection can be nested. |
| [collection(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollection) |   | ***(Public Preview)*** Returns all documents from the entire collection. The collection can be nested. |
| [collectionGroup(collectionId)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollectiongroup) |   | ***(Public Preview)*** Returns all documents from a collection ID regardless of the parent. |
| [collectionGroup(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollectiongroup) |   | ***(Public Preview)*** Returns all documents from a collection ID regardless of the parent. |
| [createFrom(query)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecreatefrom) |   | ***(Public Preview)*** Convert the given Query into an equivalent Pipeline. |
| [database()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedatabase) |   | ***(Public Preview)*** Returns all documents from the entire database. |
| [database(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedatabase) |   | ***(Public Preview)*** Returns all documents from the entire database. |
| [documents(docs)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedocuments) |   | ***(Public Preview)*** Set the pipeline's source to the documents specified by the given paths and DocumentReferences. |
| [documents(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedocuments) |   | ***(Public Preview)*** Set the pipeline's source to the documents specified by the given paths and DocumentReferences. |

## PipelineSource.collection()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns all documents from the entire collection. The collection can be nested.

**Signature:**

    collection(collection: string | Query): PipelineType;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| collection | string \| [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) | Name or reference to the collection that will be used as the Pipeline source. |

**Returns:**

PipelineType

## PipelineSource.collection()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns all documents from the entire collection. The collection can be nested.

**Signature:**

    collection(options: CollectionStageOptions): PipelineType;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [CollectionStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#collectionstageoptions) | Options defining how this CollectionStage is evaluated. |

**Returns:**

PipelineType

## PipelineSource.collectionGroup()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns all documents from a collection ID regardless of the parent.

**Signature:**

    collectionGroup(collectionId: string): PipelineType;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| collectionId | string | ID of the collection group to use as the Pipeline source. |

**Returns:**

PipelineType

## PipelineSource.collectionGroup()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns all documents from a collection ID regardless of the parent.

**Signature:**

    collectionGroup(options: CollectionGroupStageOptions): PipelineType;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [CollectionGroupStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#collectiongroupstageoptions) | Options defining how this CollectionGroupStage is evaluated. |

**Returns:**

PipelineType

## PipelineSource.createFrom()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Convert the given Query into an equivalent Pipeline.

**Signature:**

    createFrom(query: Query): Pipeline;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| query | [Query](https://firebase.google.com/docs/reference/js/firestore_.query.md#query_class) | A Query to be converted into a Pipeline. |

**Returns:**

[Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class)

#### Exceptions

`FirestoreError` Thrown if any of the provided DocumentReferences target a different project or database than the pipeline.

## PipelineSource.database()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns all documents from the entire database.

**Signature:**

    database(): PipelineType;

**Returns:**

PipelineType

## PipelineSource.database()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Returns all documents from the entire database.

**Signature:**

    database(options: DatabaseStageOptions): PipelineType;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [DatabaseStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#databasestageoptions) | Options defining how a DatabaseStage is evaluated. |

**Returns:**

PipelineType

## PipelineSource.documents()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Set the pipeline's source to the documents specified by the given paths and DocumentReferences.

**Signature:**

    documents(docs: Array<string | DocumentReference>): PipelineType;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| docs | Array\<string \| [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class)\> | An array of paths and DocumentReferences specifying the individual documents that will be the source of this pipeline. The converters for these DocumentReferences will be ignored and not have an effect on this pipeline. |

**Returns:**

PipelineType

#### Exceptions

`FirestoreError` Thrown if any of the provided DocumentReferences target a different project or database than the pipeline.

## PipelineSource.documents()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Set the pipeline's source to the documents specified by the given paths and DocumentReferences.

**Signature:**

    documents(options: DocumentsStageOptions): PipelineType;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [DocumentsStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#documentsstageoptions) | Options defining how this DocumentsStage is evaluated. |

**Returns:**

PipelineType

#### Exceptions

`FirestoreError` Thrown if any of the provided DocumentReferences target a different project or database than the pipeline.