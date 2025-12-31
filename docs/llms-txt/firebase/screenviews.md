# Source: https://firebase.google.com/docs/analytics/screenviews.md.txt

Google Analyticstracks screen transitions and attaches information about the current screen to events, enabling you to track metrics such as user engagement or user behavior per screen. Much of this data collection happens automatically, but you can also manually log screenviews. Manually tracking screens is useful if your app does not use a separate`UIViewController`,`View`, or`Activity`for each screen you may wish to track, such as in a game.

## Automatically track screens

Analyticsautomatically tracks some information about screens in your application, such as the class name of the`UIViewController`or`Activity`that is currently in focus. When a screen transition occurs,Analyticslogs a`screen_view`event that identifies the new screen. Events that occur on these screens are automatically tagged with the parameter`firebase_screen_class`(for example,`menuViewController`or`MenuActivity`) and a generated`firebase_screen_id`. If your app uses a distinct`UIViewController`or`Activity`for each screen,Analyticscan automatically track every screen transition and generate a report of user engagement broken down by screen. If your app doesn't, you can still get these reports by manually logging`screen_view`events.
| **Note:** On Apple platforms, Firebase depends on method swizzling to automatically log screen views. SwiftUI apps must manually set screen names for views that should be logged via the`FirebaseAnalyticsSwift`module, or log screen views manually (see below).

## Disable screenview tracking

Automatic screenview reporting can be turned off on iOS by setting`FirebaseAutomaticScreenReportingEnabled`to`NO`(Boolean) in the Info.plist.

And on Android, nest the following setting within the`<application>`tag of the`AndroidManifest.xml`file:  

    <meta-data android:name="google_analytics_automatic_screen_reporting_enabled" android:value="false" />

## Manually track screens

You can manually log`screen_view`events whether or not automatic tracking is enabled. You can log these events in the`onAppear`or`viewDidAppear`methods for Apple platforms and`onResume`for Android. When`screen_class`is not set,Analyticssets a default value based on the UIViewController or Activity that is in focus when the call is made.

If you've disabled swizzling in your app, all screen names must be set manually. For SwiftUI users, use theAnalytics[Swift extension SDK](https://github.com/firebase/firebase-ios-sdk/tree/master/FirebaseAnalyticsSwift#firebase-analytics-swift-sdk).  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
Analytics.logEvent(AnalyticsEventScreenView,
                   parameters: [AnalyticsParameterScreenName: screenName,
                               AnalyticsParameterScreenClass: screenClass])https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/QSSnippets/MigratedSnippets.swift#L86-L88
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
[FIRAnalytics logEventWithName:kFIREventScreenView
                    parameters:@{kFIRParameterScreenClass: screenClass,
                                 kFIRParameterScreenName: screenName}];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/QSSnippets/ObjCMigratedSnippets.m#L94-L96
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW) {
    param(FirebaseAnalytics.Param.SCREEN_NAME, screenName)
    param(FirebaseAnalytics.Param.SCREEN_CLASS, "MainActivity")
}https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L249-L252
```

### Java

```java
Bundle bundle = new Bundle();
bundle.putString(FirebaseAnalytics.Param.SCREEN_NAME, screenName);
bundle.putString(FirebaseAnalytics.Param.SCREEN_CLASS, "MainActivity");
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, bundle);https://github.com/firebase/snippets-android/blob/4c2b992d5e2f28aff48e72d2727127fe8100cae3/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L314-L317
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

const analytics = getAnalytics();
logEvent(analytics, 'screen_view', {
  firebase_screen: screenName, 
  firebase_screen_class: screenClass
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/index/analytics_record_screen_view.js#L8-L14
```

### Web

```javascript
firebase.analytics().logEvent('screen_view', {
  firebase_screen: screenName, 
  firebase_screen_class: screenClass
});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/index.js#L47-L50
```

### Dart

    await FirebaseAnalytics.instance.logEvent(
      name: 'screen_view',
      parameters: {
        'firebase_screen': screenName,
        'firebase_screen_class': screenClass,
      },
    );