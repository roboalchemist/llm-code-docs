# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md.txt

# MultiFactorConfig interface

Interface representing a multi-factor configuration. This can be used to define whether multi-factor authentication is enabled or disabled and the list of second factor challenges that are supported.

**Signature:**  

    export interface MultiFactorConfig 

## Properties

|                                                                      Property                                                                      |                                                                                    Type                                                                                     |                                                            Description                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [factorIds](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md#multifactorconfigfactorids)             | [AuthFactorType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#authfactortype)\[\]                                                           | The list of identifiers for enabled second factors. Currently only 'phone' is supported.                                          |
| [providerConfigs](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md#multifactorconfigproviderconfigs) | [MultiFactorProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorproviderconfig.md#multifactorproviderconfig_interface)\[\] | A list of multi-factor provider configurations. MFA providers (except phone) indicate whether they're enabled through this field. |
| [state](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md#multifactorconfigstate)                     | [MultiFactorConfigState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#multifactorconfigstate)                                               | The multi-factor config state.                                                                                                    |

## MultiFactorConfig.factorIds

The list of identifiers for enabled second factors. Currently only 'phone' is supported.

**Signature:**  

    factorIds?: AuthFactorType[];

## MultiFactorConfig.providerConfigs

A list of multi-factor provider configurations. MFA providers (except phone) indicate whether they're enabled through this field.

**Signature:**  

    providerConfigs?: MultiFactorProviderConfig[];

## MultiFactorConfig.state

The multi-factor config state.

**Signature:**  

    state: MultiFactorConfigState;