# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config.md.txt

# FirebaseAdmin.Auth.Providers.OidcProviderConfig Class Reference

# FirebaseAdmin.Auth.Providers.OidcProviderConfig

Represents an OIDC auth provider configuration.

## Summary

See [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0-final.html).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Providers.AuthProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config)

|                                                                                                                                                                                   ### Properties                                                                                                                                                                                   ||
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [ClientId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_1a2650e328d70163bfa5e95545238759a3)            | `string` Gets the client ID used to confirm the audience of an OIDC provider's ID token.                                          |
| [ClientSecret](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_1af2973c88a0cf09d70a5f8b397c861fbc)        | `string` Gets the client secret, which is used to verify Code response types.                                                     |
| [CodeResponseType](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_1a4075c0052f0358ccd0707dd6e902eecc)    | `bool` Gets a value indicating whether an Code type response type will be provided.                                               |
| [IdTokenResponseType](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_1a2a3d77fb6fd85ad5500cb2d1f28962ef) | `bool` Gets a value indicating whether an ID Token response type will be provided.                                                |
| [Issuer](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/oidc-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_oidc_provider_config_1a2978610f6b74c6fa54899bdb0b3bfd1d)              | `string` Gets the issuer used to match the issuer of the ID token and to determine the corresponding OIDC discovery document, eg. |

## Properties

### ClientId

```text
string ClientId
```  
Gets the client ID used to confirm the audience of an OIDC provider's ID token.  

### ClientSecret

```text
string ClientSecret
```  
Gets the client secret, which is used to verify Code response types.  

### CodeResponseType

```text
bool CodeResponseType
```  
Gets a value indicating whether an Code type response type will be provided.  

### IdTokenResponseType

```text
bool IdTokenResponseType
```  
Gets a value indicating whether an ID Token response type will be provided.  

### Issuer

```text
string Issuer
```  
Gets the issuer used to match the issuer of the ID token and to determine the corresponding OIDC discovery document, eg.

`/.well-known/openid-configuration`. This is needed for the following:

- To verify the provided issuer.
- To determine the authentication/authorization endpoint during the OAuth `id_token` authentication flow.
- To retrieve the public signing keys from `jwks_uri`, which is used to verify the signature of the ID token.
- To determine the `claims_supported`, which are passed through in the additional user info response.

<br />

ID token validation is performed as defined in [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation).