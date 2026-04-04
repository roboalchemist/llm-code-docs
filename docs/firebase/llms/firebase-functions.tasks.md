# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.md.txt

# tasks namespace

## Functions

|                                                                         Function                                                                          |                           Description                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [onTaskDispatched(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.md#tasksontaskdispatched)          | Creates a handler for tasks sent to a Google Cloud Tasks queue. |
| [onTaskDispatched(options, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.md#tasksontaskdispatched) | Creates a handler for tasks sent to a Google Cloud Tasks queue. |

## Interfaces

|                                                                               Interface                                                                               |                          Description                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [AuthData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.authdata.md#tasksauthdata_interface)                            | Metadata about the authorization used to invoke a function.    |
| [RateLimits](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.ratelimits.md#tasksratelimits_interface)                      | How congestion control should be applied to the function.      |
| [RetryConfig](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md#tasksretryconfig_interface)                   | How a task should be retried in the event of a non-2xx return. |
| [TaskQueueFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction_interface) | A handler for tasks.                                           |
| [TaskQueueOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptions_interface)    |                                                                |

## Type Aliases

|                                                      Type Alias                                                       |                   Description                   |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [Request](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.md#tasksrequest) | The request used to call a task queue function. |

## tasks.onTaskDispatched()

Creates a handler for tasks sent to a Google Cloud Tasks queue.

**Signature:**  

    export declare function onTaskDispatched<Args = any>(handler: (request: Request<Args>) => void | Promise<void>): TaskQueueFunction<Args>;

### Parameters

| Parameter |                          Type                          |             Description             |
|-----------|--------------------------------------------------------|-------------------------------------|
| handler   | (request: Request\<Args\>) =\> void \| Promise\<void\> | A callback to handle task requests. |

**Returns:**

[TaskQueueFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction_interface)\<Args\>

A function you can export and deploy.

## tasks.onTaskDispatched()

Creates a handler for tasks sent to a Google Cloud Tasks queue.

**Signature:**  

    export declare function onTaskDispatched<Args = any>(options: TaskQueueOptions, handler: (request: Request<Args>) => void | Promise<void>): TaskQueueFunction<Args>;

### Parameters

| Parameter |                                                                                Type                                                                                |                     Description                     |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| options   | [TaskQueueOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptions_interface) | Configuration for the task queue or Cloud Function. |
| handler   | (request: Request\<Args\>) =\> void \| Promise\<void\>                                                                                                             | A callback to handle task requests.                 |

**Returns:**

[TaskQueueFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction_interface)\<Args\>

A function you can export and deploy.

## tasks.Request

The request used to call a task queue function.

**Signature:**  

    export type Request<T = any> = TaskContext & {
        data: T;
    };