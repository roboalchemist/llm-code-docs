# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue.md.txt

# TaskQueue class

The `TaskQueue` interface.

**Signature:**  

    export declare class TaskQueue<Args = Record<string, any>> 

## Methods

|                                                               Method                                                                | Modifiers |                                                                              Description                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [delete(id)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue.md#taskqueuedelete)           |           | Deletes an enqueued task if it has not yet completed.                                                                                                                  |
| [enqueue(data, opts)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue.md#taskqueueenqueue) |           | Creates a task and adds it to the queue. Tasks cannot be updated after creation. This action requires `cloudtasks.tasks.create` IAM permission on the service account. |

## TaskQueue.delete()

Deletes an enqueued task if it has not yet completed.

**Signature:**  

    delete(id: string): Promise<void>;

### Parameters

| Parameter |  Type  |                 Description                 |
|-----------|--------|---------------------------------------------|
| id        | string | the ID of the task, relative to this queue. |

**Returns:**

Promise\<void\>

A promise that resolves when the task has been deleted.

## TaskQueue.enqueue()

Creates a task and adds it to the queue. Tasks cannot be updated after creation. This action requires `cloudtasks.tasks.create` IAM permission on the service account.

**Signature:**  

    enqueue(data: Args, opts?: TaskOptions): Promise<void>;

### Parameters

| Parameter |                                                     Type                                                     |                 Description                 |
|-----------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| data      | Args                                                                                                         | The data payload of the task.               |
| opts      | [TaskOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.md#taskoptions) | Optional options when enqueuing a new task. |

**Returns:**

Promise\<void\>

A promise that resolves when the task has successfully been added to the queue.