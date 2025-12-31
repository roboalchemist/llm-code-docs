# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenoptions.md.txt

# VerifyAppCheckTokenOptions interface

Interface representing options for the [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method.

**Signature:**  

    export interface VerifyAppCheckTokenOptions 

## Properties

|                                                                         Property                                                                          |  Type   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [consume](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenoptions.md#verifyappchecktokenoptionsconsume) | boolean | To use the replay protection feature, set this to `true`. The [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method will mark the token as consumed after verifying it.Tokens that are found to be already consumed will be marked as such in the response.Tokens are only considered to be consumed if it is sent to App Check backend by calling the [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method with this field set to `true`; other uses of the token do not consume it.This replay protection feature requires an additional network call to the App Check backend and forces your clients to obtain a fresh attestation from your chosen attestation providers. This can therefore negatively impact performance and can potentially deplete your attestation providers' quotas faster. We recommend that you use this feature only for protecting low volume, security critical, or expensive operations. |

## VerifyAppCheckTokenOptions.consume

To use the replay protection feature, set this to `true`. The [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method will mark the token as consumed after verifying it.

Tokens that are found to be already consumed will be marked as such in the response.

Tokens are only considered to be consumed if it is sent to App Check backend by calling the [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method with this field set to `true`; other uses of the token do not consume it.

This replay protection feature requires an additional network call to the App Check backend and forces your clients to obtain a fresh attestation from your chosen attestation providers. This can therefore negatively impact performance and can potentially deplete your attestation providers' quotas faster. We recommend that you use this feature only for protecting low volume, security critical, or expensive operations.

**Signature:**  

    consume?: boolean;