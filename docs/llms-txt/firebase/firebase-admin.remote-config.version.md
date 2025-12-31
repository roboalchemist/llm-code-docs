# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md.txt

# Version interface

Interface representing a Remote Config template version. Output only, except for the version description. Contains metadata about a particular version of the Remote Config template. All fields are set at the time the specified Remote Config template is published. A version's description field may be specified in `publishTemplate` calls.

**Signature:**  

    export interface Version 

## Properties

|                                                               Property                                                                |                                                                         Type                                                                          |                                                                            Description                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versiondescription)       | string                                                                                                                                                | The user-provided description of the corresponding Remote Config template.                                                                                        |
| [isLegacy](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versionislegacy)             | boolean                                                                                                                                               | Indicates whether this Remote Config template was published before version history was supported.                                                                 |
| [rollbackSource](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versionrollbacksource) | string                                                                                                                                                | The version number of the Remote Config template that has become the current version due to a rollback. Only present if this version is the result of a rollback. |
| [updateOrigin](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versionupdateorigin)     | ('REMOTE_CONFIG_UPDATE_ORIGIN_UNSPECIFIED' \| 'CONSOLE' \| 'REST_API' \| 'ADMIN_SDK_NODE')                                                            | The origin of the template update action.                                                                                                                         |
| [updateTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versionupdatetime)         | string                                                                                                                                                | The timestamp of when this version of the Remote Config template was written to the Remote Config backend.                                                        |
| [updateType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versionupdatetype)         | ('REMOTE_CONFIG_UPDATE_TYPE_UNSPECIFIED' \| 'INCREMENTAL_UPDATE' \| 'FORCED_UPDATE' \| 'ROLLBACK')                                                    | The type of the template update action.                                                                                                                           |
| [updateUser](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versionupdateuser)         | [RemoteConfigUser](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfiguser.md#remoteconfiguser_interface) | Aggregation of all metadata fields about the account that performed the update.                                                                                   |
| [versionNumber](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#versionversionnumber)   | string                                                                                                                                                | The version number of a Remote Config template.                                                                                                                   |

## Version.description

The user-provided description of the corresponding Remote Config template.

**Signature:**  

    description?: string;

## Version.isLegacy

Indicates whether this Remote Config template was published before version history was supported.

**Signature:**  

    isLegacy?: boolean;

## Version.rollbackSource

The version number of the Remote Config template that has become the current version due to a rollback. Only present if this version is the result of a rollback.

**Signature:**  

    rollbackSource?: string;

## Version.updateOrigin

The origin of the template update action.

**Signature:**  

    updateOrigin?: ('REMOTE_CONFIG_UPDATE_ORIGIN_UNSPECIFIED' | 'CONSOLE' | 'REST_API' | 'ADMIN_SDK_NODE');

## Version.updateTime

The timestamp of when this version of the Remote Config template was written to the Remote Config backend.

**Signature:**  

    updateTime?: string;

## Version.updateType

The type of the template update action.

**Signature:**  

    updateType?: ('REMOTE_CONFIG_UPDATE_TYPE_UNSPECIFIED' | 'INCREMENTAL_UPDATE' | 'FORCED_UPDATE' | 'ROLLBACK');

## Version.updateUser

Aggregation of all metadata fields about the account that performed the update.

**Signature:**  

    updateUser?: RemoteConfigUser;

## Version.versionNumber

The version number of a Remote Config template.

**Signature:**  

    versionNumber?: string;