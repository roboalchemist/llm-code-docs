# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/integrate-luciq-on-ios.md

# Integrate Luciq on iOS

## Installation

You can integrate Luciq using one of four methods: CocoaPods, Carthage, SPM, or manually.&#x20;

The installation process will set up the Luciq SDK to support App Performance Monitoring, Crash Reporting, and Bug Reporting, Session Replay and In-App Surveys

### 1. CocoaPods

To integrate Luciq into your Xcode project using CocoaPods, add it to your `Podfile`.

```shell
pod 'Luciq'
```

Then, run the following command

```shell
pod install
```

CocoaPods will download and install the SDK and add all the required dependencies to your Xcode project. You can follow the steps [here](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-crash-reporting/symbolication) to add a script that will automatically upload your dSYMs so that your crash reports are automatically symbolicated.

{% hint style="info" %}

### Pod Update

Since CocoaPods might not always download the latest version of the SDK when using `pod install`, we recommend that you also run `pod update Luciq` after the installation has completed or whenever you would like to update Luciq.
{% endhint %}

### 2. Swift Package Manager

To integrate Luciq into your Xcode project using SPM, follow the below steps:

1. Open target project
2. Select Swift Packages as shown below
3. Add a new package with the following link: <https://github.com/luciqai/luciq-ios-sdk>
4. Select Next then Finish

### 3. Carthage

To integrate Luciq in your Xcode project using Carthage, add it to your `Cartfile`.

```shell
binary "https://raw.githubusercontent.com/luciqai/luciq-ios-sdk/main/Luciq.json"
```

Then, run the following command.

```shell
carthage update
```

Finally, drag `LuciqSDK.xcframework` into your Xcode project. You can follow the steps [here](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-crash-reporting/symbolication) to add a script that will automatically upload your dSYMs so that your crash reports are automatically symbolicated.

### 4. Manually

1. Download the [**Luciq SDK**](https://github.com/luciqai/luciq-ios-sdk).
2. Extract it, then drag and drop `LuciqSDK.xcframework` to your project's `Embedded Binaries` section under the **General** tab, and make sure that the **Copy items if needed** checkbox is checked.
3. You can follow the steps [here](https://docs.luciq.ai/ios/setup-crash-reporting/symbolication#automatically) to add a script that will automatically upload your dSYMs so that your crash reports are automatically symbolicated.
4. You can follow the steps [here](https://docs.instabug.com/docs/ios-symbolication#section-automatically) to add a script that will automatically upload your dSYMs so that your crash reports are automatically symbolicated.

## Using Luciq

It is absolutely safe to include Luciq in your App Store builds as it doesn't use any private APIs. If you'd like to only include it in beta builds, that can be done two ways depending on how you create your builds, either by having separate builds or the same build for Beta and Production.

### Separate Beta and Production Builds

Use this method if you create your development builds for beta testers using a different build configuration than the production builds that you submit to the App Store. You can only initialize Luciq using the profile that you use for your beta builds. To show Luciq, you can set up [multiple invocation events](https://docs.luciq.ai/ios/setup-bug-reporting/showing-luciq#invocation-events).

The code below only enables Luciq for the `DEBUG` build profile.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
#if DEBUG
Luciq.start(withToken: "YOUR-TOKEN-HERE", invocationEvents: [.shake, .screenshot])
#endif
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
#ifdef DEBUG
[Luciq startWithToken:@"YOUR-TOKEN-HERE" invocationEvents: LCQInvocationEventShake | LCQInvocationEventScreenshot]
#endif
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Same Beta and Production Build

Use this method if you create your beta and production builds using the same configuration.

The following method returns YES if the app is running live from the App Store and NO if it is running from the simulator, Xcode, Fabric Beta, or TestFlight.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
func isRunningLive() -> Bool {
     #if targetEnvironment(simulator)
    return false
    #else
    let isRunningTestFlightBeta  = (Bundle.main.appStoreReceiptURL?.lastPathComponent == "sandboxReceipt")
    let hasEmbeddedMobileProvision = Bundle.main.path(forResource: "embedded", ofType: "mobileprovision") != nil
    if (isRunningTestFlightBeta || hasEmbeddedMobileProvision) {
        return false
    } else {
        return true
    }
    #endif
}

if (self.isRunningLive()) {
Luciq.start(withToken: "YOUR-LIVE-TOKEN-HERE", invocationEvents: [.shake, .screenshot])
} else {
Luciq.start(withToken: "YOUR-BETA-TOKEN-HERE", invocationEvents: [.shake, .screenshot])

}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
- (BOOL) isRunningLive {
    #if TARGET_OS_SIMULATOR
         return NO;
    #else
        BOOL isRunningTestFlightBeta = [[[[NSBundle mainBundle] appStoreReceiptURL] lastPathComponent] isEqualToString:@"sandboxReceipt"];
        BOOL hasEmbeddedMobileProvision = [[NSBundle mainBundle] pathForResource:@"embedded" ofType:@"mobileprovision"];
        if (isRunningTestFlightBeta || hasEmbeddedMobileProvision)
            return NO;
       return YES;
   #endif
}

if ([self isRunningLive])
   [Luciq startWithToken:@"YOUR-LIVE-TOKEN-HERE" invocationEvents: LCQInvocationEventShake | LCQInvocationEventScreenshot]

else
    [Luciq startWithToken:@"YOUR-BETA-TOKEN-HERE" invocationEvents: LCQInvocationEventShake | LCQInvocationEventScreenshot]
```

{% endcode %}
{% endtab %}
{% endtabs %}

You can find your app token by selecting **SDK Integration** in the **Settings** menu from your [**Luciq dashboard**](https://dashboard.luciq.ai).

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FE3CE31ebSMFGPuO4aLhW%2Fimage.png?alt=media&#x26;token=86824ac1-8fb8-4d18-a1f4-0a33f8ee3842" alt=""><figcaption></figcaption></figure>

## Managing Permissions

Luciq needs access to the device microphone and photo library to be able to let users add audio, image, and video attachments. Starting from iOS 10, apps that don’t provide a usage description for those two permissions will be rejected when submitted to the App Store.

To prevent your app from being rejected, you’ll need to add the following two keys to your app’s `info.plist` file with text that explains to your app users why those permissions are needed:

* `NSMicrophoneUsageDescription`
* `NSPhotoLibraryUsageDescription`

If your app doesn’t already access the microphone or photo library, we recommend usage descriptions like:

* " needs access to your microphone so you can attach voice notes."
* " needs access to your photo library so you can attach images."

**The permission alert for accessing the microphone/photo library will NOT appear unless users attempt to attach a voice note/photo while using Luciq.**

{% hint style="warning" %}

### Permissions Are Required

The above permissions are required in order for you to receive attachments from your users through the Luciq SDK.
{% endhint %}
