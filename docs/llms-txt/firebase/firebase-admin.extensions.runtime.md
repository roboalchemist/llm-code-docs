# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md.txt

# Runtime class

Runtime provides methods to modify an extension instance's runtime data.

**Signature:**  

    export declare class Runtime 

## Methods

|                                                                              Method                                                                              | Modifiers |                          Description                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------|
| [setFatalError(errorMessage)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md#runtimesetfatalerror)                   |           | Reports a fatal error while running a lifecycle event handler. |
| [setProcessingState(state, detailMessage)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md#runtimesetprocessingstate) |           | Sets the processing state of an extension instance.            |

## Runtime.setFatalError()

Reports a fatal error while running a lifecycle event handler.

Call this method when a lifecycle event handler fails in a way that makes the Instance inoperable. If the lifecycle event failed but the instance will still work as expected, call `setProcessingState` with the "PROCESSING_WARNING" or "PROCESSING_FAILED" state instead.

**Signature:**  

    setFatalError(errorMessage: string): Promise<void>;

### Parameters

|  Parameter   |  Type  |                       Description                       |
|--------------|--------|---------------------------------------------------------|
| errorMessage | string | A message explaining what went wrong and how to fix it. |

**Returns:**

Promise\<void\>

## Runtime.setProcessingState()

Sets the processing state of an extension instance.

Use this method to report the results of a lifecycle event handler.

If the lifecycle event failed \& the extension instance will no longer work correctly, use [Runtime.setFatalError()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md#runtimesetfatalerror) instead.

To report the status of function calls other than lifecycle event handlers, use `console.log` or the Cloud Functions logger SDK.

**Signature:**  

    setProcessingState(state: SettableProcessingState, detailMessage: string): Promise<void>;

### Parameters

|   Parameter   |                                                                 Type                                                                  |                         Description                         |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| state         | [SettableProcessingState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.md#settableprocessingstate) | The state to set the instance to.                           |
| detailMessage | string                                                                                                                                | A message explaining the results of the lifecycle function. |

**Returns:**

Promise\<void\>