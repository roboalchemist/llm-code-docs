# Source: https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/sign-in-with-klarna-react-native.md

# Sign in with Klarna - React Native

## Add Sign in with Klarna to your React Native app by integrating the Klarna In-App SDK, configuring native dependencies, and securely managing the sign-in flow and user data scopes.

## <big>**Setup your app**</big>

### Package Managers

#### NPM

If you want to add the SDK via `npm` use the following to add library dependency:

``` bash
npm install react-native-klarna-inapp-sdk --save
```

#### Yarn

If you are using yarn, then use the following to add library dependency:

``` shell
yarn add react-native-klarna-inapp-sdk
```

For installing native dependencies for iOS, go to your `ios` directory and run `pod install`.

### Android

To ensure the Sign in flow initiated by the SDK can correctly redirect back to your application, you must configure a unique return URL (deep link) for your app and provide this URL string to the SDK. This value is required specifically for the Sign in flow initiated by the SDK. **Important:** This configuration is distinct from any other return URLs the SDK might require for handling redirects from external third-party applications. Ensure you are configuring the URL for the SDK's Sign in flow. Add this snippet to your manifest file in order to set your return URL value for the SDK’s activity.

``` markup
<activity android:exported="true" android:name="com.klarna.mobile.sdk.activity.KlarnaRedirectReceiverActivity" tools:node="replace">
<intent-filter>
<action android:name="android.intent.action.VIEW"></action>
<category android:name="android.intent.category.DEFAULT"></category>
<category android:name="android.intent.category.BROWSABLE"></category>
<data android:host="&lt;YOUR-HOST&gt;" android:scheme="&lt;YOUR-SCHEME&gt;"></data>
</intent-filter>
</activity>
```

