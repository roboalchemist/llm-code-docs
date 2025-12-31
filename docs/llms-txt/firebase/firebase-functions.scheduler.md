# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.md.txt

# scheduler namespace

## Functions

|                                                                        Function                                                                        |                                              Description                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [onSchedule(schedule, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.md#scheduleronschedule) | Handler for scheduled functions. Triggered whenever the associated scheduler job sends a http request. |
| [onSchedule(options, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.md#scheduleronschedule)  | Handler for scheduled functions. Triggered whenever the associated scheduler job sends a http request. |

## Interfaces

|                                                                                 Interface                                                                                  |                                  Description                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [ScheduledEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduledevent.md#schedulerscheduledevent_interface)       | Interface representing a ScheduleEvent that is passed to the function handler. |
| [ScheduleFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.schedulefunction.md#schedulerschedulefunction_interface) | The Cloud Function type for Schedule triggers.                                 |
| [ScheduleOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptions_interface)    | Options that can be set on a Schedule trigger.                                 |

## scheduler.onSchedule()

Handler for scheduled functions. Triggered whenever the associated scheduler job sends a http request.

**Signature:**  

    export declare function onSchedule(schedule: string, handler: (event: ScheduledEvent) => void | Promise<void>): ScheduleFunction;

### Parameters

| Parameter |                                                                                                   Type                                                                                                    |                    Description                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| schedule  | string                                                                                                                                                                                                    | The schedule, in Unix Crontab or AppEngine syntax. |
| handler   | (event: [ScheduledEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduledevent.md#schedulerscheduledevent_interface)) =\> void \| Promise\<void\> | A function to execute when triggered.              |

**Returns:**

[ScheduleFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.schedulefunction.md#schedulerschedulefunction_interface)

A function that you can export and deploy.

## scheduler.onSchedule()

Handler for scheduled functions. Triggered whenever the associated scheduler job sends a http request.

**Signature:**  

    export declare function onSchedule(options: ScheduleOptions, handler: (event: ScheduledEvent) => void | Promise<void>): ScheduleFunction;

### Parameters

| Parameter |                                                                                                   Type                                                                                                    |              Description               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| options   | [ScheduleOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptions_interface)                                   | Options to set on scheduled functions. |
| handler   | (event: [ScheduledEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduledevent.md#schedulerscheduledevent_interface)) =\> void \| Promise\<void\> | A function to execute when triggered.  |

**Returns:**

[ScheduleFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.schedulefunction.md#schedulerschedulefunction_interface)

A function that you can export and deploy.