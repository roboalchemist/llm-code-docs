# Source: https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck.md.txt

# AppCheck | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [appCheck](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck).
- AppCheck

The Firebase AppCheck service interface.

Do not call this constructor directly. Instead, use
[`firebase.appCheck()`](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck).

## Index

### Methods

- [activate](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck#activate)
- [getToken](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck#gettoken)
- [onTokenChanged](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck#ontokenchanged)
- [setTokenAutoRefreshEnabled](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheck#settokenautorefreshenabled)

## Methods

### activate

- activate ( provider : [ReCaptchaV3Provider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.ReCaptchaV3Provider) \| [ReCaptchaEnterpriseProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.ReCaptchaEnterpriseProvider) \| [CustomProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.CustomProvider) \| [AppCheckProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckProvider) \| { getToken : ( ) =\> [AppCheckToken](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckToken) } \| string , isTokenAutoRefreshEnabled ? : boolean ) : void
- Activate AppCheck

  #### Parameters

  -

    ##### provider: [ReCaptchaV3Provider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.ReCaptchaV3Provider) \| [ReCaptchaEnterpriseProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.ReCaptchaEnterpriseProvider) \| [CustomProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.CustomProvider) \| [AppCheckProvider](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckProvider) \| { getToken: () =\> [AppCheckToken](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckToken) } \| string

    This can be a `ReCaptchaV3Provider` instance,
    a `ReCaptchaEnterpriseProvider` instance, a `CustomProvider` instance,
    an object with a custom `getToken()` method, or a reCAPTCHA site key.
  -

    ##### Optional isTokenAutoRefreshEnabled: boolean

    If true, the SDK automatically
    refreshes App Check tokens as needed. If undefined, defaults to the
    value of `app.automaticDataCollectionEnabled`, which defaults to
    false and can be set in the app config.

  #### Returns void

### getToken

- getToken ( forceRefresh ? : boolean ) : Promise \< [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult) \>
- Get the current App Check token. Attaches to the most recent
  in-flight request if one is present. Returns null if no token
  is present and no token requests are in-flight.

  #### Parameters

  -

    ##### Optional forceRefresh: boolean

    If true, will always try to fetch a fresh token.
    If false, will use a cached token if found in storage.

  #### Returns Promise\<[AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)\>

### onTokenChanged

- onTokenChanged ( observer : { complete ?: ( ) =\> void ; error ?: ( error : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error) ) =\> void ; next : ( tokenResult : [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult) ) =\> void } ) : Unsubscribe
- Registers a listener to changes in the token state. There can be more
  than one listener registered at the same time for one or more
  App Check instances. The listeners call back on the UI thread whenever
  the current token associated with this App Check instance changes.

  #### Parameters

  -

    ##### observer: { complete?: () =\> void; error?: (error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> void; next: (tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)) =\> void }

    An object with `next`, `error`, and `complete`
    properties. `next` is called with an
    [`AppCheckTokenResult`](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)
    whenever the token changes. `error` is optional and is called if an
    error is thrown by the listener (the `next` function). `complete`
    is unused, as the token stream is unending.
    -

      ##### Optional complete?: () =\> void

      -
        - (): void

        <!-- -->

        -

          #### Returns void

    -

      ##### Optional error?: (error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> void

      -
        - (error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)): void

        <!-- -->

        -

          #### Parameters

          -

            ##### error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)

          #### Returns void

    -

      ##### next: (tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)) =\> void

      -
        - (tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)): void

        <!-- -->

        -

          #### Parameters

          -

            ##### tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)

          #### Returns void

  #### Returns Unsubscribe

  A function that unsubscribes this listener.
- onTokenChanged ( onNext : ( tokenResult : [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult) ) =\> void , onError ? : ( error : [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error) ) =\> void , onCompletion ? : ( ) =\> void ) : Unsubscribe
- Registers a listener to changes in the token state. There can be more
  than one listener registered at the same time for one or more
  App Check instances. The listeners call back on the UI thread whenever
  the current token associated with this App Check instance changes.

  #### Parameters

  -

    ##### onNext: (tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)) =\> void

    When the token changes, this function is called with aa
    [`AppCheckTokenResult`](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult).
    -
      - (tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)): void

      <!-- -->

      -

        #### Parameters

        -

          ##### tokenResult: [AppCheckTokenResult](https://firebase.google.com/docs/reference/js/v8/firebase.appcheck.AppCheckTokenResult)

        #### Returns void

  -

    ##### Optional onError: (error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)) =\> void

    Optional. Called if there is an error thrown by the
    listener (the `onNext` function).
    -
      - (error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)): void

      <!-- -->

      -

        #### Parameters

        -

          ##### error: [Error](https://firebase.google.com/docs/reference/js/v8/firebase.functions.HttpsError#error)

        #### Returns void

  -

    ##### Optional onCompletion: () =\> void

    Currently unused, as the token stream is unending.
    -
      - (): void

      <!-- -->

      -

        #### Returns void

  #### Returns Unsubscribe

  A function that unsubscribes this listener.

### setTokenAutoRefreshEnabled

- setTokenAutoRefreshEnabled ( isTokenAutoRefreshEnabled : boolean ) : void
-

  #### Parameters

  -

    ##### isTokenAutoRefreshEnabled: boolean

    If true, the SDK automatically
    refreshes App Check tokens as needed. This overrides any value set
    during `activate()`.

  #### Returns void