# Source: https://firebase.google.com/docs/reference/appcheck/rest.md.txt

# Firebase App Check API

Firebase App Check works alongside other Firebase services to help protect your backend resources from abuse, such as billing fraud or phishing.

## Service: firebaseappcheck.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

- <https://firebaseappcheck.googleapis.com/$discovery/rest?version=v1>
- <https://firebaseappcheck.googleapis.com/$discovery/rest?version=v1beta>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebaseappcheck.googleapis.com`

## REST Resource: [v1beta.jwks](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/jwks)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/jwks/get` | `GET /v1beta/{name=jwks}` Returns a public JWK set as specified by [RFC 7517](https://tools.ietf.org/html/rfc7517) that can be used to verify App Check tokens. |

## REST Resource: [v1beta.oauthClients](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeAppAttestAssertion` | `POST /v1beta/{app=oauthClients/*}:exchangeAppAttestAssertion` Accepts an App Attest assertion and an artifact previously obtained from `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` and verifies those with Apple. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeAppAttestAttestation` | `POST /v1beta/{app=oauthClients/*}:exchangeAppAttestAttestation` Accepts an App Attest CBOR attestation and verifies it with Apple using your preconfigured team and bundle IDs. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/exchangeDebugToken` | `POST /v1beta/{app=oauthClients/*}:exchangeDebugToken` Validates a debug token secret that you have previously created using `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create#google.firebase.appcheck.v1beta.ConfigService.CreateDebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/oauthClients/generateAppAttestChallenge` | `POST /v1beta/{app=oauthClients/*}:generateAppAttestChallenge` Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAssertion`. |

## REST Resource: [v1beta.projects](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects/verifyAppCheckToken` | `POST /v1beta/{project=projects/*}:verifyAppCheckToken` Verifies the given App Check token and returns token usage signals that callers may act upon. |

## REST Resource: [v1beta.projects.apps](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion` | `POST /v1beta/{app=projects/*/apps/*}:exchangeAppAttestAssertion` Accepts an App Attest assertion and an artifact previously obtained from `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` and verifies those with Apple. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation` | `POST /v1beta/{app=projects/*/apps/*}:exchangeAppAttestAttestation` Accepts an App Attest CBOR attestation and verifies it with Apple using your preconfigured team and bundle IDs. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeCustomToken` | `POST /v1beta/{app=projects/*/apps/*}:exchangeCustomToken` Validates a custom token signed using your project's Admin SDK service account credentials. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeDebugToken` | `POST /v1beta/{app=projects/*/apps/*}:exchangeDebugToken` Validates a debug token secret that you have previously created using `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create#google.firebase.appcheck.v1beta.ConfigService.CreateDebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeDeviceCheckToken` | `POST /v1beta/{app=projects/*/apps/*}:exchangeDeviceCheckToken` Accepts a [`device_token`](https://developer.apple.com/documentation/devicecheck/dcdevice) issued by DeviceCheck, and attempts to validate it with Apple. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangePlayIntegrityToken` | `POST /v1beta/{app=projects/*/apps/*}:exchangePlayIntegrityToken` Validates an [integrity verdict response token from Play Integrity](https://developer.android.com/google/play/integrity/verdict#decrypt-verify). |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaEnterpriseToken` | `POST /v1beta/{app=projects/*/apps/*}:exchangeRecaptchaEnterpriseToken` Validates a [reCAPTCHA Enterprise response token](https://cloud.google.com/recaptcha-enterprise/docs/create-assessment#retrieve_token). |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaToken (deprecated)` | `POST /v1beta/{app=projects/*/apps/*}:exchangeRecaptchaToken` Validates a [reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3). |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaV3Token` | `POST /v1beta/{app=projects/*/apps/*}:exchangeRecaptchaV3Token` Validates a [reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3). |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generateAppAttestChallenge` | `POST /v1beta/{app=projects/*/apps/*}:generateAppAttestChallenge` Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeAppAttestAssertion`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/generatePlayIntegrityChallenge` | `POST /v1beta/{app=projects/*/apps/*}:generatePlayIntegrityChallenge` Generates a challenge that protects the integrity of an immediately following integrity verdict request to the Play Integrity API. |

