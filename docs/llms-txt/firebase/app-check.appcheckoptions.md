# Source: https://firebase.google.com/docs/reference/js/app-check.appcheckoptions.md.txt

# AppCheckOptions interface

Options for App Check initialization.

**Signature:**  

    export interface AppCheckOptions 

## Properties

|                                                                     Property                                                                     |                                                                                                                                                                                                      Type                                                                                                                                                                                                      |                                 Description                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [isTokenAutoRefreshEnabled](https://firebase.google.com/docs/reference/js/app-check.appcheckoptions.md#appcheckoptionsistokenautorefreshenabled) | boolean                                                                                                                                                                                                                                                                                                                                                                                                        | If set to true, enables automatic background refresh of App Check token.    |
| [provider](https://firebase.google.com/docs/reference/js/app-check.appcheckoptions.md#appcheckoptionsprovider)                                   | [CustomProvider](https://firebase.google.com/docs/reference/js/app-check.customprovider.md#customprovider_class) \| [ReCaptchaV3Provider](https://firebase.google.com/docs/reference/js/app-check.recaptchav3provider.md#recaptchav3provider_class) \| [ReCaptchaEnterpriseProvider](https://firebase.google.com/docs/reference/js/app-check.recaptchaenterpriseprovider.md#recaptchaenterpriseprovider_class) | A reCAPTCHA V3 provider, reCAPTCHA Enterprise provider, or custom provider. |

## AppCheckOptions.isTokenAutoRefreshEnabled

If set to true, enables automatic background refresh of App Check token.

**Signature:**  

    isTokenAutoRefreshEnabled?: boolean;

## AppCheckOptions.provider

A reCAPTCHA V3 provider, reCAPTCHA Enterprise provider, or custom provider.

**Signature:**  

    provider: CustomProvider | ReCaptchaV3Provider | ReCaptchaEnterpriseProvider;