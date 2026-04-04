# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md.txt

# DecodedAppCheckToken interface

Interface representing a decoded Firebase App Check token, returned from the [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method.

**Signature:**  

    export interface DecodedAppCheckToken 

## Properties

|                                                                  Property                                                                   |    Type    |                                                                                                                                                                                Description                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [app_id](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokenapp_id) | string     | The App ID corresponding to the App the App Check token belonged to. This value is not actually one of the JWT token claims. It is added as a convenience, and is set as the value of the [sub](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokensub) property.                                  |
| [aud](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokenaud)       | string\[\] | The audience for which this token is intended. This value is a JSON array of two strings, the first is the project number of your Firebase project, and the second is the project ID of the same project.                                                                                                                                                                  |
| [exp](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokenexp)       | number     | The App Check token's expiration time, in seconds since the Unix epoch. That is, the time at which this App Check token expires and should no longer be considered valid.                                                                                                                                                                                                  |
| [iat](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokeniat)       | number     | The App Check token's issued-at time, in seconds since the Unix epoch. That is, the time at which this App Check token was issued and should start to be considered valid.                                                                                                                                                                                                 |
| [iss](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokeniss)       | string     | The issuer identifier for the issuer of the response. This value is a URL with the format `https://firebaseappcheck.googleapis.com/<PROJECT_NUMBER>`, where `<PROJECT_NUMBER>` is the same project number specified in the [aud](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokenaud) property. |
| [sub](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokensub)       | string     | The Firebase App ID corresponding to the app the token belonged to. As a convenience, this value is copied over to the [app_id](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokenapp_id) property.                                                                                               |

## DecodedAppCheckToken.app_id

The App ID corresponding to the App the App Check token belonged to. This value is not actually one of the JWT token claims. It is added as a convenience, and is set as the value of the [sub](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokensub) property.

**Signature:**  

    app_id: string;

## DecodedAppCheckToken.aud

The audience for which this token is intended. This value is a JSON array of two strings, the first is the project number of your Firebase project, and the second is the project ID of the same project.

**Signature:**  

    aud: string[];

## DecodedAppCheckToken.exp

The App Check token's expiration time, in seconds since the Unix epoch. That is, the time at which this App Check token expires and should no longer be considered valid.

**Signature:**  

    exp: number;

## DecodedAppCheckToken.iat

The App Check token's issued-at time, in seconds since the Unix epoch. That is, the time at which this App Check token was issued and should start to be considered valid.

**Signature:**  

    iat: number;

## DecodedAppCheckToken.iss

The issuer identifier for the issuer of the response. This value is a URL with the format `https://firebaseappcheck.googleapis.com/<PROJECT_NUMBER>`, where `<PROJECT_NUMBER>` is the same project number specified in the [aud](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokenaud) property.

**Signature:**  

    iss: string;

## DecodedAppCheckToken.sub

The Firebase App ID corresponding to the app the token belonged to. As a convenience, this value is copied over to the [app_id](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktokenapp_id) property.

**Signature:**  

    sub: string;