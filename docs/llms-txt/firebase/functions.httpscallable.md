# Source: https://firebase.google.com/docs/reference/js/functions.httpscallable.md.txt

# HttpsCallable interface

A reference to a "callable" HTTP trigger in Cloud Functions.

**Signature:**  

    export interface HttpsCallable<RequestData = unknown, ResponseData = unknown, StreamData = unknown> 

## Properties

|                                                Property                                                |                                                                                                                                                                                               Type                                                                                                                                                                                                | Description |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [stream](https://firebase.google.com/docs/reference/js/functions.httpscallable.md#httpscallablestream) | (data?: RequestData \| null, options?: [HttpsCallableStreamOptions](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamoptions.md#httpscallablestreamoptions_interface)) =\> Promise\<[HttpsCallableStreamResult](https://firebase.google.com/docs/reference/js/functions.httpscallablestreamresult.md#httpscallablestreamresult_interface)\<ResponseData, StreamData\>\> |             |

## HttpsCallable.stream

**Signature:**  

    stream: (data?: RequestData | null, options?: HttpsCallableStreamOptions) => Promise<HttpsCallableStreamResult<ResponseData, StreamData>>;