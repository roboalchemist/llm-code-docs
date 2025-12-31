# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md.txt

# ServerTemplateData interface

Represents the data in a Remote Config server template.

**Signature:**  

    export interface ServerTemplateData 

## Properties

|                                                                      Property                                                                       |                                                                                            Type                                                                                            |                                       Description                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [conditions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedataconditions) | [NamedCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.namedcondition.md#namedcondition_interface)\[\]                                        | A list of conditions in descending order by priority.                                   |
| [etag](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedataetag)             | string                                                                                                                                                                                     | Current Remote Config template ETag (read-only).                                        |
| [parameters](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedataparameters) | { \[key: string\]: [RemoteConfigParameter](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparameter_interface); } | Map of parameter keys to their optional default values and optional conditional values. |
| [version](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedataversion)       | [Version](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#version_interface)                                                                 | Version information for the current Remote Config template.                             |

## ServerTemplateData.conditions

A list of conditions in descending order by priority.

**Signature:**  

    conditions: NamedCondition[];

## ServerTemplateData.etag

Current Remote Config template ETag (read-only).

**Signature:**  

    readonly etag: string;

## ServerTemplateData.parameters

Map of parameter keys to their optional default values and optional conditional values.

**Signature:**  

    parameters: {
            [key: string]: RemoteConfigParameter;
        };

## ServerTemplateData.version

Version information for the current Remote Config template.

**Signature:**  

    version?: Version;