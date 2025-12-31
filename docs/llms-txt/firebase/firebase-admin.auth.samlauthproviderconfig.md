# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlauthproviderconfig.md.txt

# SAMLAuthProviderConfig interface

The \[SAML\](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) Auth provider configuration interface. A SAML provider can be created via [BaseAuth.createProviderConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthcreateproviderconfig).

**Signature:**  

    export interface SAMLAuthProviderConfig extends BaseAuthProviderConfig 

**Extends:** [BaseAuthProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauthproviderconfig.md#baseauthproviderconfig_interface)

## Properties

|                                                                            Property                                                                            |    Type    |                                                                                                                                                                                                            Description                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [callbackURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlauthproviderconfig.md#samlauthproviderconfigcallbackurl)           | string     | This is fixed and must always be the same as the OAuth redirect URL provisioned by Firebase Auth, `https://project-id.firebaseapp.com/__/auth/handler` unless a custom `authDomain` is used. The callback URL should also be provided to the SAML IdP during configuration.                                                                                                                                                       |
| [idpEntityId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlauthproviderconfig.md#samlauthproviderconfigidpentityid)           | string     | The SAML IdP entity identifier.                                                                                                                                                                                                                                                                                                                                                                                                   |
| [rpEntityId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlauthproviderconfig.md#samlauthproviderconfigrpentityid)             | string     | The SAML relying party (service provider) entity ID. This is defined by the developer but needs to be provided to the SAML IdP.                                                                                                                                                                                                                                                                                                   |
| [ssoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlauthproviderconfig.md#samlauthproviderconfigssourl)                     | string     | The SAML IdP SSO URL. This must be a valid URL.                                                                                                                                                                                                                                                                                                                                                                                   |
| [x509Certificates](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlauthproviderconfig.md#samlauthproviderconfigx509certificates) | string\[\] | The list of SAML IdP X.509 certificates issued by CA for this provider. Multiple certificates are accepted to prevent outages during IdP key rotation (for example ADFS rotates every 10 days). When the Auth server receives a SAML response, it will match the SAML response with the certificate on record. Otherwise the response is rejected. Developers are expected to manage the certificate updates as keys are rotated. |

## SAMLAuthProviderConfig.callbackURL

This is fixed and must always be the same as the OAuth redirect URL provisioned by Firebase Auth, `https://project-id.firebaseapp.com/__/auth/handler` unless a custom `authDomain` is used. The callback URL should also be provided to the SAML IdP during configuration.

**Signature:**  

    callbackURL?: string;

## SAMLAuthProviderConfig.idpEntityId

The SAML IdP entity identifier.

**Signature:**  

    idpEntityId: string;

## SAMLAuthProviderConfig.rpEntityId

The SAML relying party (service provider) entity ID. This is defined by the developer but needs to be provided to the SAML IdP.

**Signature:**  

    rpEntityId: string;

## SAMLAuthProviderConfig.ssoURL

The SAML IdP SSO URL. This must be a valid URL.

**Signature:**  

    ssoURL: string;

## SAMLAuthProviderConfig.x509Certificates

The list of SAML IdP X.509 certificates issued by CA for this provider. Multiple certificates are accepted to prevent outages during IdP key rotation (for example ADFS rotates every 10 days). When the Auth server receives a SAML response, it will match the SAML response with the certificate on record. Otherwise the response is rejected. Developers are expected to manage the certificate updates as keys are rotated.

**Signature:**  

    x509Certificates: string[];