# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/projects.apps/exchangeDeviceCheckToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps/exchangeDeviceCheckToken.md.txt

Accepts a
[`
deviceToken
`](https://developer.apple.com/documentation/devicecheck/dcdevice)
issued by DeviceCheck, and attempts to validate it with Apple. If valid, returns an
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.

### HTTP request


`
POST https://firebaseappcheck.googleapis.com/v1/{app=projects/*/apps/*}:exchangeDeviceCheckToken
`


The URL uses
[gRPC Transcoding](https://google.aip.dev/127)
syntax.

### Path parameters

|                                                                                                                                                                        Parameters                                                                                                                                                                        ||
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` app ` | ` string ` Required. The relative resource name of the iOS app, in the format: projects/{project_number}/apps/{app_id} If necessary, the ` project_number ` element can be replaced with the project ID of the Firebase project. Learn more about using project identifiers in Google's [AIP 2510](https://google.aip.dev/cloud/2510) standard. |

### Request body


The request body contains data with the following structure:

|                   JSON representation                    |
|----------------------------------------------------------|
| ``` { "deviceToken": string, "limitedUse": boolean } ``` |

|                                                                                                                                          Fields                                                                                                                                          ||
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ` deviceToken ` | ` string ` Required. The ` deviceToken ` as returned by Apple's client-side [DeviceCheck API](https://developer.apple.com/documentation/devicecheck/dcdevice) . This is the base64 encoded ` Data ` (Swift) or ` NSData ` (ObjC) object.                                |
| ` limitedUse `  | ` boolean ` Specifies whether this attestation is for use in a *limited use* ( ` true ` ) or *session based* ( ` false ` ) context. To enable this attestation to be used with the *replay protection* feature, set this to ` true ` . The default value is ` false ` . |

### Response body


If successful, the response body contains an instance of
`
`[AppCheckToken](https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken)`
`
.