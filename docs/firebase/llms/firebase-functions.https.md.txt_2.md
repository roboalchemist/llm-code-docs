# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md.txt

# https namespace

## Functions

| Function | Description |
|---|---|
| [hasClaim(claim, value)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpshasclaim) |   |
| [isSignedIn()](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsissignedin) |   |
| [onCall(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsoncall) | Declares a callable method for clients to call using a Firebase SDK. |
| [onCall(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsoncall) | Declares a callable method for clients to call using a Firebase SDK. |
| [onCallGenkit(action)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsoncallgenkit) |   |
| [onCallGenkit(opts, flow)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsoncallgenkit) |   |
| [onRequest(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsonrequest) | Handles HTTPS requests. |
| [onRequest(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsonrequest) | Handles HTTPS requests. |

## Classes

| Class | Description |
|---|---|
| [HttpsError](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpserror.md#httpshttpserror_class) | An explicit error that can be thrown from a handler to send an error to the client that called the function. |

## Interfaces

| Interface | Description |
|---|---|
| [CallableFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablefunction.md#httpscallablefunction_interface) | Creates a callable method for clients to call using a Firebase SDK. |
| [CallableOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md#httpscallableoptions_interface) | Options that can be set on a callable HTTPS function. |
| [CallableRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequest_interface) | The request used to call a callable function. |
| [CallableResponse](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableresponse.md#httpscallableresponse_interface) | `CallableProxyResponse` allows streaming response chunks and listening to signals triggered in events such as a disconnect. |
| [HttpsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptions_interface) | Options that can be set on an onRequest HTTPS function. |
| [Request](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.request.md#httpsrequest_interface) | An express request with the wire format representation of the request body. |

## Type Aliases

| Type Alias | Description |
|---|---|
| [FunctionsErrorCode](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpsfunctionserrorcode) | The set of Firebase Functions status codes. The codes are the same at the ones exposed by [gRPC](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md). |
| [HttpsFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpshttpsfunction) | Handles HTTPS requests. |

## https.hasClaim()

> > [!WARNING]
> > **Warning:** This API is now obsolete.
>
> An auth policy that requires a user to be both signed in and have a specific claim (optionally with a specific value)

**Signature:**

    hasClaim: (claim: string, value?: string) => (auth: AuthData | null) => boolean

### Parameters

| Parameter | Type | Description |
|---|---|---|
| claim | string |   |
| value | string |   |

**Returns:**

(auth: AuthData \| null) =\> boolean

## https.isSignedIn()

> > [!WARNING]
> > **Warning:** This API is now obsolete.
>
> An auth policy that requires a user to be signed in.

**Signature:**

    isSignedIn: () => (auth: AuthData | null) => boolean

**Returns:**

(auth: AuthData \| null) =\> boolean

## https.onCall()

Declares a callable method for clients to call using a Firebase SDK.

**Signature:**

    export declare function onCall<T = any, Return = any | Promise<any>, Stream = unknown>(opts: CallableOptions<T>, handler: (request: CallableRequest<T>, response?: CallableResponse<Stream>) => Return): CallableFunction<T, Return extends Promise<unknown> ? Return : Promise<Return>, Stream>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| opts | [CallableOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md#httpscallableoptions_interface)\<T\> | Options to set on this function. |
| handler | (request: [CallableRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequest_interface)\<T\>, response?: [CallableResponse](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableresponse.md#httpscallableresponse_interface)\<Stream\>) =\> Return | A function that takes a [https.CallableRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequest_interface). |

**Returns:**

CallableFunction\<T, Return extends Promise\<unknown\> ? Return : Promise\<Return\>, Stream\>

A function that you can export and deploy.

## https.onCall()

Declares a callable method for clients to call using a Firebase SDK.

**Signature:**

    export declare function onCall<T = any, Return = any | Promise<any>, Stream = unknown>(handler: (request: CallableRequest<T>, response?: CallableResponse<Stream>) => Return): CallableFunction<T, Return extends Promise<unknown> ? Return : Promise<Return>>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| handler | (request: [CallableRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequest_interface)\<T\>, response?: [CallableResponse](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableresponse.md#httpscallableresponse_interface)\<Stream\>) =\> Return | A function that takes a [https.CallableRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequest_interface). |

**Returns:**

CallableFunction\<T, Return extends Promise\<unknown\> ? Return : Promise\<Return\>\>

A function that you can export and deploy.

## https.onCallGenkit()

**Signature:**

    export declare function onCallGenkit<A extends GenkitAction>(action: A): CallableFunction<ActionInput<A>, Promise<ActionOutput<A>>, ActionStream<A>>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| action | A |   |

**Returns:**

CallableFunction\<ActionInput\<A\>, Promise\<ActionOutput\<A\>\>, ActionStream\<A\>\>

## https.onCallGenkit()

**Signature:**

    export declare function onCallGenkit<A extends GenkitAction>(opts: CallableOptions<ActionInput<A>>, flow: A): CallableFunction<ActionInput<A>, Promise<ActionOutput<A>>, ActionStream<A>>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| opts | [CallableOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md#httpscallableoptions_interface)\<ActionInput\<A\>\> |   |
| flow | A |   |

**Returns:**

CallableFunction\<ActionInput\<A\>, Promise\<ActionOutput\<A\>\>, ActionStream\<A\>\>

## https.onRequest()

Handles HTTPS requests.

**Signature:**

    export declare function onRequest(opts: HttpsOptions, handler: (request: Request, response: express.Response) => void | Promise<void>): HttpsFunction;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| opts | [HttpsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptions_interface) | Options to set on this function |
| handler | (request: Request, response: express.Response) =\> void \| Promise\<void\> | A function that takes a [https.Request](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.request.md#httpsrequest_interface) and response object, same signature as an Express app. |

**Returns:**

[HttpsFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpshttpsfunction)

A function that you can export and deploy.

## https.onRequest()

Handles HTTPS requests.

**Signature:**

    export declare function onRequest(handler: (request: Request, response: express.Response) => void | Promise<void>): HttpsFunction;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| handler | (request: Request, response: express.Response) =\> void \| Promise\<void\> | A function that takes a [https.Request](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.request.md#httpsrequest_interface) and response object, same signature as an Express app. |

**Returns:**

[HttpsFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpshttpsfunction)

A function that you can export and deploy.

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

## https.HttpsFunction

Handles HTTPS requests.

**Signature:**

    export type HttpsFunction = ((
    req: Request, 
    res: express.Response) => void | Promise<void>) & {
        __trigger?: unknown;
        __endpoint: ManifestEndpoint;
    };