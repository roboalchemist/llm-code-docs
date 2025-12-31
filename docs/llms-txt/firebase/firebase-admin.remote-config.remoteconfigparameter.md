# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md.txt

# RemoteConfigParameter interface

Interface representing a Remote Config parameter. At minimum, a `defaultValue` or a `conditionalValues` entry must be present for the parameter to have any effect.

**Signature:**  

    export interface RemoteConfigParameter 

## Properties

|                                                                                Property                                                                                 |                                                                                 Type                                                                                 |                                                                                        Description                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [conditionalValues](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparameterconditionalvalues) | { \[key: string\]: [RemoteConfigParameterValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#remoteconfigparametervalue); } | A `(condition name, value)` map. The condition name of the highest priority (the one listed first in the Remote Config template's conditions list) determines the value of this parameter. |
| [defaultValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparameterdefaultvalue)           | [RemoteConfigParameterValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#remoteconfigparametervalue)                       | The value to set the parameter to, when none of the named conditions evaluate to `true`.                                                                                                   |
| [description](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparameterdescription)             | string                                                                                                                                                               | A description for this parameter. Should not be over 100 characters and may contain any Unicode characters.                                                                                |
| [valueType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparametervaluetype)                 | [ParameterValueType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#parametervaluetype)                                       | The data type for all values of this parameter in the current version of the template. Defaults to `ParameterValueType.STRING` if unspecified.                                             |

## RemoteConfigParameter.conditionalValues

A `(condition name, value)` map. The condition name of the highest priority (the one listed first in the Remote Config template's conditions list) determines the value of this parameter.

**Signature:**  

    conditionalValues?: {
            [key: string]: RemoteConfigParameterValue;
        };

## RemoteConfigParameter.defaultValue

The value to set the parameter to, when none of the named conditions evaluate to `true`.

**Signature:**  

    defaultValue?: RemoteConfigParameterValue;

## RemoteConfigParameter.description

A description for this parameter. Should not be over 100 characters and may contain any Unicode characters.

**Signature:**  

    description?: string;

## RemoteConfigParameter.valueType

The data type for all values of this parameter in the current version of the template. Defaults to `ParameterValueType.STRING` if unspecified.

**Signature:**  

    valueType?: ParameterValueType;