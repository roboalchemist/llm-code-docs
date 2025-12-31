# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config-args.md.txt

# FirebaseAdmin.Auth.Providers.SamlProviderConfigArgs Class Reference

# FirebaseAdmin.Auth.Providers.SamlProviderConfigArgs

Represents a SAML auth provider configuration.

## Summary

See [SAML technical overview](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html).

### Inheritance

Inherits from: [FirebaseAdmin.Auth.Providers.AuthProviderConfigArgs\< T \>](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/auth-provider-config-args-t-)

|                                                                                                                                                                               ### Properties                                                                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [CallbackUrl](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_args_1ac0f7f7b152cab6bcafb3218fc690b15e)      | `string` Gets or sets the SAML callback URL.                                                                       |
| [IdpEntityId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_args_1a95043d03a027a67c2a53cdf7565ff148)      | `string` Gets or sets the SAML IdP entity identifier.                                                              |
| [RpEntityId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_args_1a2b431088cfab8b5c64a16614a9feee54)       | `string` Gets or sets the SAML relying party (service provider) entity ID.                                         |
| [SsoUrl](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_args_1adde9416e161ccde83809f55f5f1af8cb)           | `string` Gets or sets the SAML IdP SSO URL.                                                                        |
| [X509Certificates](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/providers/saml-provider-config-args#class_firebase_admin_1_1_auth_1_1_providers_1_1_saml_provider_config_args_1a70cca000ec785d2e98b3dce80ce6aa7e) | `IEnumerable< string >` Gets or sets the collection of SAML IdP X.509 certificates issued by CA for this provider. |

## Properties

### CallbackUrl

```text
string CallbackUrl
```  
Gets or sets the SAML callback URL.

This is fixed and must always be the same as the OAuth redirect URL provisioned by Firebase [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth), <https://project-id.firebaseapp.com/__/auth/handler> unless a custom `authDomain` is used. The callback URL should also be provided to the SAML IdP during configuration.  

### IdpEntityId

```text
string IdpEntityId
```  
Gets or sets the SAML IdP entity identifier.  

### RpEntityId

```text
string RpEntityId
```  
Gets or sets the SAML relying party (service provider) entity ID.

This is defined by the developer but needs to be provided to the SAML IdP.  

### SsoUrl

```text
string SsoUrl
```  
Gets or sets the SAML IdP SSO URL.  

### X509Certificates

```text
IEnumerable< string > X509Certificates
```  
Gets or sets the collection of SAML IdP X.509 certificates issued by CA for this provider.

Multiple certificates are accepted to prevent outages during IdP key rotation (for example ADFS rotates every 10 days). When the [Auth](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth#namespace_firebase_admin_1_1_auth) server receives a SAML response, it will match the SAML response with the certificate on record. Otherwise the response is rejected. Developers are expected to manage the certificate updates as keys are rotated.