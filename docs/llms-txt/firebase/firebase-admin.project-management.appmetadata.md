# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md.txt

# AppMetadata interface

Metadata about a Firebase app.

**Signature:**  

    export interface AppMetadata 

## Properties

|                                                                    Property                                                                    |                                                         Type                                                          |                                                               Description                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [appId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadataappid)               | string                                                                                                                | The globally unique, Firebase-assigned identifier of the app.                                                                            |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadatadisplayname)   | string                                                                                                                | The optional user-assigned display name of the app.                                                                                      |
| [platform](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadataplatform)         | [AppPlatform](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.md#appplatform) | The development platform of the app. Supporting Android and iOS app platforms.                                                           |
| [projectId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadataprojectid)       | string                                                                                                                | The globally unique, user-assigned ID of the parent project for the app.                                                                 |
| [resourceName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadataresourcename) | string                                                                                                                | The fully-qualified resource name that identifies this app.This is useful when manually constructing requests for Firebase's public API. |

## AppMetadata.appId

The globally unique, Firebase-assigned identifier of the app.

**Signature:**  

    appId: string;

### Example

    var appId = appMetadata.appId;

## AppMetadata.displayName

The optional user-assigned display name of the app.

**Signature:**  

    displayName?: string;

### Example

    var displayName = appMetadata.displayName;

## AppMetadata.platform

The development platform of the app. Supporting Android and iOS app platforms.

**Signature:**  

    platform: AppPlatform;

### Example

    var platform = AppPlatform.ANDROID;

## AppMetadata.projectId

The globally unique, user-assigned ID of the parent project for the app.

**Signature:**  

    projectId: string;

### Example

    var projectId = appMetadata.projectId;

## AppMetadata.resourceName

The fully-qualified resource name that identifies this app.

This is useful when manually constructing requests for Firebase's public API.

**Signature:**  

    resourceName: string;

### Example

    var resourceName = androidAppMetadata.resourceName;