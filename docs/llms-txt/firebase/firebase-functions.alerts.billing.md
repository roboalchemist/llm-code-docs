# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.md.txt

# alerts.billing namespace

## Functions

|                                                                                              Function                                                                                               |                                 Description                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [onPlanAutomatedUpdatePublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.md#alertsbillingonplanautomatedupdatepublished)       | Declares a function that can handle an automated billing plan update event. |
| [onPlanAutomatedUpdatePublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.md#alertsbillingonplanautomatedupdatepublished) | Declares a function that can handle an automated billing plan update event. |
| [onPlanUpdatePublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.md#alertsbillingonplanupdatepublished)                         | Declares a function that can handle a billing plan update event.            |
| [onPlanUpdatePublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.md#alertsbillingonplanupdatepublished)                   | Declares a function that can handle a billing plan update event.            |

## Interfaces

|                                                                                                     Interface                                                                                                     |                                                       Description                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)                                           | A custom CloudEvent for billing Firebase Alerts (with custom extension attributes).                                     |
| [PlanAutomatedUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayload_interface) | The internal payload object for billing plan automated updates. Payload is wrapped inside a `FirebaseAlertData` object. |
| [PlanUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayload_interface)                            | The internal payload object for billing plan updates. Payload is wrapped inside a `FirebaseAlertData` object.           |

## alerts.billing.onPlanAutomatedUpdatePublished()

Declares a function that can handle an automated billing plan update event.

**Signature:**  

    export declare function onPlanAutomatedUpdatePublished(handler: (event: BillingEvent<PlanAutomatedUpdatePayload>) => any | Promise<any>): CloudFunction<BillingEvent<PlanAutomatedUpdatePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                              Type                                                                                                                                                                                                               |                                  Description                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| handler   | (event: [BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanAutomatedUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time an automated billing plan update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanAutomatedUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayload_interface)\>\>

A function that you can export and deploy.

## alerts.billing.onPlanAutomatedUpdatePublished()

Declares a function that can handle an automated billing plan update event.

**Signature:**  

    export declare function onPlanAutomatedUpdatePublished(opts: options.EventHandlerOptions, handler: (event: BillingEvent<PlanAutomatedUpdatePayload>) => any | Promise<any>): CloudFunction<BillingEvent<PlanAutomatedUpdatePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                              Type                                                                                                                                                                                                               |                                  Description                                   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| opts      | [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)                                                                                                                                                                                                                                                        | Options that can be set on the function.                                       |
| handler   | (event: [BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanAutomatedUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time an automated billing plan update occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanAutomatedUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayload_interface)\>\>

A function that you can export and deploy.

## alerts.billing.onPlanUpdatePublished()

Declares a function that can handle a billing plan update event.

**Signature:**  

    export declare function onPlanUpdatePublished(handler: (event: BillingEvent<PlanUpdatePayload>) => any | Promise<any>): CloudFunction<BillingEvent<PlanUpdatePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                 Type                                                                                                                                                                                                 |                           Description                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| handler   | (event: [BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a billing plan is updated. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayload_interface)\>\>

A function that you can export and deploy.

## alerts.billing.onPlanUpdatePublished()

Declares a function that can handle a billing plan update event.

**Signature:**  

    export declare function onPlanUpdatePublished(opts: options.EventHandlerOptions, handler: (event: BillingEvent<PlanUpdatePayload>) => any | Promise<any>): CloudFunction<BillingEvent<PlanUpdatePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                 Type                                                                                                                                                                                                 |                           Description                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| opts      | [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)                                                                                                                                                                                                                             | Options that can be set on the function.                         |
| handler   | (event: [BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a billing plan is updated. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[BillingEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingevent_interface)\<[PlanUpdatePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayload_interface)\>\>

A function that you can export and deploy.