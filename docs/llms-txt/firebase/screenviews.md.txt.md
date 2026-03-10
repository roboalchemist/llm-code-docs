# Source: https://firebase.google.com/docs/analytics/screenviews.md.txt

Google Analytics tracks screen transitions and attaches information
about the current screen to events, enabling you to track metrics such as user
engagement or user behavior per screen. Much of this data collection happens
automatically, but you can also manually log screenviews. Manually tracking
screens is useful if your app does not use a separate `UIViewController`,
`View`, or `Activity` for each screen you may wish to track, such as in a game.

## Automatically track screens

Analytics automatically tracks some information about screens in your
application, such as the class name of the `UIViewController` or `Activity` that
is currently in focus. When a screen transition occurs, Analytics logs a
`screen_view` event that identifies the new screen. Events that occur on these
screens are automatically tagged with the parameter `firebase_screen_class` (for
example, `menuViewController` or `MenuActivity`) and a generated
`firebase_screen_id`. If your app uses a distinct `UIViewController` or
`Activity` for each screen, Analytics can automatically track every screen
transition and generate a report of user engagement broken down by screen. If
your app doesn't, you can still get these reports by manually logging
`screen_view` events.

> [!NOTE]
> **Note:** On Apple platforms, Firebase depends on method swizzling to automatically log screen views. SwiftUI apps must manually set screen names for views that should be logged via the `FirebaseAnalyticsSwift` module, or log screen views manually (see below).

## Disable screenview tracking

Automatic screenview reporting can be turned off on iOS by setting
`FirebaseAutomaticScreenReportingEnabled` to `NO` (Boolean) in the Info.plist.

And on Android, nest the following setting within the `<application>` tag of the
`AndroidManifest.xml` file:

    <meta-data android:name="google_analytics_automatic_screen_reporting_enabled" android:value="false" />

## Manually track screens

You can manually log `screen_view` events whether or not automatic tracking is
enabled. You can log these events in the `onAppear` or `viewDidAppear` methods
for Apple platforms and `onResume` for Android. When `screen_class` is not set,
Analytics sets a default value based on the UIViewController or Activity
that is in focus when the call is made.

If you've disabled swizzling in your app, all screen names must be set manually.
For SwiftUI users, use the Analytics
[Swift extension SDK](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseAnalyticsSwift#firebase-analytics-swift-sdk).

### Swift


**Note:** This Firebase product is not available on the macOS target.

```swift
Analytics.logEvent(AnalyticsEventScreenView,
                   parameters: [AnalyticsParameterScreenName: screenName,
                               AnalyticsParameterScreenClass: screenClass])
```

### Objective-C


**Note:** This Firebase product is not available on the macOS target.

```objective-c
[FIRAnalytics logEventWithName:kFIREventScreenView
                    parameters:@{kFIRParameterScreenClass: screenClass,
                                 kFIRParameterScreenName: screenName}];
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW) {
    param(FirebaseAnalytics.Param.SCREEN_NAME, screenName)
    param(FirebaseAnalytics.Param.SCREEN_CLASS, "MainActivity")
}
```

### Java

```java
Bundle bundle = new Bundle();
bundle.putString(FirebaseAnalytics.Param.SCREEN_NAME, screenName);
bundle.putString(FirebaseAnalytics.Param.SCREEN_CLASS, "MainActivity");
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, bundle);
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

const analytics = getAnalytics();
logEvent(analytics, 'screen_view', {
  firebase_screen: screenName, 
  firebase_screen_class: screenClass
});
```

### Web

```javascript
firebase.analytics().logEvent('screen_view', {
  firebase_screen: screenName, 
  firebase_screen_class: screenClass
});
```

### Dart

    await FirebaseAnalytics.instance.logEvent(
      name: 'screen_view',
      parameters: {
        'firebase_screen': screenName,
        'firebase_screen_class': screenClass,
      },
    );