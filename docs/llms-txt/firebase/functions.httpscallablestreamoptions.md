# Source: https://firebase.google.com/docs/reference/js/functions.httpscallablestreamoptions.md.txt

# HttpsCallableStreamOptions interface

An interface for metadata about how a stream call should be executed.

**Signature:**  

    export interface HttpsCallableStreamOptions 

## Properties

|                                                                               Property                                                                               |    Type     |                                                                                                                                                         Description                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [limitedUseAppCheckTokens](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamoptions.md#httpscallablestreamoptionslimiteduseappchecktokens) | boolean     | If set to true, uses a limited-use App Check token for callable function requests from this instance of [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface). You must use limited-use tokens to call functions with replay protection enabled. By default, this is false. |
| [signal](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamoptions.md#httpscallablestreamoptionssignal)                                     | AbortSignal | An `AbortSignal` that can be used to cancel the streaming response. When the signal is aborted, the underlying HTTP connection will be terminated.                                                                                                                                                                          |

## HttpsCallableStreamOptions.limitedUseAppCheckTokens

If set to true, uses a limited-use App Check token for callable function requests from this instance of [Functions](https://firebase.google.com/docs/reference/js/functions.functions.md#functions_interface). You must use limited-use tokens to call functions with replay protection enabled. By default, this is false.

**Signature:**  

    limitedUseAppCheckTokens?: boolean;

## HttpsCallableStreamOptions.signal

An `AbortSignal` that can be used to cancel the streaming response. When the signal is aborted, the underlying HTTP connection will be terminated.

**Signature:**  

    signal?: AbortSignal;