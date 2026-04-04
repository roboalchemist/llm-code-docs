# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablefunction.md.txt

# https.CallableFunction interface

Creates a callable method for clients to call using a Firebase SDK.

**Signature:**  

    export interface CallableFunction<T, Return, Stream = unknown> extends HttpsFunction 

**Extends:** [HttpsFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpshttpsfunction)

## Methods

|                                                                                 Method                                                                                  |                                      Description                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [run(request)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablefunction.md#httpscallablefunctionrun)                 | Executes the handler function with the provided data as input. Used for unit testing. |
| [stream(request, response)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablefunction.md#httpscallablefunctionstream) |                                                                                       |

## https.CallableFunction.run()

Executes the handler function with the provided data as input. Used for unit testing.

**Signature:**  

    run(request: CallableRequest<T>): Return;

### Parameters

| Parameter |                                                                                 Type                                                                                 | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [CallableRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequest_interface)\<T\> |             |

**Returns:**

Return

The output of the handler function.

## https.CallableFunction.stream()

**Signature:**  

    stream(request: CallableRequest<T>, response: CallableResponse<Stream>): {
            stream: AsyncIterable<Stream>;
            output: Return;
        };

### Parameters

| Parameter |                                                                                     Type                                                                                     | Description |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| request   | [CallableRequest](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablerequest.md#httpscallablerequest_interface)\<T\>         |             |
| response  | [CallableResponse](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableresponse.md#httpscallableresponse_interface)\<Stream\> |             |

**Returns:**

{ stream: AsyncIterable\<Stream\>; output: Return; }