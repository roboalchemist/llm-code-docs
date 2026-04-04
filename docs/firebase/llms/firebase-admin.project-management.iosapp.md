# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md.txt

# IosApp class

A reference to a Firebase iOS app.

Do not call this constructor directly. Instead, use [ProjectManagement.iosApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementiosapp).

**Signature:**  

    export declare class IosApp 

## Properties

|                                                        Property                                                        | Modifiers |  Type  | Description |
|------------------------------------------------------------------------------------------------------------------------|-----------|--------|-------------|
| [appId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosappappid) |           | string |             |

## Methods

|                                                                          Method                                                                          | Modifiers |                        Description                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------|
| [getConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosappgetconfig)                         |           | Gets the configuration artifact associated with this app. |
| [getMetadata()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosappgetmetadata)                     |           | Retrieves metadata about this iOS app.                    |
| [setDisplayName(newDisplayName)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosappsetdisplayname) |           | Sets the optional user-assigned display name of the app.  |

## IosApp.appId

**Signature:**  

    readonly appId: string;

## IosApp.getConfig()

Gets the configuration artifact associated with this app.

**Signature:**  

    getConfig(): Promise<string>;

**Returns:**

Promise\<string\>

A promise that resolves to the iOS app's Firebase config file, in UTF-8 string format. This string is typically intended to be written to a plist file that gets shipped with your iOS app.

## IosApp.getMetadata()

Retrieves metadata about this iOS app.

**Signature:**  

    getMetadata(): Promise<IosAppMetadata>;

**Returns:**

Promise\<[IosAppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosappmetadata.md#iosappmetadata_interface)\>

A promise that resolves to the retrieved metadata about this iOS app.

## IosApp.setDisplayName()

Sets the optional user-assigned display name of the app.

**Signature:**  

    setDisplayName(newDisplayName: string): Promise<void>;

### Parameters

|   Parameter    |  Type  |         Description          |
|----------------|--------|------------------------------|
| newDisplayName | string | The new display name to set. |

**Returns:**

Promise\<void\>

A promise that resolves when the display name has been set.