## REST Resource: [v1beta.projects.apps.appAttestConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.appAttestConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.appAttestConfig/batchGet` | `GET /v1beta/{parent=projects/*}/apps/-/appAttestConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.appAttestConfig#AppAttestConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.appAttestConfig/get` | `GET /v1beta/{name=projects/*/apps/*/appAttestConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.appAttestConfig#AppAttestConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.appAttestConfig/patch` | `PATCH /v1beta/{appAttestConfig.name=projects/*/apps/*/appAttestConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.appAttestConfig#AppAttestConfig` for the specified app. |

## REST Resource: [v1beta.projects.apps.debugTokens](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/create` | `POST /v1beta/{parent=projects/*/apps/*}/debugTokens` Creates a new `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/delete` | `DELETE /v1beta/{name=projects/*/apps/*/debugTokens/*}` Deletes the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/get` | `GET /v1beta/{name=projects/*/apps/*/debugTokens/*}` Gets the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/list` | `GET /v1beta/{parent=projects/*/apps/*}/debugTokens` Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`s for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens/patch` | `PATCH /v1beta/{debugToken.name=projects/*/apps/*/debugTokens/*}` Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.debugTokens#DebugToken`. |

## REST Resource: [v1beta.projects.apps.deviceCheckConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig/batchGet` | `GET /v1beta/{parent=projects/*}/apps/-/deviceCheckConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig/get` | `GET /v1beta/{name=projects/*/apps/*/deviceCheckConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig/patch` | `PATCH /v1beta/{deviceCheckConfig.name=projects/*/apps/*/deviceCheckConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.deviceCheckConfig#DeviceCheckConfig` for the specified app. |

## REST Resource: [v1beta.projects.apps.playIntegrityConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig/batchGet` | `GET /v1beta/{parent=projects/*}/apps/-/playIntegrityConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig/get` | `GET /v1beta/{name=projects/*/apps/*/playIntegrityConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig/patch` | `PATCH /v1beta/{playIntegrityConfig.name=projects/*/apps/*/playIntegrityConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.playIntegrityConfig#PlayIntegrityConfig` for the specified app. |

## REST Resource: [v1beta.projects.apps.recaptchaConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig/batchGet (deprecated)` | `GET /v1beta/{parent=projects/*}/apps/-/recaptchaConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig/get (deprecated)` | `GET /v1beta/{name=projects/*/apps/*/recaptchaConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig/patch (deprecated)` | `PATCH /v1beta/{recaptchaConfig.name=projects/*/apps/*/recaptchaConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaConfig#RecaptchaConfig` for the specified app. |

## REST Resource: [v1beta.projects.apps.recaptchaEnterpriseConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig/batchGet` | `GET /v1beta/{parent=projects/*}/apps/-/recaptchaEnterpriseConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig/get` | `GET /v1beta/{name=projects/*/apps/*/recaptchaEnterpriseConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig/patch` | `PATCH /v1beta/{recaptchaEnterpriseConfig.name=projects/*/apps/*/recaptchaEnterpriseConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` for the specified app. |

## REST Resource: [v1beta.projects.apps.recaptchaV3Config](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config/batchGet` | `GET /v1beta/{parent=projects/*}/apps/-/recaptchaV3Config:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config#RecaptchaV3Config`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config/get` | `GET /v1beta/{name=projects/*/apps/*/recaptchaV3Config}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config#RecaptchaV3Config` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config/patch` | `PATCH /v1beta/{recaptchaV3Config.name=projects/*/apps/*/recaptchaV3Config}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps.recaptchaV3Config#RecaptchaV3Config` for the specified app. |

## REST Resource: [v1beta.projects.services](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/batchUpdate` | `POST /v1beta/{parent=projects/*}/services:batchUpdate` Atomically updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configurations. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/get` | `GET /v1beta/{name=projects/*/services/*}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configuration for the specified service name. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/list` | `GET /v1beta/{parent=projects/*}/services` Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configurations for the specified project. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services/patch` | `PATCH /v1beta/{service.name=projects/*/services/*}` Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services#Service` configuration. |

