# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md.txt

# Tenant class

Represents a tenant configuration.

Multi-tenancy support requires Google Cloud's Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

Before multi-tenancy can be used on a Google Cloud Identity Platform project, tenants must be allowed on that project via the Cloud Console UI.

A tenant configuration provides information such as the display name, tenant identifier and email authentication configuration. For OIDC/SAML provider configuration management, `TenantAwareAuth` instances should be used instead of a `Tenant` to retrieve the list of configured IdPs on a tenant. When configuring these providers, note that tenants will inherit whitelisted domains and authenticated redirect URIs of their parent project.

All other settings of a tenant will also be inherited. These will need to be managed from the Cloud Console UI.

**Signature:**  

    export declare class Tenant 

## Properties

|                                                                  Property                                                                  | Modifiers |                                                                                         Type                                                                                         |                                                                                      Description                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [anonymousSignInEnabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantanonymoussigninenabled) |           | boolean                                                                                                                                                                              |                                                                                                                                                                                        |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantdisplayname)                       |           | string                                                                                                                                                                               | The tenant display name.                                                                                                                                                               |
| [emailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantemailprivacyconfig)         |           | [EmailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailprivacyconfig.md#emailprivacyconfig_interface)                                   | The email privacy configuration for the tenant                                                                                                                                         |
| [emailSignInConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantemailsigninconfig)           |           | [EmailSignInProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailsigninproviderconfig.md#emailsigninproviderconfig_interface) \| undefined | The email sign in provider configuration.                                                                                                                                              |
| [multiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantmultifactorconfig)           |           | [MultiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md#multifactorconfig_interface) \| undefined                         | The multi-factor auth configuration on the current tenant.                                                                                                                             |
| [passwordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantpasswordpolicyconfig)     |           | [PasswordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md#passwordpolicyconfig_interface)                             | The password policy configuration for the tenant                                                                                                                                       |
| [recaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantrecaptchaconfig)               |           | [RecaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfig_interface) \| undefined                               | The recaptcha config auth configuration of the current tenant.                                                                                                                         |
| [smsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenantsmsregionconfig)               |           | [SmsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#smsregionconfig)                                                                      | The SMS Regions Config to update a tenant. Configures the regions where users are allowed to send verification SMS. This is based on the calling code of the destination phone number. |
| [tenantId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenanttenantid)                             |           | string                                                                                                                                                                               | The tenant identifier.                                                                                                                                                                 |
| [testPhoneNumbers](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenanttestphonenumbers)             |           | { \[phoneNumber: string\]: string; }                                                                                                                                                 | The map containing the test phone number / code pairs for the tenant.                                                                                                                  |

## Methods

|                                                    Method                                                    | Modifiers |                        Description                         |
|--------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenant.md#tenanttojson) |           | Returns a JSON-serializable representation of this object. |

## Tenant.anonymousSignInEnabled

**Signature:**  

    readonly anonymousSignInEnabled: boolean;

## Tenant.displayName

The tenant display name.

**Signature:**  

    readonly displayName?: string;

## Tenant.emailPrivacyConfig

The email privacy configuration for the tenant

**Signature:**  

    readonly emailPrivacyConfig?: EmailPrivacyConfig;

## Tenant.emailSignInConfig

The email sign in provider configuration.

**Signature:**  

    get emailSignInConfig(): EmailSignInProviderConfig | undefined;

## Tenant.multiFactorConfig

The multi-factor auth configuration on the current tenant.

**Signature:**  

    get multiFactorConfig(): MultiFactorConfig | undefined;

## Tenant.passwordPolicyConfig

The password policy configuration for the tenant

**Signature:**  

    readonly passwordPolicyConfig?: PasswordPolicyConfig;

## Tenant.recaptchaConfig

The recaptcha config auth configuration of the current tenant.

**Signature:**  

    get recaptchaConfig(): RecaptchaConfig | undefined;

## Tenant.smsRegionConfig

The SMS Regions Config to update a tenant. Configures the regions where users are allowed to send verification SMS. This is based on the calling code of the destination phone number.

**Signature:**  

    readonly smsRegionConfig?: SmsRegionConfig;

## Tenant.tenantId

The tenant identifier.

**Signature:**  

    readonly tenantId: string;

## Tenant.testPhoneNumbers

The map containing the test phone number / code pairs for the tenant.

**Signature:**  

    readonly testPhoneNumbers?: {
            [phoneNumber: string]: string;
        };

## Tenant.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.