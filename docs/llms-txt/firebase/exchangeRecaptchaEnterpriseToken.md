# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeRecaptchaEnterpriseToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeRecaptchaEnterpriseToken.md.txt

Validates a
[reCAPTCHA Enterprise response token](https://cloud.google.com/recaptcha-enterprise/docs/create-assessment#retrieve_token)
. If valid, returns an App Check token
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken)`
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1beta/{app=projects/*/apps/*}:exchangeRecaptchaEnterpriseToken
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

|                          JSON representation                          |
|-----------------------------------------------------------------------|
| ``` { "recaptchaEnterpriseToken": string, "limitedUse": boolean } ``` |

|                                                                                                                                                Fields                                                                                                                                                 ||
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` recaptchaEnterpriseToken ` | ` string ` Required. The reCAPTCHA token as returned by the [reCAPTCHA Enterprise JavaScript API](https://cloud.google.com/recaptcha-enterprise/docs/instrument-web-pages) .                                                                                            |
| ` limitedUse `               | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` . |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken)`
`
.