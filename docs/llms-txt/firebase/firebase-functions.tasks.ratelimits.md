# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.ratelimits.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.ratelimits.md.txt

# tasks.RateLimits interface

How congestion control should be applied to the function.

**Signature:**  

    export interface RateLimits 

## Properties

|                                                                                  Property                                                                                  |                                                                                       Type                                                                                       |                                                Description                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [maxConcurrentDispatches](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.ratelimits.md#tasksratelimitsmaxconcurrentdispatches) | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | The maximum number of requests that can be processed at a time. If left unspecified, will default to 1000. |
| [maxDispatchesPerSecond](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.ratelimits.md#tasksratelimitsmaxdispatchespersecond)   | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | The maximum number of requests that can be invoked per second. If left unspecified, will default to 500.   |

## tasks.RateLimits.maxConcurrentDispatches

The maximum number of requests that can be processed at a time. If left unspecified, will default to 1000.

**Signature:**  

    maxConcurrentDispatches?: number | Expression<number> | ResetValue;

## tasks.RateLimits.maxDispatchesPerSecond

The maximum number of requests that can be invoked per second. If left unspecified, will default to 500.

**Signature:**  

    maxDispatchesPerSecond?: number | Expression<number> | ResetValue;