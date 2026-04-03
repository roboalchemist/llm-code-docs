# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosappmetadata.md.txt

# IosAppMetadata interface

Metadata about a Firebase iOS App.

**Signature:**  

    export interface IosAppMetadata extends AppMetadata 

**Extends:** [AppMetadata](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.appmetadata.md#appmetadata_interface)

## Properties

|                                                                   Property                                                                   |                                                                  Type                                                                   |                                   Description                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [bundleId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosappmetadata.md#iosappmetadatabundleid) | string                                                                                                                                  | The canonical bundle ID of the iOS App as it would appear in the iOS App Store. |
| [platform](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.iosappmetadata.md#iosappmetadataplatform) | [AppPlatform.IOS](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.md#appplatformios_enummember) |                                                                                 |

## IosAppMetadata.bundleId

The canonical bundle ID of the iOS App as it would appear in the iOS App Store.

**Signature:**  

    bundleId: string;

### Example

    var bundleId = iosAppMetadata.bundleId;

## IosAppMetadata.platform

**Signature:**  

    platform: AppPlatform.IOS;