# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md.txt

# UpdateProjectConfigRequest interface

Interface representing the properties to update on the provided project config.

**Signature:**  

    export interface UpdateProjectConfigRequest 

## Properties

|                                                                                    Property                                                                                    |                                                                           Type                                                                           |                                                                                                    Description                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [emailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md#updateprojectconfigrequestemailprivacyconfig)     | [EmailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailprivacyconfig.md#emailprivacyconfig_interface)       | The email privacy configuration to update on the project                                                                                                                                                          |
| [mobileLinksConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md#updateprojectconfigrequestmobilelinksconfig)       | [MobileLinksConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.mobilelinksconfig.md#mobilelinksconfig_interface)          | The mobile links configuration for the project                                                                                                                                                                    |
| [multiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md#updateprojectconfigrequestmultifactorconfig)       | [MultiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md#multifactorconfig_interface)          | The multi-factor auth configuration to update on the project.                                                                                                                                                     |
| [passwordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md#updateprojectconfigrequestpasswordpolicyconfig) | [PasswordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md#passwordpolicyconfig_interface) | The password policy configuration to update on the project                                                                                                                                                        |
| [recaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md#updateprojectconfigrequestrecaptchaconfig)           | [RecaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfig_interface)                | The reCAPTCHA configuration to update on the project. By enabling reCAPTCHA Enterprise integration, you are agreeing to the reCAPTCHA Enterprise [Term of Service](https://cloud.google.com/terms/service-terms). |
| [smsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md#updateprojectconfigrequestsmsregionconfig)           | [SmsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#smsregionconfig)                                          | The SMS configuration to update on the project.                                                                                                                                                                   |

## UpdateProjectConfigRequest.emailPrivacyConfig

The email privacy configuration to update on the project

**Signature:**  

    emailPrivacyConfig?: EmailPrivacyConfig;

## UpdateProjectConfigRequest.mobileLinksConfig

The mobile links configuration for the project

**Signature:**  

    mobileLinksConfig?: MobileLinksConfig;

## UpdateProjectConfigRequest.multiFactorConfig

The multi-factor auth configuration to update on the project.

**Signature:**  

    multiFactorConfig?: MultiFactorConfig;

## UpdateProjectConfigRequest.passwordPolicyConfig

The password policy configuration to update on the project

**Signature:**  

    passwordPolicyConfig?: PasswordPolicyConfig;

## UpdateProjectConfigRequest.recaptchaConfig

The reCAPTCHA configuration to update on the project. By enabling reCAPTCHA Enterprise integration, you are agreeing to the reCAPTCHA Enterprise [Term of Service](https://cloud.google.com/terms/service-terms).

**Signature:**  

    recaptchaConfig?: RecaptchaConfig;

## UpdateProjectConfigRequest.smsRegionConfig

The SMS configuration to update on the project.

**Signature:**  

    smsRegionConfig?: SmsRegionConfig;