# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchakey.md.txt

# RecaptchaKey interface

The reCAPTCHA key config.

**Signature:**  

    export interface RecaptchaKey 

## Properties

|                                                      Property                                                      |                                                             Type                                                              |           Description           |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| [key](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchakey.md#recaptchakeykey)   | string                                                                                                                        | The reCAPTCHA site key.         |
| [type](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.recaptchakey.md#recaptchakeytype) | [RecaptchaKeyClientType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.md#recaptchakeyclienttype) | The key's client platform type. |

## RecaptchaKey.key

The reCAPTCHA site key.

**Signature:**  

    key: string;

## RecaptchaKey.type

The key's client platform type.

**Signature:**  

    type?: RecaptchaKeyClientType;