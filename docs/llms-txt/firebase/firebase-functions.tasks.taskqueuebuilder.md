# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuebuilder.md.txt

# tasks.TaskQueueBuilder class

Builder for creating a `TaskQueueFunction`.

**Signature:**  

    export declare class TaskQueueBuilder 

## Methods

|                                                                          Method                                                                          | Modifiers |                           Description                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------|
| [onDispatch(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuebuilder.md#taskstaskqueuebuilderondispatch) |           | Creates a handler for tasks sent to a Google Cloud Tasks queue. |

## tasks.TaskQueueBuilder.onDispatch()

Creates a handler for tasks sent to a Google Cloud Tasks queue.

**Signature:**  

    onDispatch(handler: (data: any, context: TaskContext) => void | Promise<void>): TaskQueueFunction;

### Parameters

| Parameter |                                                                                           Type                                                                                           |             Description             |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| handler   | (data: any, context: [TaskContext](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontext_interface)) =\> void \| Promise\<void\> | A callback to handle task requests. |

**Returns:**

[TaskQueueFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunction_interface)

A function you can export and deploy.