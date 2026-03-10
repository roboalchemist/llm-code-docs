# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/react-native-requirements.mdx

# React Native Requirements

React Native mobile applications require extra configuration for both iOS and Android to ensure that Cash App deeplinks successfully during the Cash App Pay mobile user flow. This is caused because your application cannot see, or directly interact with, most external packages without explicitly requesting allowance. Therefore, you must declare your app’s need for increased visibility with Cash App.

## iOS

### Problem

Launch Services provides support for launching apps and matching document types to apps. Therefore, the keys recognized by Launch Services allow you to specify the desired execution environment for your code packages. See more at [Launch Services Keys.](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14)

### Solution

The following configuration must be added to the `info.plist` file:

```.plist
<key>LSApplicationQueriesSchemes</key>
<array> 
    <string>cashme</string>
</array>
```

## Android

### Problem

When your app queries information about other apps that are installed on an Android (11 or higher) device, the information is filtered by default. This filtering behavior means that your app can’t detect all the apps installed on the device. This helps minimize the potentially sensitive information that your app can access but doesn't really need for its use cases. See more at [Package visibility filtering on Android.](https://developer.android.com/training/package-visibility)

### Solution

The following configuration must be added to the `AndroidManifest.xml` file:

```xml
<queries>
    <intent>  
        <action android:name="android.intent.action.VIEW" /> 
            <data 
                android:host="*" 
                android:scheme="cashme" /> 
    </intent> 
</queries>
```
