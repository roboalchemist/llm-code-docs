# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retrypolicy.md.txt

How a task should be retried in the event of a non-2xx return.

<br />

**Signature:**  

    export interface RetryConfig 

## Properties

|                                                                             Property                                                                             |  Type  |                                                Description                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------|
| [maxAttempts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retrypolicy.md#tasksretrypolicymaxattempts)             | number | Maximum number of times a request should be attempted. If left unspecified, will default to 3.             |
| [maxBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retrypolicy.md#tasksretrypolicymaxbackoffseconds) | number | The maximum amount of time to wait between attempts. If left unspecified will default to 1hr.              |
| [maxDoublings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retrypolicy.md#tasksretrypolicymaxdoublings)           | number | The maximum number of times to double the backoff between retries. If left unspecified will default to 16. |
| [maxRetrySeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retrypolicy.md#tasksretrypolicymaxretryseconds)     | number | Maximum amount of time for retrying failed task. If left unspecified will retry indefinitely.              |
| [minBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retrypolicy.md#tasksretrypolicyminbackoffseconds) | number | The minimum time to wait between attempts. If left unspecified will default to 100ms.                      |

## tasks.RetryPolicy.maxAttempts

Maximum number of times a request should be attempted. If left unspecified, will default to 3.

**Signature:**  

    maxAttempts?: number;

## tasks.RetryPolicy.maxBackoffSeconds

The maximum amount of time to wait between attempts. If left unspecified will default to 1hr.

**Signature:**  

    maxBackoffSeconds?: number;

## tasks.RetryPolicy.maxDoublings

The maximum number of times to double the backoff between retries. If left unspecified will default to 16.

**Signature:**  

    maxDoublings?: number;

## tasks.RetryPolicy.maxRetrySeconds

Maximum amount of time for retrying failed task. If left unspecified will retry indefinitely.

**Signature:**  

    maxRetrySeconds?: number;

## tasks.RetryPolicy.minBackoffSeconds

The minimum time to wait between attempts. If left unspecified will default to 100ms.

**Signature:**  

    minBackoffSeconds?: number;