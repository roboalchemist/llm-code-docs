# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md.txt

# https.CallableOptions interface

Options that can be set on a callable HTTPS function.

**Signature:**  

    export interface CallableOptions<T = any> extends HttpsOptions 

**Extends:** [HttpsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptions_interface)

## Properties

|                                                                                    Property                                                                                    |                                Type                                 |                                                                                                 Description                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [authPolicy](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md#httpscallableoptionsauthpolicy)                     | (auth: AuthData \| null, data: T) =\> boolean \| Promise\<boolean\> | (Deprecated) Callback for whether a request is authorized.Designed to allow reusable auth policies to be passed as an options object. Two built-in reusable policies exist: isSignedIn and hasClaim.        |
| [consumeAppCheckToken](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md#httpscallableoptionsconsumeappchecktoken) | boolean                                                             | Determines whether Firebase App Check token is consumed on request. Defaults to false.                                                                                                                      |
| [enforceAppCheck](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md#httpscallableoptionsenforceappcheck)           | boolean                                                             | Determines whether Firebase AppCheck is enforced. When true, requests with invalid tokens autorespond with a 401 (Unauthorized) error. When false, requests with invalid tokens set event.app to undefiend. |
| [heartbeatSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callableoptions.md#httpscallableoptionsheartbeatseconds)         | number \| null                                                      | Time in seconds between sending heartbeat messages to keep the connection alive. Set to `null` to disable heartbeats.Defaults to 30 seconds.                                                                |

## https.CallableOptions.authPolicy

> | **Warning:** This API is now obsolete.

(Deprecated) Callback for whether a request is authorized.

Designed to allow reusable auth policies to be passed as an options object. Two built-in reusable policies exist: isSignedIn and hasClaim.

**Signature:**  

    authPolicy?: (auth: AuthData | null, data: T) => boolean | Promise<boolean>;

## https.CallableOptions.consumeAppCheckToken

Determines whether Firebase App Check token is consumed on request. Defaults to false.

Set this to true to enable the App Check replay protection feature by consuming the App Check token on callable request. Tokens that are found to be already consumed will have request.app.alreadyConsumed property set true.

Tokens are only considered to be consumed if it is sent to the App Check service by setting this option to true. Other uses of the token do not consume it.

This replay protection feature requires an additional network call to the App Check backend and forces the clients to obtain a fresh attestation from the chosen attestation providers. This can therefore negatively impact performance and can potentially deplete your attestation providers' quotas faster. Use this feature only for protecting low volume, security critical, or expensive operations.

This option does not affect the enforceAppCheck option. Setting the latter to true will cause the callable function to automatically respond with a 401 Unauthorized status code when request includes an invalid App Check token. When request includes valid but consumed App Check tokens, requests will not be automatically rejected. Instead, the request.app.alreadyConsumed property will be set to true and pass the execution to the handler code for making further decisions, such as requiring additional security checks or rejecting the request.

**Signature:**  

    consumeAppCheckToken?: boolean;

## https.CallableOptions.enforceAppCheck

Determines whether Firebase AppCheck is enforced. When true, requests with invalid tokens autorespond with a 401 (Unauthorized) error. When false, requests with invalid tokens set event.app to undefiend.

**Signature:**  

    enforceAppCheck?: boolean;

## https.CallableOptions.heartbeatSeconds

Time in seconds between sending heartbeat messages to keep the connection alive. Set to `null` to disable heartbeats.

Defaults to 30 seconds.

**Signature:**  

    heartbeatSeconds?: number | null;