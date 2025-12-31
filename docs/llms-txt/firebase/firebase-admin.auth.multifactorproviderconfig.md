# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorproviderconfig.md.txt

# MultiFactorProviderConfig interface

Interface representing a multi-factor auth provider configuration. This interface is used for second factor auth providers other than SMS. Currently, only TOTP is supported.

**Signature:**  

    export interface MultiFactorProviderConfig 

## Properties

|                                                                                 Property                                                                                 |                                                                                        Type                                                                                         |                             Description                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [state](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorproviderconfig.md#multifactorproviderconfigstate)                           | [MultiFactorConfigState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#multifactorconfigstate)                                                       | Indicates whether this multi-factor provider is enabled or disabled. |
| [totpProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorproviderconfig.md#multifactorproviderconfigtotpproviderconfig) | [TotpMultiFactorProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.totpmultifactorproviderconfig.md#totpmultifactorproviderconfig_interface) | TOTP multi-factor provider config.                                   |

## MultiFactorProviderConfig.state

Indicates whether this multi-factor provider is enabled or disabled.

**Signature:**  

    state: MultiFactorConfigState;

## MultiFactorProviderConfig.totpProviderConfig

TOTP multi-factor provider config.

**Signature:**  

    totpProviderConfig?: TotpMultiFactorProviderConfig;