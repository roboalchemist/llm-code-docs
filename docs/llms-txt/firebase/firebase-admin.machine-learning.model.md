# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md.txt

# Model class

A Firebase ML Model output object.

**Signature:**  

    export declare class Model 

## Properties

|                                                                Property                                                                | Modifiers |                                                                          Type                                                                          |                                                                                                                      Description                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [createTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelcreatetime)           |           | string                                                                                                                                                 | The timestamp of the model's creation.                                                                                                                                                                                                                |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modeldisplayname)         |           | string                                                                                                                                                 | The model's name. This is the name you use from your app to load the model.                                                                                                                                                                           |
| [etag](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modeletag)                       |           | string                                                                                                                                                 | The ETag identifier of the current version of the model. This value changes whenever you update any of the model's properties.                                                                                                                        |
| [locked](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modellocked)                   |           | boolean                                                                                                                                                | True if the model is locked by a server-side operation. You can't make changes to a locked model. See [Model.waitForUnlocked()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelwaitforunlocked). |
| [modelHash](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelmodelhash)             |           | string \| undefined                                                                                                                                    | The hash of the model's `tflite` file. This value changes only when you upload a new TensorFlow Lite model.                                                                                                                                           |
| [modelId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelmodelid)                 |           | string                                                                                                                                                 | The ID of the model.                                                                                                                                                                                                                                  |
| [published](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelpublished)             |           | boolean                                                                                                                                                | True if the model is published.                                                                                                                                                                                                                       |
| [tags](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modeltags)                       |           | string\[\]                                                                                                                                             | The model's tags, which can be used to group or filter models in list operations.                                                                                                                                                                     |
| [tfliteModel](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modeltflitemodel)         |           | [TFLiteModel](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.tflitemodel.md#tflitemodel_interface) \| undefined | Metadata about the model's TensorFlow Lite model file.                                                                                                                                                                                                |
| [updateTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelupdatetime)           |           | string                                                                                                                                                 | The timestamp of the model's most recent update.                                                                                                                                                                                                      |
| [validationError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelvalidationerror) |           | string \| undefined                                                                                                                                    | Error message when model validation fails.                                                                                                                                                                                                            |

## Methods

|                                                                        Method                                                                         | Modifiers |            Description             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modeltojson)                                |           | Return the model as a JSON object. |
| [waitForUnlocked(maxTimeMillis)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelwaitforunlocked) |           | Wait for the model to be unlocked. |

## Model.createTime

The timestamp of the model's creation.

**Signature:**  

    get createTime(): string;

## Model.displayName

The model's name. This is the name you use from your app to load the model.

**Signature:**  

    get displayName(): string;

## Model.etag

The ETag identifier of the current version of the model. This value changes whenever you update any of the model's properties.

**Signature:**  

    get etag(): string;

## Model.locked

True if the model is locked by a server-side operation. You can't make changes to a locked model. See [Model.waitForUnlocked()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.model.md#modelwaitforunlocked).

**Signature:**  

    get locked(): boolean;

## Model.modelHash

The hash of the model's `tflite` file. This value changes only when you upload a new TensorFlow Lite model.

**Signature:**  

    get modelHash(): string | undefined;

## Model.modelId

The ID of the model.

**Signature:**  

    get modelId(): string;

## Model.published

True if the model is published.

**Signature:**  

    get published(): boolean;

## Model.tags

The model's tags, which can be used to group or filter models in list operations.

**Signature:**  

    get tags(): string[];

## Model.tfliteModel

Metadata about the model's TensorFlow Lite model file.

**Signature:**  

    get tfliteModel(): TFLiteModel | undefined;

## Model.updateTime

The timestamp of the model's most recent update.

**Signature:**  

    get updateTime(): string;

## Model.validationError

Error message when model validation fails.

**Signature:**  

    get validationError(): string | undefined;

## Model.toJSON()

Return the model as a JSON object.

**Signature:**  

    toJSON(): {
            [key: string]: any;
        };

**Returns:**

{ \[key: string\]: any; }

## Model.waitForUnlocked()

Wait for the model to be unlocked.

**Signature:**  

    waitForUnlocked(maxTimeMillis?: number): Promise<void>;

### Parameters

|   Parameter   |  Type  |                                             Description                                             |
|---------------|--------|-----------------------------------------------------------------------------------------------------|
| maxTimeMillis | number | The maximum time in milliseconds to wait. If not specified, a default maximum of 2 minutes is used. |

**Returns:**

Promise\<void\>

A promise that resolves when the model is unlocked or the maximum wait time has passed.