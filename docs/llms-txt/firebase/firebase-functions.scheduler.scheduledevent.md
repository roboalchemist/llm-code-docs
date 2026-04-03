# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduledevent.md.txt

# scheduler.ScheduledEvent interface

Interface representing a ScheduleEvent that is passed to the function handler.

**Signature:**  

    export interface ScheduledEvent 

## Properties

|                                                                               Property                                                                               |  Type  |                                                                                                                              Description                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [jobName](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduledevent.md#schedulerscheduledeventjobname)           | string | The Cloud Scheduler job name. Populated via the X-CloudScheduler-JobName header.If invoked manually, this field is undefined.                                                                                                                                         |
| [scheduleTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduledevent.md#schedulerscheduledeventscheduletime) | string | For Cloud Scheduler jobs specified in the unix-cron format, this is the job schedule time in RFC3339 UTC "Zulu" format. Populated via the X-CloudScheduler-ScheduleTime header.If the schedule is manually triggered, this field will be the function execution time. |

## scheduler.ScheduledEvent.jobName

The Cloud Scheduler job name. Populated via the X-CloudScheduler-JobName header.

If invoked manually, this field is undefined.

**Signature:**  

    jobName?: string;

## scheduler.ScheduledEvent.scheduleTime

For Cloud Scheduler jobs specified in the unix-cron format, this is the job schedule time in RFC3339 UTC "Zulu" format. Populated via the X-CloudScheduler-ScheduleTime header.

If the schedule is manually triggered, this field will be the function execution time.

**Signature:**  

    scheduleTime: string;