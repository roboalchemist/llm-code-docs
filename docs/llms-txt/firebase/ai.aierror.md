# Source: https://firebase.google.com/docs/reference/js/ai.aierror.md.txt

# AIError class

Error class for the Firebase AI SDK.

**Signature:**  

    export declare class AIError extends FirebaseError 

**Extends:** [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class)

## Constructors

|                                                           Constructor                                                           | Modifiers |                    Description                    |
|---------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------|
| [(constructor)(code, message, customErrorData)](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierrorconstructor) |           | Constructs a new instance of the `AIError` class. |

## Properties

|                                               Property                                                | Modifiers |                                                             Type                                                              | Description |
|-------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------|-------------|
| [code](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierrorcode)                       |           | [AIErrorCode](https://firebase.google.com/docs/reference/js/ai.md#aierrorcode)                                                |             |
| [customErrorData](https://firebase.google.com/docs/reference/js/ai.aierror.md#aierrorcustomerrordata) |           | [CustomErrorData](https://firebase.google.com/docs/reference/js/ai.customerrordata.md#customerrordata_interface) \| undefined |             |

## AIError.(constructor)

Constructs a new instance of the `AIError` class.

**Signature:**  

    constructor(code: AIErrorCode, message: string, customErrorData?: CustomErrorData | undefined);

#### Parameters

|    Parameter    |                                                             Type                                                              |                                             Description                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| code            | [AIErrorCode](https://firebase.google.com/docs/reference/js/ai.md#aierrorcode)                                                | The error code from [AIErrorCode](https://firebase.google.com/docs/reference/js/ai.md#aierrorcode). |
| message         | string                                                                                                                        | A human-readable message describing the error.                                                      |
| customErrorData | [CustomErrorData](https://firebase.google.com/docs/reference/js/ai.customerrordata.md#customerrordata_interface) \| undefined | Optional error data.                                                                                |

## AIError.code

**Signature:**  

    readonly code: AIErrorCode;

## AIError.customErrorData

**Signature:**  

    readonly customErrorData?: CustomErrorData | undefined;