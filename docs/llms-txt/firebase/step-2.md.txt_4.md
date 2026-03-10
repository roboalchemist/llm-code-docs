# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2.md.txt

# Tutorial: Measure iOS Ads conversions

## Step 2: Integrate Google Analytics

<br />

|---|
| Introduction: [Measure iOS Ads conversions](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/index-first-party) |
| Step 1: [Implement a sign-in experience](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-1) <br /> |
| **Step 2: Integrate Google Analytics** <br /> |
| Step 3: [Initiate on-device conversion measurement using Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3) |
| Step 4: [Troubleshoot and handle common issues](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-4) |

<br />

Now that you've implemented an authentication system to collect users' emails
or phone numbers, you can begin integrating the Google Analytics for
Firebase SDK.

### Integrate the Google Analytics for Firebase SDK

Integrate with the latest Google Analytics for Firebase SDK version.

> [!NOTE]
> **Note:** `GoogleAdsOnDeviceConversion` is not subject to [Apple's privacy manifest requirements](https://developer.apple.com/news/?id=3d8a9yyh) and does not include a privacy manifest. No additional action is required to enable on-device conversion measurement.

#### Use Cocoapods

If your app uses Cocoapods, ensure your project's Podfile contains either:

    pod 'FirebaseAnalytics`  # includes GoogleAdsOnDeviceConversion

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
2. Follow the README instructions from the public zip file to add the frameworks to the project directly. Be sure to add the frameworks from the `FirebaseAnalytics` directory.
3. In Xcode, add the `-ObjC` and `-lc++` flags to "Other Linker Settings" in your app target's build settings.

#### Unity

1. Add the [Firebase Unity SDK](https://firebase.google.com/download/unity)
   (specifically, `FirebaseAnalytics.unitypackage`) to your Unity project. More detailed instructions can be found in [Add Firebase Unity SDKs](https://firebase.google.com/docs/unity/setup#add-sdks).

2. Select the platform iOS at **File** \> **Build Settings** , then click
   **Build and Run**.

3. In the generated build folder, locate the Podfile and add the following:

       pod 'GoogleAdsOnDeviceConversion'

### Enable debug mode

Enable debug mode by adding `-FIRDebugEnabled` under "Arguments Passed on Launch"
in Xcode's scheme editor. Upon launching the app in Xcode, ensure that a
message like the following appears in the Xcode debug console:

    [Firebase/Analytics][I-ACS023007] Analytics v.x.x.x started
    ...
    [Firebase/Analytics][I-ACS023009] Debug logging enabled

<br />

*** ** * ** ***

<br />

[**Step 1**: Implement a sign-in experience](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-1)
[**Step 3** : Initiate measurements using Google Analytics](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3)

<br />

*** ** * ** ***