# Source: https://firebase.google.com/docs/reference/node/firebase.auth.AuthSettings.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthSettings.md.txt

# AuthSettings | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [auth](https://firebase.google.com/docs/reference/js/v8/firebase.auth).
- AuthSettings

Interface representing an Auth instance's settings, currently used for
enabling/disabling app verification for phone Auth testing.

## Index

### Properties

- [appVerificationDisabledForTesting](https://firebase.google.com/docs/reference/js/v8/firebase.auth.AuthSettings#appverificationdisabledfortesting)

## Properties

### appVerificationDisabledForTesting

appVerificationDisabledForTesting: boolean  
When set, this property disables app verification for the purpose of testing
phone authentication. For this property to take effect, it needs to be set
before rendering a reCAPTCHA app verifier. When this is disabled, a
mock reCAPTCHA is rendered instead. This is useful for manual testing during
development or for automated integration tests.

In order to use this feature, you will need to
[whitelist your phone number](https://firebase.google.com/docs/auth/web/phone-auth#test-with-whitelisted-phone-numbers) via the
Firebase Console.

The default value is false (app verification is enabled).