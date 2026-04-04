# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md.txt

# remoteConfig.TemplateVersion interface

An interface representing a Remote Config template version metadata object emitted when a project is updated.

**Signature:**  

    export interface TemplateVersion 

## Properties

|                                                                              Property                                                                               |                                                                                Type                                                                                 |                                                                                                         Description                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversiondescription)       | string                                                                                                                                                              | A description associated with this Remote Config template version.                                                                                                                                                           |
| [rollbackSource](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversionrollbacksource) | number                                                                                                                                                              | The version number of the Remote Config template that this update rolled back to. Only applies if this update was a rollback.                                                                                                |
| [updateOrigin](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversionupdateorigin)     | string                                                                                                                                                              | The origin of the caller - either the Firebase console or the Remote Config REST API. See \[`RemoteConfigUpdateOrigin`\](/docs/reference/remote-config/rest/v1/Version#remoteconfigupdateorigin) for valid values.           |
| [updateTime](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversionupdatetime)         | string                                                                                                                                                              | When the template was updated in format (ISO8601 timestamp).                                                                                                                                                                 |
| [updateType](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversionupdatetype)         | string                                                                                                                                                              | The type of update action that was performed, whether forced, incremental, or a rollback operation. See \[`RemoteConfigUpdateType`\](/docs/reference/remote-config/rest/v1/Version#remoteconfigupdatetype) for valid values. |
| [updateUser](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversionupdateuser)         | [RemoteConfigUser](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.remoteconfiguser.md#remoteconfigremoteconfiguser_interface) | Metadata about the account that performed the update, of type \[`RemoteConfigUser`\](/docs/reference/remote-config/rest/v1/Version#remoteconfiguser).                                                                        |
| [versionNumber](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig.templateversion.md#remoteconfigtemplateversionversionnumber)   | number                                                                                                                                                              | The version number of the updated Remote Config template.                                                                                                                                                                    |

## remoteConfig.TemplateVersion.description

A description associated with this Remote Config template version.

**Signature:**  

    description: string;

## remoteConfig.TemplateVersion.rollbackSource

The version number of the Remote Config template that this update rolled back to. Only applies if this update was a rollback.

**Signature:**  

    rollbackSource?: number;

## remoteConfig.TemplateVersion.updateOrigin

The origin of the caller - either the Firebase console or the Remote Config REST API. See \[`RemoteConfigUpdateOrigin`\](/docs/reference/remote-config/rest/v1/Version#remoteconfigupdateorigin) for valid values.

**Signature:**  

    updateOrigin: string;

## remoteConfig.TemplateVersion.updateTime

When the template was updated in format (ISO8601 timestamp).

**Signature:**  

    updateTime: string;

## remoteConfig.TemplateVersion.updateType

The type of update action that was performed, whether forced, incremental, or a rollback operation. See \[`RemoteConfigUpdateType`\](/docs/reference/remote-config/rest/v1/Version#remoteconfigupdatetype) for valid values.

**Signature:**  

    updateType: string;

## remoteConfig.TemplateVersion.updateUser

Metadata about the account that performed the update, of type \[`RemoteConfigUser`\](/docs/reference/remote-config/rest/v1/Version#remoteconfiguser).

**Signature:**  

    updateUser: RemoteConfigUser;

## remoteConfig.TemplateVersion.versionNumber

The version number of the updated Remote Config template.

**Signature:**  

    versionNumber: number;