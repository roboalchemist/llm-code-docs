# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md.txt

# Schedule interface

Configuration options for scheduled functions.

**Signature:**  

    export interface Schedule 

## Properties

|                                                        Property                                                        |                                                                        Type                                                                         |                                                                                                                              Description                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [retryConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md#scheduleretryconfig) | [ScheduleRetryConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfig_interface) | Settings that determine the retry behavior.                                                                                                                                                                                                                            |
| [schedule](https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md#scheduleschedule)       | string                                                                                                                                              | Describes the schedule on which the job will be executed.The schedule can be either of the following types:1. [Crontab](https://en.wikipedia.org/wiki/Cron#Overview)2. English-like [schedule](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules) |
| [timeZone](https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md#scheduletimezone)       | string \| ResetValue                                                                                                                                | Specifies the time zone to be used in interpreting [Schedule.schedule](https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md#scheduleschedule).The value of this field must be a time zone name from the tz database.                    |

## Schedule.retryConfig

Settings that determine the retry behavior.

**Signature:**  

    retryConfig?: ScheduleRetryConfig;

## Schedule.schedule

Describes the schedule on which the job will be executed.

The schedule can be either of the following types:

1. [Crontab](https://en.wikipedia.org/wiki/Cron#Overview)

2. English-like [schedule](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules)

**Signature:**  

    schedule: string;

### Example

    // Crontab schedule
    schedule: "0 9 * * 1"` // Every Monday at 09:00 AM

    // English-like schedule
    schedule: "every 5 minutes"

## Schedule.timeZone

Specifies the time zone to be used in interpreting [Schedule.schedule](https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md#scheduleschedule).

The value of this field must be a time zone name from the tz database.

**Signature:**  

    timeZone?: string | ResetValue;