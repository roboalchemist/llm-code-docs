# Source: https://firebase.google.com/docs/reference/js/vertexai.vertexaierror.md.txt

# VertexAIError class

Error class for the Vertex AI in Firebase SDK.

**Signature:**  

    export declare class VertexAIError extends FirebaseError 

**Extends:** [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class)

## Constructors

|                                                                    Constructor                                                                    | Modifiers |                       Description                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------|
| [(constructor)(code, message, customErrorData)](https://firebase.google.com/docs/reference/js/vertexai.vertexaierror.md#vertexaierrorconstructor) |           | Constructs a new instance of the `VertexAIError` class. |

## Properties

|                                                        Property                                                         | Modifiers |                                                                Type                                                                 | Description |
|-------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [code](https://firebase.google.com/docs/reference/js/vertexai.vertexaierror.md#vertexaierrorcode)                       |           | [VertexAIErrorCode](https://firebase.google.com/docs/reference/js/vertexai.md#vertexaierrorcode)                                    |             |
| [customErrorData](https://firebase.google.com/docs/reference/js/vertexai.vertexaierror.md#vertexaierrorcustomerrordata) |           | [CustomErrorData](https://firebase.google.com/docs/reference/js/vertexai.customerrordata.md#customerrordata_interface) \| undefined |             |

## VertexAIError.(constructor)

Constructs a new instance of the `VertexAIError` class.

**Signature:**  

    constructor(code: VertexAIErrorCode, message: string, customErrorData?: CustomErrorData | undefined);

#### Parameters

|    Parameter    |                                                                Type                                                                 |                                                      Description                                                      |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| code            | [VertexAIErrorCode](https://firebase.google.com/docs/reference/js/vertexai.md#vertexaierrorcode)                                    | The error code from [VertexAIErrorCode](https://firebase.google.com/docs/reference/js/vertexai.md#vertexaierrorcode). |
| message         | string                                                                                                                              | A human-readable message describing the error.                                                                        |
| customErrorData | [CustomErrorData](https://firebase.google.com/docs/reference/js/vertexai.customerrordata.md#customerrordata_interface) \| undefined | Optional error data.                                                                                                  |

## VertexAIError.code

**Signature:**  

    readonly code: VertexAIErrorCode;

## VertexAIError.customErrorData

**Signature:**  

    readonly customErrorData?: CustomErrorData | undefined;