# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients.md.txt

# REST Resource: oauthClients

## Resource

There is no persistent data associated with this resource.

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeAppAttestAssertion` | Accepts an App Attest assertion and an artifact previously obtained from `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` and verifies those with Apple. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeAppAttestAttestation` | Accepts an App Attest CBOR attestation and verifies it with Apple using your preconfigured team and bundle IDs. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeDebugToken` | Validates a debug token secret that you have previously created using `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create#google.firebase.appcheck.v1beta.ConfigService.CreateDebugToken`. |
| ### `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/generateAppAttestChallenge` | Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAssertion`. |