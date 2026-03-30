# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md.txt

# PipelineResult class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A PipelineResult contains data read from a Firestore Pipeline. The data can be extracted with the [PipelineResult.data()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultdata) or [PipelineResult.get()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultget) methods.

<br />

If the PipelineResult represents a non-document result, `ref` will return a undefined value.

**Signature:**

    export declare class PipelineResult<AppModelType = DocumentData> 

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [createTime](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultcreatetime) |   | [Timestamp](https://firebase.google.com/docs/reference/js/firestore_.timestamp.md#timestamp_class) \| undefined | ***(Public Preview)*** The time the document was created. Undefined if this result is not a document. |
| [id](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultid) |   | string \| undefined | ***(Public Preview)*** The ID of the document for which this PipelineResult contains data, if it is a document; otherwise `undefined`. |
| [ref](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultref) |   | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class) \| undefined | ***(Public Preview)*** The reference of the document, if it is a document; otherwise `undefined`. |
| [updateTime](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultupdatetime) |   | [Timestamp](https://firebase.google.com/docs/reference/js/firestore_.timestamp.md#timestamp_class) \| undefined | ***(Public Preview)*** The time the document was last updated (at the time the snapshot was generated). Undefined if this result is not a document. |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [data()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultdata) |   | ***(Public Preview)*** Retrieves all fields in the result as an object. |
| [get(fieldPath)](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultget) |   | ***(Public Preview)*** Retrieves the field specified by `field`. |

## PipelineResult.createTime

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The time the document was created. Undefined if this result is not a document.

**Signature:**

    get createTime(): Timestamp | undefined;

## PipelineResult.id

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The ID of the document for which this PipelineResult contains data, if it is a document; otherwise `undefined`.

**Signature:**

    get id(): string | undefined;

## PipelineResult.ref

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The reference of the document, if it is a document; otherwise `undefined`.

**Signature:**

    get ref(): DocumentReference | undefined;

## PipelineResult.updateTime

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The time the document was last updated (at the time the snapshot was generated). Undefined if this result is not a document.

**Signature:**

    get updateTime(): Timestamp | undefined;

## PipelineResult.data()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Retrieves all fields in the result as an object.

**Signature:**

    data(): AppModelType;

**Returns:**

AppModelType

An object containing all fields in the document or 'undefined' if the document doesn't exist.

### Example

    let p = firestore.pipeline().collection('col');

    p.execute().then(results => {
      let data = results[0].data();
      console.log(`Retrieved data: ${JSON.stringify(data)}`);
    });

## PipelineResult.get()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Retrieves the field specified by `field`.

**Signature:**

    get(fieldPath: string | FieldPath | Field): any;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldPath | string \| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class) \| [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) |   |

**Returns:**

any

The data at the specified field location or `undefined` if no such field exists.

### Example

    let p = firestore.pipeline().collection('col');

    p.execute().then(results => {
      let field = results[0].get('a.b');
      console.log(`Retrieved field value: ${field}`);
    });