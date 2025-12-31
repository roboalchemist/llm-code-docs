# Source: https://firebase.google.com/docs/reference/functions.md.txt

# Source: https://firebase.google.com/docs/functions.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/functions.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/functions.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/functions/functions.md.txt

# Source: https://firebase.google.com/docs/hosting/functions.md.txt

# Source: https://firebase.google.com/docs/extensions/publishers/functions.md.txt

# Source: https://firebase.google.com/docs/reference/js/functions.md.txt

# Source: https://firebase.google.com/docs/extensions/publishers/functions.md.txt

# Source: https://firebase.google.com/docs/reference/js/functions.md.txt

# functions package

Cloud Functions for Firebase

## Functions

|                                                                        Function                                                                        |                                                                       Description                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                                                 |                                                                                                                                                          |
| [getFunctions(app, regionOrCustomDomain)](https://firebase.google.com/docs/reference/js/functions.md#getfunctions_60f2095)                             | Returns a [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface) instance for the given app.              |
| **function(functionsInstance, ...)**                                                                                                                   |                                                                                                                                                          |
| [connectFunctionsEmulator(functionsInstance, host, port)](https://firebase.google.com/docs/reference/js/functions.md#connectfunctionsemulator_505c08d) | Modify this instance to communicate with the Cloud Functions emulator.Note: this must be called before this instance has been used to do any operations. |
| [httpsCallable(functionsInstance, name, options)](https://firebase.google.com/docs/reference/js/functions.md#httpscallable_1dd297c)                    | Returns a reference to the callable HTTPS trigger with the given name.                                                                                   |
| [httpsCallableFromURL(functionsInstance, url, options)](https://firebase.google.com/docs/reference/js/functions.md#httpscallablefromurl_7af6987)       | Returns a reference to the callable HTTPS trigger with the specified url.                                                                                |

## Classes

|                                                      Class                                                       |                                                                                           Description                                                                                           |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FunctionsError](https://firebase.google.com/docs/reference/js/functions.functionserror.md#functionserror_class) | An error returned by the Firebase Functions client SDK.See [FunctionsErrorCode](https://firebase.google.com/docs/reference/js/functions.md#functionserrorcode) for full documentation of codes. |

## Interfaces

|                                                                        Interface                                                                         |                                     Description                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface)                                                    | A `Functions` instance.                                                              |
| [HttpsCallable](https://firebase.google.com/docs/reference/js/functions.httpscallable.md#httpscallable_interface)                                        | A reference to a "callable" HTTP trigger in Cloud Functions.                         |
| [HttpsCallableOptions](https://firebase.google.com/docs/reference/js/functions.httpscallableoptions.md#httpscallableoptions_interface)                   | An interface for metadata about how calls should be executed.                        |
| [HttpsCallableResult](https://firebase.google.com/docs/reference/js/functions.httpscallableresult.md#httpscallableresult_interface)                      | An `HttpsCallableResult` wraps a single result from a function call.                 |
| [HttpsCallableStreamOptions](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamoptions.md#httpscallablestreamoptions_interface) | An interface for metadata about how a stream call should be executed.                |
| [HttpsCallableStreamResult](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamresult.md#httpscallablestreamresult_interface)    | An `HttpsCallableStreamResult` wraps a single streaming result from a function call. |

## Type Aliases

|                                                 Type Alias                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FunctionsErrorCode](https://firebase.google.com/docs/reference/js/functions.md#functionserrorcode)         | The set of Firebase Functions status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.mdPossible values: - 'cancelled': The operation was cancelled (typically by the caller). - 'unknown': Unknown error or an error from a different error domain. - 'invalid-argument': Client specified an invalid argument. Note that this differs from 'failed-precondition'. 'invalid-argument' indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name). - 'deadline-exceeded': Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. - 'not-found': Some requested document was not found. - 'already-exists': Some document that we attempted to create already exists. - 'permission-denied': The caller does not have permission to execute the specified operation. - 'resource-exhausted': Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. - 'failed-precondition': Operation was rejected because the system is not in a state required for the operation's execution. - 'aborted': The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. - 'out-of-range': Operation was attempted past the valid range. - 'unimplemented': Operation is not implemented or not supported/enabled. - 'internal': Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken. - 'unavailable': The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff. - 'data-loss': Unrecoverable data loss or corruption. - 'unauthenticated': The request does not have valid authentication credentials for the operation. |
| [FunctionsErrorCodeCore](https://firebase.google.com/docs/reference/js/functions.md#functionserrorcodecore) | Functions error code string appended after "functions/" product prefix. See [FunctionsErrorCode](https://firebase.google.com/docs/reference/js/functions.md#functionserrorcode) for full documentation of codes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## function(app, ...)

### getFunctions(app, regionOrCustomDomain)

Returns a [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface) instance for the given app.

**Signature:**  

    export declare function getFunctions(app?: FirebaseApp, regionOrCustomDomain?: string): Functions;

#### Parameters

|      Parameter       |                                                 Type                                                  |                                                                        Description                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app                  | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) to use.                                          |
| regionOrCustomDomain | string                                                                                                | one of: a) The region the callable functions are located in (ex: us-central1) b) A custom domain hosting the callable functions (ex: https://mydomain.com) |

**Returns:**

[Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface)

## function(functionsInstance, ...)

### connectFunctionsEmulator(functionsInstance, host, port)

Modify this instance to communicate with the Cloud Functions emulator.
| **Note:** this must be called before this instance has been used to do any operations.

**Signature:**  

    export declare function connectFunctionsEmulator(functionsInstance: Functions, host: string, port: number): void;

#### Parameters

|     Parameter     |                                                 Type                                                  |            Description            |
|-------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------|
| functionsInstance | [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface) |                                   |
| host              | string                                                                                                | The emulator host (ex: localhost) |
| port              | number                                                                                                | The emulator port (ex: 5001)      |

**Returns:**

void

### httpsCallable(functionsInstance, name, options)

Returns a reference to the callable HTTPS trigger with the given name.

**Signature:**  

    export declare function httpsCallable<RequestData = unknown, ResponseData = unknown, StreamData = unknown>(functionsInstance: Functions, name: string, options?: HttpsCallableOptions): HttpsCallable<RequestData, ResponseData, StreamData>;

#### Parameters

|     Parameter     |                                                                  Type                                                                  |       Description        |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| functionsInstance | [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface)                                  |                          |
| name              | string                                                                                                                                 | The name of the trigger. |
| options           | [HttpsCallableOptions](https://firebase.google.com/docs/reference/js/functions.httpscallableoptions.md#httpscallableoptions_interface) |                          |

**Returns:**

[HttpsCallable](https://firebase.google.com/docs/reference/js/functions.httpscallable.md#httpscallable_interface)\<RequestData, ResponseData, StreamData\>

### httpsCallableFromURL(functionsInstance, url, options)

Returns a reference to the callable HTTPS trigger with the specified url.

**Signature:**  

    export declare function httpsCallableFromURL<RequestData = unknown, ResponseData = unknown, StreamData = unknown>(functionsInstance: Functions, url: string, options?: HttpsCallableOptions): HttpsCallable<RequestData, ResponseData, StreamData>;

#### Parameters

|     Parameter     |                                                                  Type                                                                  |       Description       |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| functionsInstance | [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface)                                  |                         |
| url               | string                                                                                                                                 | The url of the trigger. |
| options           | [HttpsCallableOptions](https://firebase.google.com/docs/reference/js/functions.httpscallableoptions.md#httpscallableoptions_interface) |                         |

**Returns:**

[HttpsCallable](https://firebase.google.com/docs/reference/js/functions.httpscallable.md#httpscallable_interface)\<RequestData, ResponseData, StreamData\>

## FunctionsErrorCode

The set of Firebase Functions status codes. The codes are the same at the ones exposed by gRPC here: https://github.com/grpc/grpc/blob/master/doc/statuscodes.md

Possible values: - 'cancelled': The operation was cancelled (typically by the caller). - 'unknown': Unknown error or an error from a different error domain. - 'invalid-argument': Client specified an invalid argument. Note that this differs from 'failed-precondition'. 'invalid-argument' indicates arguments that are problematic regardless of the state of the system (e.g. an invalid field name). - 'deadline-exceeded': Deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. - 'not-found': Some requested document was not found. - 'already-exists': Some document that we attempted to create already exists. - 'permission-denied': The caller does not have permission to execute the specified operation. - 'resource-exhausted': Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. - 'failed-precondition': Operation was rejected because the system is not in a state required for the operation's execution. - 'aborted': The operation was aborted, typically due to a concurrency issue like transaction aborts, etc. - 'out-of-range': Operation was attempted past the valid range. - 'unimplemented': Operation is not implemented or not supported/enabled. - 'internal': Internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken. - 'unavailable': The service is currently unavailable. This is most likely a transient condition and may be corrected by retrying with a backoff. - 'data-loss': Unrecoverable data loss or corruption. - 'unauthenticated': The request does not have valid authentication credentials for the operation.

**Signature:**  

    export type FunctionsErrorCode = `functions/${FunctionsErrorCodeCore}`;

## FunctionsErrorCodeCore

Functions error code string appended after "functions/" product prefix. See [FunctionsErrorCode](https://firebase.google.com/docs/reference/js/functions.md#functionserrorcode) for full documentation of codes.

**Signature:**  

    export type FunctionsErrorCodeCore = 'ok' | 'cancelled' | 'unknown' | 'invalid-argument' | 'deadline-exceeded' | 'not-found' | 'already-exists' | 'permission-denied' | 'resource-exhausted' | 'failed-precondition' | 'aborted' | 'out-of-range' | 'unimplemented' | 'internal' | 'unavailable' | 'data-loss' | 'unauthenticated';