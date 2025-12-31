# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md.txt

# RemoteConfigTemplate interface

Represents a Remote Config client template.

**Signature:**  

    export interface RemoteConfigTemplate 

## Properties

|                                                                             Property                                                                              |                                                                                                   Type                                                                                                    |                                                                                                                             Description                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [conditions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplateconditions)           | [RemoteConfigCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigcondition.md#remoteconfigcondition_interface)\[\]                                  | A list of conditions in descending order by priority.                                                                                                                                                                                                                |
| [etag](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplateetag)                       | string                                                                                                                                                                                                    | ETag of the current Remote Config template (readonly).                                                                                                                                                                                                               |
| [parameterGroups](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplateparametergroups) | { \[key: string\]: [RemoteConfigParameterGroup](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparametergroup.md#remoteconfigparametergroup_interface); } | Map of parameter group names to their parameter group objects. A group's name is mutable but must be unique among groups in the Remote Config template. The name is limited to 256 characters and intended to be human-readable. Any Unicode characters are allowed. |
| [parameters](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplateparameters)           | { \[key: string\]: [RemoteConfigParameter](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparameter_interface); }                | Map of parameter keys to their optional default values and optional conditional values.                                                                                                                                                                              |
| [version](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplateversion)                 | [Version](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#version_interface)                                                                                | Version information for the current Remote Config template.                                                                                                                                                                                                          |

## RemoteConfigTemplate.conditions

A list of conditions in descending order by priority.

**Signature:**  

    conditions: RemoteConfigCondition[];

## RemoteConfigTemplate.etag

ETag of the current Remote Config template (readonly).

**Signature:**  

    readonly etag: string;

## RemoteConfigTemplate.parameterGroups

Map of parameter group names to their parameter group objects. A group's name is mutable but must be unique among groups in the Remote Config template. The name is limited to 256 characters and intended to be human-readable. Any Unicode characters are allowed.

**Signature:**  

    parameterGroups: {
            [key: string]: RemoteConfigParameterGroup;
        };

## RemoteConfigTemplate.parameters

Map of parameter keys to their optional default values and optional conditional values.

**Signature:**  

    parameters: {
            [key: string]: RemoteConfigParameter;
        };

## RemoteConfigTemplate.version

Version information for the current Remote Config template.

**Signature:**  

    version?: Version;