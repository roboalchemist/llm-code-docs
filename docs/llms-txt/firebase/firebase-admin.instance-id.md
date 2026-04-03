# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.md.txt

# firebase-admin.instance-id package

Firebase Instance ID service.

## Functions

|                                                            Function                                                             |                                                                                                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getInstanceId(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.md#getinstanceid_8a40afc) | Gets the [InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceid_class) service for the default app or a given app.This API is deprecated. Developers are advised to use the [getInstallations()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.md#getinstallations_8a40afc) API to delete their instance IDs and Firebase installation IDs.`getInstanceId()` can be called with no arguments to access the default app's `InstanceId` service or as `getInstanceId(app)` to access the `InstanceId` service associated with a specific app. |

## Classes

|                                                                                   Class                                                                                    |                                                    Description                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [FirebaseInstanceIdError](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.firebaseinstanceiderror.md#firebaseinstanceiderror_class)       | Firebase instance ID error code structure. This extends FirebaseError.                                             |
| [InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceid_class)                                              | The `InstanceId` service enables deleting the Firebase instance IDs associated with Firebase client app instances. |
| [InstanceIdClientErrorCode](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceidclienterrorcode.md#instanceidclienterrorcode_class) |                                                                                                                    |

## getInstanceId(app)

> | **Warning:** This API is now obsolete.
>
> Use [getInstallations()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.md#getinstallations_8a40afc) instead.

Gets the [InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceid_class) service for the default app or a given app.

This API is deprecated. Developers are advised to use the [getInstallations()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.md#getinstallations_8a40afc) API to delete their instance IDs and Firebase installation IDs.

`getInstanceId()` can be called with no arguments to access the default app's `InstanceId` service or as `getInstanceId(app)` to access the `InstanceId` service associated with a specific app.

**Signature:**  

    export declare function getInstanceId(app?: App): InstanceId;

### Parameters

| Parameter | Type |                                                      Description                                                       |
|-----------|------|------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app whose `InstanceId` service to return. If not provided, the default `InstanceId` service will be returned. |

**Returns:**

[InstanceId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceid_class)

The default `InstanceId` service if no app is provided or the `InstanceId` service associated with the provided app.

### Example 1

    // Get the Instance ID service for the default app
    const defaultInstanceId = getInstanceId();

### Example 2

    // Get the Instance ID service for a given app
    const otherInstanceId = getInstanceId(otherApp);

This API is deprecated. Developers are advised to use the `admin.installations()` API to delete their instance IDs and Firebase installation IDs.