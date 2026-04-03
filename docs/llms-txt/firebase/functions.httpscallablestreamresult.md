# Source: https://firebase.google.com/docs/reference/js/functions.httpscallablestreamresult.md.txt

# HttpsCallableStreamResult interface

An `HttpsCallableStreamResult` wraps a single streaming result from a function call.

**Signature:**  

    export interface HttpsCallableStreamResult<ResponseData = unknown, StreamData = unknown> 

## Properties

|                                                            Property                                                            |            Type             | Description |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------|
| [data](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamresult.md#httpscallablestreamresultdata)     | Promise\<ResponseData\>     |             |
| [stream](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamresult.md#httpscallablestreamresultstream) | AsyncIterable\<StreamData\> |             |

## HttpsCallableStreamResult.data

**Signature:**  

    readonly data: Promise<ResponseData>;

## HttpsCallableStreamResult.stream

**Signature:**  

    readonly stream: AsyncIterable<StreamData>;