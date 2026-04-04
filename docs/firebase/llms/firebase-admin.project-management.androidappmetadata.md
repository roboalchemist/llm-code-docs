# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidappmetadata.md.txt

# AndroidAppMetadata interface

Metadata about a Firebase Android App.

**Signature:**  

    export interface AndroidAppMetadata extends AppMetadata 

**Extends:** [AppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadata_interface)

## Properties

|                                                                          Property                                                                          |                                                                      Type                                                                       |                                             Description                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [packageName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidappmetadata.md#androidappmetadatapackagename) | string                                                                                                                                          | The canonical package name of the Android App, as would appear in the Google Play Developer Console. |
| [platform](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.androidappmetadata.md#androidappmetadataplatform)       | [AppPlatform.ANDROID](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.md#appplatformandroid_enummember) |                                                                                                      |

## AndroidAppMetadata.packageName

The canonical package name of the Android App, as would appear in the Google Play Developer Console.

**Signature:**  

    packageName: string;

### Example

    var packageName = androidAppMetadata.packageName;

## AndroidAppMetadata.platform

**Signature:**  

    platform: AppPlatform.ANDROID;