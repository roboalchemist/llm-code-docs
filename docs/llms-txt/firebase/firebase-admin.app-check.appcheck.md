# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md.txt

# AppCheck class

The Firebase `AppCheck` service interface.

**Signature:**  

    export declare class AppCheck 

## Properties

|                                                   Property                                                    | Modifiers | Type | Description |
|---------------------------------------------------------------------------------------------------------------|-----------|------|-------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckapp) |           | App  |             |

## Methods

|                                                                        Method                                                                         | Modifiers |                                                                                        Description                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [createToken(appId, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckcreatetoken)         |           | Creates a new [AppCheckToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktoken.md#appchecktoken_interface) that can be sent back to a client. |
| [verifyToken(appCheckToken, options)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appcheck.md#appcheckverifytoken) |           | Verifies a Firebase App Check token (JWT). If the token is valid, the promise is fulfilled with the token's decoded claims; otherwise, the promise is rejected.                           |

## AppCheck.app

**Signature:**  

    readonly app: App;

## AppCheck.createToken()

Creates a new [AppCheckToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktoken.md#appchecktoken_interface) that can be sent back to a client.

**Signature:**  

    createToken(appId: string, options?: AppCheckTokenOptions): Promise<AppCheckToken>;

### Parameters

| Parameter |                                                                             Type                                                                              |                         Description                          |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| appId     | string                                                                                                                                                        | The app ID to use as the JWT app_id.                         |
| options   | [AppCheckTokenOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktokenoptions.md#appchecktokenoptions_interface) | Optional options object when creating a new App Check Token. |

**Returns:**

Promise\<[AppCheckToken](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.appchecktoken.md#appchecktoken_interface)\>

A promise that fulfills with a `AppCheckToken`.

## AppCheck.verifyToken()

Verifies a Firebase App Check token (JWT). If the token is valid, the promise is fulfilled with the token's decoded claims; otherwise, the promise is rejected.

**Signature:**  

    verifyToken(appCheckToken: string, options?: VerifyAppCheckTokenOptions): Promise<VerifyAppCheckTokenResponse>;

### Parameters

|   Parameter   |                                                                                      Type                                                                                       |                                                                                                            Description                                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| appCheckToken | string                                                                                                                                                                          | The App Check token to verify.                                                                                                                                                                                                     |
| options       | [VerifyAppCheckTokenOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenoptions.md#verifyappchecktokenoptions_interface) | Optional [VerifyAppCheckTokenOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenoptions.md#verifyappchecktokenoptions_interface) object when verifying an App Check Token. |

**Returns:**

Promise\<[VerifyAppCheckTokenResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.app-check.verifyappchecktokenresponse.md#verifyappchecktokenresponse_interface)\>

A promise fulfilled with the token's decoded claims if the App Check token is valid; otherwise, a rejected promise.