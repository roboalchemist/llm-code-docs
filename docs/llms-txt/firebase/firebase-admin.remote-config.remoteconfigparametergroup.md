# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparametergroup.md.txt

# RemoteConfigParameterGroup interface

Interface representing a Remote Config parameter group. Grouping parameters is only for management purposes and does not affect client-side fetching of parameter values.

**Signature:**  

    export interface RemoteConfigParameterGroup 

## Properties

|                                                                               Property                                                                                |                                                                                            Type                                                                                            |                                                                                                                                                              Description                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [description](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparametergroup.md#remoteconfigparametergroupdescription) | string                                                                                                                                                                                     | A description for the group. Its length must be less than or equal to 256 characters. A description may contain any Unicode characters.                                                                                                                                                                                                |
| [parameters](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparametergroup.md#remoteconfigparametergroupparameters)   | { \[key: string\]: [RemoteConfigParameter](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparameter_interface); } | Map of parameter keys to their optional default values and optional conditional values for parameters that belong to this group. A parameter only appears once per Remote Config template. An ungrouped parameter appears at the top level, whereas a parameter organized within a group appears within its group's map of parameters. |

## RemoteConfigParameterGroup.description

A description for the group. Its length must be less than or equal to 256 characters. A description may contain any Unicode characters.

**Signature:**  

    description?: string;

## RemoteConfigParameterGroup.parameters

Map of parameter keys to their optional default values and optional conditional values for parameters that belong to this group. A parameter only appears once per Remote Config template. An ungrouped parameter appears at the top level, whereas a parameter organized within a group appears within its group's map of parameters.

**Signature:**  

    parameters: {
            [key: string]: RemoteConfigParameter;
        };