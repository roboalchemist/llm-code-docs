# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md.txt

# UpdateTenantRequest interface

Interface representing the properties to update on the provided tenant.

**Signature:**  

    export interface UpdateTenantRequest 

## Properties

|                                                                               Property                                                                               |                                                                                  Type                                                                                   |                                                                                                   Description                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [anonymousSignInEnabled](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestanonymoussigninenabled) | boolean                                                                                                                                                                 | Whether the anonymous provider is enabled.                                                                                                                                                                       |
| [displayName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestdisplayname)                       | string                                                                                                                                                                  | The tenant display name.                                                                                                                                                                                         |
| [emailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestemailprivacyconfig)         | [EmailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailprivacyconfig.md#emailprivacyconfig_interface)                      | The email privacy configuration for the tenant                                                                                                                                                                   |
| [emailSignInConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestemailsigninconfig)           | [EmailSignInProviderConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailsigninproviderconfig.md#emailsigninproviderconfig_interface) | The email sign in configuration.                                                                                                                                                                                 |
| [multiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestmultifactorconfig)           | [MultiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md#multifactorconfig_interface)                         | The multi-factor auth configuration to update on the tenant.                                                                                                                                                     |
| [passwordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestpasswordpolicyconfig)     | [PasswordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md#passwordpolicyconfig_interface)                | The password policy configuration for the tenant                                                                                                                                                                 |
| [recaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestrecaptchaconfig)               | [RecaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfig_interface)                               | The reCAPTCHA configuration to update on the tenant. By enabling reCAPTCHA Enterprise integration, you are agreeing to the reCAPTCHA Enterprise [Term of Service](https://cloud.google.com/terms/service-terms). |
| [smsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequestsmsregionconfig)               | [SmsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#smsregionconfig)                                                         | The SMS configuration to update on the project.                                                                                                                                                                  |
| [testPhoneNumbers](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updatetenantrequest.md#updatetenantrequesttestphonenumbers)             | { \[phoneNumber: string\]: string; } \| null                                                                                                                            | The updated map containing the test phone number / code pairs for the tenant. Passing null clears the previously save phone number / code pairs.                                                                 |

## UpdateTenantRequest.anonymousSignInEnabled

Whether the anonymous provider is enabled.

**Signature:**  

    anonymousSignInEnabled?: boolean;

## UpdateTenantRequest.displayName

The tenant display name.

**Signature:**  

    displayName?: string;

## UpdateTenantRequest.emailPrivacyConfig

The email privacy configuration for the tenant

**Signature:**  

    emailPrivacyConfig?: EmailPrivacyConfig;

## UpdateTenantRequest.emailSignInConfig

The email sign in configuration.

**Signature:**  

    emailSignInConfig?: EmailSignInProviderConfig;

## UpdateTenantRequest.multiFactorConfig

The multi-factor auth configuration to update on the tenant.

**Signature:**  

    multiFactorConfig?: MultiFactorConfig;

## UpdateTenantRequest.passwordPolicyConfig

The password policy configuration for the tenant

**Signature:**  

    passwordPolicyConfig?: PasswordPolicyConfig;

## UpdateTenantRequest.recaptchaConfig

The reCAPTCHA configuration to update on the tenant. By enabling reCAPTCHA Enterprise integration, you are agreeing to the reCAPTCHA Enterprise [Term of Service](https://cloud.google.com/terms/service-terms).

**Signature:**  

    recaptchaConfig?: RecaptchaConfig;

## UpdateTenantRequest.smsRegionConfig

The SMS configuration to update on the project.

**Signature:**  

    smsRegionConfig?: SmsRegionConfig;

## UpdateTenantRequest.testPhoneNumbers

The updated map containing the test phone number / code pairs for the tenant. Passing null clears the previously save phone number / code pairs.

**Signature:**  

    testPhoneNumbers?: {
            [phoneNumber: string]: string;
        } | null;