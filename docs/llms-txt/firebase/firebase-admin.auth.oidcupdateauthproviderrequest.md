# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcupdateauthproviderrequest.md.txt

# OIDCUpdateAuthProviderRequest interface

The request interface for updating an OIDC Auth provider. This is used when updating an OIDC provider's configuration via [BaseAuth.updateProviderConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthupdateproviderconfig).

**Signature:**  

    export interface OIDCUpdateAuthProviderRequest 

## Properties

|                                                                               Property                                                                               |                                                                      Type                                                                       |                                                           Description                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [clientId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcupdateauthproviderrequest.md#oidcupdateauthproviderrequestclientid)         | string                                                                                                                                          | The OIDC provider's updated client ID. If not provided, the existing configuration's value is not modified.                      |
| [clientSecret](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcupdateauthproviderrequest.md#oidcupdateauthproviderrequestclientsecret) | string                                                                                                                                          | The OIDC provider's client secret to enable OIDC code flow. If not provided, the existing configuration's value is not modified. |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcupdateauthproviderrequest.md#oidcupdateauthproviderrequestdisplayname)   | string                                                                                                                                          | The OIDC provider's updated display name. If not provided, the existing configuration's value is not modified.                   |
| [enabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcupdateauthproviderrequest.md#oidcupdateauthproviderrequestenabled)           | boolean                                                                                                                                         | Whether the OIDC provider is enabled or not. If not provided, the existing configuration's setting is not modified.              |
| [issuer](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcupdateauthproviderrequest.md#oidcupdateauthproviderrequestissuer)             | string                                                                                                                                          | The OIDC provider's updated issuer. If not provided, the existing configuration's value is not modified.                         |
| [responseType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcupdateauthproviderrequest.md#oidcupdateauthproviderrequestresponsetype) | [OAuthResponseType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oauthresponsetype.md#oauthresponsetype_interface) | The OIDC provider's response object for OAuth authorization flow.                                                                |

## OIDCUpdateAuthProviderRequest.clientId

The OIDC provider's updated client ID. If not provided, the existing configuration's value is not modified.

**Signature:**  

    clientId?: string;

## OIDCUpdateAuthProviderRequest.clientSecret

The OIDC provider's client secret to enable OIDC code flow. If not provided, the existing configuration's value is not modified.

**Signature:**  

    clientSecret?: string;

## OIDCUpdateAuthProviderRequest.displayName

The OIDC provider's updated display name. If not provided, the existing configuration's value is not modified.

**Signature:**  

    displayName?: string;

## OIDCUpdateAuthProviderRequest.enabled

Whether the OIDC provider is enabled or not. If not provided, the existing configuration's setting is not modified.

**Signature:**  

    enabled?: boolean;

## OIDCUpdateAuthProviderRequest.issuer

The OIDC provider's updated issuer. If not provided, the existing configuration's value is not modified.

**Signature:**  

    issuer?: string;

## OIDCUpdateAuthProviderRequest.responseType

The OIDC provider's response object for OAuth authorization flow.

**Signature:**  

    responseType?: OAuthResponseType;