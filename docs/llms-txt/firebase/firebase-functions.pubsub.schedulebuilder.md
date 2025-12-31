# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md.txt

# pubsub.ScheduleBuilder class

The builder for scheduled functions, which are powered by Google Pub/Sub and Cloud Scheduler. Describes the Cloud Scheduler job that is deployed to trigger a scheduled function at the provided frequency. For more information, see \[Schedule functions\](/docs/functions/schedule-functions).

Access via `functions.pubsub.schedule()`.

**Signature:**  

    export declare class ScheduleBuilder 

## Constructors

|                                                                                  Constructor                                                                                  | Modifiers |                       Description                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------|
| [(constructor)(triggerResource, options)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilderconstructor) |           | Constructs a new instance of the `ScheduleBuilder` class |

## Methods

|                                                                          Method                                                                           | Modifiers |                                                   Description                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------|
| [onRun(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilderonrun)            |           | Event handler for scheduled functions. Triggered whenever the associated scheduler job sends a Pub/Sub message. |
| [retryConfig(config)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilderretryconfig) |           |                                                                                                                 |
| [timeZone(timeZone)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuildertimezone)     |           |                                                                                                                 |

## pubsub.ScheduleBuilder.(constructor)

Constructs a new instance of the `ScheduleBuilder` class

**Signature:**  

    constructor(triggerResource: () => string, options: DeploymentOptions);

### Parameters

|    Parameter    |                                                                     Type                                                                      | Description |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| triggerResource | () =\> string                                                                                                                                 |             |
| options         | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

## pubsub.ScheduleBuilder.onRun()

Event handler for scheduled functions. Triggered whenever the associated scheduler job sends a Pub/Sub message.

**Signature:**  

    onRun(handler: (context: EventContext) => PromiseLike<any> | any): CloudFunction<unknown>;

### Parameters

| Parameter |                                                                                  Type                                                                                   |                                    Description                                    |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| handler   | (context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Handler that fires whenever the associated scheduler job sends a Pub/Sub message. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<unknown\>

A function that you can export and deploy.

## pubsub.ScheduleBuilder.retryConfig()

**Signature:**  

    retryConfig(config: ScheduleRetryConfig): ScheduleBuilder;

### Parameters

| Parameter |                                                                        Type                                                                         | Description |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| config    | [ScheduleRetryConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfig_interface) |             |

**Returns:**

[ScheduleBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilder_class)

## pubsub.ScheduleBuilder.timeZone()

**Signature:**  

    timeZone(timeZone: string): ScheduleBuilder;

### Parameters

| Parameter |  Type  | Description |
|-----------|--------|-------------|
| timeZone  | string |             |

**Returns:**

[ScheduleBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilder_class)