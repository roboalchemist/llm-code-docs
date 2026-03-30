# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.md.txt

# tasks namespace

## Functions

| Function | Description |
|---|---|
| [taskQueue(options)](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.md#taskstaskqueue) | Declares a function that can handle tasks enqueued using the Firebase Admin SDK. |

## Classes

| Class | Description |
|---|---|
| [TaskQueueBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuebuilder.md#taskstaskqueuebuilder_class) | Builder for creating a `TaskQueueFunction`. |

## Interfaces

| Interface | Description |
|---|---|
| [RateLimits](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.ratelimits.md#tasksratelimits_interface) | How congestion control should be applied to the function. |
| [RetryConfig](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.retryconfig.md#tasksretryconfig_interface) | How a task should be retried in the event of a non-2xx return. |
| [TaskContext](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontext_interface) | Metadata about a call to a Task Queue function. |
| [TaskQueueFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction_interface) | A handler for tasks. |
| [TaskQueueOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptions_interface) | Options for configuring the task queue to listen to. |

## tasks.taskQueue()

Declares a function that can handle tasks enqueued using the Firebase Admin SDK.

**Signature:**

    export declare function taskQueue(options?: TaskQueueOptions): TaskQueueBuilder;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [TaskQueueOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptions_interface) | Configuration for the Task Queue that feeds into this function. Omitting options will configure a Task Queue with default settings. |

**Returns:**

[TaskQueueBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuebuilder.md#taskstaskqueuebuilder_class)