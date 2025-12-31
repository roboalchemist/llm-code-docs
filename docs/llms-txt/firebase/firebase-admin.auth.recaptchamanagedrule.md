# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchamanagedrule.md.txt

# RecaptchaManagedRule interface

The config for a reCAPTCHA action rule.

**Signature:**  

    export interface RecaptchaManagedRule 

## Properties

|                                                                  Property                                                                  |                                                      Type                                                       |                                       Description                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [action](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchamanagedrule.md#recaptchamanagedruleaction)     | [RecaptchaAction](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#recaptchaaction) | The action for reCAPTCHA-protected requests.                                             |
| [endScore](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchamanagedrule.md#recaptchamanagedruleendscore) | number                                                                                                          | The action will be enforced if the reCAPTCHA score of a request is larger than endScore. |

## RecaptchaManagedRule.action

The action for reCAPTCHA-protected requests.

**Signature:**  

    action?: RecaptchaAction;

## RecaptchaManagedRule.endScore

The action will be enforced if the reCAPTCHA score of a request is larger than endScore.

**Signature:**  

    endScore: number;