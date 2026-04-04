# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueuefunction.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueuefunction.md.txt

# tasks.TaskQueueFunction interface

A handler for tasks.

**Signature:**  

    export interface TaskQueueFunction<T = any> extends HttpsFunction 

**Extends:** [HttpsFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.md#httpshttpsfunction)

## Methods

|                                                                          Method                                                                           |                         Description                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [run(request)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueuefunction.md#taskstaskqueuefunctionrun) | The callback passed to the `TaskQueueFunction` constructor. |

## tasks.TaskQueueFunction.run()

The callback passed to the `TaskQueueFunction` constructor.

**Signature:**  

    run(request: Request<T>): void | Promise<void>;

### Parameters

| Parameter |     Type     |                     Description                     |
|-----------|--------------|-----------------------------------------------------|
| request   | Request\<T\> | A TaskRequest containing data and auth information. |

**Returns:**

void \| Promise\<void\>

Any return value. Google Cloud Functions will await any promise before shutting down your function. Resolved return values are only used for unit testing purposes.