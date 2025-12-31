# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md.txt

The request used to call a callable function.

**Signature:**  

    export interface CallableRequest<T = any> 

## Properties

|                                                                                Property                                                                                |     Type     |                                                                                                                                   Description                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [acceptsStreaming](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequestacceptsstreaming) | boolean      | Whether this is a streaming request. Code can be optimized by not trying to generate a stream of chunks to call`response.sendChunk`if`request.acceptsStreaming`is false. It is always safe, however, to call`response.sendChunk`as this will noop if`acceptsStreaming`is false. |
| [app](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequestapp)                           | AppCheckData | The result of decoding and verifying a Firebase App Check token.                                                                                                                                                                                                                |
| [auth](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequestauth)                         | AuthData     | The result of decoding and verifying a Firebase Auth ID token.                                                                                                                                                                                                                  |
| [data](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequestdata)                         | T            | The parameters used by a client when calling this function.                                                                                                                                                                                                                     |
| [instanceIdToken](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequestinstanceidtoken)   | string       | An unverified token for a Firebase Instance ID.                                                                                                                                                                                                                                 |
| [rawRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequestrawrequest)             | Request      | The raw request handled by the callable.                                                                                                                                                                                                                                        |

## https.CallableRequest.acceptsStreaming

Whether this is a streaming request. Code can be optimized by not trying to generate a stream of chunks to call`response.sendChunk`if`request.acceptsStreaming`is false. It is always safe, however, to call`response.sendChunk`as this will noop if`acceptsStreaming`is false.

**Signature:**  

    acceptsStreaming: boolean;

## https.CallableRequest.app

The result of decoding and verifying a Firebase App Check token.

**Signature:**  

    app?: AppCheckData;

## https.CallableRequest.auth

The result of decoding and verifying a Firebase Auth ID token.

**Signature:**  

    auth?: AuthData;

## https.CallableRequest.data

The parameters used by a client when calling this function.

**Signature:**  

    data: T;

## https.CallableRequest.instanceIdToken

An unverified token for a Firebase Instance ID.

**Signature:**  

    instanceIdToken?: string;

## https.CallableRequest.rawRequest

The raw request handled by the callable.

**Signature:**  

    rawRequest: Request;