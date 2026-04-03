# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfig.md.txt

The base Auth provider configuration interface.

<br />

**Signature:**  

    export interface AuthProviderConfig 

## Properties

|                                                                   Property                                                                   |  Type   |                                                                        Description                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfig.md#authproviderconfigdisplayname) | string  | The user-friendly display name to the current configuration. This name is also used as the provider label in the Cloud Console.                            |
| [enabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfig.md#authproviderconfigenabled)         | boolean | Whether the provider configuration is enabled or disabled. A user cannot sign in using a disabled provider.                                                |
| [providerId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.authproviderconfig.md#authproviderconfigproviderid)   | string  | The provider ID defined by the developer. For a SAML provider, this is always prefixed by`saml.`. For an OIDC provider, this is always prefixed by`oidc.`. |

## AuthProviderConfig.displayName

The user-friendly display name to the current configuration. This name is also used as the provider label in the Cloud Console.

**Signature:**  

    displayName?: string;

## AuthProviderConfig.enabled

Whether the provider configuration is enabled or disabled. A user cannot sign in using a disabled provider.

**Signature:**  

    enabled: boolean;

## AuthProviderConfig.providerId

The provider ID defined by the developer. For a SAML provider, this is always prefixed by`saml.`. For an OIDC provider, this is always prefixed by`oidc.`.

**Signature:**  

    providerId: string;