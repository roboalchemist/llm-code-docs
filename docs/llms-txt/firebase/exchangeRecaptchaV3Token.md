# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaV3Token.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeRecaptchaV3Token.md.txt

Validates a
[reCAPTCHA v3 response token](https://developers.google.com/recaptcha/docs/v3)
. If valid, returns an
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1/{app=projects/*/apps/*}:exchangeRecaptchaV3Token
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

|                      JSON representation                      |
|---------------------------------------------------------------|
| ``` { "recaptchaV3Token": string, "limitedUse": boolean } ``` |

|                                                                                                                                            Fields                                                                                                                                             ||
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` recaptchaV3Token ` | ` string ` Required. The reCAPTCHA token as returned by the [reCAPTCHA v3 JavaScript API](https://developers.google.com/recaptcha/docs/v3) .                                                                                                                            |
| ` limitedUse `       | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` . |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.