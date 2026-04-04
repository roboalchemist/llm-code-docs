# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskretrypolicy.md.txt

How a task should be retried in the event of a non-2xx return.

<br />

**Signature:**  

    export interface TaskRetryConfig 

## Properties

|                                                                                 Property                                                                                 |  Type  |                                                Description                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------|
| [maxAttempts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskretrypolicy.md#httpstaskretrypolicymaxattempts)             | number | Maximum number of times a request should be attempted. If left unspecified, will default to 3.             |
| [maxBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskretrypolicy.md#httpstaskretrypolicymaxbackoffseconds) | number | The maximum amount of time to wait between attempts. If left unspecified will default to 1hr.              |
| [maxDoublings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskretrypolicy.md#httpstaskretrypolicymaxdoublings)           | number | The maximum number of times to double the backoff between retries. If left unspecified will default to 16. |
| [minBackoffSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskretrypolicy.md#httpstaskretrypolicyminbackoffseconds) | number | The minimum time to wait between attempts. If left unspecified will default to 100ms.                      |

## https.TaskRetryPolicy.maxAttempts

Maximum number of times a request should be attempted. If left unspecified, will default to 3.

**Signature:**  

    maxAttempts?: number;

## https.TaskRetryPolicy.maxBackoffSeconds

The maximum amount of time to wait between attempts. If left unspecified will default to 1hr.

**Signature:**  

    maxBackoffSeconds?: number;

## https.TaskRetryPolicy.maxDoublings

The maximum number of times to double the backoff between retries. If left unspecified will default to 16.

**Signature:**  

    maxDoublings?: number;

## https.TaskRetryPolicy.minBackoffSeconds

The minimum time to wait between attempts. If left unspecified will default to 100ms.

**Signature:**  

    minBackoffSeconds?: number;