# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.retryconfig.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md.txt

# tasks.RetryConfig interface

How a task should be retried in the event of a non-2xx return.

**Signature:**  

    export interface RetryConfig 

## Properties

|                                                                             Property                                                                             |                                                                                       Type                                                                                       |                                                Description                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [maxAttempts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md#tasksretryconfigmaxattempts)             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | Maximum number of times a request should be attempted. If left unspecified, will default to 3.             |
| [maxBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md#tasksretryconfigmaxbackoffseconds) | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | The maximum amount of time to wait between attempts. If left unspecified will default to 1hr.              |
| [maxDoublings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md#tasksretryconfigmaxdoublings)           | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | The maximum number of times to double the backoff between retries. If left unspecified will default to 16. |
| [maxRetrySeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md#tasksretryconfigmaxretryseconds)     | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | Maximum amount of time for retrying failed task. If left unspecified will retry indefinitely.              |
| [minBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md#tasksretryconfigminbackoffseconds) | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | The minimum time to wait between attempts. If left unspecified will default to 100ms.                      |

## tasks.RetryConfig.maxAttempts

Maximum number of times a request should be attempted. If left unspecified, will default to 3.

**Signature:**  

    maxAttempts?: number | Expression<number> | ResetValue;

## tasks.RetryConfig.maxBackoffSeconds

The maximum amount of time to wait between attempts. If left unspecified will default to 1hr.

**Signature:**  

    maxBackoffSeconds?: number | Expression<number> | ResetValue;

## tasks.RetryConfig.maxDoublings

The maximum number of times to double the backoff between retries. If left unspecified will default to 16.

**Signature:**  

    maxDoublings?: number | Expression<number> | ResetValue;

## tasks.RetryConfig.maxRetrySeconds

Maximum amount of time for retrying failed task. If left unspecified will retry indefinitely.

**Signature:**  

    maxRetrySeconds?: number | Expression<number> | ResetValue;

## tasks.RetryConfig.minBackoffSeconds

The minimum time to wait between attempts. If left unspecified will default to 100ms.

**Signature:**  

    minBackoffSeconds?: number | Expression<number> | ResetValue;