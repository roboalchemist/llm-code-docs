# Source: https://docs.logrocket.com/docs/mobile-sdk-changelog.md

# Mobile SDK Changelog

<sup>*This page covers mobile SDK releases from version 1.47.2 onward. Earlier versions can be found[ here](https://docs.logrocket.com/docs/mobile-sdk-changelog-archive)                                            .*</sup>

## 2.1.0 (2026-03-10)

**Minimum Self-Hosted Release `24.78.0`**

* \[Android] Prevent sessions from ending prematurely when the app is closed
* \[Android] Improve reliability of event capture when the SDK is offline

## 2.0.2 (2026-03-06)

* \[Android] Fix a Proguard configuration issue introduced in `2.0.0` that lead to `cannot find symbol` errors in Flutter and React Native

## 2.0.1 (2026-03-05)

* \[iOS] Fix an issue that could cause iOS apps to freeze when moving to the background
* \[Android] Fix clip outlines in Jetpack Compose 1.10 session replays
* \[Android] Fix an issue introduced in `2.0.0` where the `setLogLevel` configuration option was ignored

## 2.0.0 (2026-02-27)

**Minimum Self-Hosted Release `24.33.0`**

* \[Android] Updated View Capture approach. See [full details here](https://docs.logrocket.com/reference/android-sdk-20).

<Callout icon="📘" theme="info">
  The Jetpack Compose dependency must be installed for apps using Jetpack Compose for versions 2.0.0 and above. See [full details here](https://docs.logrocket.com/reference/android-sdk-20#jetpack-compose).
</Callout>

##

## 1.62.0 (2026-02-13)

**Minimum Self-Hosted Release `23.387.0`**

* \[iOS] Fix a view capture bug that can lead to missing views in replay, especially within scroll containers.
* \[Android] Increase image size capture limit
* \[All] Add event timeline entry for when the app is opened or brought to the foreground

## 1.61.2 (2026-02-10)

* \[Android] Add support for Jetpack Compose 1.10
* \[iOS] Capture more SwiftUI image layers

## 1.61.1 (2026-02-05)

* \[iOS] Reduces risk of non-redacted text appearing in apps utilizing SwiftUI views compiled with Xcode 26 when passing `textSanitizer: .excluded`. Some views may become over-redacted to prevent text from leaking. See more info [here](https://docs.logrocket.com/reference/ios-automatically-sanitize-text).
* \[Android] Prevent exceptions from being thrown from null inputs in user identification, custom events, or page tags

## 1.61.0 (2026-02-04)

**Minimum Self-Hosted Release `23.334.0`**

* \[All] Added support for configuring [conditional recording](https://docs.logrocket.com/docs/conditional-recording) rules based on platform.
* \[iOS] Fixed a potential crash that could occur when initializing the SDK from an NSURLSession callback.

## 1.60.0 (2026-01-23)

**Minimum Self-Hosted Release `23.282.0`**

* \[iOS] Events are now properly attributed when a new session is started.
* \[iOS] Fix potential crash when an NRF matches during session resumption.
* \[React Native] Properly resume in progress recordings during disruptions.

## 1.59.6 (2026-01-20)

* \[React Native Android] Gradient text blocks will display properly in replays instead of displaying as rectangles
* \[Android] Improve Jetpack Compose touch attribution
* \[iOS] Remove build warning caused by the LogRocket iOS SDK

## 1.59.5 (2026-01-14)

> ❗️ Important
>
> A bug present in this release can result in app crashes on iOS. This was resolved in [1.59.6](#1596-2026-01-20) for iOS.

* \[Android] Prevent a rare concurrent modification crash
* \[iOS React Native] Prevent potential touch unresponsiveness after the app is backgrounded and reopened
* \[Flutter] Prevent fatal exceptions from occurring during touch encoding

## 1.59.4 (2025-12-29)

* \[All] Improves crash report delivery when SDK initialization is delayed
* \[Android] Fixes an issue introduced in 1.59.0 which could cause app crashes under heavy event volume during the session initialization process.

## 1.59.3 (2025-12-22)

> ❗️ Important
>
> A bug present in this release can result in app crashes on Android. This was resolved in [1.59.4](#1594-2025-12-29) for Android.

* \[iOS] Fixes an issue introduced in 1.59.0 which could cause app crashes under heavy event volume during the session initialization process.

## 1.59.2 (2025-12-12)

> ❗️ Important
>
> A bug present in this release can result in app crashes on iOS and Android. This was resolved in [1.59.3](#1593-2025-12-22) for iOS and [1.59.4](#1594-2025-12-29) for Android.

* \[iOS] Fixes an issue introduced in 1.58.0 which could cause hangs on app backgrounding.
* \[iOS] Improves log level categorization of captured `stderr` logs.

## 1.59.1 (2025-12-02)

> ❗️ Important
>
> A bug present in this release can result in app crashes on iOS and Android. This was resolved in [1.59.3](#1593-2025-12-22) for iOS and [1.59.4](#1594-2025-12-29) for Android.

* \[iOS] Adds `maxCapturedIosVersion` init configuration. This controls the maximum device iOS version to record and defaults to the latest publicly available major version number.
* \[Android] Adds `maxCapturedAndroidApiLevel` init configuration. This controls the maximum device Android API level to record and defaults to the latest publicly available API level.
* \[All] Adds `getSessionUrlStatus`. Not available for Flutter. See docs for [iOS](https://docs.logrocket.com/reference/ios-get-session-url#/session-url-status), [Android](https://docs.logrocket.com/reference/android-get-session-url#/session-url-status), and [React Native](https://docs.logrocket.com/reference/react-native-get-session-url#/session-url-status).

## 1.59.0 (2025-11-25)

> ❗️ Important
>
> A bug present in this release can result in app crashes on iOS and Android. This was resolved in [1.59.3](#1593-2025-12-22) for iOS and [1.59.4](#1594-2025-12-29) for Android.

**Minimum Self-Hosted Release `23.98.0`**

* \[All] Can now match events to filters and observe conditional recording rules while session initialization is in progress
* \[All] Add warning during replay when session contains wireframe capture.
* \[Android] Add support for Jetpack Compose 1.9.4

## 1.58.1 (2025-11-20)

* \[iOS] Fix issue causing sessions to be limited to one custom event per session.

## 1.58.0 (2025-11-14)

> ⚠️ Warning
>
> A build issue limited iOS sessions to a single custom event per session. This was resolved in 1.58.1.

**Minimum Self-Hosted Release `23.64.0`**

* \[All] Improved ability to resume sessions when a user leaves and returns to the app if disk persistence is not available.
* \[iOS] Resolve an issue that could lead to data loss if a user backgrounds an application.
* \[React Native] Prevent "Invalid resource ID" error logs in Android React Native applications.

## 1.57.5 (2025-10-17)

* \[All] Add support for Active Time in Session filters for [Conditional Recording](https://docs.logrocket.com/docs/conditional-recording)
* \[All] Add a color fill in replay for elements not recorded due to view capture timeouts

## 1.57.4 (2025-10-08)

* \[React Native] Prevent exception from being thrown when LogRocket.identify is called with only user traits and no user ID
* \[All] Prevent interpreting user scrolling as Rage Clicks

## 1.57.3 (2025-09-30)

* \[iOS] Improve replay layout accuracy for apps built with Xcode 26 and run on iOS 26

## 1.57.2 (2025-09-25)

* \[All] Adds support for metric aggregations on network body JSON fields as documented [here](https://docs.logrocket.com/docs/timeseries-1#network-requestresponse-body).
* \[Android] Prevent app background starts from resulting in nonsensically long app start times in the session replay performance timeline.

## 1.57.1 (2025-09-17)

* \[React Native Android] Fix issues with custom font capture
* \[Android] Improve replay fidelity for animated components, including React Native drawers.
* \[React Native iOS] Added configuration settings to enable network capture in native iOS in React Native. See [docs](https://docs.logrocket.com/reference/react-native-network#ios-native-network-capture-in-react-native) for configuration details.

## 1.57.0 (2025-09-11)

* \[iOS] Makes changes necessary for correct redaction of SwiftUI views in apps compiled by Xcode 26 on devices running iOS 26.

> ❗️ Important
>
> Before submitting an app update to the App Store compiled with Xcode 26, it is critical that you update the LogRocket SDK to 1.57.0. It is possible that apps compiled with Xcode 26 with a version of LogRocket prior to 1.57.0 will leak views marked for redaction during view capture on iOS 26.

* \[iOS] Introduces experimental `lrShowWithContainer` and `lrHideWithContainer` methods available as substitutes for `lrShow` and `lrHide` when redacting or explicitly allowing SwiftUI views.

> ⚠️ Warning
>
> It is possible for views redacted or allowed with the `withContainer` variants of `lrHide` and `lrShow` to subtly affect the layout of your app at runtime, particularly when the marked view and its siblings are text-based. For more information about redaction support in iOS 26, see this documentation page.

## 1.56.3 (2025-09-08)

* \[All] Prevent a race condition that could lead to session corruption when a new session is triggered from inside a Web View.

## 1.56.2 (2025-09-03)

* \[iOS] Improves replay fidelity for devices running the upcoming iOS 26 release.
* \[iOS] Prevents a crash that could occur when processing extremely large events.

## 1.56.1 (2025-08-21)

* \[All] Resolved an issue with some layer render locations in session replay.
* \[React Native] Resolved an issue introduced in `1.55.0` where XHR network response blobs would be dropped even when `shouldParseXHRBlob` was specified.

## 1.56.0 (2025-08-13)

**Minimum Self-Hosted Release `21.318.0`**

* \[iOS] Improve accuracy and stability of SwiftUI view redaction.
* \[iOS] Exclude autocorrect hints from view capture.
* <Callout icon="🚧" theme="warn">
    If your iOS app is built using **SwiftUI**, we recommend confirming all views are redacted as you expect when upgrading to 1.56.0, and adjusting your use of `.lrHide()` and `.lrShow()` if necessary. The LogRocket SDK will now more accurately redact or allow only the views which have been tagged with `.lrHide()` or `.lrShow()`. [See full documentation here.](https://docs.logrocket.com/reference/swiftui-about#individual-view-redaction)
  </Callout>

## 1.55.1 (2025-08-08)

* \[React Native] Add support for specifying multiple custom font directories.
* \[Android] Allow tags will now prevent text from being redacted by text sanitizer in Jetpack Compose.
* \[Flutter] Improve error handling during initialization of `LogRocketWidget`.

## 1.55.0 (2025-08-01)

**Minimum Self-Hosted Release `21.281.0`**

* \[All] Eliminated the potential for a recording shutdown to occur were excessive session data to be recorded in a short timeframe.
* \[iOS] Fixed an issue that could result in crashes during crash handling in circumstances where the SDK has been shut down.
* \[All] Improved view capture performance when Element Visible filters or conditional recording are in use.
* \[Flutter] Improved navigation capture stability.

## 1.54.3 (2025-07-23)

* \[iOS] Fix potential crash that can occur while capturing replays that include images
* \[Flutter] Improve accuracy of captured network response durations

## 1.54.2 (2025-07-14)

* \[Android, iOS] Add support for redacting and allowing individual views with `SDK.redactView` and `SDK.allowView`
* \[iOS] Fix thread safety issue in `captureException`
* \[Flutter] Add support for "Clicked when URL ..." filters

## 1.54.1 (2025-07-08)

* \[iOS] Prevent network capture conflicts with BrazeSDK
* \[Android] Adds Jetpack Compose support for Compose Foundation 1.8
* > ❗️ Jetpack Compose 1.8 Redaction
  >
  > Redaction through `semantics` modifiers is no longer supported in Jetpack Compose 1.8. See all [supported redaction methods here](https://docs.logrocket.com/reference/jetpack-compose-about#redaction).
  >
  > ```kotlin
  > // this will NOT be redacted from LogRocket sessions in a Jetpack Compose 1.8 apps
  > Row(modifier = Modifier.semantics {
  >   testTag = "lr-hide"
  > })
  >
  > // this WILL be redacted
  > Row(modifier = Modifier.testTag("lr-hide"))
  > ```

## 1.54.0 (2025-07-02)

**Minimum Self-Hosted Release `21.173.0`**

* \[iOS] Fixed an issue where automatic navigation capture was disabled by default when initializing an SDK configuration instance using only an appID.

<Callout icon="📘" theme="info">
  Note that though this is a bug fix and restores documented behavior, it does result in a change to default behavior for apps using the `appID`-only constructor. To turn off automatic navigation capture, pass `enableAutomaticLifecycleCapture: false` to your `Configuration` instance at SDK initialization.
</Callout>

* \[Flutter] Fixed an issue which caused network requests to have erroneous 0 ms durations on Android when examining network requests in metrics detail views.

## 1.53.3 (2025-06-27)

* \[Flutter] Add `screenshotPixelRatio` init configuration to allow reducing captured screenshot sizes, which can reduce LogRocket SDK bandwidth usage.
* \[Flutter] Improves performance while scrolling.

## 1.53.2 (2025-06-24)

* \[Flutter] Adds support for nested `LogRocketNavigatorObserver`s.

## 1.53.1 (2025-06-18)

**Minimum Self-Hosted Release `21.112.0`**

* \[Android, iOS, React Native] Captures wireframes of remaining elements when view capture times out.
* \[iOS] Adds initial support for Lottie animation capture in Swift UI via the new `lottieCaptureEnabled` config option.
* \[Flutter] Allows `LogRocket` via a `LogRocket()` class instance in order to mock static function calls for testing.

## 1.53.0 (2025-06-17)

* LogRocket's automated release process encountered an error during this release so this version number is not used.

## 1.52.3 (2025-06-03)

* \[All] Reduces delays between when new sessions start on a device and when they are visible in the LogRocket dashboard.
* \[iOS] Fixes a crash that could occur while processing GraphQL Responses.
* \[React Native] Prevents excessively large redux actions from causing sessions to stop recording, and instead disables Redux capture.

## 1.52.2 (2025-05-30)

* \[Flutter] Prevents Android sessions from continuing indefinitely while the app is in the background

## 1.52.1 (2025-05-29)

* \[iOS] Improved the safety and reliability of crash capture.
* \[Flutter] Fixed an issue which could cause automatic network capture to interfere with network requests.

## 1.52.0 (2025-05-21)

**Minimum Self-Hosted Release `21.35.0`**

* \[All] Improves navigation tracking when a new session is started after a period of inactivity.

## 1.51.2 (2025-05-13)

* \[iOS] Improves how redacted views in iOS apps are displayed in session replays.

## 1.51.1 (2025-05-07)

* \[iOS] Increases session upload frequency when battery is sufficiently charged or is currently charging.
* \[React Native] Allows disabling iOS native log capture by providing init config `nativeLogCaptureEnabled: false`.

## 1.51.0 (2025-05-02)

**Minimum Self-Hosted Release `20.98.0`**

* \[Android] Adds support for session recording on Android 16 devices.
* \[All] Resolves an issue where `getSessionURL` callbacks may not run or may be provided an empty string when using Conditional Recording.

## 1.50.7 (2025-04-30)

* \[Flutter] Fix an issue that could prevent view capture from starting on iOS when using `wrapAndInitialize`.
* \[Flutter] Fix an issue on Android that could cause a new tab to register at the start of a session.

## 1.50.6 (2025-04-28)

* \[All] Resolve an issue introduced in 1.50.4 that could cause Mobile SDKs to ignore conditional recording rules.

## 1.50.5 (2025-04-25)

**This release contains an issue with Conditional Recording that may cause all sessions to be captured.**

* \[iOS] Fixed an issue that could lead to uncaptured network responses.

## 1.50.4 (2025-04-17)

**This release contains an issue with Conditional Recording that may cause all sessions to be captured.**

* \[iOS] Fixed an issue that impacted the position accuracy of certain iOS view elements rendered in session replay.

## 1.50.3 (2025-04-14)

* \[All] Allow custom page tags ([iOS](https://docs.logrocket.com/reference/capture-custom-pages-ios#/), [Android](https://docs.logrocket.com/reference/capture-custom-pages-android#/), [React Native](https://docs.logrocket.com/reference/capture-custom-pages-reactnative#/), [Flutter](https://docs.logrocket.com/reference/flutter-navigation-capture#/tag-pages)) to satisfy "Visited URL / Mobile Page" recording conditions and time between events filters.

## 1.50.2 (2025-04-08)

* \[Android] Reduce memory consumption while capturing some images and SVGs, which are especially common in Jetpack Compose.
* \[iOS] Prevent any errors that occur while reading stderr or stdout logs from causing app crashes.

## 1.50.1 (2025-04-04)

* \[React Native] Update Expo plugin to automatically update the LogRocket custom font plugin version.

## 1.50.0 (2025-04-02)

**Minimum Self-Hosted Release `20.9.0`**

* \[Android] Resolve an issue causing build failures for apps with many custom font files.
* \[All] Allow tags will now prevent text from being redacted by text sanitizer (excluding Jetpack Compose apps).

> 📘 Introducing Flutter support (Beta)
>
> See the configuration guide [here](https://docs.logrocket.com/reference/configure-flutter-sdk#/) for setup instructions

## 1.49.0 (2025-04-01)

**Minimum Self-Hosted Release `20.3.0`**

* \[Android] Prevent view capture from causing app hangs.
* \[Both] Fixed an issue with Conditional Recording sessions introduced in **1.47.5**. Prevents sessions started when an app is reopened from the background from being recorded without satisfying recording conditions.
* \[Both] Added "GraphQL Error" Issue type capture

## 1.48.4 (2025-03-25)

* \[iOS] Prevented potential memory access errors when the `extendedViewTextCaptureEnabled` flag is disabled.
* \[iOS] Added `networkCaptureRedactedOrigins` configuration setting for redacting network capture on specified origins.

## 1.48.3 (2025-03-21)

* \[iOS] Added configuration settings for disabling unexpected exception capture.

## 1.48.2 (2025-03-13)

* \[iOS] Fixed an issue that impacted the accuracy of iOS session duration reporting in the dashboard.
* \[iOS] Fixed an issue that could result in bad memory accesses during view controller text capture in rare instances.
* \[iOS] Fixed an issue that prevented page-tagging the view controller visible at SDK initialization.

## 1.48.1 (2025-03-06)

* \[React Native] Added LogRocket.info, warn, error, and debug functions for manually recording logs in a LogRocket session.
* \[iOS] Improved view capture performance.

## 1.48.0 (2025-02-27)

**Minimum Self-Hosted Release `19.418.0`**

* \[iOS] Fix an issue where LogRocket network capture could cause certain streamed requests to fail with a timeout.
* \[iOS] Fixed a bug which caused WebSocket connections to fail with network capture enabled.

## 1.47.10 (2025-02-21)

* \[All] Conditional recording sessions confirmed from inside a web view now confirm the accompanying native session, and vice versa.
* \[React Native iOS] Fixed a bug which could cause capture of views marked for redaction via the `nativeID` component prop on some devices.

## 1.47.9 (2025-02-12)

* \[iOS] Removed the source of a potential deadlock in the iOS crash reporting logic.

## 1.47.8 (2025-02-11)

* \[Android] Resolved an issue that inadvertently required a `minCompileSdk` of API 32 instead of API 25.

## 1.47.7 (2025-02-04)

* \[Android] Improved replay fidelity when device changes orientation.
* \[React Native] Added 'expoChannel' config value for use with Updates.channel.

## 1.47.6 (2025-01-30)

* \[iOS] Resolved potential crash that can occur while capturing details about uncaught exceptions.

## 1.47.5 (2025-01-27)

* \[Android] Improve replay fidelity when device changes orientation.
* \[Android] Prevent a crash that can occur if `tagPage` is called inside an Activity's `onCreate` or a Fragment's `onCreateView()`.

## 1.47.4 (2025-01-15)

* \[All] Added a `enableAutomaticLifecycleCapture` configuration option to control whether iOS view controller and Android activity lifecycle events are tracked. If the SDK is initialized with this option set to false, the SDK will only emit lifecycle events when pages are manually tagged via `tagPage`.

## 1.47.3 (2025-01-14)

* \[iOS] Improve page name tracking.
* \[React Native] Prevent UI freezes under certain circumstances on iOS.

## 1.47.2 (2025-01-03)

* \[All] Improved user attribution of crash reports
* \[React Native] Improved typescript definitions for network sanitizers

## Older versions

* See [Mobile SDK Changelog (cont.)](https://docs.logrocket.com/docs/mobile-sdk-changelog-archive#1471-2024-12-20) for more