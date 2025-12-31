# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskratelimits.md.txt

How congestion control should be applied to the function.

<br />

**Signature:**  

    export interface TaskRateLimits 

## Properties

|                                                                                      Property                                                                                      |  Type  | Description |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------|
| [maxBurstSize](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskratelimits.md#httpstaskratelimitsmaxburstsize)                       | number |             |
| [maxConcurrentDispatches](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskratelimits.md#httpstaskratelimitsmaxconcurrentdispatches) | number |             |
| [maxDispatchesPerSecond](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskratelimits.md#httpstaskratelimitsmaxdispatchespersecond)   | number |             |

## https.TaskRateLimits.maxBurstSize

**Signature:**  

    maxBurstSize?: number;

## https.TaskRateLimits.maxConcurrentDispatches

**Signature:**  

    maxConcurrentDispatches?: number;

## https.TaskRateLimits.maxDispatchesPerSecond

**Signature:**  

    maxDispatchesPerSecond?: number;