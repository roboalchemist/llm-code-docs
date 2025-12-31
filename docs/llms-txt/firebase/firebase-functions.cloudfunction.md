# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md.txt

# CloudFunction interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A handler for CloudEvents.

**Signature:**  

    export interface CloudFunction<EventType extends CloudEvent<unknown>> 

## Properties

|                                                                  Property                                                                   |       Type       | Description |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------|-------------|
| [__endpoint](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction__endpoint) | ManifestEndpoint |             |
| [__trigger](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction__trigger)   | unknown          |             |

## Methods

|                                                                Method                                                                |                                            Description                                             |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [run(event)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunctionrun) | ***(BETA)*** The callback passed to the `CloudFunction` constructor. Use `run` to test a function. |

## CloudFunction.__endpoint

**Signature:**  

    __endpoint: ManifestEndpoint;

## CloudFunction.__trigger

**Signature:**  

    __trigger?: unknown;

## CloudFunction.run()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The callback passed to the `CloudFunction` constructor. Use `run` to test a function.

**Signature:**  

    run(event: EventType): any | Promise<any>;

### Parameters

| Parameter |   Type    |         Description         |
|-----------|-----------|-----------------------------|
| event     | EventType | The parsed event to handle. |

**Returns:**

any \| Promise\<any\>

Any return value. Cloud Functions awaits any promise before shutting down your function. Resolved return values are only used for unit testing purposes.