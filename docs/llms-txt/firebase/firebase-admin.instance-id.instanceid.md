# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md.txt

# InstanceId class

> | **Warning:** This API is now obsolete.
>
> Use [Installations](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installations_class) instead.

The `InstanceId` service enables deleting the Firebase instance IDs associated with Firebase client app instances.

**Signature:**  

    export declare class InstanceId 

## Properties

|                                                      Property                                                       | Modifiers | Type |                        Description                        |
|---------------------------------------------------------------------------------------------------------------------|-----------|------|-----------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceidapp) |           | App  | Returns the app associated with this InstanceId instance. |

## Methods

|                                                                          Method                                                                           | Modifiers |                                                                                                                                                                                         Description                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [deleteInstanceId(instanceId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.instance-id.instanceid.md#instanceiddeleteinstanceid) |           | Deletes the specified instance ID and the associated data from Firebase.Note that Google Analytics for Firebase uses its own form of Instance ID to keep track of analytics data. Therefore deleting a Firebase Instance ID does not delete Analytics data. See [Delete an Instance ID](https://firebase.google.com/support/privacy/manage-iids#delete_an_instance_id) for more information. |

## InstanceId.app

Returns the app associated with this InstanceId instance.

**Signature:**  

    get app(): App;

## InstanceId.deleteInstanceId()

Deletes the specified instance ID and the associated data from Firebase.

Note that Google Analytics for Firebase uses its own form of Instance ID to keep track of analytics data. Therefore deleting a Firebase Instance ID does not delete Analytics data. See [Delete an Instance ID](https://firebase.google.com/support/privacy/manage-iids#delete_an_instance_id) for more information.

**Signature:**  

    deleteInstanceId(instanceId: string): Promise<void>;

### Parameters

| Parameter  |  Type  |          Description           |
|------------|--------|--------------------------------|
| instanceId | string | The instance ID to be deleted. |

**Returns:**

Promise\<void\>

A promise fulfilled when the instance ID is deleted.