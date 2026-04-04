# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenresponse.md.txt

# VerifyAppCheckTokenResponse interface

Interface representing a verified App Check token response.

**Signature:**  

    export interface VerifyAppCheckTokenResponse 

## Properties

|                                                                                  Property                                                                                   |                                                                             Type                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [alreadyConsumed](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenresponse.md#verifyappchecktokenresponsealreadyconsumed) | boolean                                                                                                                                                       | Indicates weather this token was already consumed. If this is the first time [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method has seen this token, this field will contain the value `false`. The given token will then be marked as `already_consumed` for all future invocations of this [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method for this token.When this field is `true`, the caller is attempting to reuse a previously consumed token. You should take precautions against such a caller; for example, you can take actions such as rejecting the request or ask the caller to pass additional layers of security checks. |
| [appId](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenresponse.md#verifyappchecktokenresponseappid)                     | string                                                                                                                                                        | The App ID corresponding to the App the App Check token belonged to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [token](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenresponse.md#verifyappchecktokenresponsetoken)                     | [DecodedAppCheckToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktoken_interface) | The decoded Firebase App Check token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## VerifyAppCheckTokenResponse.alreadyConsumed

Indicates weather this token was already consumed. If this is the first time [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method has seen this token, this field will contain the value `false`. The given token will then be marked as `already_consumed` for all future invocations of this [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method for this token.

When this field is `true`, the caller is attempting to reuse a previously consumed token. You should take precautions against such a caller; for example, you can take actions such as rejecting the request or ask the caller to pass additional layers of security checks.

**Signature:**  

    alreadyConsumed?: boolean;

## VerifyAppCheckTokenResponse.appId

The App ID corresponding to the App the App Check token belonged to.

**Signature:**  

    appId: string;

## VerifyAppCheckTokenResponse.token

The decoded Firebase App Check token.

**Signature:**  

    token: DecodedAppCheckToken;