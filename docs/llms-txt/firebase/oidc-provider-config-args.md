# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config-args.md.txt

# FirebaseAdmin.Auth.Providers.OidcProviderConfigArgs Class Reference

# FirebaseAdmin.Auth.Providers.OidcProviderConfigArgs

Represents an OIDC auth provider configuration.

## Summary

See [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0-final.html).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Providers.AuthProviderConfigArgs\< T \>](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config-args-t-)

|                                                                                                                                                                                            ### Properties                                                                                                                                                                                            ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [ClientId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_args_1a47197833fa7e75eb807a1334d8a536f3)            | `string` Gets or sets the client ID used to confirm the audience of an OIDC provider's ID token.                                          |
| [ClientSecret](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_args_1ae29585f3e82f17b6e401beccafeb22b0)        | `string` Gets or sets the client secret, which is used to verify Code response types.                                                     |
| [CodeResponseType](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_args_1a5caa11047395363dc01e4b5c105d76a7)    | `bool` Gets or sets a value indicating whether this OIDC provider uses a Code response type.                                              |
| [IdTokenResponseType](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_args_1a46c33fd0399f84601512f72f9e79d14a) | `bool` Gets or sets a value indicating whether this OIDC provider uses an ID Token response type.                                         |
| [Issuer](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_args_1adbe4f09cb171ce2f7cc21e5c9cd11089)              | `string` Gets or sets the issuer used to match the issuer of the ID token and to determine the corresponding OIDC discovery document, eg. |

## Properties

### ClientId

```text
string ClientId
```  
Gets or sets the client ID used to confirm the audience of an OIDC provider's ID token.  

### ClientSecret

```text
string ClientSecret
```  
Gets or sets the client secret, which is used to verify Code response types.  

### CodeResponseType

```text
bool CodeResponseType
```  
Gets or sets a value indicating whether this OIDC provider uses a Code response type.  

### IdTokenResponseType

```text
bool IdTokenResponseType
```  
Gets or sets a value indicating whether this OIDC provider uses an ID Token response type.  

### Issuer

```text
string Issuer
```  
Gets or sets the issuer used to match the issuer of the ID token and to determine the corresponding OIDC discovery document, eg.

`/.well-known/openid-configuration`. This is needed for the following:

- To verify the provided issuer.
- To determine the authentication/authorization endpoint during the OAuth `id_token` authentication flow.
- To retrieve the public signing keys from `jwks_uri`, which is used to verify the signature of the ID token.
- To determine the `claims_supported`, which are passed through in the additional user info response.

<br />

ID token validation is performed as defined in [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation).