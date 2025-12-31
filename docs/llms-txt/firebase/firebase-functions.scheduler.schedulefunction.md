# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.schedulefunction.md.txt

# scheduler.ScheduleFunction interface

The Cloud Function type for Schedule triggers.

**Signature:**  

    export interface ScheduleFunction extends HttpsFunction 

**Extends:** [HttpsFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpshttpsfunction)

## Properties

|                                                                                   Property                                                                                   |          Type           | Description |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------|
| [__requiredAPIs](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.schedulefunction.md#schedulerschedulefunction__requiredapis) | ManifestRequiredAPI\[\] |             |

## Methods

|                                                                            Method                                                                            | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [run(data)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.schedulefunction.md#schedulerschedulefunctionrun) |             |

## scheduler.ScheduleFunction.__requiredAPIs

**Signature:**  

    __requiredAPIs?: ManifestRequiredAPI[];

## scheduler.ScheduleFunction.run()

**Signature:**  

    run(data: ScheduledEvent): void | Promise<void>;

### Parameters

| Parameter |                                                                                 Type                                                                                 | Description |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| data      | [ScheduledEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduledevent.md#schedulerscheduledevent_interface) |             |

**Returns:**

void \| Promise\<void\>