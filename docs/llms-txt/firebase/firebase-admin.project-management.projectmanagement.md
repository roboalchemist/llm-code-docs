# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md.txt

# ProjectManagement class

The Firebase ProjectManagement service interface.

**Signature:**  

    export declare class ProjectManagement 

## Properties

|                                                                 Property                                                                 | Modifiers | Type | Description |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------|------|-------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementapp) |           | App  |             |

## Methods

|                                                                                            Method                                                                                            | Modifiers |                                                               Description                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [androidApp(appId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementandroidapp)                                |           | Creates an `AndroidApp` object, referencing the specified Android app within this Firebase project.This method does not perform an RPC. |
| [createAndroidApp(packageName, displayName)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementcreateandroidapp) |           | Creates a new Firebase Android app associated with this Firebase project.                                                               |
| [createIosApp(bundleId, displayName)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementcreateiosapp)            |           | Creates a new Firebase iOS app associated with this Firebase project.                                                                   |
| [iosApp(appId)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementiosapp)                                        |           | Creates an `iOSApp` object, referencing the specified iOS app within this Firebase project.This method does not perform an RPC.         |
| [listAndroidApps()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementlistandroidapps)                           |           | Lists up to 100 Firebase Android apps associated with this Firebase project.                                                            |
| [listAppMetadata()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementlistappmetadata)                           |           | Lists up to 100 Firebase apps associated with this Firebase project.                                                                    |
| [listIosApps()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementlistiosapps)                                   |           | Lists up to 100 Firebase iOS apps associated with this Firebase project.                                                                |
| [setDisplayName(newDisplayName)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementsetdisplayname)               |           | Update the display name of this Firebase project.                                                                                       |
| [shaCertificate(shaHash)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.projectmanagement.md#projectmanagementshacertificate)                      |           | Creates a `ShaCertificate` object.This method does not perform an RPC.                                                                  |

## ProjectManagement.app

**Signature:**  

    readonly app: App;

## ProjectManagement.androidApp()

Creates an `AndroidApp` object, referencing the specified Android app within this Firebase project.

This method does not perform an RPC.

**Signature:**  

    androidApp(appId: string): AndroidApp;

### Parameters

| Parameter |  Type  |                 Description                  |
|-----------|--------|----------------------------------------------|
| appId     | string | The `appId` of the Android app to reference. |

**Returns:**

[AndroidApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidapp_class)

An `AndroidApp` object that references the specified Firebase Android app.

## ProjectManagement.createAndroidApp()

Creates a new Firebase Android app associated with this Firebase project.

**Signature:**  

    createAndroidApp(packageName: string, displayName?: string): Promise<AndroidApp>;

### Parameters

|  Parameter  |  Type  |                                             Description                                              |
|-------------|--------|------------------------------------------------------------------------------------------------------|
| packageName | string | The canonical package name of the Android App, as would appear in the Google Play Developer Console. |
| displayName | string | An optional user-assigned display name for this new app.                                             |

**Returns:**

Promise\<[AndroidApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidapp_class)\>

A promise that resolves to the newly created Android app.

## ProjectManagement.createIosApp()

Creates a new Firebase iOS app associated with this Firebase project.

**Signature:**  

    createIosApp(bundleId: string, displayName?: string): Promise<IosApp>;

### Parameters

|  Parameter  |  Type  |                       Description                        |
|-------------|--------|----------------------------------------------------------|
| bundleId    | string | The iOS app bundle ID to use for this new app.           |
| displayName | string | An optional user-assigned display name for this new app. |

**Returns:**

Promise\<[IosApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosapp_class)\>

A promise that resolves to the newly created iOS app.

## ProjectManagement.iosApp()

Creates an `iOSApp` object, referencing the specified iOS app within this Firebase project.

This method does not perform an RPC.

**Signature:**  

    iosApp(appId: string): IosApp;

### Parameters

| Parameter |  Type  |               Description                |
|-----------|--------|------------------------------------------|
| appId     | string | The `appId` of the iOS app to reference. |

**Returns:**

[IosApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosapp_class)

An `iOSApp` object that references the specified Firebase iOS app.

## ProjectManagement.listAndroidApps()

Lists up to 100 Firebase Android apps associated with this Firebase project.

**Signature:**  

    listAndroidApps(): Promise<AndroidApp[]>;

**Returns:**

Promise\<[AndroidApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidapp.md#androidapp_class)\[\]\>

The list of Android apps.

## ProjectManagement.listAppMetadata()

Lists up to 100 Firebase apps associated with this Firebase project.

**Signature:**  

    listAppMetadata(): Promise<AppMetadata[]>;

**Returns:**

Promise\<[AppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadata_interface)\[\]\>

A promise that resolves to the metadata list of the apps.

## ProjectManagement.listIosApps()

Lists up to 100 Firebase iOS apps associated with this Firebase project.

**Signature:**  

    listIosApps(): Promise<IosApp[]>;

**Returns:**

Promise\<[IosApp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosapp.md#iosapp_class)\[\]\>

The list of iOS apps.

## ProjectManagement.setDisplayName()

Update the display name of this Firebase project.

**Signature:**  

    setDisplayName(newDisplayName: string): Promise<void>;

### Parameters

|   Parameter    |  Type  |             Description             |
|----------------|--------|-------------------------------------|
| newDisplayName | string | The new display name to be updated. |

**Returns:**

Promise\<void\>

A promise that resolves when the project display name has been updated.

## ProjectManagement.shaCertificate()

Creates a `ShaCertificate` object.

This method does not perform an RPC.

**Signature:**  

    shaCertificate(shaHash: string): ShaCertificate;

### Parameters

| Parameter |  Type  |                   Description                   |
|-----------|--------|-------------------------------------------------|
| shaHash   | string | The SHA-1 or SHA-256 hash for this certificate. |

**Returns:**

[ShaCertificate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificate_class)

A `ShaCertificate` object contains the specified SHA hash.