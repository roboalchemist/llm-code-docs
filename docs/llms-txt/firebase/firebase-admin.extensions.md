# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.md.txt

# firebase-admin.extensions package

Firebase Extensions service.

## Functions

|                                                            Function                                                            |                                                                                                                                                                                    Description                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getExtensions(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.md#getextensions_8a40afc) | Gets the [Extensions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.extensions.md#extensions_class) service for the default app or a given app.`getExtensions()` can be called with no arguments to access the default app's `Extensions` service or as `getExtensions(app)` to access the `Extensions` service associated with a specific app. |

## Classes

|                                                            Class                                                             |                               Description                                |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [Extensions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.extensions.md#extensions_class) | The Firebase `Extensions` service interface.                             |
| [Runtime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md#runtime_class)          | Runtime provides methods to modify an extension instance's runtime data. |

## Type Aliases

|                                                              Type Alias                                                               |                                                       Description                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [SettableProcessingState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.md#settableprocessingstate) | `SettableProcessingState` represents all the processing states that can be set on an Extension instance's runtime data. |

## getExtensions(app)

Gets the [Extensions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.extensions.md#extensions_class) service for the default app or a given app.

`getExtensions()` can be called with no arguments to access the default app's `Extensions` service or as `getExtensions(app)` to access the `Extensions` service associated with a specific app.

**Signature:**  

    export declare function getExtensions(app?: App): Extensions;

### Parameters

| Parameter | Type |                                                        Description                                                        |
|-----------|------|---------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app for which to return the `Extensions` service. If not provided, the default `Extensions` service is returned. |

**Returns:**

[Extensions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.extensions.md#extensions_class)

The default `Extensions` service if no app is provided, or the `Extensions` service associated with the provided app.

### Example 1

    // Get the `Extensions` service for the default app
    const defaultExtensions = getExtensions();

### Example 2

    // Get the `Extensions` service for a given app
    const otherExtensions = getExtensions(otherApp);

## SettableProcessingState

`SettableProcessingState` represents all the processing states that can be set on an Extension instance's runtime data.

You can set the following states:

- `NONE`: No relevant lifecycle event work has been done. Set this to clear out old statuses.

- `PROCESSING_COMPLETE`: Lifecycle event work completed with no errors.

- `PROCESSING_WARNING`: Lifecycle event work succeeded partially, or something happened that the user should be warned about.

- `PROCESSING_FAILED`: Lifecycle event work failed completely, but the instance will still work correctly going forward.

If the extension instance is in a broken state due to errors, instead call [Runtime.setFatalError()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.extensions.runtime.md#runtimesetfatalerror).

The "processing" state gets set automatically when a lifecycle event handler starts; you can't set it explicitly. To report the ongoing status of an extension's function, use `console.log` or the Cloud Functions logger SDK.

**Signature:**  

    export type SettableProcessingState = 'NONE' | 'PROCESSING_COMPLETE' | 'PROCESSING_WARNING' | 'PROCESSING_FAILED';