# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md.txt

# remoteConfig.ConfigUpdateData interface

The data within Firebase Remote Config update events.

**Signature:**  

    export interface ConfigUpdateData 

## Properties

|                                                                                      Property                                                                                      |                                                                              Type                                                                              |                                                                   Description                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedatadescription)       | string                                                                                                                                                         | The user-provided description of the corresponding Remote Config template.                                                                      |
| [rollbackSource](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedatarollbacksource) | number                                                                                                                                                         | Only present if this version is the result of a rollback, and will be the version number of the Remote Config template that was rolled-back to. |
| [updateOrigin](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedataupdateorigin)     | [ConfigUpdateOrigin](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md#remoteconfigconfigupdateorigin)      | Where the update action originated.                                                                                                             |
| [updateTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedataupdatetime)         | string                                                                                                                                                         | When the Remote Config template was written to the Remote Config server.                                                                        |
| [updateType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedataupdatetype)         | [ConfigUpdateType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.md#remoteconfigconfigupdatetype)          | What type of update was made.                                                                                                                   |
| [updateUser](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedataupdateuser)         | [ConfigUser](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configuser.md#remoteconfigconfiguser_interface) | Aggregation of all metadata fields about the account that performed the update.                                                                 |
| [versionNumber](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.remoteconfig.configupdatedata.md#remoteconfigconfigupdatedataversionnumber)   | number                                                                                                                                                         | The version number of the version's corresponding Remote Config template.                                                                       |

## remoteConfig.ConfigUpdateData.description

The user-provided description of the corresponding Remote Config template.

**Signature:**  

    description: string;

## remoteConfig.ConfigUpdateData.rollbackSource

Only present if this version is the result of a rollback, and will be the version number of the Remote Config template that was rolled-back to.

**Signature:**  

    rollbackSource: number;

## remoteConfig.ConfigUpdateData.updateOrigin

Where the update action originated.

**Signature:**  

    updateOrigin: ConfigUpdateOrigin;

## remoteConfig.ConfigUpdateData.updateTime

When the Remote Config template was written to the Remote Config server.

**Signature:**  

    updateTime: string;

## remoteConfig.ConfigUpdateData.updateType

What type of update was made.

**Signature:**  

    updateType: ConfigUpdateType;

## remoteConfig.ConfigUpdateData.updateUser

Aggregation of all metadata fields about the account that performed the update.

**Signature:**  

    updateUser: ConfigUser;

## remoteConfig.ConfigUpdateData.versionNumber

The version number of the version's corresponding Remote Config template.

**Signature:**  

    versionNumber: number;