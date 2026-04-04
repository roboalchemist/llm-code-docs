# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md.txt

# AndroidApp class

A reference to a Firebase Android app.

Do not call this constructor directly. Instead, use [ProjectManagement.androidApp()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementandroidapp).

**Signature:**  

    export declare class AndroidApp 

## Properties

|                                                            Property                                                            | Modifiers |  Type  | Description |
|--------------------------------------------------------------------------------------------------------------------------------|-----------|--------|-------------|
| [appId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidappappid) |           | string |             |

## Methods

|                                                                                      Method                                                                                       | Modifiers |                                   Description                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------|
| [addShaCertificate(certificateToAdd)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidappaddshacertificate)          |           | Adds the given SHA certificate to this Android app.                             |
| [deleteShaCertificate(certificateToDelete)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidappdeleteshacertificate) |           | Deletes the specified SHA certificate from this Android app.                    |
| [getConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidappgetconfig)                                          |           | Gets the configuration artifact associated with this app.                       |
| [getMetadata()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidappgetmetadata)                                      |           | Retrieves metadata about this Android app.                                      |
| [getShaCertificates()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidappgetshacertificates)                        |           | Gets the list of SHA certificates associated with this Android app in Firebase. |
| [setDisplayName(newDisplayName)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidappsetdisplayname)                  |           | Sets the optional user-assigned display name of the app.                        |

## AndroidApp.appId

**Signature:**  

    readonly appId: string;

## AndroidApp.addShaCertificate()

Adds the given SHA certificate to this Android app.

**Signature:**  

    addShaCertificate(certificateToAdd: ShaCertificate): Promise<void>;

### Parameters

|    Parameter     |                                                                       Type                                                                       |         Description         |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| certificateToAdd | [ShaCertificate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificate_class) | The SHA certificate to add. |

**Returns:**

Promise\<void\>

A promise that resolves when the given certificate has been added to the Android app.

## AndroidApp.deleteShaCertificate()

Deletes the specified SHA certificate from this Android app.

**Signature:**  

    deleteShaCertificate(certificateToDelete: ShaCertificate): Promise<void>;

### Parameters

|      Parameter      |                                                                       Type                                                                       |          Description           |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| certificateToDelete | [ShaCertificate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificate_class) | The SHA certificate to delete. |

**Returns:**

Promise\<void\>

A promise that resolves when the specified certificate has been removed from the Android app.

## AndroidApp.getConfig()

Gets the configuration artifact associated with this app.

**Signature:**  

    getConfig(): Promise<string>;

**Returns:**

Promise\<string\>

A promise that resolves to the Android app's Firebase config file, in UTF-8 string format. This string is typically intended to be written to a JSON file that gets shipped with your Android app.

## AndroidApp.getMetadata()

Retrieves metadata about this Android app.

**Signature:**  

    getMetadata(): Promise<AndroidAppMetadata>;

**Returns:**

Promise\<[AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidappmetadata.md#androidappmetadata_interface)\>

A promise that resolves to the retrieved metadata about this Android app.

## AndroidApp.getShaCertificates()

Gets the list of SHA certificates associated with this Android app in Firebase.

**Signature:**  

    getShaCertificates(): Promise<ShaCertificate[]>;

**Returns:**

Promise\<[ShaCertificate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificate_class)\[\]\>

The list of SHA-1 and SHA-256 certificates associated with this Android app in Firebase.

## AndroidApp.setDisplayName()

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