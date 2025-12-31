# Source: https://firebase.google.com/docs/reference/js/firestore_.loadbundletask.md.txt

# LoadBundleTask class

Represents the task of loading a Firestore bundle. It provides progress of bundle loading, as well as task completion and error events.

The API is compatible with `Promise<LoadBundleTaskProgress>`.

**Signature:**  

    export declare class LoadBundleTask implements PromiseLike<LoadBundleTaskProgress> 

**Implements:** PromiseLike\<[LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogress_interface)\>

## Methods

|                                                                  Method                                                                  | Modifiers |                            Description                            |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------|
| [catch(onRejected)](https://firebase.google.com/docs/reference/js/firestore_.loadbundletask.md#loadbundletaskcatch)                      |           | Implements the `Promise<LoadBundleTaskProgress>.catch` interface. |
| [onProgress(next, error, complete)](https://firebase.google.com/docs/reference/js/firestore_.loadbundletask.md#loadbundletaskonprogress) |           | Registers functions to listen to bundle loading progress events.  |
| [then(onFulfilled, onRejected)](https://firebase.google.com/docs/reference/js/firestore_.loadbundletask.md#loadbundletaskthen)           |           | Implements the `Promise<LoadBundleTaskProgress>.then` interface.  |

## LoadBundleTask.catch()

Implements the `Promise<LoadBundleTaskProgress>.catch` interface.

**Signature:**  

    catch<R>(onRejected: (a: Error) => R | PromiseLike<R>): Promise<R | LoadBundleTaskProgress>;

#### Parameters

| Parameter  |                 Type                 |                    Description                     |
|------------|--------------------------------------|----------------------------------------------------|
| onRejected | (a: Error) =\> R \| PromiseLike\<R\> | Called when an error occurs during bundle loading. |

**Returns:**

Promise\<R \| [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogress_interface)\>

## LoadBundleTask.onProgress()

Registers functions to listen to bundle loading progress events.

**Signature:**  

    onProgress(next?: (progress: LoadBundleTaskProgress) => unknown, error?: (err: Error) => unknown, complete?: () => void): void;

#### Parameters

| Parameter |                                                                                 Type                                                                                  |                                                                    Description                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| next      | (progress: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogress_interface)) =\> unknown | Called when there is a progress update from bundle loading. Typically `next` calls occur each time a Firestore document is loaded from the bundle. |
| error     | (err: Error) =\> unknown                                                                                                                                              | Called when an error occurs during bundle loading. The task aborts after reporting the error, and there should be no more updates after this.      |
| complete  | () =\> void                                                                                                                                                           | Called when the loading task is complete.                                                                                                          |

**Returns:**

void

## LoadBundleTask.then()

Implements the `Promise<LoadBundleTaskProgress>.then` interface.

**Signature:**  

    then<T, R>(onFulfilled?: (a: LoadBundleTaskProgress) => T | PromiseLike<T>, onRejected?: (a: Error) => R | PromiseLike<R>): Promise<T | R>;

#### Parameters

|  Parameter  |                                                                                     Type                                                                                     |                                                                        Description                                                                         |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| onFulfilled | (a: [LoadBundleTaskProgress](https://firebase.google.com/docs/reference/js/firestore_.loadbundletaskprogress.md#loadbundletaskprogress_interface)) =\> T \| PromiseLike\<T\> | Called on the completion of the loading task with a final `LoadBundleTaskProgress` update. The update will always have its `taskState` set to `"Success"`. |
| onRejected  | (a: Error) =\> R \| PromiseLike\<R\>                                                                                                                                         | Called when an error occurs during bundle loading.                                                                                                         |

**Returns:**

Promise\<T \| R\>