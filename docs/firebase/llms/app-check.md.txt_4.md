# Source: https://firebase.google.com/docs/reference/js/app-check.md.txt

# app-check package

The Firebase App Check Web SDK.

Firebase App Check does not work in a Node.js environment using `ReCaptchaV3Provider` or `ReCaptchaEnterpriseProvider`, but can be used in Node.js if you use `CustomProvider` and write your own attestation method.

## Functions

| Function | Description |
|---|---|
| **function(app, ...)** |   |
| [initializeAppCheck(app, options)](https://firebase.google.com/docs/reference/js/app-check.md#initializeappcheck_5548dfc) | Activate App Check for the given app. Can be called only once per app. |
| **function(appCheckInstance, ...)** |   |
| [getLimitedUseToken(appCheckInstance)](https://firebase.google.com/docs/reference/js/app-check.md#getlimitedusetoken_53ef5e3) | Requests a Firebase App Check token. This method should be used only if you need to authorize requests to a non-Firebase backend.Returns limited-use tokens that are intended for use with your non-Firebase backend endpoints that are protected with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). This method does not affect the token generation behavior of the #getAppCheckToken() method. |
| [getToken(appCheckInstance, forceRefresh)](https://firebase.google.com/docs/reference/js/app-check.md#gettoken_39fc1b3) | Get the current App Check token. If `forceRefresh` is false, this function first checks for a valid token in memory, then local persistence (IndexedDB). If not found, or if `forceRefresh` is true, it makes a request to the App Check endpoint for a fresh token. That request attaches to the most recent in-flight request if one is present. |
| [onTokenChanged(appCheckInstance, observer)](https://firebase.google.com/docs/reference/js/app-check.md#ontokenchanged_9761e16) | Registers a listener to changes in the token state. There can be more than one listener registered at the same time for one or more App Check instances. The listeners call back on the UI thread whenever the current token associated with this App Check instance changes. |
| [onTokenChanged(appCheckInstance, onNext, onError, onCompletion)](https://firebase.google.com/docs/reference/js/app-check.md#ontokenchanged_8ef80a7) | Registers a listener to changes in the token state. There can be more than one listener registered at the same time for one or more App Check instances. The listeners call back on the UI thread whenever the current token associated with this App Check instance changes. |
| [setTokenAutoRefreshEnabled(appCheckInstance, isTokenAutoRefreshEnabled)](https://firebase.google.com/docs/reference/js/app-check.md#settokenautorefreshenabled_057a76c) | Set whether App Check will automatically refresh tokens as needed. |

## Classes

| Class | Description |
|---|---|
| [CustomProvider](https://firebase.google.com/docs/reference/js/app-check.customprovider.md#customprovider_class) | Custom provider class. |
| [ReCaptchaEnterpriseProvider](https://firebase.google.com/docs/reference/js/app-check.recaptchaenterpriseprovider.md#recaptchaenterpriseprovider_class) | App Check provider that can obtain a reCAPTCHA Enterprise token and exchange it for an App Check token. |
| [ReCaptchaV3Provider](https://firebase.google.com/docs/reference/js/app-check.recaptchav3provider.md#recaptchav3provider_class) | App Check provider that can obtain a reCAPTCHA V3 token and exchange it for an App Check token. |

## Interfaces

| Interface | Description |
|---|---|
| [AppCheck](https://firebase.google.com/docs/reference/js/app-check.appcheck.md#appcheck_interface) | The Firebase App Check service interface. |
| [AppCheckOptions](https://firebase.google.com/docs/reference/js/app-check.appcheckoptions.md#appcheckoptions_interface) | Options for App Check initialization. |
| [AppCheckToken](https://firebase.google.com/docs/reference/js/app-check.appchecktoken.md#appchecktoken_interface) | The token returned from an App Check provider. |
| [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/app-check.appchecktokenresult.md#appchecktokenresult_interface) | Result returned by `getToken()`. |
| [CustomProviderOptions](https://firebase.google.com/docs/reference/js/app-check.customprovideroptions.md#customprovideroptions_interface) | Options when creating a [CustomProvider](https://firebase.google.com/docs/reference/js/app-check.customprovider.md#customprovider_class). |

## Type Aliases

| Type Alias | Description |
|---|---|
| [AppCheckTokenListener](https://firebase.google.com/docs/reference/js/app-check.md#appchecktokenlistener) | A listener that is called whenever the App Check token changes. |

## function(app, ...)

### initializeAppCheck(app, options)

Activate App Check for the given app. Can be called only once per app.

**Signature:**

    export declare function initializeAppCheck(app: FirebaseApp | undefined, options: AppCheckOptions): AppCheck;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| app | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) \| undefined | the [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) to activate App Check for |
| options | [AppCheckOptions](https://firebase.google.com/docs/reference/js/app-check.appcheckoptions.md#appcheckoptions_interface) | App Check initialization options |

**Returns:**

[AppCheck](https://firebase.google.com/docs/reference/js/app-check.appcheck.md#appcheck_interface)

## function(appCheckInstance, ...)

### getLimitedUseToken(appCheckInstance)

Requests a Firebase App Check token. This method should be used only if you need to authorize requests to a non-Firebase backend.

Returns limited-use tokens that are intended for use with your non-Firebase backend endpoints that are protected with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). This method does not affect the token generation behavior of the #getAppCheckToken() method.

**Signature:**

    export declare function getLimitedUseToken(appCheckInstance: AppCheck): Promise<AppCheckTokenResult>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| appCheckInstance | [AppCheck](https://firebase.google.com/docs/reference/js/app-check.appcheck.md#appcheck_interface) | The App Check service instance. |

**Returns:**

Promise\<[AppCheckTokenResult](https://firebase.google.com/docs/reference/js/app-check.appchecktokenresult.md#appchecktokenresult_interface)\>

The limited use token.

### getToken(appCheckInstance, forceRefresh)

Get the current App Check token. If `forceRefresh` is false, this function first checks for a valid token in memory, then local persistence (IndexedDB). If not found, or if `forceRefresh` is true, it makes a request to the App Check endpoint for a fresh token. That request attaches to the most recent in-flight request if one is present.

**Signature:**

    export declare function getToken(appCheckInstance: AppCheck, forceRefresh?: boolean): Promise<AppCheckTokenResult>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| appCheckInstance | [AppCheck](https://firebase.google.com/docs/reference/js/app-check.appcheck.md#appcheck_interface) | The App Check service instance. |
| forceRefresh | boolean | If true, will always try to fetch a fresh token. If false, will use a cached token if found in storage. |

**Returns:**

Promise\<[AppCheckTokenResult](https://firebase.google.com/docs/reference/js/app-check.appchecktokenresult.md#appchecktokenresult_interface)\>

### onTokenChanged(appCheckInstance, observer)

Registers a listener to changes in the token state. There can be more than one listener registered at the same time for one or more App Check instances. The listeners call back on the UI thread whenever the current token associated with this App Check instance changes.

**Signature:**

    export declare function onTokenChanged(appCheckInstance: AppCheck, observer: PartialObserver<AppCheckTokenResult>): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| appCheckInstance | [AppCheck](https://firebase.google.com/docs/reference/js/app-check.appcheck.md#appcheck_interface) | The App Check service instance. |
| observer | [PartialObserver](https://firebase.google.com/docs/reference/js/util.md#partialobserver)\<[AppCheckTokenResult](https://firebase.google.com/docs/reference/js/app-check.appchecktokenresult.md#appchecktokenresult_interface)\> | An object with `next`, `error`, and `complete` properties. `next` is called with an [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/app-check.appchecktokenresult.md#appchecktokenresult_interface) whenever the token changes. `error` is optional and is called if an error is thrown by the listener (the `next` function). `complete` is unused, as the token stream is unending. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

A function that unsubscribes this listener.

### onTokenChanged(appCheckInstance, onNext, onError, onCompletion)

Registers a listener to changes in the token state. There can be more than one listener registered at the same time for one or more App Check instances. The listeners call back on the UI thread whenever the current token associated with this App Check instance changes.

**Signature:**

    export declare function onTokenChanged(appCheckInstance: AppCheck, onNext: (tokenResult: AppCheckTokenResult) => void, onError?: (error: Error) => void, onCompletion?: () => void): Unsubscribe;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| appCheckInstance | [AppCheck](https://firebase.google.com/docs/reference/js/app-check.appcheck.md#appcheck_interface) | The App Check service instance. |
| onNext | (tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/app-check.appchecktokenresult.md#appchecktokenresult_interface)) =\> void | When the token changes, this function is called with an [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/app-check.appchecktokenresult.md#appchecktokenresult_interface). |
| onError | (error: Error) =\> void | Optional. Called if there is an error thrown by the listener (the `onNext` function). |
| onCompletion | () =\> void | Currently unused, as the token stream is unending. |

**Returns:**

[Unsubscribe](https://firebase.google.com/docs/reference/js/util.md#unsubscribe)

A function that unsubscribes this listener.

### setTokenAutoRefreshEnabled(appCheckInstance, isTokenAutoRefreshEnabled)

Set whether App Check will automatically refresh tokens as needed.

**Signature:**

    export declare function setTokenAutoRefreshEnabled(appCheckInstance: AppCheck, isTokenAutoRefreshEnabled: boolean): void;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| appCheckInstance | [AppCheck](https://firebase.google.com/docs/reference/js/app-check.appcheck.md#appcheck_interface) | The App Check service instance. |
| isTokenAutoRefreshEnabled | boolean | If true, the SDK automatically refreshes App Check tokens as needed. This overrides any value set during `initializeAppCheck()`. |

**Returns:**

void

## AppCheckTokenListener

A listener that is called whenever the App Check token changes.

**Signature:**

    export type AppCheckTokenListener = (token: AppCheckTokenResult) => void;