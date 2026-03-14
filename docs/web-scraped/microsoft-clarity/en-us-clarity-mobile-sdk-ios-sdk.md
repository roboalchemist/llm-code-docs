# Source: https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk

Title: iOS SDK Installation

URL Source: https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk

Markdown Content:
Important

*   The Clarity iOS SDK collects sessions from iOS versions within the supported range specified at [Platform/Framework Support Matrix](https://learn.microsoft.com/en-us/clarity/mobile-sdk/mobile-sdk-overview#platformframework-support-matrix).
*   While applications build and run successfully for iOS versions 13 and 14, data isn't sent to Clarity for these versions.
*   Due to some SwiftUI limitations, it is **strongly advised** to review the [SwiftUI Modifiers](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#swiftui-modifiers) section for guidance.

Install the Clarity SDK in order to track how users interact with your app. The Clarity iOS SDK is available as a Swift package and a CocoaPods pod. It can take up to 2 hours to start seeing data.

*   [Swift Package Manager](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#tabpanel_1_swift-package-manager)
*   [CocoaPods](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#tabpanel_1_cocoapods)

Option 1: Using XCode

1.   "Right click" on your XCode project and select **Add Package Dependencies...**
2.   Paste `https://github.com/microsoft/clarity-apps` in the search bar, select **clarity-apps**, and select **Add Package**.

Option 2: If the **Package.swift** file is used, add Clarity package as a dependency:

```
let package = Package(
    // ...
    dependencies: [
        //// Option 1: Fetch latest version available. This allows automatic major version updates that may contain non-backward compatible changes.
        .package(url: "https://github.com/microsoft/clarity-apps", branch: "main")
        //// Option 2: Fetch a specific minor version range (For example, 3.0.0 up to, but not including, 4.0.0).
        // .package(url: "https://github.com/microsoft/clarity-apps", from: "3.0.0")
    ],
    targets: [
        .target(
            name: "<target-name>",
            dependencies: [
                .product(name: "Clarity", package: "clarity-apps")
            ]
        )
    ]
)
```

Note

Initialization has to run from the main thread.

*   [Swift](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#tabpanel_2_swift)
*   [Objective-C](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#tabpanel_2_objective-c)

Add the following code to **AppDelegate.swift** file:

```
import Clarity

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Note: Replace `<project-id>` with actual project ID found Clarity Settings -> Overview page.
        // Note: Set `.verbose` value for `logLevel` parameter while testing to debug initialization issues.
        let clarityConfig = ClarityConfig(projectId: "<project-id>")
        ClaritySDK.initialize(config: clarityConfig)
        return true
    }
    // ...
}
```

For SwiftUI, you can add the initialization code to your App's `init()` function.

Once you integrated Clarity with your application, ensure the following if you want to test it on a device or a simulator:

1.   Your device or simulator must be connected to the internet.
2.   The iOS version on your device or simulator should be within the supported range specified at [Platform/Framework Support Matrix](https://learn.microsoft.com/en-us/clarity/mobile-sdk/mobile-sdk-overview#platformframework-support-matrix).
3.   For initial setup, consider setting the log level to Verbose. This provides detailed logs that can help identify any initialization issues.

Allow approximately 2 hours for complete sessions to appear in your Clarity project on the Clarity website. However, in-progress sessions can still be viewed in real time. See [Clarity Recordings in Real Time](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-real-time).

```
class ClarityConfig {
    init(
        projectId: String,
        userId: String? = nil, // DEPRECATED
        logLevel: ClarityLogLevel = .none,
        applicationFramework: ClarityApplicationFramework = .native
    ) { }
}
```

The unique identifier assigned to your Clarity project. You can find it on the **Settings** page of Clarity dashboard. This ID is essential for routing data to the correct Clarity project.

The unique identifier associated with the application user. This ID persists across multiple sessions on the same device.

*   **Deprecated:** This field is deprecated and would be removed in a future major version. Use [`setCustomUserId`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setcustomuserid) instead.
*   If `userId` isn't provided, a random one is generated automatically.
*   Must be a base-36 string smaller than `1z141z4` and without any uppercase letters.
*   If an invalid `userId` is supplied: 
    *   If `customUserId` isn't specified: `userId` acts as the `customUserId`, and a new random `userId` is assigned.
    *   If `customUserId` is specified: the invalid `userId` is ignored.

Note

For greater flexibility in user identification, use the [`setCustomUserId`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setcustomuserid) API. Ensure that the `customUserId` length is between 1 and 255 characters.

The level of logging to show in the device's or Xcode's console while debugging. By default, the SDK logs nothing.

Allowed log levels are:

*   `.verbose`
*   `.debug`
*   `.info`
*   `.warning`
*   `.error`
*   `.none`

Signals to the SDK which framework is being used to develop the current application. This parameter is internal to the SDK and shouldn't be set manually.

Note

For Clarity versions `3.0.0` and above, the SDK supports SwiftUI. In earlier versions, the `enableSwiftUI_Experimental` configuration option is necessary to enable SwiftUI capture.

For Clarity versions `3.0.0` and above, the following configuration options are no longer configurable from code and can now be adjusted dynamically from the Clarity dashboard:

*   **Allow Metered Network Usage** (`allowMeteredNetworkUsage`): Allows uploading session data to the servers on device's metered networks. By default, the SDK only uploads sessions on unmetered networks.
*   **Enable WebView Capture** (`enableWebViewCapture`): Allows Clarity to capture the web views DOM content for recording and heatmap reconstruction.
*   **Disable on Low-End Devices** (`disableOnLowEndDevices`): When enabled, Clarity doesn't capture any data for the low-end devices.

```
static func initialize(config: ClarityConfig) -> Bool
```

Initializes Clarity to start capturing the current session data.

`config` ClarityConfig

Configuration of Clarity that tunes the SDK behavior (for example, which project to send to, which log level to use, and so on).

Bool

`true` if Clarity initialization is possible; otherwise `false`.

*   The initialization function is asynchronous and returns before Clarity is fully initialized.
*   For actions that require Clarity to be fully initialized, it's recommended to use the [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) function.
*   This function should only be called on the main thread.

```
static func pause()
```

Pauses the Clarity session capturing until a call to the [`resume`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#resume) function is made.

This function should only be called on the main thread.

```
static func resume()
```

Resumes the Clarity session capturing only if it was previously paused by a call to the [`pause`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#pause) function.

This function should only be called on the main thread.

```
static func isPaused() -> Bool
```

Checks if Clarity session capturing is currently paused based on an earlier call to the [`pause`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#pause) function.

Bool

`true` if Clarity session capturing is currently in the paused state based on an earlier call to the [`pause`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#pause) function; otherwise `false`.

```
static func startNewSession(callback: OnSessionStartedCallback?) -> Bool {
```

Forces Clarity to start a new session asynchronously.

`callback` OnSessionStartedCallback?

A callback that is invoked when the new session starts. The callback receives the new session ID as a string parameter.

Bool

`true` if a new session can start asynchronously; otherwise `false`.

*   This function is asynchronous and returns before the new session is started.
*   Use the `callback` parameter to execute logic that needs to run after the new session begins.
*   Events that occur before invoking the callback are associated with the previous session.
*   To ensure proper association of custom tags, user ID, or session ID with the new session, set them within the callback.
*   This function should only be called on the main thread.

```
static func maskView(_ view: UIView)
```

Masks a specific `UIView` to prevent Clarity from capturing its content (text or images). Masked content is replaced with placeholders.

`view` UIView

The `UIView` instance to mask its content.

This function should only be called on the main thread.

```
static func unmaskView(_ view: UIView)
```

Unmasks a specific `UIView` to allow Clarity to capture its content, even if it's a child of a masked view or within a masked screen.

`view` UIView

The `UIView` instance to unmask its content.

This function should only be called on the main thread.

```
static func setCustomUserId(_ customUserId: String) -> Bool
```

Sets a custom user ID for the current session. This ID can be used to filter sessions on the Clarity dashboard.

`customUserId` String

The custom user ID to associate with the current session. The value must be a nonempty string with a maximum length of 255 characters and can't consist only of whitespace.

Bool

`true` if the custom user ID was set successfully; otherwise `false`.

*   To ensure that the custom user ID is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#startnewsession).
*   Unlike the `userID`, the `customUserId` value has fewer restrictions.
*   We recommend **not** to set any [Personally Identifiable Information (PII)](https://learn.microsoft.com/en-us/clarity/setup-and-installation/glossary-of-terms) values inside this field.
*   This function should only be called on the main thread.

```
static func setCustomSessionId(_ customSessionId: String) -> Bool
```

Sets a custom session ID for the current session. This ID can be used to filter sessions on the Clarity dashboard.

`customSessionId` String

The custom session ID to associate with the current session. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Bool

`true` if the custom session ID was set successfully; otherwise `false`.

*   To ensure that the custom session ID is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#startnewsession).
*   This function should only be called on the main thread.

```
static func getCurrentSessionId() -> String?
```

Returns the ID of the currently active Clarity session if a session has already started; otherwise `nil`.

String?

A string representing the ID of the currently active Clarity session if a session has already started; otherwise `nil`.

*   **Deprecated:** This API is deprecated and would be removed in a future major version. Use [`getcurrentsessionurl`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#getcurrentsessionurl) instead.
*   The session ID can be used to correlate Clarity sessions with other telemetry services.
*   Initially, this function might return `nil` until a Clarity session begins.
*   To ensure a valid session ID, use this method within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#startnewsession).
*   This function should only be called on the main thread.

```
static func getCurrentSessionUrl() -> String?
```

Returns the URL of the current Clarity session recording on the Clarity dashboard if a session has already started; otherwise `nil`.

String?

A string representing the URL of the current Clarity session recording on the Clarity dashboard if a session has already started; otherwise `nil`.

*   Initially, this function might return `nil` until a Clarity session begins.
*   To ensure a valid session URL, use this method within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#startnewsession).
*   This function should only be called on the main thread.

```
static func setCustomTag(key: String, value: String) -> Bool
```

Sets a custom tag for the current session. This tag can be used to filter sessions on the Clarity dashboard.

`key` String

The key for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

`value` String

The value for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Bool

`true` if the custom tag was set successfully; otherwise `false`.

*   To ensure that the custom tag is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#startnewsession).
*   This function should only be called on the main thread.

```
static func setCustomTag(key: String, value: String...) -> Bool
```

Sets a custom tag for the current session. This tag can be used to filter sessions on the Clarity dashboard.

`key` String

The key for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

`value` String

The value(s) for the custom tag. Each value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Bool

`true` if the custom tag was set successfully; otherwise `false`.

*   To ensure that the custom tag is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#startnewsession).
*   This function should only be called on the main thread.

```
static func setCustomTag(key: String, values: Set<String>) -> Bool
```

Sets a custom tag for the current session. This tag can be used to filter sessions on the Clarity dashboard.

`key` String

The key for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

`values` String

The set of values for the custom tag. Each value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Bool

`true` if the custom tag was set successfully; otherwise `false`.

*   To ensure that the custom tag is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/ios-sdk#startnewsession).
*   This function should only be called on the main thread.

```
static func sendCustomEvent(value: String) -> Bool
```

Sends a custom event to the current Clarity session. These custom events can be used to track specific user interactions or actions that Clarity's built-in event tracking doesn't capture.

`value` String

The name of the custom event. The value must be a nonempty string, with a maximum length of 254 characters, and can't consist only of whitespace.

Bool

`true` if the custom event was sent successfully; otherwise `false`.

*   This API can be called multiple times per page to track various user actions.
*   Each custom event is logged individually and can be filtered, viewed, and analyzed on the Clarity dashboard.

```
static func setCurrentScreenName(name: String?) -> Bool
```

This function allows you to provide a custom screen name that replaces the default screen name. The default name is automatically generated based on the currently presented view controller's title or type.

`name` String?

The desired screen name. The value must be a nonempty string with a maximum length of 255 characters and can't consists of only whitespace. Set to `nil` to reset.

Bool

`true` if the specified screen name was set successfully; otherwise `false`.

*   If the presented view controller is a `TabBarController` with the title property set to _"Main Tab Bar"_ and `setCurrentScreenName("Settings")` is called, the screen name is tracked as _"Settings"_.
*   If `setCurrentScreenName(nil)` is called on the same view controller, the screen name is tracked as _"Main Tab Bar"_ (or _"TabBarController"_ in the next major release).

*   Clarity starts a new page whenever the screen name changes.
*   To mask or disallow a screen, specify the view controller type shown as _"ViewController"_ custom tag of the page visit on the Clarity dashboard's recordings. For example, to mask the view controller in the earlier example, mask the _&TabBarController_ screen instead of _&Settings_.
*   The custom screen name is set globally and persists across all subsequent view controllers until explicitly reset.
*   For accurate tracking, call this function immediately after adding the relevant views to the view controller's view hierarchy and within the same CATransaction (for example, inside `viewIsAppearing`).
*   The view controller's title is no longer used to generate the default screen name in the next major release.
*   This function should only be called on the main thread.

```
func setOnSessionStartedCallback(_ callback: @escaping (String) -> Void) -> Bool
```

Sets a callback function that's invoked whenever a new Clarity session starts or an existing session is resumed at app startup.

`callback` (String) -> Void

The callback to be invoked whenever a Clarity session starts. The callback receives the new or resumed session ID as a string parameter.

Bool

`true` if the callback was set successfully; otherwise `false`.

*   If the callback is set after a session has already started, the callback is invoked right away with the current session ID.
*   The specified callback is guaranteed to run on the main thread.

Important

*   **Force masking of input fields is not currently supported**. Apply the `clarityMask` modifier to each input field individually.
*   **Clarity might not capture text content when using custom fonts**. In such case, use the `clarityFontNameHint` modifier when working with versions `3.0.9` and earlier.

```
func clarityMask()
```

Marks a view's content to be masked by Clarity. Masked content is replaced with placeholders.

```
func clarityUnmask()
```

Marks a view's content to be unmasked by Clarity. This is useful for capturing specific parts of a masked view.

```
func clarityFontNameHint(name: String)
```

Provides a hint to Clarity about the font name used in a view. This is helpful for capturing text content when custom fonts are used.

**Deprecated**: This modifier is scheduled for removal in an upcoming major release. Starting from version `3.0.10` and later, it no longer has any effect.

`name` String

The face name of the view's custom font (for example, `"HelveticaBold"` or `customUIFont.fontName`).

*   The invocation of View masking APIs should occur in the `viewDidLoad()` of the view controller that hosts the targeted view.

Important

Remember to update your terms & conditions (if any) for your app users after integrating Clarity with your mobile app.

Additionally, since force masking of input fields isn't supported yet, apply masking to each input field instance individually.

For more answers, refer to [FAQ](https://learn.microsoft.com/en-us/clarity/faq#clarity-for-mobile-apps).
