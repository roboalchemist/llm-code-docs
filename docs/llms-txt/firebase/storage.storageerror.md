# Source: https://firebase.google.com/docs/reference/js/storage.storageerror.md.txt

# StorageError class

An error returned by the Firebase Storage SDK.

**Signature:**  

    export declare class StorageError extends FirebaseError 

**Extends:** [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class)

## Constructors

|                                                              Constructor                                                               | Modifiers |                      Description                      |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------|
| [(constructor)(code, message, status_)](https://firebase.google.com/docs/reference/js/storage.storageerror.md#storageerrorconstructor) |           | Constructs a new instance of the `StorageError` class |

## Properties

|                                                      Property                                                      | Modifiers |                Type                 |                       Description                       |
|--------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------|---------------------------------------------------------|
| [customData](https://firebase.google.com/docs/reference/js/storage.storageerror.md#storageerrorcustomdata)         |           | { serverResponse: string \| null; } | Stores custom error data unique to the `StorageError`.  |
| [serverResponse](https://firebase.google.com/docs/reference/js/storage.storageerror.md#storageerrorserverresponse) |           | null \| string                      | Optional response message that was added by the server. |
| [status](https://firebase.google.com/docs/reference/js/storage.storageerror.md#storageerrorstatus)                 |           | number                              |                                                         |

## Methods

|                                                       Method                                                       | Modifiers |                                    Description                                     |
|--------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------|
| [_codeEquals(code)](https://firebase.google.com/docs/reference/js/storage.storageerror.md#storageerror_codeequals) |           | Compares a `StorageErrorCode` against this error's code, filtering out the prefix. |

## StorageError.(constructor)

Constructs a new instance of the `StorageError` class

**Signature:**  

    constructor(code: StorageErrorCode, message: string, status_?: number);

#### Parameters

| Parameter |                                             Type                                              |                                           Description                                           |
|-----------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| code      | [StorageErrorCode](https://firebase.google.com/docs/reference/js/storage.md#storageerrorcode) | A `StorageErrorCode` string to be prefixed with 'storage/' and added to the end of the message. |
| message   | string                                                                                        | Error message.                                                                                  |
| status_   | number                                                                                        | Corresponding HTTP Status Code                                                                  |

## StorageError.customData

Stores custom error data unique to the `StorageError`.

**Signature:**  

    customData: {
            serverResponse: string | null;
        };

## StorageError.serverResponse

Optional response message that was added by the server.

**Signature:**  

    get serverResponse(): null | string;

    set serverResponse(serverResponse: string | null);

## StorageError.status

**Signature:**  

    get status(): number;

    set status(status: number);

## StorageError._codeEquals()

Compares a `StorageErrorCode` against this error's code, filtering out the prefix.

**Signature:**  

    _codeEquals(code: StorageErrorCode): boolean;

#### Parameters

| Parameter |                                             Type                                              | Description |
|-----------|-----------------------------------------------------------------------------------------------|-------------|
| code      | [StorageErrorCode](https://firebase.google.com/docs/reference/js/storage.md#storageerrorcode) |             |

**Returns:**

boolean