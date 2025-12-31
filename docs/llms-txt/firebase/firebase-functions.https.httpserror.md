# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.https.httpserror.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpserror.md.txt

# https.HttpsError class

An explicit error that can be thrown from a handler to send an error to the client that called the function.

**Signature:**  

    export declare class HttpsError extends Error 

**Extends:** Error

## Constructors

|                                                                                 Constructor                                                                                  | Modifiers |                     Description                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------|
| [(constructor)(code, message, details)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpserror.md#httpshttpserrorconstructor) |           | Constructs a new instance of the `HttpsError` class |

## Properties

|                                                                        Property                                                                        | Modifiers |                                                                    Type                                                                     |                                                                   Description                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [code](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpserror.md#httpshttpserrorcode)                   |           | [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsfunctionserrorcode) | A standard error code that will be returned to the client. This also determines the HTTP status code of the response, as defined in code.proto. |
| [details](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpserror.md#httpshttpserrordetails)             |           | unknown                                                                                                                                     | Extra data to be converted to JSON and included in the error response.                                                                          |
| [httpErrorCode](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpserror.md#httpshttpserrorhttperrorcode) |           | HttpErrorCode                                                                                                                               | A wire format representation of a provided error code.                                                                                          |

## Methods

|                                                                   Method                                                                   | Modifiers |                        Description                         |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpserror.md#httpshttpserrortojson) |           | Returns a JSON-serializable representation of this object. |

## https.HttpsError.(constructor)

Constructs a new instance of the `HttpsError` class

**Signature:**  

    constructor(code: FunctionsErrorCode, message: string, details?: unknown);

### Parameters

| Parameter |                                                                    Type                                                                     | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| code      | [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsfunctionserrorcode) |             |
| message   | string                                                                                                                                      |             |
| details   | unknown                                                                                                                                     |             |

## https.HttpsError.code

A standard error code that will be returned to the client. This also determines the HTTP status code of the response, as defined in code.proto.

**Signature:**  

    readonly code: FunctionsErrorCode;

## https.HttpsError.details

Extra data to be converted to JSON and included in the error response.

**Signature:**  

    readonly details: unknown;

## https.HttpsError.httpErrorCode

A wire format representation of a provided error code.

**Signature:**  

    readonly httpErrorCode: HttpErrorCode;

## https.HttpsError.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): HttpErrorWireFormat;

**Returns:**

HttpErrorWireFormat