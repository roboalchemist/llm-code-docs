# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md.txt

# ScheduleRetryConfig interface

Scheduler retry options. Applies only to scheduled functions.

**Signature:**  

    export interface ScheduleRetryConfig 

## Properties

|                                                                          Property                                                                          |                                                                                Type                                                                                 |                                                                                                                                                                 Description                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [maxBackoffDuration](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigmaxbackoffduration) | string \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | The maximum amount of time to wait before retrying a job after it fails.                                                                                                                                                                                                                                                                    |
| [maxDoublings](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigmaxdoublings)             | number \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | The max number of backoff doubling applied at each retry.                                                                                                                                                                                                                                                                                   |
| [maxRetryDuration](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigmaxretryduration)     | string \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | The time limit for retrying a failed job, measured from time when an execution was first attempted.If specified with [ScheduleRetryConfig.retryCount](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigretrycount), the job will be retried until both limits are reached. |
| [minBackoffDuration](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigminbackoffduration) | string \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | The minimum amount of time to wait before retrying a job after it fails.                                                                                                                                                                                                                                                                    |
| [retryCount](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigretrycount)                 | number \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | The number of attempts that the system will make to run a job using the exponential backoff procedure described by [ScheduleRetryConfig.maxDoublings](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigmaxdoublings).                                                      |

## ScheduleRetryConfig.maxBackoffDuration

The maximum amount of time to wait before retrying a job after it fails.

**Signature:**  

    maxBackoffDuration?: string | Expression<string> | ResetValue;

## ScheduleRetryConfig.maxDoublings

The max number of backoff doubling applied at each retry.

**Signature:**  

    maxDoublings?: number | Expression<number> | ResetValue;

## ScheduleRetryConfig.maxRetryDuration

The time limit for retrying a failed job, measured from time when an execution was first attempted.

If specified with [ScheduleRetryConfig.retryCount](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigretrycount), the job will be retried until both limits are reached.

**Signature:**  

    maxRetryDuration?: string | Expression<string> | ResetValue;

## ScheduleRetryConfig.minBackoffDuration

The minimum amount of time to wait before retrying a job after it fails.

**Signature:**  

    minBackoffDuration?: string | Expression<string> | ResetValue;

## ScheduleRetryConfig.retryCount

The number of attempts that the system will make to run a job using the exponential backoff procedure described by [ScheduleRetryConfig.maxDoublings](https://firebase.google.com/docs/reference/functions/firebase-functions.scheduleretryconfig.md#scheduleretryconfigmaxdoublings).

**Signature:**  

    retryCount?: number | Expression<number> | ResetValue;