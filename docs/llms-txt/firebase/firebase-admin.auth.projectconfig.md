# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md.txt

# ProjectConfig class

Represents a project configuration.

**Signature:**  

    export declare class ProjectConfig 

## Properties

|                                                                       Property                                                                       | Modifiers |                                                                             Type                                                                             |                                                                                     Description                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [emailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfigemailprivacyconfig)     |           | [EmailPrivacyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.emailprivacyconfig.md#emailprivacyconfig_interface)           | The email privacy configuration for the project                                                                                                                                     |
| [mobileLinksConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfigmobilelinksconfig)       |           | [MobileLinksConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.mobilelinksconfig.md#mobilelinksconfig_interface)              | The mobile links configuration for the project                                                                                                                                      |
| [multiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfigmultifactorconfig)       |           | [MultiFactorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.multifactorconfig.md#multifactorconfig_interface) \| undefined | The multi-factor auth configuration.                                                                                                                                                |
| [passwordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfigpasswordpolicyconfig) |           | [PasswordPolicyConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.passwordpolicyconfig.md#passwordpolicyconfig_interface)     | The password policy configuration for the project                                                                                                                                   |
| [recaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfigrecaptchaconfig)           |           | [RecaptchaConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfig_interface) \| undefined       | The reCAPTCHA configuration.                                                                                                                                                        |
| [smsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfigsmsregionconfig)           |           | [SmsRegionConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#smsregionconfig)                                              | The SMS Regions Config for the project. Configures the regions where users are allowed to send verification SMS. This is based on the calling code of the destination phone number. |

## Methods

|                                                           Method                                                           | Modifiers |                        Description                         |
|----------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [toJSON()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfigtojson) |           | Returns a JSON-serializable representation of this object. |

## ProjectConfig.emailPrivacyConfig

The email privacy configuration for the project

**Signature:**  

    readonly emailPrivacyConfig?: EmailPrivacyConfig;

## ProjectConfig.mobileLinksConfig

The mobile links configuration for the project

**Signature:**  

    readonly mobileLinksConfig?: MobileLinksConfig;

## ProjectConfig.multiFactorConfig

The multi-factor auth configuration.

**Signature:**  

    get multiFactorConfig(): MultiFactorConfig | undefined;

## ProjectConfig.passwordPolicyConfig

The password policy configuration for the project

**Signature:**  

    readonly passwordPolicyConfig?: PasswordPolicyConfig;

## ProjectConfig.recaptchaConfig

The reCAPTCHA configuration.

**Signature:**  

    get recaptchaConfig(): RecaptchaConfig | undefined;

## ProjectConfig.smsRegionConfig

The SMS Regions Config for the project. Configures the regions where users are allowed to send verification SMS. This is based on the calling code of the destination phone number.

**Signature:**  

    readonly smsRegionConfig?: SmsRegionConfig;

## ProjectConfig.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**  

    toJSON(): object;

**Returns:**

object

A JSON-serializable representation of this object.