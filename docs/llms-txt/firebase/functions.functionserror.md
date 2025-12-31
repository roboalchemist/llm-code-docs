# Source: https://firebase.google.com/docs/reference/js/functions.functionserror.md.txt

# FunctionsError class

An error returned by the Firebase Functions client SDK.

See [FunctionsErrorCode](https://firebase.google.com/docs/reference/js/functions.md#functionserrorcode) for full documentation of codes.

**Signature:**  

    export declare class FunctionsError extends FirebaseError 

**Extends:** [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class)

## Constructors

|                                                                 Constructor                                                                  | Modifiers |                       Description                        |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------|
| [(constructor)(code, message, details)](https://firebase.google.com/docs/reference/js/functions.functionserror.md#functionserrorconstructor) |           | Constructs a new instance of the `FunctionsError` class. |

## Properties

|                                                  Property                                                  | Modifiers |  Type   |                                  Description                                   |
|------------------------------------------------------------------------------------------------------------|-----------|---------|--------------------------------------------------------------------------------|
| [details](https://firebase.google.com/docs/reference/js/functions.functionserror.md#functionserrordetails) |           | unknown | Additional details to be converted to JSON and included in the error response. |

## FunctionsError.(constructor)

Constructs a new instance of the `FunctionsError` class.

**Signature:**  

    constructor(
        code: FunctionsErrorCode, message?: string, 
        details?: unknown);

#### Parameters

| Parameter |                                                  Type                                                   | Description |
|-----------|---------------------------------------------------------------------------------------------------------|-------------|
| code      | [FunctionsErrorCode](https://firebase.google.com/docs/reference/js/functions.md#functionserrorcodecore) |             |
| message   | string                                                                                                  |             |
| details   | unknown                                                                                                 |             |

## FunctionsError.details

Additional details to be converted to JSON and included in the error response.

**Signature:**  

    readonly details?: unknown;