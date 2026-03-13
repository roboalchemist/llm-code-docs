# Source: https://docs.logrocket.com/reference/ios.md

# Initialize SDK

Initialize LogRocket and start recording sessions

Call `SDK.initialize()` with your appID to configure and start LogRocket. You can find your appID on [https://app.logrocket.com](https://app.logrocket.com) under Settings > Project Setup.

##

### Swift Package Manager

The LogRocket iOS SDK is available as a Swift Package. To install the SDK as a Swift Package go to **File -> Add Packages...** in XCode and enter `https://github.com/LogRocket/logrocket-ios-swift-package` into the "Search or Enter Package URL" field.

Once the package has been added continue on to [**Initializing the SDK**](#initializing-the-sdk).

### CocoaPods

Integrating your app with the LogRocket SDK currently requires [CocoaPods](https://cocoapods.org/) to handle dependencies and versioning. If you already use CocoaPods in your app, skip to the next step.

1. Follow the instructions to install CocoaPods and use `pod init` in your app's Xcode project directory to create a `Podfile`
2. Update your `Podfile` to use the correct iOS version, e.g., `platform :ios, '12.0'` or greater.

From now on, make sure you use the CocoaPods generated XCode workspace (if you didn't already have a workspace) so that any installed pods are available to your application.

### Adding the SDK

Add the LogRocket pod in the app target of your `Podfile` and then run `pod install` to add our framework to your application. New releases of the LogRocket Native SDKs are catalogued on our [Mobile SDK Changelog](https://docs.logrocket.com/docs/mobile-sdk-changelog).

```ruby
platform :ios, '12.0'

target 'app' do
  pod 'LogRocket', '~> 1.0'
end
```

### Initializing the SDK

The LogRocket iOS SDK must be initialized from your app delegate's `application` handler.

Replace `<APP_SLUG>` with your LogRocket application slug, located in our [dashboard's quick start guides](https://app.logrocket.com/r/settings/setup).

```swift
import LogRocket

class AppDelegate: UIResponder, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Configuration options listed below can be provided to the Configuration constructor.
    SDK.initialize(configuration: Configuration(appID: "<APP_SLUG>"))
    return true
  }
}
```

```objectivec
#import <LogRocket/LogRocket-Swift.h>
  
@implementation AppDelegate

- (BOOL) application:(UIApplication*)application didFinishLaunchingWithOptions:(NSDictionary*)launchOptions
{
    LROConfiguration *configuration = [[LROConfiguration alloc] initWithAppID:@"<APP_SLUG>"];
    // Configuration options listed below can be assigned to the configuration object.
    [LROSDK initializeWithConfiguration:configuration];

    return YES;
}

@end
```

### Supported iOS Versions

The LogRocket iOS SDK supports iOS 12.0 and up.