# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md.txt

# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.https.md.txt

# https namespace

## Functions

|                                                       Function                                                        |                             Description                              |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [onCall(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.https.md#httpsoncall)       | Declares a callable method for clients to call using a Firebase SDK. |
| [onRequest(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.https.md#httpsonrequest) | Handle HTTP requests.                                                |

## Classes

|                                                              Class                                                              |                                                 Description                                                  |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [HttpsError](https://firebase.google.com/docs/reference/functions/firebase-functions.https.httpserror.md#httpshttpserror_class) | An explicit error that can be thrown from a handler to send an error to the client that called the function. |

## Interfaces

|                                                                     Interface                                                                      |                                 Description                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [CallableContext](https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md#httpscallablecontext_interface) | The interface for metadata for the API as passed to the handler.            |
| [Request](https://firebase.google.com/docs/reference/functions/firebase-functions.https.request.md#httpsrequest_interface)                         | An express request with the wire format representation of the request body. |

## Type Aliases

|                                                           Type Alias                                                           |                                                                          Description                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/firebase-functions.https.md#httpsfunctionserrorcode) | The set of Firebase Functions status codes. The codes are the same at the ones exposed by [gRPC](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md). |

## https.onCall()

Declares a callable method for clients to call using a Firebase SDK.

**Signature:**  

    export declare function onCall(handler: (data: any, context: CallableContext) => any | Promise<any>): HttpsFunction & Runnable<any>;

### Parameters

| Parameter |                                                                                                Type                                                                                                |                         Description                         |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| handler   | (data: any, context: [CallableContext](https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md#httpscallablecontext_interface)) =\> any \| Promise\<any\> | A method that takes a data and context and returns a value. |

**Returns:**

[HttpsFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction_interface) \& [Runnable](https://firebase.google.com/docs/reference/functions/firebase-functions.runnable.md#runnable_interface)\<any\>

## https.onRequest()

Handle HTTP requests.

**Signature:**  

    export declare function onRequest(handler: (req: Request, resp: express.Response) => void | Promise<void>): HttpsFunction;

### Parameters

| Parameter |                                Type                                |                                      Description                                       |
|-----------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| handler   | (req: Request, resp: express.Response) =\> void \| Promise\<void\> | A function that takes a request and response object, same signature as an Express app. |

**Returns:**

[HttpsFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.httpsfunction.md#httpsfunction_interface)

## https.FunctionsErrorCode

The set of Firebase Functions status codes. The codes are the same at the ones exposed by [gRPC](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md).

Possible values:

- `cancelled`: The operation was cancelled (typically by the caller).

- `unknown`: Unknown error or an error from a different error domain.

- `invalid-argument`: Client specified an invalid argument. Note that this differs from `failed-precondition`. `invalid-argument` indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name).

- `deadline-exceeded`: Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.

- `not-found`: Some requested document was not found.

- `already-exists`: Some document that we attempted to create already exists.

- `permission-denied`: The caller does not have permission to execute the specified operation.

- `resource-exhausted`: Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.

- `failed-precondition`: Operation was rejected because the system is not in a state required for the operation's execution.

- `aborted`: The operation was aborted, typically due to a concurrency issue like transaction aborts, etc.

- `out-of-range`: Operation was attempted past the valid range.

- `unimplemented`: Operation is not implemented or not supported/enabled.

- `internal`: Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken.

- `unavailable`: The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff.

- `data-loss`: Unrecoverable data loss or corruption.

- `unauthenticated`: The request does not have valid authentication credentials for the operation.

**Signature:**  

    export type FunctionsErrorCode = "ok" | "cancelled" | "unknown" | "invalid-argument" | "deadline-exceeded" | "not-found" | "already-exists" | "permission-denied" | "resource-exhausted" | "failed-precondition" | "aborted" | "out-of-range" | "unimplemented" | "internal" | "unavailable" | "data-loss" | "unauthenticated";