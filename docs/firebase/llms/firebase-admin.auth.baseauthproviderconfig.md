# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauthproviderconfig.md.txt

# BaseAuthProviderConfig interface

The base Auth provider configuration interface.

**Signature:**  

    export interface BaseAuthProviderConfig 

## Properties

|                                                                       Property                                                                       |  Type   |                                                                         Description                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauthproviderconfig.md#baseauthproviderconfigdisplayname) | string  | The user-friendly display name to the current configuration. This name is also used as the provider label in the Cloud Console.                              |
| [enabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauthproviderconfig.md#baseauthproviderconfigenabled)         | boolean | Whether the provider configuration is enabled or disabled. A user cannot sign in using a disabled provider.                                                  |
| [providerId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauthproviderconfig.md#baseauthproviderconfigproviderid)   | string  | The provider ID defined by the developer. For a SAML provider, this is always prefixed by `saml.`. For an OIDC provider, this is always prefixed by `oidc.`. |

## BaseAuthProviderConfig.displayName

The user-friendly display name to the current configuration. This name is also used as the provider label in the Cloud Console.

**Signature:**  

    displayName?: string;

## BaseAuthProviderConfig.enabled

Whether the provider configuration is enabled or disabled. A user cannot sign in using a disabled provider.

**Signature:**  

    enabled: boolean;

## BaseAuthProviderConfig.providerId

The provider ID defined by the developer. For a SAML provider, this is always prefixed by `saml.`. For an OIDC provider, this is always prefixed by `oidc.`.

**Signature:**  

    providerId: string;