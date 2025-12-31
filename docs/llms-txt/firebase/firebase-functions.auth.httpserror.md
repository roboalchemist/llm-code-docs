# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.auth.httpserror.md.txt

# auth.HttpsError class

An explicit error that can be thrown from a handler to send an error to the client that called the function.

**Signature:**  

    export declare class HttpsError extends Error 

**Extends:** Error

## Constructors

|                                                                          Constructor                                                                          | Modifiers |                     Description                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------|
| [(constructor)(code, message, details)](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.httpserror.md#authhttpserrorconstructor) |           | Constructs a new instance of the `HttpsError` class |

## Properties

|                                                                Property                                                                 | Modifiers |                                                              Type                                                              |                                                                   Description                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [code](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.httpserror.md#authhttpserrorcode)                   |           | [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/firebase-functions.https.md#httpsfunctionserrorcode) | A standard error code that will be returned to the client. This also determines the HTTP status code of the response, as defined in code.proto. |
| [details](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.httpserror.md#authhttpserrordetails)             |           | unknown                                                                                                                        | Extra data to be converted to JSON and included in the error response.                                                                          |
| [httpErrorCode](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.httpserror.md#authhttpserrorhttperrorcode) |           | HttpErrorCode                                                                                                                  | A wire format representation of a provided error code.                                                                                          |

## Methods

|                                                           Method                                                            | Modifiers |                        Description                         |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.httpserror.md#authhttpserrortojson) |           | Returns a JSON-serializable representation of this object. |

## auth.HttpsError.(constructor)

Constructs a new instance of the `HttpsError` class

**Signature:**  

    constructor(code: FunctionsErrorCode, message: string, details?: unknown);

### Parameters

| Parameter |                                                              Type                                                              | Description |
|-----------|--------------------------------------------------------------------------------------------------------------------------------|-------------|
| code      | [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/firebase-functions.https.md#httpsfunctionserrorcode) |             |
| message   | string                                                                                                                         |             |
| details   | unknown                                                                                                                        |             |

## auth.HttpsError.code

A standard error code that will be returned to the client. This also determines the HTTP status code of the response, as defined in code.proto.

**Signature:**  

    readonly code: FunctionsErrorCode;

## auth.HttpsError.details

Extra data to be converted to JSON and included in the error response.

**Signature:**  

    readonly details: unknown;

## auth.HttpsError.httpErrorCode

A wire format representation of a provided error code.

**Signature:**  

    readonly httpErrorCode: HttpErrorCode;

## auth.HttpsError.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): HttpErrorWireFormat;

**Returns:**

HttpErrorWireFormat