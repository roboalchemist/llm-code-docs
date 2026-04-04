# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.md.txt

# firebase-admin.app-check package

Firebase App Check.

## Functions

|                                                         Function                                                          |                                                                                                                                                                            Description                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getAppCheck(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.md#getappcheck_8a40afc) | Gets the [AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheck_class) service for the default app or a given app.`getAppCheck()` can be called with no arguments to access the default app's `AppCheck` service or as `getAppCheck(app)` to access the `AppCheck` service associated with a specific app. |

## Classes

|                                                         Class                                                         |                Description                 |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| [AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheck_class) | The Firebase `AppCheck` service interface. |

## Interfaces

|                                                                                     Interface                                                                                      |                                                                                                          Description                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AppCheckToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktoken.md#appchecktoken_interface)                                           | Interface representing an App Check token.                                                                                                                                                                                    |
| [AppCheckTokenOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktokenoptions.md#appchecktokenoptions_interface)                      | Interface representing App Check token options.                                                                                                                                                                               |
| [DecodedAppCheckToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.decodedappchecktoken.md#decodedappchecktoken_interface)                      | Interface representing a decoded Firebase App Check token, returned from the [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method. |
| [VerifyAppCheckTokenOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenoptions.md#verifyappchecktokenoptions_interface)    | Interface representing options for the [AppCheck.verifyToken()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) method.                                       |
| [VerifyAppCheckTokenResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenresponse.md#verifyappchecktokenresponse_interface) | Interface representing a verified App Check token response.                                                                                                                                                                   |

## getAppCheck(app)

Gets the [AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheck_class) service for the default app or a given app.

`getAppCheck()` can be called with no arguments to access the default app's `AppCheck` service or as `getAppCheck(app)` to access the `AppCheck` service associated with a specific app.

**Signature:**  

    export declare function getAppCheck(app?: App): AppCheck;

### Parameters

| Parameter | Type |                                                      Description                                                      |
|-----------|------|-----------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app for which to return the `AppCheck` service. If not provided, the default `AppCheck` service is returned. |

**Returns:**

[AppCheck](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheck_class)

The default `AppCheck` service if no app is provided, or the `AppCheck` service associated with the provided app.

### Example 1

    // Get the `AppCheck` service for the default app
    const defaultAppCheck = getAppCheck();

### Example 2

    // Get the `AppCheck` service for a given app
    const otherAppCheck = getAppCheck(otherApp);