In version 2.6.11 and later, a new activity called \`**KlarnaRedirectReceiverActivity**\` has been introduced in the Android SDK.

## Implementing Sign in with Klarna

### 1. Set up Sign in with Klarna

Before starting to work with the Sign In With Klarna, the Android and iOS parts of your React Native app need to be updated in order to provide the best experience and functionality to the users. Please read and follow the `before you start -&gt; setting the return url` guide for [Android](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/sign-in-with-klarna-android/#before-you-start) and `preparation` guide for [iOS](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/sign-in-with-klarna-ios/#preparation-aswebauthenticationpresentationcontextproviding).

### 2. Create an instance

You just need to import the `KlarnaSignInSDK` class from Klarna's React Native Mobile SDK as follows:

``` typescript
import {KlarnaSignInSDK} from 'react-native-klarna-inapp-sdk';
```

To create an instance of <span>`KlarnaSignInSDK`</span> you need to call the <span>`KlarnaSignInSDK`</span>`.createInstance()`:

``` typescript
KlarnaSignInSDK.createInstance({
    environment: KlarnaEnvironment.Staging,
    region: KlarnaRegion.EU,
    returnUrl: 'myApp://signInWithKlarna',
})
.then(klarnaSignInInstance =&gt; {
    console.log('KlarnaSignIn instance created: ', klarnaSignInInstance);
    klarnaSignIn = klarnaSignInInstance
})
.catch(e =&gt; {
    console.error('KlarnaSignIn instance creation failed: ', e);
});
```

If an instance of <span>`KlarnaSignInSDK`</span> is initialized correctly, you will get a reference to it in the promise return value. If there is an error during initialization, it will be returned in the catch block of the promise.

#### Parameters

| NAME | TYPE | REQUIRED | DESCRIPTION |
|----|----|--------|-----------|
| `environment` | String | No | An enumeration that is used to configure the endpoints and other behaviours that the `KlarnaSignIn` will be operating with. The possible values are as follows. If not set, the default value will be `production` . * playground * production * staging |
| `region` | String | No | An enumeration that defines the regional API endpoints to which the `KlarnaSignIn` flow will send/receive requests. The possible values are as follows. If not set, the default value will be `eu` . * eu * na * oc |
| `returnUrl` | String | Yes | The URL you defined as your redirect URI for Sign in with Klarna integration in the preparation section. You can find more information about the URL in our [iOS](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/sign-in-with-klarna-ios/#before-you-start-2-setting-the-return-url) getting started guide and [Android](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/sign-in-with-klarna-android/#before-you-start-1-setting-the-return-url) before you start guide. |

### **3.Initiate the Sign In**

To start the sign in flow, you need to call the `signIn()` function:

``` typescript
klarnaSignIn.signIn(clientId, scope, market, locale, tokenizationId)
```

After calling the `signIn` function, the sign in flow will be presented to the user. When the user finishes the sign in flow, you would either receive a successful or an error result in the promise returned by the `signIn` function.

#### Parameters

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION** |
|----|----|----|----|
| `clientId` | String | Yes | The UUID you get when creating your Klarna OAuth 2.0 app. |
| `scope` | String | Yes | A space-separated list of [scopes](https://docs-portal-eu.staging.c2c.klarna.net/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/sign-in-with-klarna-react-native/#scopes) you would like to request from the user. |
| `market` | String | Yes | The market or the country where this integration is available, for example, `SE` for Sweden. |
| `locale` | String | Yes | The language to present to the user, for example, `sv-SE` or `en-SE` for Sweden. |
| `tokenizationId` | String | No | The ID to enable tokenization. |

##### Scopes

The table below lists the available scopes and how they correspond to claims and permissions. 

| Scope | Claims | Type | Can be toggled off |
|----|----|----|----|
| profile:name | given_name | string | No |
| profile:name | family_name | string | No |
| profile:email | email | string (Email) | No |
| profile:email | email_verified | boolean |  |
| profile:phone | phone | string (E. 164) | No |
| profile:phone | phone_verified | boolean |  |
| profile:date_of_birth | date_of_birth | string (ISO 8601) | Yes |
| profile:billing_address | street_address | string | Yes |
| profile:billing_address | street_address2 | string |  |
| profile:billing_address | postal_code | string |  |
| profile:billing_address | city | string |  |
| profile:billing_address | region | string |  |
| profile:billing_address | country | string (ISO 3166-1 alpha-2) |  |
| profile:shipping_address | street_address | string | Yes |
| profile:shipping_address | street_address2 | string |  |
| profile:shipping_address | postal_code | string |  |
| profile:shipping_address | city | string |  |
| profile:shipping_address | region | string |  |
| profile:shipping_address | country | string (ISO 3166-1 alpha-2) |  |
| profile:national_id | national_id | string | Yes |
| profile:country | country | string (ISO 3166-1 alpha-2) | Yes |
| profile:locale | locale | string (ISO 3166) | Yes |
| payment:consumer_present | trigger on-demand flow | N/A | N/A |
| payment:consumer_not_present | trigger subscription flow | N/A | N/A |

Remember to always add 'openid', 'offline_access' and 'payment:request:create' scopes to receive full functionality of Sign in with Klarna. The mock-ups below show how users will see required versus optional scopes when entering the Sign in with Klarna flow.    ![](e0d14625-c96b-4268-a3b0-dff196b42b93_Siwk_mock_up.jpeg)

#### Handle results and errors

There are two main action values to look for, **KlarnaSignInUserCancelled** triggered when the user cancelled the flow at any point and the **KlarnaSignInToken** event, received after the signIn process is completed. You can get the tokens from the `KlarnaProductEvent` params for **KlarnaSignInToken** event and send it to your backend.

``` typescript
klarnaSignIn
      ?.signIn(clientId, scope, market, locale, tokenizationId)
      .then(r =&gt; {
        switch (r.action) {
          case 'KlarnaSignInUserCancelled':
            console.log('User cancelled sign in');
            break;
          case 'KlarnaSignInToken':
            console.log('Token event received: ', r);
            // Access token
            const accessToken = r.params?.KlarnaSignInToken.access_token
            break;
          default:
            console.log('Other sign in event received: ', r)
            break;
        }
      })
      .catch(e =&gt; {
        console.error('Sign in failed with error: ', e);
      });
```

##### **KlarnaProductEvent**

When the `signIn` method resolves, a **KlarnaProductEvent** is returned as a result. This event type includes three properties, `action, params and sessionId`.

| **NAME** | **TYPE** | **DESCRIPTION** |
|----|----|----|
| `action` | String | Represents the name of the event. |
| `params` | String | Contains a payload that may or may not be returned, depending on the specific event. |
| `sessionId` | String | An identifier that can be useful when contacting Klarna for support. |

### 4. Dispose the instance

After the flow is complete and the token has been retrieved and you no longer need the `KlarnaSignInSDK` instance, you can call the `dispose()` method to release the resources used by the object.

``` typescript
klarnaSignIn?.dispose();
```