## REST Resource: [v1beta.projects.services.resourcePolicies](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/batchUpdate` | `POST /v1beta/{parent=projects/*/services/*}/resourcePolicies:batchUpdate` Atomically updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configurations. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/create` | `POST /v1beta/{parent=projects/*/services/*}/resourcePolicies` Creates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configuration. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/delete` | `DELETE /v1beta/{name=projects/*/services/*/resourcePolicies/*}` Deletes the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configuration. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/get` | `GET /v1beta/{name=projects/*/services/*/resourcePolicies/*}` Gets the requested `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configuration. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/list` | `GET /v1beta/{parent=projects/*/services/*}/resourcePolicies` Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configurations for the specified project and service. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies/patch` | `PATCH /v1beta/{resourcePolicy.name=projects/*/services/*/resourcePolicies/*}` Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.services.resourcePolicies#ResourcePolicy` configuration. |

## REST Resource: [v1.jwks](https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/jwks/get` | `GET /v1/{name=jwks}` Returns a public JWK set as specified by [RFC 7517](https://tools.ietf.org/html/rfc7517) that can be used to verify App Check tokens. |

## REST Resource: [v1.oauthClients](https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/exchangeAppAttestAssertion` | `POST /v1/{app=oauthClients/*}:exchangeAppAttestAssertion` Accepts an App Attest assertion and an artifact previously obtained from `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation` and verifies those with Apple. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/exchangeAppAttestAttestation` | `POST /v1/{app=oauthClients/*}:exchangeAppAttestAttestation` Accepts an App Attest CBOR attestation and verifies it with Apple using your preconfigured team and bundle IDs. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/exchangeDebugToken` | `POST /v1/{app=oauthClients/*}:exchangeDebugToken` Validates a debug token secret that you have previously created using `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/create#google.firebase.appcheck.v1.ConfigService.CreateDebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/oauthClients/generateAppAttestChallenge` | `POST /v1/{app=oauthClients/*}:generateAppAttestChallenge` Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAssertion`. |

## REST Resource: [v1.projects.apps](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion` | `POST /v1/{app=projects/*/apps/*}:exchangeAppAttestAssertion` Accepts an App Attest assertion and an artifact previously obtained from `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation` and verifies those with Apple. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation` | `POST /v1/{app=projects/*/apps/*}:exchangeAppAttestAttestation` Accepts an App Attest CBOR attestation and verifies it with Apple using your preconfigured team and bundle IDs. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeCustomToken` | `POST /v1/{app=projects/*/apps/*}:exchangeCustomToken` Validates a custom token signed using your project's Admin SDK service account credentials. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeDebugToken` | `POST /v1/{app=projects/*/apps/*}:exchangeDebugToken` Validates a debug token secret that you have previously created using `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/create#google.firebase.appcheck.v1.ConfigService.CreateDebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeDeviceCheckToken` | `POST /v1/{app=projects/*/apps/*}:exchangeDeviceCheckToken` Accepts a [`device_token`](https://developer.apple.com/documentation/devicecheck/dcdevice) issued by DeviceCheck, and attempts to validate it with Apple. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangePlayIntegrityToken` | `POST /v1/{app=projects/*/apps/*}:exchangePlayIntegrityToken` Validates an [integrity verdict response token from Play Integrity](https://developer.android.com/google/play/integrity/verdict#decrypt-verify). |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeRecaptchaEnterpriseToken` | `POST /v1/{app=projects/*/apps/*}:exchangeRecaptchaEnterpriseToken` Validates a [reCAPTCHA Enterprise response token](https://cloud.google.com/recaptcha-enterprise/docs/create-assessment#retrieve_token). |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeRecaptchaV3Token` | `POST /v1/{app=projects/*/apps/*}:exchangeRecaptchaV3Token` Validates a [reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3). |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/generateAppAttestChallenge` | `POST /v1/{app=projects/*/apps/*}:generateAppAttestChallenge` Generates a challenge that protects the integrity of an immediately following call to `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAttestation#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAttestation` or `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeAppAttestAssertion#google.firebase.appcheck.v1.TokenExchangeService.ExchangeAppAttestAssertion`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/generatePlayIntegrityChallenge` | `POST /v1/{app=projects/*/apps/*}:generatePlayIntegrityChallenge` Generates a challenge that protects the integrity of an immediately following integrity verdict request to the Play Integrity API. |

