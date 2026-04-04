# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchatollfraudmanagedrule.md.txt

# RecaptchaTollFraudManagedRule interface

The managed rules for toll fraud provider, containing the enforcement status. The toll fraud provider contains all SMS related user flows.

**Signature:**  

    export interface RecaptchaTollFraudManagedRule 

## Properties

|                                                                             Property                                                                             |                                                      Type                                                       |                                        Description                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [action](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchatollfraudmanagedrule.md#recaptchatollfraudmanagedruleaction)         | [RecaptchaAction](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#recaptchaaction) | The action for reCAPTCHA-protected requests.                                               |
| [startScore](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchatollfraudmanagedrule.md#recaptchatollfraudmanagedrulestartscore) | number                                                                                                          | The action will be enforced if the reCAPTCHA score of a request is larger than startScore. |

## RecaptchaTollFraudManagedRule.action

The action for reCAPTCHA-protected requests.

**Signature:**  

    action?: RecaptchaAction;

## RecaptchaTollFraudManagedRule.startScore

The action will be enforced if the reCAPTCHA score of a request is larger than startScore.

**Signature:**  

    startScore: number;