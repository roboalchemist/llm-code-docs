# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.tflitemodel.md.txt

# TFLiteModel interface

A TensorFlow Lite Model output object

**Signature:**  

    export interface TFLiteModel 

## Properties

|                                                                   Property                                                                   |  Type  |                            Description                            |
|----------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------|
| [gcsTfliteUri](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.tflitemodel.md#tflitemodelgcstfliteuri) | string | The URI from which the model was originally provided to Firebase. |
| [sizeBytes](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning.tflitemodel.md#tflitemodelsizebytes)       | number | The size of the model.                                            |

## TFLiteModel.gcsTfliteUri

The URI from which the model was originally provided to Firebase.

**Signature:**  

    readonly gcsTfliteUri?: string;

## TFLiteModel.sizeBytes

The size of the model.

**Signature:**  

    readonly sizeBytes: number;