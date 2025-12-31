# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaToken.md.txt

| This method is deprecated; it has been renamed to
| `
| `[ExchangeRecaptchaV3Token](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaV3Token#google.firebase.appcheck.v1beta.TokenExchangeService.ExchangeRecaptchaV3Token)`
| `
| .

Validates a
[reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3)
. If valid, returns an
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken)`
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1beta/{app=projects/*/apps/*}:exchangeRecaptchaToken
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

|                                                                                                                                                                        Parameters                                                                                                                                                                        ||
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` app ` | ` string ` Required. The relative resource name of the web app, in the format: projects/{project_number}/apps/{app_id} If necessary, the ` project_number ` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body


The request body contains data with the following structure:

|         JSON representation          |
|--------------------------------------|
| ``` { "recaptchaToken": string } ``` |

|                                                                              Fields                                                                              ||
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ` recaptchaToken ` | ` string ` Required. The reCAPTCHA token as returned by the [reCAPTCHA v3 JavaScript API](https://developers.google.com/recaptcha/docs/v3) . |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken)`
`
.