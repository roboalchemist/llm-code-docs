# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.md.txt

## Functions

|                                                                                              Function                                                                                              |                                 Description                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [onThresholdAlertPublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.md#alertsperformanceonthresholdalertpublished)        | Declares a function that can handle receiving performance threshold alerts. |
| [onThresholdAlertPublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.md#alertsperformanceonthresholdalertpublished) | Declares a function that can handle receiving performance threshold alerts. |
| [onThresholdAlertPublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.md#alertsperformanceonthresholdalertpublished)  | Declares a function that can handle receiving performance threshold alerts. |

## Interfaces

|                                                                                                 Interface                                                                                                  |                                            Description                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [PerformanceEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.performanceevent.md#alertsperformanceperformanceevent_interface)                | A custom CloudEvent for Firebase Alerts (with custom extension attributes).                        |
| [PerformanceOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.performanceoptions.md#alertsperformanceperformanceoptions_interface)          | Configuration for app distribution functions.                                                      |
| [ThresholdAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.thresholdalertpayload.md#alertsperformancethresholdalertpayload_interface) | The internal payload object for a performance threshold alert. Payload is wrapped inside a object. |

## alerts.performance.onThresholdAlertPublished()

Declares a function that can handle receiving performance threshold alerts.

**Signature:**  

    export declare function onThresholdAlertPublished(handler: (event: PerformanceEvent<ThresholdAlertPayload>) => any | Promise<any>): CloudFunction<PerformanceEvent<ThresholdAlertPayload>>;

### Parameters

| Parameter |                                     Type                                     |                             Description                              |
|-----------|------------------------------------------------------------------------------|----------------------------------------------------------------------|
| handler   | (event: PerformanceEvent\<ThresholdAlertPayload\>) =\> any \| Promise\<any\> | Event handler which is run every time a threshold alert is received. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<PerformanceEvent\<ThresholdAlertPayload\>\>

A function that you can export and deploy.

## alerts.performance.onThresholdAlertPublished()

Declares a function that can handle receiving performance threshold alerts.

**Signature:**  

    export declare function onThresholdAlertPublished(appId: string, handler: (event: PerformanceEvent<ThresholdAlertPayload>) => any | Promise<any>): CloudFunction<PerformanceEvent<ThresholdAlertPayload>>;

### Parameters

| Parameter |                                     Type                                     |                             Description                              |
|-----------|------------------------------------------------------------------------------|----------------------------------------------------------------------|
| appId     | string                                                                       | A specific application the handler will trigger on.                  |
| handler   | (event: PerformanceEvent\<ThresholdAlertPayload\>) =\> any \| Promise\<any\> | Event handler which is run every time a threshold alert is received. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<PerformanceEvent\<ThresholdAlertPayload\>\>

A function that you can export and deploy.

## alerts.performance.onThresholdAlertPublished()

Declares a function that can handle receiving performance threshold alerts.

**Signature:**  

    export declare function onThresholdAlertPublished(opts: PerformanceOptions, handler: (event: PerformanceEvent<ThresholdAlertPayload>) => any | Promise<any>): CloudFunction<PerformanceEvent<ThresholdAlertPayload>>;

### Parameters

| Parameter |                                     Type                                     |                             Description                              |
|-----------|------------------------------------------------------------------------------|----------------------------------------------------------------------|
| opts      | PerformanceOptions                                                           | Options that can be set on the function.                             |
| handler   | (event: PerformanceEvent\<ThresholdAlertPayload\>) =\> any \| Promise\<any\> | Event handler which is run every time a threshold alert is received. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<PerformanceEvent\<ThresholdAlertPayload\>\>

A function that you can export and deploy.