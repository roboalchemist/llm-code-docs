# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.md.txt

# firebase-admin.functions package

Firebase Functions service.

## Functions

|                                                          Function                                                           |                                                                                                                                                                                Description                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getFunctions(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.md#getfunctions_8a40afc) | Gets the [Functions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.functions.md#functions_class) service for the default app or a given app.`getFunctions()` can be called with no arguments to access the default app's `Functions` service or as `getFunctions(app)` to access the `Functions` service associated with a specific app. |

## Classes

|                                                          Class                                                           |                 Description                 |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| [Functions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.functions.md#functions_class) | The Firebase `Functions` service interface. |
| [TaskQueue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskqueue.md#taskqueue_class) | The `TaskQueue` interface.                  |

## Interfaces

|                                                                               Interface                                                                                |                         Description                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [AbsoluteDelivery](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.absolutedelivery.md#absolutedelivery_interface)                      | Interface representing task options with absolute delivery. |
| [DelayDelivery](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.delaydelivery.md#delaydelivery_interface)                               | Interface representing task options with delayed delivery.  |
| [TaskOptionsExperimental](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.taskoptionsexperimental.md#taskoptionsexperimental_interface) | Type representing experimental (beta) task options.         |

## Type Aliases

|                                                       Type Alias                                                       |                                                                                                                                                                                       Description                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DeliverySchedule](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.md#deliveryschedule) | Type representing delivery schedule options. `DeliverySchedule` is a union type of [DelayDelivery](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.delaydelivery.md#delaydelivery_interface) and [AbsoluteDelivery](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.absolutedelivery.md#absolutedelivery_interface) types. |
| [TaskOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.md#taskoptions)           | Type representing task options.                                                                                                                                                                                                                                                                                                                                                          |

## getFunctions(app)

Gets the [Functions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.functions.md#functions_class) service for the default app or a given app.

`getFunctions()` can be called with no arguments to access the default app's `Functions` service or as `getFunctions(app)` to access the `Functions` service associated with a specific app.

**Signature:**  

    export declare function getFunctions(app?: App): Functions;

### Parameters

| Parameter | Type |                                                       Description                                                       |
|-----------|------|-------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app for which to return the `Functions` service. If not provided, the default `Functions` service is returned. |

**Returns:**

[Functions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.functions.md#functions_class)

The default `Functions` service if no app is provided, or the `Functions` service associated with the provided app.

### Example 1

    // Get the `Functions` service for the default app
    const defaultFunctions = getFunctions();

### Example 2

    // Get the `Functions` service for a given app
    const otherFunctions = getFunctions(otherApp);

## DeliverySchedule

Type representing delivery schedule options. `DeliverySchedule` is a union type of [DelayDelivery](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.delaydelivery.md#delaydelivery_interface) and [AbsoluteDelivery](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.absolutedelivery.md#absolutedelivery_interface) types.

**Signature:**  

    export type DeliverySchedule = DelayDelivery | AbsoluteDelivery;

## TaskOptions

Type representing task options.

**Signature:**  

    export type TaskOptions = DeliverySchedule & TaskOptionsExperimental & {
        dispatchDeadlineSeconds?: number;
        id?: string;
        headers?: Record<string, string>;
    };