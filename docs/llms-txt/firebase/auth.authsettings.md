# Source: https://firebase.google.com/docs/reference/js/auth.authsettings.md.txt

# AuthSettings interface

Interface representing an [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance's settings.

Currently used for enabling/disabling app verification for phone Auth testing.

**Signature:**  

    export interface AuthSettings 

## Properties

|                                                                       Property                                                                        |  Type   |                                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [appVerificationDisabledForTesting](https://firebase.google.com/docs/reference/js/auth.authsettings.md#authsettingsappverificationdisabledfortesting) | boolean | When set, this property disables app verification for the purpose of testing phone authentication. For this property to take effect, it needs to be set before rendering a reCAPTCHA app verifier. When this is disabled, a mock reCAPTCHA is rendered instead. This is useful for manual testing during development or for automated integration tests.In order to use this feature, you will need to [whitelist your phone number](https://firebase.google.com/docs/auth/web/phone-auth#test-with-whitelisted-phone-numbers) via the Firebase Console.The default value is false (app verification is enabled). |

## AuthSettings.appVerificationDisabledForTesting

When set, this property disables app verification for the purpose of testing phone authentication. For this property to take effect, it needs to be set before rendering a reCAPTCHA app verifier. When this is disabled, a mock reCAPTCHA is rendered instead. This is useful for manual testing during development or for automated integration tests.

In order to use this feature, you will need to [whitelist your phone number](https://firebase.google.com/docs/auth/web/phone-auth#test-with-whitelisted-phone-numbers) via the Firebase Console.

The default value is false (app verification is enabled).

**Signature:**  

    appVerificationDisabledForTesting: boolean;