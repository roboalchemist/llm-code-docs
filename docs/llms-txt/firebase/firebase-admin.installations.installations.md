# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md.txt

# Installations class

The `Installations` service for the current app.

**Signature:**  

    export declare class Installations 

## Properties

|                                                          Property                                                           | Modifiers | Type |                         Description                          |
|-----------------------------------------------------------------------------------------------------------------------------|-----------|------|--------------------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installationsapp) |           | App  | Returns the app associated with this Installations instance. |

## Methods

|                                                                             Method                                                                             | Modifiers |                                 Description                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------|
| [deleteInstallation(fid)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.installations.installations.md#installationsdeleteinstallation) |           | Deletes the specified installation ID and the associated data from Firebase. |

## Installations.app

Returns the app associated with this Installations instance.

**Signature:**  

    get app(): App;

## Installations.deleteInstallation()

Deletes the specified installation ID and the associated data from Firebase.

**Signature:**  

    deleteInstallation(fid: string): Promise<void>;

### Parameters

| Parameter |  Type  |                 Description                 |
|-----------|--------|---------------------------------------------|
| fid       | string | The Firebase installation ID to be deleted. |

**Returns:**

Promise\<void\>

A promise fulfilled when the installation ID is deleted.