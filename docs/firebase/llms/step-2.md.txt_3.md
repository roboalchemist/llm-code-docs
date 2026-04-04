# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-2.md.txt

# Tutorial: Measure iOS Ads conversions using event data

## Step 2: Integrate Google Analytics

<br />

|---|
| Introduction: [Measure iOS Ads conversions](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/index-event-driven) |
| Step 1: [Link Your Ads Account with Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-1) |
| **Step 2: Integrate Google Analytics** <br /> |
| Step 3: [Troubleshoot and handle common issues](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-3) |

<br />

Now that you've linked your Ads account, you can begin integrating the
Google Analytics for Firebase SDK.

### Integrate the Google Analytics for Firebase SDK

Integrate with the latest Google Analytics for Firebase SDK version.

> [!NOTE]
> **Note:** `GoogleAdsOnDeviceConversion` is not subject to [Apple's privacy manifest
> requirements](https://developer.apple.com/news/?id=3d8a9yyh) and does not include a privacy manifest. No additional action is required to enable on-device conversion measurement.

#### Use Cocoapods

If your app uses Cocoapods, verify your project's Podfile contains the
`GoogleAppAdsOnDeviceConversion` pod, through either the main
`FirebaseAnalytics` pod or by including it explicitly as a standalone pod:

    pod 'FirebaseAnalytics' # includes GoogleAdsOnDeviceConversion

or

    pod 'FirebaseAnalytics/Core'
    pod 'GoogleAdsOnDeviceConversion'

Then, run the commands `pod repo update` and `pod install`.

#### Use Swift Package Manager

If your app uses Swift Package Manager, follow the steps at
[Swift Package Manager for Firebase](https://firebase.google.com/docs/ios/installation-methods#swift-package-manager).
When you reach the step "Choose the Firebase libraries that you want include in
your app", check `FirebaseAnalytics` before continuing to the next steps.
Alternatively, check `FirebaseAnalytics/Core` *and*
`GoogleAdsOnDeviceConversion`.

#### Alternative integration

If your app does not use Cocoapods or Swift Package Manager, integrate as
follows:

1. Download the public zip file of Firebase from the [firebase-ios-sdk GitHub repo](https://github.com/firebase/firebase-ios-sdk/releases).
2. Follow the README instructions from the public zip file to add the frameworks to the project directly. Be sure to add the frameworks from the `FirebaseAnalytics`directory.
3. In Xcode, add the `-ObjC` and `-lc++` flags to **Other Linker Settings** in your app target's build settings.

### Verify integration

Enable debug mode by adding `-FIRDebugEnabled` under
**Arguments Passed on Launch** in Xcode's scheme editor.

Delete the app in the Simulator or device.
Upon launching the app in Xcode, verify that a message like the following
appears in the Xcode debug console:

    [Firebase/Analytics][I-ACS023007] Analytics v.X.X.X started
    ...
    [Firebase/Analytics][I-ACS023009] Debug logging enabled
    ...
    [FirebaseAnalytics][I-ACS023278] Conversion service GoogleAdsOnDeviceConversion framework is linked

Wait around 15 seconds and verify that the `_psmvalue_gads` message appears in
the Xcode debug console:

    [FirebaseAnalytics][I-ACS023087] User property set. Name, value: _psmvalue_gads, XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

> [!NOTE]
> **Note:** This message won't appear for users/devices located in the European Economic Area (EEA), the United Kingdom, and Switzerland.

<br />

*** ** * ** ***

<br />

[**Step 1** Link Your Ads Account with Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-1)
[**Step 3** : Troubleshoot and handle common issues](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement-event-data/step-3)

<br />

*** ** * ** ***