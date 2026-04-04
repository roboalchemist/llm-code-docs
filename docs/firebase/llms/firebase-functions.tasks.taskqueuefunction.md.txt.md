# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md.txt

# tasks.TaskQueueFunction interface

A handler for tasks.

**Signature:**

    export interface TaskQueueFunction 

## Properties

| Property | Type | Description |
|---|---|---|
| [__endpoint](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction__endpoint) | ManifestEndpoint |   |
| [__requiredAPIs](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction__requiredapis) | ManifestRequiredAPI\[\] |   |
| [__trigger](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction__trigger) | unknown |   |

## Methods

| Method | Description |
|---|---|
| [run(data, context)](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunctionrun) | The callback passed to the `TaskQueueFunction` constructor. |

## tasks.TaskQueueFunction.__endpoint

**Signature:**

    __endpoint: ManifestEndpoint;

## tasks.TaskQueueFunction.__requiredAPIs

**Signature:**

    __requiredAPIs?: ManifestRequiredAPI[];

## tasks.TaskQueueFunction.__trigger

**Signature:**

    __trigger: unknown;

## tasks.TaskQueueFunction.run()

The callback passed to the `TaskQueueFunction` constructor.

**Signature:**

    run(data: any, context: TaskContext): void | Promise<void>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| data | any | The body enqueued into a task queue. |
| context | [TaskContext](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontext_interface) | The request context of the enqueued task |

**Returns:**

void \| Promise\<void\>

Any return value. Google Cloud Functions will await any promise before shutting down your function. Resolved return values are only used for unit testing purposes.