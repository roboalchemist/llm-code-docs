# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md.txt

# RecaptchaConfig interface

The request interface for updating a reCAPTCHA Config. By enabling reCAPTCHA Enterprise Integration you are agreeing to reCAPTCHA Enterprise [Term of Service](https://cloud.google.com/terms/service-terms).

**Signature:**  

    export interface RecaptchaConfig 

## Properties

|                                                                                  Property                                                                                  |                                                                                          Type                                                                                           |                                                                           Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [emailPasswordEnforcementState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfigemailpasswordenforcementstate) | [RecaptchaProviderEnforcementState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#recaptchaproviderenforcementstate)                                     | The enforcement state of the email password provider.                                                                                                            |
| [managedRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfigmanagedrules)                                   | [RecaptchaManagedRule](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchamanagedrule.md#recaptchamanagedrule_interface)\[\]                            | The reCAPTCHA managed rules.                                                                                                                                     |
| [phoneEnforcementState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfigphoneenforcementstate)                 | [RecaptchaProviderEnforcementState](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#recaptchaproviderenforcementstate)                                     | The enforcement state of the phone provider.                                                                                                                     |
| [recaptchaKeys](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfigrecaptchakeys)                                 | [RecaptchaKey](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchakey.md#recaptchakey_interface)\[\]                                                    | The reCAPTCHA keys.                                                                                                                                              |
| [smsTollFraudManagedRules](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfigsmstollfraudmanagedrules)           | [RecaptchaTollFraudManagedRule](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchatollfraudmanagedrule.md#recaptchatollfraudmanagedrule_interface)\[\] | The managed rules for toll fraud provider, containing the enforcement status. The toll fraud provider contains all SMS related user flows.                       |
| [useAccountDefender](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfiguseaccountdefender)                       | boolean                                                                                                                                                                                 | Whether to use account defender for reCAPTCHA assessment. The default value is false.                                                                            |
| [useSmsBotScore](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfigusesmsbotscore)                               | boolean                                                                                                                                                                                 | Whether to use the rCE bot score for reCAPTCHA phone provider. Can only be true when the phone_enforcement_state is AUDIT or ENFORCE.                            |
| [useSmsTollFraudProtection](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchaconfig.md#recaptchaconfigusesmstollfraudprotection)         | boolean                                                                                                                                                                                 | Whether to use the rCE SMS toll fraud protection risk score for reCAPTCHA phone provider. Can only be true when the phone_enforcement_state is AUDIT or ENFORCE. |

## RecaptchaConfig.emailPasswordEnforcementState

The enforcement state of the email password provider.

**Signature:**  

    emailPasswordEnforcementState?: RecaptchaProviderEnforcementState;

## RecaptchaConfig.managedRules

The reCAPTCHA managed rules.

**Signature:**  

    managedRules?: RecaptchaManagedRule[];

## RecaptchaConfig.phoneEnforcementState

The enforcement state of the phone provider.

**Signature:**  

    phoneEnforcementState?: RecaptchaProviderEnforcementState;

## RecaptchaConfig.recaptchaKeys

The reCAPTCHA keys.

**Signature:**  

    recaptchaKeys?: RecaptchaKey[];

## RecaptchaConfig.smsTollFraudManagedRules

The managed rules for toll fraud provider, containing the enforcement status. The toll fraud provider contains all SMS related user flows.

**Signature:**  

    smsTollFraudManagedRules?: RecaptchaTollFraudManagedRule[];

## RecaptchaConfig.useAccountDefender

Whether to use account defender for reCAPTCHA assessment. The default value is false.

**Signature:**  

    useAccountDefender?: boolean;

## RecaptchaConfig.useSmsBotScore

Whether to use the rCE bot score for reCAPTCHA phone provider. Can only be true when the phone_enforcement_state is AUDIT or ENFORCE.

**Signature:**  

    useSmsBotScore?: boolean;

## RecaptchaConfig.useSmsTollFraudProtection

Whether to use the rCE SMS toll fraud protection risk score for reCAPTCHA phone provider. Can only be true when the phone_enforcement_state is AUDIT or ENFORCE.

**Signature:**  

    useSmsTollFraudProtection?: boolean;