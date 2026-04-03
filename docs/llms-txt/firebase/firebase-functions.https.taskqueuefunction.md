# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskqueuefunction.md.txt

**Signature:**

<br />

    export interface TaskQueueFunction<T = any> extends HttpsFunction 

**Extends:**HttpsFunction

## Methods

|                                                                         Method                                                                         | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [run(data)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.taskqueuefunction.md#httpstaskqueuefunctionrun) |             |

## https.TaskQueueFunction.run()

**Signature:**  

    run(data: TaskRequest<T>): void | Promise<void>;

### Parameters

| Parameter |       Type       | Description |
|-----------|------------------|-------------|
| data      | TaskRequest\<T\> |             |

**Returns:**

void \| Promise\<void\>