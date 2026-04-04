# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md.txt

# https.CallableContext interface

The interface for metadata for the API as passed to the handler.

**Signature:**  

    export interface CallableContext 

## Properties

|                                                                        Property                                                                         |     Type     |                           Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md#httpscallablecontextapp)                         | AppCheckData | The result of decoding and verifying a Firebase AppCheck token. |
| [auth](https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md#httpscallablecontextauth)                       | AuthData     | The result of decoding and verifying a Firebase Auth ID token.  |
| [instanceIdToken](https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md#httpscallablecontextinstanceidtoken) | string       | An unverified token for a Firebase Instance ID.                 |
| [rawRequest](https://firebase.google.com/docs/reference/functions/firebase-functions.https.callablecontext.md#httpscallablecontextrawrequest)           | Request      | The raw request handled by the callable.                        |

## https.CallableContext.app

The result of decoding and verifying a Firebase AppCheck token.

**Signature:**  

    app?: AppCheckData;

## https.CallableContext.auth

The result of decoding and verifying a Firebase Auth ID token.

**Signature:**  

    auth?: AuthData;

## https.CallableContext.instanceIdToken

An unverified token for a Firebase Instance ID.

**Signature:**  

    instanceIdToken?: string;

## https.CallableContext.rawRequest

The raw request handled by the callable.

**Signature:**  

    rawRequest: Request;