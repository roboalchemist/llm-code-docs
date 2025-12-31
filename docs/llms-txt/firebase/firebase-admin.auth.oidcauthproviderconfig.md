# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcauthproviderconfig.md.txt

# OIDCAuthProviderConfig interface

The \[OIDC\](https://openid.net/specs/openid-connect-core-1_0-final.html) Auth provider configuration interface. An OIDC provider can be created via [BaseAuth.createProviderConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthcreateproviderconfig).

**Signature:**  

    export interface OIDCAuthProviderConfig extends BaseAuthProviderConfig 

**Extends:** [BaseAuthProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauthproviderconfig.md#baseauthproviderconfig_interface)

## Properties

|                                                                        Property                                                                        |                                                                      Type                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                            Description                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [clientId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcauthproviderconfig.md#oidcauthproviderconfigclientid)         | string                                                                                                                                          | This is the required client ID used to confirm the audience of an OIDC provider's \[ID token\](https://openid.net/specs/openid-connect-core-1_0-final.html#IDToken).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [clientSecret](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcauthproviderconfig.md#oidcauthproviderconfigclientsecret) | string                                                                                                                                          | The OIDC provider's client secret to enable OIDC code flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [issuer](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcauthproviderconfig.md#oidcauthproviderconfigissuer)             | string                                                                                                                                          | This is the required provider issuer used to match the provider issuer of the ID token and to determine the corresponding OIDC discovery document, eg. \[`/.well-known/openid-configuration`\](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig). This is needed for the following: - To verify the provided issuer. - Determine the authentication/authorization endpoint during the OAuth `id_token` authentication flow. - To retrieve the public signing keys via `jwks_uri` to verify the OIDC provider's ID token's signature. - To determine the claims_supported to construct the user attributes to be returned in the additional user info response. ID token validation will be performed as defined in the \[spec\](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation). |
| [responseType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oidcauthproviderconfig.md#oidcauthproviderconfigresponsetype) | [OAuthResponseType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.oauthresponsetype.md#oauthresponsetype_interface) | The OIDC provider's response object for OAuth authorization flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## OIDCAuthProviderConfig.clientId

This is the required client ID used to confirm the audience of an OIDC provider's \[ID token\](https://openid.net/specs/openid-connect-core-1_0-final.html#IDToken).

**Signature:**  

    clientId: string;

## OIDCAuthProviderConfig.clientSecret

The OIDC provider's client secret to enable OIDC code flow.

**Signature:**  

    clientSecret?: string;

## OIDCAuthProviderConfig.issuer

This is the required provider issuer used to match the provider issuer of the ID token and to determine the corresponding OIDC discovery document, eg. \[`/.well-known/openid-configuration`\](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig). This is needed for the following:

- To verify the provided issuer.
- Determine the authentication/authorization endpoint during the OAuth `id_token` authentication flow.
- To retrieve the public signing keys via `jwks_uri` to verify the OIDC provider's ID token's signature.
- To determine the claims_supported to construct the user attributes to be returned in the additional user info response.

ID token validation will be performed as defined in the \[spec\](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation).

<br />

**Signature:**  

    issuer: string;

## OIDCAuthProviderConfig.responseType

The OIDC provider's response object for OAuth authorization flow.

**Signature:**  

    responseType?: OAuthResponseType;