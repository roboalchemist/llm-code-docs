# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.md.txt

# REST Resource: projects.apps

## Resource

There is no persistent data associated with this resource.

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion` | Accepts an App Attest assertion and an artifact previously obtained from `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` and verifies those with Apple. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation` | Accepts an App Attest CBOR attestation and verifies it with Apple using your preconfigured team and bundle IDs. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeCustomToken` | Validates a custom token signed using your project's Admin SDK service account credentials. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeDebugToken` | Validates a debug token secret that you have previously created using `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create#google.firebase.appcheck.v1beta.ConfigService.CreateDebugToken`. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeDeviceCheckToken` | Accepts a [`device_token`](https://developer.apple.com/documentation/devicecheck/dcdevice) issued by DeviceCheck, and attempts to validate it with Apple. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangePlayIntegrityToken` | Validates an [integrity verdict response token from Play Integrity](https://developer.android.com/google/play/integrity/verdict#decrypt-verify). |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaEnterpriseToken` | Validates a [reCAPTCHA Enterprise response token](https://cloud.google.com/recaptcha-enterprise/docs/create-assessment#retrieve_token). |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaToken (deprecated)` | Validates a [reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3). |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaV3Token` | Validates a [reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3). |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generateAppAttestChallenge` | Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAssertion`. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generatePlayIntegrityChallenge` | Generates a challenge that protects the integrity of an immediately following integrity verdict request to the Play Integrity API. |