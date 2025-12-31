# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.functions.md.txt

# Functions class

The Firebase `Functions` service interface.

**Signature:**  

    export declare class Functions 

## Properties

|                                                    Property                                                     | Modifiers | Type | Description |
|-----------------------------------------------------------------------------------------------------------------|-----------|------|-------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.functions.md#functionsapp) |           | App  |             |

## Methods

|                                                                         Method                                                                         | Modifiers |                                                                                                                                                                                                                                                                                                       Description                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [taskQueue(functionName, extensionId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.functions.md#functionstaskqueue) |           | Creates a reference to a [TaskQueue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue.md#taskqueue_class) for a given function name. The function name can be either:1) A fully qualified function resource name: `projects/{project}/locations/{location}/functions/{functionName}`2) A partial resource name with location and function name, in which case the runtime project ID is used: `locations/{location}/functions/{functionName}`3) A partial function name, in which case the runtime project ID and the default location, `us-central1`, is used: `{functionName}` |

## Functions.app

**Signature:**  

    readonly app: App;

## Functions.taskQueue()

Creates a reference to a [TaskQueue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue.md#taskqueue_class) for a given function name. The function name can be either:

1) A fully qualified function resource name: `projects/{project}/locations/{location}/functions/{functionName}`

2) A partial resource name with location and function name, in which case the runtime project ID is used: `locations/{location}/functions/{functionName}`

3) A partial function name, in which case the runtime project ID and the default location, `us-central1`, is used: `{functionName}`

**Signature:**  

    taskQueue<Args = Record<string, any>>(functionName: string, extensionId?: string): TaskQueue<Args>;

### Parameters

|  Parameter   |  Type  |           Description           |
|--------------|--------|---------------------------------|
| functionName | string | The name of the function.       |
| extensionId  | string | Optional Firebase extension ID. |

**Returns:**

[TaskQueue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue.md#taskqueue_class)\<Args\>

A promise that fulfills with a `TaskQueue`.