## REST Resource: [v1.projects.apps.appAttestConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/batchGet` | `GET /v1/{parent=projects/*}/apps/-/appAttestConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/get` | `GET /v1/{name=projects/*/apps/*/appAttestConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig/patch` | `PATCH /v1/{appAttestConfig.name=projects/*/apps/*/appAttestConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig#AppAttestConfig` for the specified app. |

## REST Resource: [v1.projects.apps.debugTokens](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/create` | `POST /v1/{parent=projects/*/apps/*}/debugTokens` Creates a new `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/delete` | `DELETE /v1/{name=projects/*/apps/*/debugTokens/*}` Deletes the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/get` | `GET /v1/{name=projects/*/apps/*/debugTokens/*}` Gets the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken`. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/list` | `GET /v1/{parent=projects/*/apps/*}/debugTokens` Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken`s for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens/patch` | `PATCH /v1/{debugToken.name=projects/*/apps/*/debugTokens/*}` Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens#DebugToken`. |

## REST Resource: [v1.projects.apps.deviceCheckConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig/batchGet` | `GET /v1/{parent=projects/*}/apps/-/deviceCheckConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig#DeviceCheckConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig/get` | `GET /v1/{name=projects/*/apps/*/deviceCheckConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig#DeviceCheckConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig/patch` | `PATCH /v1/{deviceCheckConfig.name=projects/*/apps/*/deviceCheckConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig#DeviceCheckConfig` for the specified app. |

## REST Resource: [v1.projects.apps.playIntegrityConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/batchGet` | `GET /v1/{parent=projects/*}/apps/-/playIntegrityConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/get` | `GET /v1/{name=projects/*/apps/*/playIntegrityConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig/patch` | `PATCH /v1/{playIntegrityConfig.name=projects/*/apps/*/playIntegrityConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig#PlayIntegrityConfig` for the specified app. |

## REST Resource: [v1.projects.apps.recaptchaEnterpriseConfig](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig/batchGet` | `GET /v1/{parent=projects/*}/apps/-/recaptchaEnterpriseConfig:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig/get` | `GET /v1/{name=projects/*/apps/*/recaptchaEnterpriseConfig}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig/patch` | `PATCH /v1/{recaptchaEnterpriseConfig.name=projects/*/apps/*/recaptchaEnterpriseConfig}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig#RecaptchaEnterpriseConfig` for the specified app. |

## REST Resource: [v1.projects.apps.recaptchaV3Config](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config/batchGet` | `GET /v1/{parent=projects/*}/apps/-/recaptchaV3Config:batchGet` Atomically gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config`s for the specified list of apps. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config/get` | `GET /v1/{name=projects/*/apps/*/recaptchaV3Config}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config` for the specified app. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config/patch` | `PATCH /v1/{recaptchaV3Config.name=projects/*/apps/*/recaptchaV3Config}` Updates the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config#RecaptchaV3Config` for the specified app. |

## REST Resource: [v1.projects.services](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/batchUpdate` | `POST /v1/{parent=projects/*}/services:batchUpdate` Atomically updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service` configurations. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/get` | `GET /v1/{name=projects/*/services/*}` Gets the `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service` configuration for the specified service name. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/list` | `GET /v1/{parent=projects/*}/services` Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service` configurations for the specified project. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services/patch` | `PATCH /v1/{service.name=projects/*/services/*}` Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services#Service` configuration. |

## REST Resource: [v1.projects.services.resourcePolicies](https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/batchUpdate` | `POST /v1/{parent=projects/*/services/*}/resourcePolicies:batchUpdate` Atomically updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configurations. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/create` | `POST /v1/{parent=projects/*/services/*}/resourcePolicies` Creates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configuration. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/delete` | `DELETE /v1/{name=projects/*/services/*/resourcePolicies/*}` Deletes the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configuration. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/get` | `GET /v1/{name=projects/*/services/*/resourcePolicies/*}` Gets the requested `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configuration. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/list` | `GET /v1/{parent=projects/*/services/*}/resourcePolicies` Lists all `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configurations for the specified project and service. |
| `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies/patch` | `PATCH /v1/{resourcePolicy.name=projects/*/services/*/resourcePolicies/*}` Updates the specified `https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services.resourcePolicies#ResourcePolicy` configuration. |