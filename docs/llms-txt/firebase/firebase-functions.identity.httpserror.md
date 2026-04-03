# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.httpserror.md.txt

# identity.HttpsError class

An explicit error that can be thrown from a handler to send an error to the client that called the function.

**Signature:**  

    export declare class HttpsError extends Error 

**Extends:** Error

## Constructors

|                                                                                    Constructor                                                                                     | Modifiers |                     Description                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------|
| [(constructor)(code, message, details)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.httpserror.md#identityhttpserrorconstructor) |           | Constructs a new instance of the `HttpsError` class |

## Properties

|                                                                           Property                                                                           | Modifiers |                                                                    Type                                                                     |                                                                   Description                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [code](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.httpserror.md#identityhttpserrorcode)                   |           | [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsfunctionserrorcode) | A standard error code that will be returned to the client. This also determines the HTTP status code of the response, as defined in code.proto. |
| [details](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.httpserror.md#identityhttpserrordetails)             |           | unknown                                                                                                                                     | Extra data to be converted to JSON and included in the error response.                                                                          |
| [httpErrorCode](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.httpserror.md#identityhttpserrorhttperrorcode) |           | HttpErrorCode                                                                                                                               | A wire format representation of a provided error code.                                                                                          |

## Methods

|                                                                      Method                                                                      | Modifiers |                        Description                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.httpserror.md#identityhttpserrortojson) |           | Returns a JSON-serializable representation of this object. |

## identity.HttpsError.(constructor)

Constructs a new instance of the `HttpsError` class

**Signature:**  

    constructor(code: FunctionsErrorCode, message: string, details?: unknown);

### Parameters

| Parameter |                                                                    Type                                                                     | Description |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| code      | [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsfunctionserrorcode) |             |
| message   | string                                                                                                                                      |             |
| details   | unknown                                                                                                                                     |             |

## identity.HttpsError.code

A standard error code that will be returned to the client. This also determines the HTTP status code of the response, as defined in code.proto.

**Signature:**  

    readonly code: FunctionsErrorCode;

## identity.HttpsError.details

Extra data to be converted to JSON and included in the error response.

**Signature:**  

    readonly details: unknown;

## identity.HttpsError.httpErrorCode

A wire format representation of a provided error code.

**Signature:**  

    readonly httpErrorCode: HttpErrorCode;

## identity.HttpsError.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): HttpErrorWireFormat;

**Returns:**

HttpErrorWireFormat