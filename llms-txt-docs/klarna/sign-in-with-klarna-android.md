# Source: https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/sign-in-with-klarna-android.md

# Sign in with Klarna

## In this step-by-step guide you will learn how to integrate Sign in with Klarna into your Android app.

## Before you start

Before starting to add the Sign in with Klarna button or using the Sign in with Klarna SDK you will need to do two things:

1.  Setting the return URL
2.  Defining an event handler

### 1. Setting the Return URL

To ensure the Sign in flow initiated by the SDK can correctly redirect back to your application, you must configure a unique return URL (deep link) for your app and provide this URL string to the SDK. This value is required specifically for the Sign in flow initiated by the SDK.

**Important:** This configuration is distinct from any other return URLs the SDK might require for handling redirects from external third-party applications. Ensure you are configuring the URL for the SDK's Sign in flow.

Add this snippet to your manifest file in order to set your return URL value for the SDK’s activity.

``` markup
<activity android:exported="true" android:name="com.klarna.mobile.sdk.activity.KlarnaRedirectReceiverActivity" tools:node="replace">
<intent-filter>
<action android:name="android.intent.action.VIEW"></action>
<category android:name="android.intent.category.DEFAULT"></category>
<category android:name="android.intent.category.BROWSABLE"></category>
<data android:host="<YOUR-HOST>" android:scheme="<YOUR-SCHEME>"></data>
</intent-filter>
</activity>
```

In version 2.6.11 and later, a new activity called \`**KlarnaRedirectReceiverActivity**\` has been introduced in the Android SDK.

When setting the returnURL parameter for KlarnaSignInButton or KlarnaSignInSDK , you need to concatenate the scheme and host you specified in AndroidManifest.xml into one value using `://` as the separator, as shown here:

``` kotlin
val button = KlarnaSignInButton(... returnURL =  “<your-scheme>://<your-host>”)
```

Utilizing \`**FLAG_ACTIVITY_NEW_DOCUMENT**\` when initializing an activity that proceeds to the Sign in with Klarna operation can interfere with the user navigation within the app. This flag might induce Android to spawn a new app instance upon returning to the app via the return URL deep linking, consequently disrupting the login process. To evade potential user inconveniences, **we recommend avoiding \`FLAG_ACTIVITY_NEW_DOCUMENT\` when launching an activity that may trigger the Sign in with Klarna procedure.**

### 2. Defining an Event Handler

While the user is interacting with the Sign in with Klarna flow or when the flow is completed, you'll receive events by setting an event handler when creating an instance of `KlarnaSignInSDK`.

``` kotlin
val eventHandler = object : KlarnaEventHandler {
   override fun onEvent(klarnaComponent: KlarnaComponent, event: KlarnaProductEvent) {
      when(event.action) {
         KlarnaSignInEvent.USER_TAPPED_BUTTON -> {
            // User tapped the KlarnaSignInButton, auth process starting
         }
         KlarnaSignInEvent.USER_AUTH -> {
            // User completed interactive auth, tokens will be fetched
         }
         KlarnaSignInEvent.USER_CANCELLED -> {
            // User manually canceled sign in
         }
         KlarnaSignInEvent.SIGN_IN_TOKEN -> {
            // User is authorized. You can read the results      
            // in event.params attribute by casting it to the
            // KlarnaSignInToken model.

            val token =
               event.params[KlarnaSignInEvent.ParamKey.KlarnaSignInToken] 
               as? KlarnaSignInToken

            val accessToken = token?.accessToken
            ...
         }
      }
   }

   override fun onError(klarnaComponent: KlarnaComponent, error: KlarnaMobileSDKError) {
      // In case of any errors, check the 'error' parameter for more details, 
      // for example if the error is fatal or not.

      val errorMessage = error.message
      val isFatal = error.isFatal
      when(error.name) {         
         KlarnaSignInError.InvalidClientID -> {
            // The client ID value is invalid
         }
         KlarnaSignInError.InvalidScope -> {
            // The scope value is invalid
            ...
         }
         KlarnaSignInError.InvalidMarket -> {
            // The market value is invalid
            ...
         }
         KlarnaSignInError.InvalidCustomTabsReturnUrl -> {
            // The AndroidManifest needs to be set up for KlarnaCustomTabActivity
            ...
         }
         KlarnaSignInError.SignInFailed -> {
            // User authorization step failed
            val signInError = error.params[KlarnaSignInError.ParamKey.Error]
            val signInErrorDescription = error.params[KlarnaSignInError.ParamKey.ErrorDescription]
            ...
         }
         KlarnaSignInError.RenderButtonFailed -> {
            // Button failed to render
            ...
         }
         KlarnaSignInError.AlreadyInProgress -> {
            // Sign in is already in progress, user tap or signIn method call is ignored
            ...
         }
      }
   }
}
```

`KlarnaEventHandler` reference will be kept weak in the SDK to avoid memory leaks, thus it's required for integrator to keep the strong reference.

## Sign in with Klarna Button

To integrate the button for Sign in with Klarna as a native view in your Android app, you need to create an instance of it, add it to your view hierarchy, and receive the results once the flow is completed.

### Create the Button

The button for Sign in with Klarna native view in Android is called `KlarnaSignInButton`. You can create an instance programmatically or inflate it from an XML layout file. You can set the parameters of the button both programatically or in the XML layout file.

### Create the Button Programmatically

You can create the Sign in with Klarna button programmatically and place it in your app with desired layout options. You can see a sample on the right.

``` kotlin
//Create an instance of KlarnaSignInButton
val button = KlarnaSignInButton(...)

