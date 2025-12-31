# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md.txt

# SAMLUpdateAuthProviderRequest interface

The request interface for updating a SAML Auth provider. This is used when updating a SAML provider's configuration via [BaseAuth.updateProviderConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauthupdateproviderconfig).

**Signature:**  

    export interface SAMLUpdateAuthProviderRequest 

## Properties

|                                                                                   Property                                                                                   |    Type    |                                                        Description                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------|
| [callbackURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md#samlupdateauthproviderrequestcallbackurl)           | string     | The SAML provider's callback URL. If not provided, the existing configuration's value is not modified.                    |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md#samlupdateauthproviderrequestdisplayname)           | string     | The SAML provider's updated display name. If not provided, the existing configuration's value is not modified.            |
| [enabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md#samlupdateauthproviderrequestenabled)                   | boolean    | Whether the SAML provider is enabled or not. If not provided, the existing configuration's setting is not modified.       |
| [idpEntityId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md#samlupdateauthproviderrequestidpentityid)           | string     | The SAML provider's updated IdP entity ID. If not provided, the existing configuration's value is not modified.           |
| [rpEntityId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md#samlupdateauthproviderrequestrpentityid)             | string     | The SAML provider's updated RP entity ID. If not provided, the existing configuration's value is not modified.            |
| [ssoURL](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md#samlupdateauthproviderrequestssourl)                     | string     | The SAML provider's updated SSO URL. If not provided, the existing configuration's value is not modified.                 |
| [x509Certificates](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.samlupdateauthproviderrequest.md#samlupdateauthproviderrequestx509certificates) | string\[\] | The SAML provider's updated list of X.509 certificated. If not provided, the existing configuration list is not modified. |

## SAMLUpdateAuthProviderRequest.callbackURL

The SAML provider's callback URL. If not provided, the existing configuration's value is not modified.

**Signature:**  

    callbackURL?: string;

## SAMLUpdateAuthProviderRequest.displayName

The SAML provider's updated display name. If not provided, the existing configuration's value is not modified.

**Signature:**  

    displayName?: string;

## SAMLUpdateAuthProviderRequest.enabled

Whether the SAML provider is enabled or not. If not provided, the existing configuration's setting is not modified.

**Signature:**  

    enabled?: boolean;

## SAMLUpdateAuthProviderRequest.idpEntityId

The SAML provider's updated IdP entity ID. If not provided, the existing configuration's value is not modified.

**Signature:**  

    idpEntityId?: string;

## SAMLUpdateAuthProviderRequest.rpEntityId

The SAML provider's updated RP entity ID. If not provided, the existing configuration's value is not modified.

**Signature:**  

    rpEntityId?: string;

## SAMLUpdateAuthProviderRequest.ssoURL

The SAML provider's updated SSO URL. If not provided, the existing configuration's value is not modified.

**Signature:**  

    ssoURL?: string;

## SAMLUpdateAuthProviderRequest.x509Certificates

The SAML provider's updated list of X.509 certificated. If not provided, the existing configuration list is not modified.

**Signature:**  

    x509Certificates?: string[];