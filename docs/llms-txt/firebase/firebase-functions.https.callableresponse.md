# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableresponse.md.txt

# https.CallableResponse interface

`CallableProxyResponse` allows streaming response chunks and listening to signals triggered in events such as a disconnect.

**Signature:**  

    export interface CallableResponse<T = unknown> 

## Properties

|                                                                          Property                                                                          |               Type                |                                                                                                                                          Description                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [sendChunk](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableresponse.md#httpscallableresponsesendchunk) | (chunk: T) =\> Promise\<boolean\> | Writes a chunk of the response body to the client. This method can be called multiple times to stream data progressively. Returns a promise of whether the data was written. This can be false, for example, if the request was not a streaming request. Rejects if there is a network error. |
| [signal](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableresponse.md#httpscallableresponsesignal)       | AbortSignal                       | An `AbortSignal` that is triggered when the client disconnects or the request is terminated prematurely.                                                                                                                                                                                      |

## https.CallableResponse.sendChunk

Writes a chunk of the response body to the client. This method can be called multiple times to stream data progressively. Returns a promise of whether the data was written. This can be false, for example, if the request was not a streaming request. Rejects if there is a network error.

**Signature:**  

    sendChunk: (chunk: T) => Promise<boolean>;

## https.CallableResponse.signal

An `AbortSignal` that is triggered when the client disconnects or the request is terminated prematurely.

**Signature:**  

    signal: AbortSignal;