// Add it to your container with desired layout parameters
val layoutParams = ViewGroup.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT,
ViewGroup.LayoutParams.WRAP_CONTENT)
containerViewGroup.addView(button, 0, layoutParams)
```

### Create the Button in XML

You can also add the Sign in with Klarna button into your XML layout file and get the view instance programmatically either by `findViewById` or by the generated View Binding instance of your layout (if you're using View Binding).

``` markup
 <com.klarna.mobile.sdk.api.signin.klarnasigninbutton android:id="@+id/klarnaSignInButton" android:layout_height="wrap_content" android:layout_width="wrap_content" …=""></com.klarna.mobile.sdk.api.signin.klarnasigninbutton>
```

### Settings the Parameters

You can set the parameters of the Sign in with Klarna button either by setting them on the button instance or by setting them as attributes in the XML layout file.

| Parameter | Type | Required | Description |
|---------|----|--------|-----------|
| `context` | Context | Yes | The context of the Activity the button is in. |
| `clientId` | String | Yes (optional in the constructor) | The UUID you get when creating your Klarna OAuth 2.0 app. The XML attribute of this parameter is `app:KlarnaSignInButtonClientId.` |
| `scope` | String | Yes (optional in the constructor) | A space-separated list of scopes you would like to request from the user. For example, request `billing_address` if you need the billing address in your account creation. The XML attribute of this parameter is `app:KlarnaSignInButtonScope.` The claims of the requested scopes will be returned as part of the JWT token `id_token` . Note: `openid` is always requested by default even if you don't request it explicitly. Available scopes are as follows: <ul><li>offline_access</li><li>profile:email</li><li>profile:phone</li><li>profile:name</li><li>profile:date_of_birth</li><li>profile:billing_address</li><li>profile:national_identification</li><li>profile:country</li><li>payment:request:create</li></ul> |
| `market` | String | Yes (optional in the constructor) | The market or the country where this integration is available, for example, `SE` for Sweden. The XML attribute of this parameter is `app:KlarnaSignInButtonMarket.` |
| `locale` | String | Yes (optional in the constructor) | The language in which the Sign in with Klarna button is presented to the user, for example, `sv-SE` or `en-SE` for Sweden. The XML attribute of this parameter is `app:KlarnaSignInButtonLocale` . |
| `eventHandler` | KlarnaEventHandler | Yes (optional in the constructor) | The interface to receive the results from the Sign in with Klarna flow. Will be kept as weak reference. |
| `environment` | KlarnaEnvironment | No | Configures the endpoints and other behaviors that the SDK will be operating with. When set to `production` , the SDK will make requests to production endpoints and perform real validation, whereas for other environments will not. The XML attribute of this parameter is `app:klarnaEnvironment` . |
| `region` | KlarnaRegion | No | Defines the regional API endpoints to which the SDK will send requests. The XML attribute of this parameter is `app:klarnaRegion` . |
| `theme` | KlarnaTheme | No | Defines the theming for the Sign in with Klarna UI, but not the button itself. The XML attribute of this parameter is `app:klarnaTheme` . |
| `returnURL` | String | Yes (optional in the constructor) | The URL you defined in your `AndroidManifest.xml` file in the preparation section. The XML attribute of this parameter is `app:klarnaReturnUrl` . |
| `loggingLevel` | KlarnaLoggingLevel | No | The logging level which will be used when logging messages to the Logcat. The XML attribute of this parameter is `app:klarnaLoggingLevel` . |
| `resourceEndpoint` | KlarnaResourceEndpoint | No | Defines the cloud provider to which the SDK will send requests. Please note that this should not be changed or overridden. The XML attribute of this parameter is `app:klarnaResourceEndpoint` . |

### Customizing the Look and Feel of the Button

In addition the the parameters list above, Klarna offers several themes, labels, and shapes to customize the button's appearance to match the look and feel of your app.

| Parameter | Type | Description |
|----|----|----|
| `buttonTheme` | KlarnaButtonTheme | Enumerated value to style the button in the light or dark theme. |
| `buttonShape` | KlarnaButtonShape | Enumerated value specifying the button's shape. |
| `buttonLabel` | KlarnaButtonLabel | Enumerated value specifying the text that will be displayed on the button. |

### Button Theme

The `KlarnaButtonTheme` enumeration defines which style is applied to the button, depending on either the app’s configuration or the system settings.

| Value | Description |
|----|----|
| `KLARNA` | Renders the button in the Klarna pink theme. We recommend this theme as it has the highest brand recognition and the likelihood of usage by your customers. |
| `LIGHT` | Renders the button in white. We recommend this theme for dark backgrounds. |
| `DARK` | Renders the button in black. We recommend this theme for light backgrounds. |
| `AUTO` | Automatic theme (light or dark) that will depend on the system’s UI theme. |

### Button Shape

In order for the button to fit into the aesthetic of your app, we offer different button shapes:

| Value          | Description                                             |
|----------------|---------------------------------------------------------|
| `ROUNDED_RECT` | Renders the button as a rectangle with rounded corners. |
| `PILL`         | Renders the button as a pill-shaped button.             |
| `RECTANGLE`    | Renders the button as a rectangle with square corners.  |

## Sign in with Klarna SDK

To integrate the Sign in with Klarna SDK in your Android app, you need to create an instance of `KlarnaSignInSDK`, call its `signIn()` function, and receive the results once the flow is completed.

To create an instance of the SDK you need to specify the following parameters:

| Parameter | Type | Required | Description |
|----|----|----|----|
| `activity` | Activity | Yes | The activity instance of your app. |
| `returnURL` | String | Yes | The URL you defined in your `AndroidManifest.xml` file in the preparation section. |
| `eventHandler` | KlarnaEventHandler | Yes (optional in the constructor) | The interface to receive the results from the Sign in with Klarna flow. |
| `environment` | KlarnaEnvironment | No | Enumerated value to set the working environment for the SDK. |
| `region` | KlarnaRegion | No | Enumerated value to set the regional API endpoints to which the SDK will send requests. |
| `theme` | KlarnaTheme | No | Defines the theming for the Sign in with Klarna UI, but not the button itself. |
| `loggingLevel` | KlarnaLoggingLevel | No | The logging level which will be used when logging messages to the Logcat. |
| `resourceEndpoint` | KlarnaResourceEndpoint | No | Defines the cloud provider to which the SDK will send requests. |

### Calling the signIn() function

To initiate the sign in flow for the user, you need to call the `signIn()` function of the SDK and specify the following parameters:

| Parameter | Type | Required | Description |
|---------|----|--------|-----------|
| `clientId` | String | Yes | The UUID you get when creating your Klarna OAuth 2.0 app. |
| `scope` | String | Yes | A space-separated list of scopes you would like to request from the user. For example, request `billing_address` if you need the billing address in your account creation. The claims of the requested scopes will be returned as part of the JWT token `id_token` . Note: `openid` is always requested by default even if you don't request it explicitly. Available scopes are as follows: <ul><li>offline_access</li><li>profile:email</li><li>profile:phone</li><li>profile:name</li><li>profile:date_of_birth</li><li>profile:billing_address</li><li>profile:national_identification</li><li>profile:country</li><li>payment:request:create</li></ul> |
| `market` | String | Yes | The market or the country where this integration is available, for example, `SE` for Sweden. |
| `locale` | String | No | The language to present to the user, for example, `sv-SE` or `en-SE` for Sweden. |

After calling the `signIn()` function you will receive the events in the event handler that you've passed to the SDK.</your-host></your-scheme>