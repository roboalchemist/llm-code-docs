# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md.txt

# scheduler.ScheduleOptions interface

Options that can be set on a Schedule trigger.

**Signature:**  

    export interface ScheduleOptions extends options.GlobalOptions 

**Extends:** [options.GlobalOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptions_interface)

## Properties

|                                                                                     Property                                                                                     |                                                                                        Type                                                                                        |                    Description                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [maxBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptionsmaxbackoffseconds) | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue   | The maximum time to wait before retrying.          |
| [maxDoublings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptionsmaxdoublings)           | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue   | The time between will double max doublings times.  |
| [maxRetrySeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptionsmaxretryseconds)     | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue   | The time limit for retrying.                       |
| [minBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptionsminbackoffseconds) | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue   | The minimum time to wait before retying.           |
| [retryCount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptionsretrycount)               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue   | The number of retry attempts for a failed run.     |
| [schedule](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptionsschedule)                   | string                                                                                                                                                                             | The schedule, in Unix Crontab or AppEngine syntax. |
| [timeZone](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.scheduler.scheduleoptions.md#schedulerscheduleoptionstimezone)                   | timezone \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | The timezone that the schedule executes in.        |

## scheduler.ScheduleOptions.maxBackoffSeconds

The maximum time to wait before retrying.

**Signature:**  

    maxBackoffSeconds?: number | Expression<number> | ResetValue;

## scheduler.ScheduleOptions.maxDoublings

The time between will double max doublings times.

**Signature:**  

    maxDoublings?: number | Expression<number> | ResetValue;

## scheduler.ScheduleOptions.maxRetrySeconds

The time limit for retrying.

**Signature:**  

    maxRetrySeconds?: number | Expression<number> | ResetValue;

## scheduler.ScheduleOptions.minBackoffSeconds

The minimum time to wait before retying.

**Signature:**  

    minBackoffSeconds?: number | Expression<number> | ResetValue;

## scheduler.ScheduleOptions.retryCount

The number of retry attempts for a failed run.

**Signature:**  

    retryCount?: number | Expression<number> | ResetValue;

## scheduler.ScheduleOptions.schedule

The schedule, in Unix Crontab or AppEngine syntax.

**Signature:**  

    schedule: string;

## scheduler.ScheduleOptions.timeZone

The timezone that the schedule executes in.

**Signature:**  

    timeZone?: timezone | Expression<string> | ResetValue;