# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/post-purchase.md

# Post-Purchase on Android

​To use Post Purchase SDK in your application, you need to create an instance of the SDK and perform some operations on it. You can read more about the flow [here](https://docs.klarna.com/payments/mobile-payments/before-you-start/post-purchase-overview). This guide will teach you how to:

- Create an instance of the SDK and initialize it
- Get user’s consent for sharing their information 
- Fetching user purchases and render an operation for a specific order

## Create an instance of the SDK

To create an instance of the SDK, you need to provide the following parameters:

| Parameter | Type | Description |
|---------|----|-----------|
| hostActivity | Activity | The activity you are using the SDK inside. |
| environment | KlarnaEnvironment | The environment you want to use for the SDK. Possible values are: * PLAYGROUND * STAGING * PRODUCTION |
| region | KlarnaRegion | The region you want to use for the SDK. Possible values are: * EU (Europe) * NA (North America) * OC (Oceania) |
| callback | KlarnaPostPurchaseSDKCallback | The callback interface to receive results for different operations. |

``` kotlin
val postPurchaseSDK = KlarnaPostPurchaseSDK(
            activity = activity,
            environment = KlarnaEnvironment.PRODUCTION,
            region = KlarnaRegion.EU,
            callback = callback
)
```

Sample code

### Post Purchase SDK Callback

The callback is an interface that you need to implement and pass to the SDK so you can receive the results for each operation you perform via the SDK. If needed, you can add a new callback later on to the SDK. This will replace the callback that was provided when constructing the SDK instance:

``` kotlin
postPurchaseSDK.addCallback(callback)
```

Sample code You can also remove the callback from the SDK. After calling this method no results from the operations performed from the SDK will be received until a new callback is set:

``` kotlin
postPurchaseSDK.removeCallback(callback)
```

Sample code

## Initialize the SDK

After creating an instance of the SDK, you need to initialize it with the following parameters. **This is a mandatory step; you must wait for its result before doing any other operation.**

| Parameter | Type | Description |
|----|----|----|
| locale | String | A string representing the user locale.\* Setting an invalid locale might lead to other operations not working as expected. |
| purchaseCountry | String | Two-letter country code representing the purchase country. (For example, SE for Sweden) |
| design | String (optional) | Optional value representing the design ID associated with you as a merchant. |

**List of valid locale values supported by the SDK:** de-AT, en-AT en-AU nl-BE, fr-BE, en-BE en-CA, fr-CA de-CH, en-CH, fr-CH, it-CH de-DE, en-DE da-DK, en-DK es-ES, en-ES pt-PT, en-PT fi-FI, sv-FI, en-FI fr-FR, en-FR en-GB it-IT, en-IT nl-NL, en-NL no-NO, nb-NO, en-NO pl-PL, en-PL sv-SE, en-SE en-US, es-US en-IE cs-CZ, en-CZ el-GR, en-GR es-MX, en-MX

``` kotlin
postPurchaseSDK.initialize(
            locale = “en-SE”,
            purchaseCountry = ”SE”,
            design = “design”
)
```

Sample code If the result of initialize operation is successful, the "onInitialized" method in your callback will be invoked. Otherwise, you will receive the error in the "onError" method. To know more about the errors, please refer to the "Handling Errors" section.

## Authorize (User Consent)

To fetch a user's orders list, you need a valid OAuth 2.0 access token. If you have never received this token for a user before, you need to trigger an OAuth flow in which the user will consent to the information sharing.  The consent is market-specific and is based on the credentials you use when triggering the OAuth flow. If you want data for different markets, a separate consent flow needs to be triggered.

| Parameter | Type | Description |
|----|----|----|
| clientId | String | The client ID that is provided to you for the user. |
| scope | String | OAuth scope that defines what the returned token will be able to access. It can be a space-separated list of scopes. These values define the consent screen that Klarna displays to the user. |
| redirectUri | String | URI to redirect the user after they have finished the consent flow. If successful, this will contain the authorization code as a query parameter (see Klarna OAuth API documentation). The value must exactly match one of the values provided to Klarna in advance. |
| locale | String (optional) | A string representing the user locale. |
| state | String (optional) | A string value your application uses to maintain the state between your authorization request and the authorization server's response. The Authorization server returns the exact value that you send to the redirectUri as a URL parameter. |
| loginHint | String (optional) | If your application knows which user is trying to authenticate, it can use this parameter to provide a hint to Klarna’s Authorization Server. The server uses the hint to simplify the login flow by prefilling the email field in the sign-in form. It’s recommended to use this as it will improve the user experience. |
| responseType | String (optional) | The desired grant type. We only support “code” type currently and it is the default value. |

``` kotlin
postPurchaseSDK.authorizationRequest(
           clientId = “497043bl6of4306lh54kgg54dslt39rg”,
           scope = “read:consumer_order”,
           redirectUri = “http://auth.example.com/callback”,
           locale = “en-SE”,
           state = “myState”,
           loginHint = “myuser@example.com”,
           responseType = “code”
        )
```

Sample code If the authorization flow (user consent) is successfully started, which means the user is presented with Klarna consent page, the "onAuthorizeRequested" method in your callback will be invoked. **Important Note:** The "onAuthorizeRequested" does not mean the consent flow is finished or successful. You will know the result of the flow in your *redirectUri* parameter. If for any reason, SDK fails to start the consent flow in the first place, you will receive the error in the "onError" method. To know more about the errors, please refer to the "Handling Errors" section. After the flow is finished and has been redirected to the *redirectUri*, you will have to exchange the returned *authorization code* for an *access and refresh token* using the */authorize* endpoint of the Klarna OAuth API. A successful consent flow will redirect to *redirectUri* with a “code”  URL parameter: 

``` http
http://auth.example.com/callback?code=0f25f67b4dahktj7782464gk0161e5beb14462e1
```

A rejected or canceled consent flow will redirect to *redirectUri* with an “error” URL parameter:

``` http
http://auth.example.com/callback?error=access_denied
```

## Access User Orders

You can use the authorization code you retrieved in the previous step to read the user's orders. In a nutshell:

1.  You need to exchange the authorization code with *access token* and *refresh token*
2.  Use the *access token* to read the user's orders

Please contact your Klarna delivery manager for more information on how to accomplish this step.

## Render Operation

Once you have user orders, you can present them in your application. Each order item contains a list of available operations (each with a unique token) so you can show them to the user in the order detail overview section and let the user initiate a Post-Purchase operation using the SDK. When you call the "renderOperation" method, the SDK will render the relevant UI as a modal window in your application.

| Parameter | Type | Description |
|----|----|----|
| operationToken | String | The token for the selected operation. |
| locale | String (Optional) | A string representing the user locale. |
| redirectUri | String (Optional) | In some operations, Klarna has to navigate the user away to an external app or a web page. In such cases, this parameter can be used to navigate the user back to your application. |

``` kotlin
postPurchaseSDK.renderOperation(
           operationToken = ”s0u035ijoifkjg0j0ej0ierhj0”,
           locale = “en-SE”,
           redirectUri = “my-app://klarna-post-purchase”
)
```

After calling this method, you can show a loading indicator to the user while the Klarna UI modal is being created and presented. You should dismiss the loading when you get the result back in "onRenderedOperation" method in your callback. Possible result values in the callback method are found in the *KlarnaPostPurchaseRenderResult* enum class and are as follows:

| Value | Description |
|----|----|
| STATE_CHANGE | You need to pull the updated order data via Klarna’s API. This happens when an operation has resulted in a change of the order state. |
| NO_STATE_CHANGE | The operation finished without a change of the order state. You don’t need to pull any updates. |

If the SDK fails to render the operation, you will receive the error in the "onError" method. To know more about the errors, please refer to the "Handling Errors" section.

## Handling Errors

In case of any issues or errors while using the Post Purchase SDK functions, you will receive an error object of type *KlarnaPostPurchaseError* in the "onError" method of your callback with the following attributes:

| Parameter | Type | Description |
|----|----|----|
| name | String | Name of the error. |
| message | String | Message of the error. |
| status | String (Optional) | Status of the error specifically for render operation errors. |
| isFatal | Boolean | true If the error is not fixable and you should terminate the process, false otherwise.  |

These are the predefined names for errors during the Post Purchase flow. These names are available as static variables inside *KlarnaPostPurchaseError* class.

| Error Name | Description |
|----|----|
| KlarnaPostPurchaseErrorCreate | Error occurred while creating an instance of Post Purchase SDK. |
| KlarnaPostPurchaseErrorInitialize | Error occurred while performing \`initialize\` |
| KlarnaPostPurchaseErrorAuthorize | Error occurred while performing \`authorize\` |
| KlarnaPostPurchaseErrorRender | Error occurred while performing \`render\` |
| KlarnaPostPurchaseErrorUnknown | An error happened. We couldn't identify the cause of the error or the action it's related to. |
| KlarnaPostPurchaseErrorSdkNotAvailable | Klarna SDK is not available at this moment. Please try again later. |

Possible (but not limited to) *status* values in the error object for "renderOperation" method:

| Status | Description |
|----|----|
| STATE_CHANGE | This happens when the order state has changed, and the operation is no longer relevant. You need to pull the updated order data via our API. |
| TOKEN_EXPIRED | The operation token has expired. Refresh the OAuth access token and then fetch the order details again to get new operation tokens. |
| ERROR | There was an error and the operation was not completed. |