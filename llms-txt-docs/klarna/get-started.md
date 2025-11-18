# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/get-started.md

# Getting started

## Get started integrating Klarna Mobile SDK for Android

## ADDING THE SDK AS A DEPENDENCY

### Add the Repository

Add the Klarna Mobile SDK repository in the apps build.gradle file.

``` json
repositories {
maven {
url 'https://x.klarnacdn.net/mobile-sdk/'
}
}
```

### Add Compile Options for the Callbacks

If you’re using Java, add compile options to support Java version 1.8 in the apps build.gradle.

``` json
android {
...
compileOptions {
sourceCompatibility JavaVersion.VERSION_1_8
targetCompatibility JavaVersion.VERSION_1_8
}
...
}
```

### Add the Dependency

Add the SDK as a dependency to your app’s build.gradle:

``` json
dependencies {
implementation 'com.klarna.mobile:sdk:2.x.x'
}
```

For a stable integration we require all integrators to update their SDK version at least once every quarter to ensure the application uses a recent version of the SDK. This is mainly due to continuous development on Klarna products and the SDK are being aligned by each release along with the SDK specific improvements and the nature of native mobile development where we are required to cater for platform changes as much as your application does.

#### More information

For more information check out the [Klarna Mobile SDK Github repository](https://github.com/klarna/klarna-mobile-sdk-android).

## CONFIGURE YOUR APP

### Return URL

Both the hybrid and native integrations might, at some point, open third-party applications. To automatically return the user, these third-party applications need to know how to build a return intent or URL. To do that, you’ll need to provide the SDK with what we call a “return URL” parameter. If you haven’t done so already, You can register an intent-filter for the Activity you’d like to return to in your app’s AndroidManifest.xml:

``` json
<application...>
<activity...>
<intent-filter>
<action android:name="android.intent.action.VIEW"></action>
<category android:name="android.intent.category.DEFAULT"></category>
<category android:name="android.intent.category.BROWSABLE"></category>
<data android:scheme="<your-custom-scheme>"></data>
<data android:host="<your-custom-host>"></data>
</intent-filter>


```

**Important:** Construct the return URL string passed to the SDK by combining the attributes defined in your <intent-filter>'s `<data>` tag, following the standard URL format: `scheme://host:port/path`You can read more about how deep links and intent filters work [on the Android Developers site](https://developer.android.com/training/app-links/deep-linking). The hosting Activity should be using launchMode of type singleTask or singleTop to prevent a new instance from being created when returning from an external application.

### Klarna Component Classes

There are some base properties that every integration in our SDK separately defines and uses in the process. These properties are declared in an Interface called \`KlarnaComponent\` that each integration implements and you can set or get their values:

| Property | Type | Description |
|----|----|----|
| loggingLevel | KlarnaLoggingLevel | The level of events and errors that the integration will log to the console. |
| eventHandler | KlarnaEventHandler | The interface to receive results from the integration. |
| returnURL | String | The URL schema as defined in your AndroidManifest.xml to return from external applications. |
| region | KlarnaRegion | The geographical region of the user/application. |
| environment | KlarnaEnvironment | The working environment of the integration. |
| theme | KlarnaTheme | The style of integration in light and dark configurations. |
| resourceEndpoint | KlarnaResourceEndpoint | The resources endpoint configuration for the integration. |

Some of the classes that implement these properties are

- KlarnaPaymentView
- KlarnaCheckoutView
- KlarnaHybridSDK
- KlarnaSignInButton
- …

### Setting the Logging Level

The SDK will log events and errors to the system’s log while running. You can set the logging level for the SDK using the \`loggingLevel\` property:

``` kotlin
// Example of how to set the logging level for an integration
val KlarnaPaymentView = KlarnaPaymentView(...)
KlarnaPaymentView.loggingLevel = KlarnaLoggingLevel.Verbose
```

Possible values to set as the logging level:

| Value                      | Description                        |
|----------------------------|------------------------------------|
| KlarnaLoggingLevel.Off     | No logging                         |
| KlarnaLoggingLevel.Error   | Log error messages only            |
| KlarnaLoggingLevel.Verbose | Log all messages (debug and error) |

### Internet Permissions

The SDK will require access to the internet, as such, if you don’t explicitly declare access in your manifest, we will merge manifests to get access.</data></intent-filter></activity...></application...>