# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config.md.txt

# FirebaseAdmin.Auth.Providers.SamlProviderConfig Class Reference

# FirebaseAdmin.Auth.Providers.SamlProviderConfig

Represents a SAML auth provider configuration.

## Summary

See [SAML technical overview](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Providers.AuthProviderConfig](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config)

|                                                                                                                                                                      ### Properties                                                                                                                                                                      ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [CallbackUrl](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_1a4e39323a2fabf1d22715579049cf2ecb)      | `string` Gets the SAML callback URL.                                                                       |
| [IdpEntityId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_1a5a209a86301d25c9af73ec62ae327b43)      | `string` Gets the SAML IdP entity identifier.                                                              |
| [RpEntityId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_1ab0abeea01218a1230cfeafe65b0d4e8b)       | `string` Gets the SAML relying party (service provider) entity ID.                                         |
| [SsoUrl](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_1ada67de37620a6a57af58463ff75297c6)           | `string` Gets the SAML IdP SSO URL.                                                                        |
| [X509Certificates](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_1a86d2978f0904bf1afe43b956aad50997) | `IEnumerable< string >` Gets the collection of SAML IdP X.509 certificates issued by CA for this provider. |

## Properties

### CallbackUrl

```text
string CallbackUrl
```  
Gets the SAML callback URL.

This is fixed and must always be the same as the OAuth redirect URL provisioned by Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth), <https://project-id.firebaseapp.com/__/auth/handler> unless a custom `authDomain` is used. The callback URL should also be provided to the SAML IdP during configuration.  

### IdpEntityId

```text
string IdpEntityId
```  
Gets the SAML IdP entity identifier.  

### RpEntityId

```text
string RpEntityId
```  
Gets the SAML relying party (service provider) entity ID.

This is defined by the developer but needs to be provided to the SAML IdP.  

### SsoUrl

```text
string SsoUrl
```  
Gets the SAML IdP SSO URL.  

### X509Certificates

```text
IEnumerable< string > X509Certificates
```  
Gets the collection of SAML IdP X.509 certificates issued by CA for this provider.

Multiple certificates are accepted to prevent outages during IdP key rotation (for example ADFS rotates every 10 days). When the [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) server receives a SAML response, it will match the SAML response with the certificate on record. Otherwise the response is rejected. Developers are expected to manage the certificate updates as keys are rotated.