# Source: https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk

Title: Android SDK Installation

URL Source: https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk

Published Time: Mon, 08 Dec 2025 07:03:38 GMT

Markdown Content:
Important

*   The Clarity Android SDK collects sessions from Android API levels within the supported range specified at [Platform/Framework Support Matrix](https://learn.microsoft.com/en-us/clarity/mobile-sdk/mobile-sdk-overview#platformframework-support-matrix). Applications with API levels 19-28 inclusive build successfully, but they can't send data to Clarity.
*   If your app uses Jetpack Compose, use `clarity-compose` package. For more information, see [Jetpack compose support](https://learn.microsoft.com/en-us/clarity/mobile-sdk/clarity-compose-sdk).

Install the Clarity SDK in order to track how users interact with your app. The Clarity Android SDK is available on a MavenCentral. It can take up to 2 hours to start seeing data.

Add `mavenCentral()` to your project repositories. Add the dependency to your module `build.gradle` script.

**Note**: You can find the latest [version here](https://central.sonatype.com/artifact/com.microsoft.clarity/clarity/versions).

```
repositories {
   mavenCentral()
}

dependencies {
   implementation 'com.microsoft.clarity:clarity:3.+'
}
```

* * *

Add the following code to your startup activity only:

*   [Kotlin](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#tabpanel_1_kotlin)
*   [Java](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#tabpanel_1_java)

```
import com.microsoft.clarity.Clarity
import com.microsoft.clarity.ClarityConfig

override fun onCreate(savedInstanceState: Bundle?) {
   ...
   val config = ClarityConfig(
       projectId = "<ProjectId>",
       logLevel = LogLevel.Verbose // default is None
   )

   Clarity.initialize(applicationContext, config)
   ...
}
```

Note

You need to invoke this function only once during your startup activity. If you have multiple startup activities, you can either call it within a custom application class or duplicate the call in each startup activity.

If you want to late initialize Clarity after the activity `onCreate` function is called, you can use a different initialization function that takes the current activity as a parameter:

```
Clarity.initialize(currentActivity, config)
```

Note

*   This function has to be called on the main thread.
*   If you use a custom `WorkManager` initializer, Clarity initialization must take place after the `WorkManager` initializer. Otherwise, Clarity won't function properly.

* * *

Once you integrated Clarity with your application, ensure the following if you want to test it on a device or an emulator:

1.   Your device/emulator is connected to the internet.
2.   Your device/emulator Android version is within the supported range specified at [Platform/Framework Support Matrix](https://learn.microsoft.com/en-us/clarity/mobile-sdk/mobile-sdk-overview#platformframework-support-matrix).
3.   Your first run might require setting the log level to Verbose to obtain the Clarity logs. These logs could help identify any initialization errors, if present.

Allow approximately 2 hours for complete sessions to appear in your Clarity project on the Clarity website. However, in-progress sessions can still be viewed in real time. See [Clarity Recordings in Real Time](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-real-time).

```
class ClarityConfig(
   val projectId: String,
   val userId: String? = null, // DEPRECATED
   val logLevel: LogLevel = LogLevel.None
)
```

The unique identifier assigned to your Clarity project. You can find it on the **Settings** page of Clarity dashboard. This ID is essential for routing data to the correct Clarity project.

The unique identifier associated with the application user. This ID persists across multiple sessions on the same device.

*   **Deprecated:** This field is deprecated and would be removed in a future major version. Use [`setCustomUserId`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setcustomuserid) instead.
*   If `userId` isn't provided, a random one is generated automatically.
*   Must be a base-36 string smaller than `1z141z4` and without any uppercase letters.
*   If an invalid `userId` is supplied: 
    *   If `customUserId` isn't specified: `userId` acts as the `customUserId`, and a new random `userId` is assigned.
    *   If `customUserId` is specified: the invalid `userId` is ignored.

Note

For greater flexibility in user identification, use the [`setCustomUserId`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setcustomuserid) API. Ensure that the `customUserId` length is between 1 and 255 characters.

The level of logging to show in the device's Logcat while debugging. By default, the SDK logs nothing.

Allowed log levels are:

*   `Verbose`
*   `Debug`
*   `Info`
*   `Warning`
*   `Error`
*   `None`

Signals to the SDK which framework is being used to develop the current application. This parameter is internal to the SDK and shouldn't be set manually.

Note

For Clarity versions `3.0.0` and above, the following configuration options are no longer configurable from code and can now be adjusted dynamically from the Clarity dashboard:

*   **Allow Metered Network Usage** (`allowMeteredNetworkUsage`): Allows uploading session data to the servers on device's metered networks. By default, the SDK only uploads sessions on unmetered networks.
*   **Enable WebView Capture** (`enableWebViewCapture`): Allows Clarity to capture the web views DOM content for recording and heatmap reconstruction.
*   **Disable on Low-End Devices** (`disableOnLowEndDevices`): When enabled, Clarity doesn't capture any data for the low-end devices.
*   **Allow or disallow activities** (`allowedActivities`, `disallowedActivities`): Include or exclude some activities from being recorded by Clarity. By default, all activities are included.
*   **Network limit** (`maximumDailyNetworkUsageInMB`): Daily limit of wifi/cellular data per device that could be used to upload session recordings.
*   **Allowed domains** (`allowedDomains`): The accepted domains for Clarity to track and capture DOM content. This has now been updated to **Allowed URLs**, which can be configured from the dashboard to specify the accepted URLs. By default, all URLs are included.

Initializes Clarity to start capturing the current session data.

```
initialize(Context context, ClarityConfig config)
```

> It's a must to be called in the startup activity onCreate().

```
initialize(Activity activity, ClarityConfig config)
```

> Use this function if you want to initialize clarity later, i.e. later stages of an activity's lifecycle, like when the activity has resumed.

`config` ClarityConfig

Configuration of Clarity that tunes the SDK behavior (for example, which project to send to, which log level to use, and so on).

Boolean

`true` if Clarity initialization is possible; otherwise `false`.

*   The initialization function is asynchronous, meaning it returns before Clarity is fully initialized.
*   For actions that require Clarity to be fully initialized, it's recommended to use the [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setonsessionstartedcallback) function.
*   This function should only be called on the main thread.

```
pause()
```

Pauses the Clarity session capturing until a call to the [`resume`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#resume) function is made.

Boolean

`true` if Clarity was successfully paused; otherwise `false`.

```
resume()
```

Resumes the Clarity session capturing only if it was previously paused by a call to the [`pause`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#pause) function.

Boolean

`true` if Clarity was successfully resumed; otherwise `false`.

This function should only be called on the main thread.

```
isPaused()
```

Boolean

`true` if Clarity session capturing is currently in the paused state based on an earlier call to the [`pause`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#pause) function; otherwise `false`.

```
startNewSession(Function1<String, Unit> callback)
```

Forces Clarity to start a new session asynchronously.

`callback` Function1<String, Unit>

A callback that is invoked when the new session starts. The callback receives the new session ID as a string parameter.

Boolean

`true` if a new session can start asynchronously; otherwise `false`.

*   This function is asynchronous, meaning it returns before the new session is started.
*   Use the `callback` parameter to execute logic that needs to run after the new session begins.
*   Events that occur before invoking the callback are associated with the previous session.
*   To ensure proper association of custom tags, user ID, or session ID with the new session, set them within the callback.
*   This function should only be called on the main thread.

```
maskView(View view)
```

Masks a specific `View` to prevent Clarity from capturing its content (text or images). Masked content is replaced with placeholders.

`view` View

The `View` instance to mask its content.

Boolean

`true` if the view was added to the masked views; otherwise `false`.

This function should only be called on the main thread.

```
unmaskView(View view)
```

Unmasks a specific `View` to allow Clarity to capture its content, even if it's a child of a masked view or within a masked screen.

`view` View

The view instance to unmask.

Boolean

`true` if the view was added to the unmasked views; otherwise `false`.

This function should only be called on the main thread.

```
setCustomUserId(String customUserId)
```

Sets a custom user ID for the current session. This ID can be used to filter sessions on the Clarity dashboard.

`customUserId` String

The custom user ID to associate with the current session. The value must be a nonempty string with a maximum length of 255 characters and can't consist only of whitespace.

Boolean

`true` if the custom user ID was set successfully; otherwise `false`.

*   To ensure that the custom user ID is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#startnewsession).
*   Unlike the `userID`, the `customUserId` value has fewer restrictions.
*   We recommend **not** to set any [Personally Identifiable Information (PII)](https://learn.microsoft.com/en-us/clarity/setup-and-installation/glossary-of-terms) values inside this field.
*   This function should only be called on the main thread.

```
setCustomSessionId(String customSessionId)
```

Sets a custom session ID for the current session. This ID can be used to filter sessions on the Clarity dashboard.

`customSessionId` String

The custom session ID to associate with the current session. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Boolean

`true` if the custom session ID was set successfully; otherwise `false`.

*   To ensure that the custom session ID is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#startnewsession).
*   This function should only be called on the main thread.

```
getCurrentSessionId()
```

A string representing the ID of the currently active Clarity session if a session has already started; otherwise `null`.

String

The current active session ID. If there's no active session, it returns `null`.

*   **Deprecated:** This API is deprecated and would be removed in a future major version. Use [`getcurrentsessionurl`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#getcurrentsessionurl) instead.
*   The session ID can be used to correlate Clarity sessions with other telemetry services.
*   Initially, this function might return `null` until a Clarity session begins.
*   To ensure a valid session ID, use this method within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#startnewsession).
*   This function should only be called on the main thread.

```
getCurrentSessionUrl()
```

Returns the URL of the current Clarity session recording on the Clarity dashboard if a session has already started; otherwise `null`.

String

A string representing the URL of the current Clarity session recording on the Clarity dashboard if a session has already started; otherwise `null`.

*   Initially, this function might return `null` until a Clarity session begins.
*   To ensure a valid session URL, use this method within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#startnewsession).
*   This function should only be called on the main thread.

```
setCustomTag(String key, String... values)
```

Sets a custom tag for the current session. This tag can be used to filter sessions on the Clarity dashboard.

`key` String

The key for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

`values` String...

The values for the custom tag. Each value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Boolean

`true` if the custom tag was set successfully; otherwise `false`.

*   To ensure that the custom tag is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#setonsessionstartedcallback) or [`startNewSession`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/android-sdk#startnewsession).
*   This function should only be called on the main thread.

```
sendCustomEvent(String value)
```

Sends a custom event to the current Clarity session. These custom events can be used to track specific user interactions or actions that Clarity's built-in event tracking doesn't automatically capture.

`value` String

The name of the custom event. The value must be a nonempty string, with a maximum length of 254 characters, and can't consist only of whitespace.

Boolean

`true` if the custom event was sent successfully; otherwise `false`.

*   This API can be called multiple times per page to track various user actions.
*   Each custom event is logged individually and can be filtered, viewed, and analyzed on the Clarity dashboard.

```
setCurrentScreenName(String screenName)
```

This function allows you to provide a custom screen name that replaces the default screen name. The default name is automatically generated based on the current activity name.

`screenName` String

The desired screen name. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace. Set to `null` to reset.

Boolean

`true` if the specified screen name was set successfully; otherwise `false`.

*   If the current activity is `MainActivity`, and `setCurrentScreenName("Home")` is called, the screen name is tracked as _"Home"_.
*   If `setCurrentScreenName(null)` is called on the same activity, the screen name is tracked as _"MainActivity"_.

*   Clarity starts a new page whenever the screen name changes.
*   To mask or disallow a screen, specify the activity name that is displayed as _"Activity"_ custom tag of the page visit on the Clarity dashboard's recordings, rather than the custom screen name. For example, to mask the activity in the previous example, mask the _"MainActivity"_ screen instead of _"Home"_.
*   The custom screen name is set globally and persists across all subsequent activities until explicitly reset.
*   For accurate tracking, call this function immediately after navigating to the new screen: 
    *   If there are activities, you can call it inside `Activity.onResume` function.
    *   While using `androidx.navigation`, you can call it inside [OnDestinationChangedListener](https://developer.android.com/reference/androidx/navigation/NavController.OnDestinationChangedListener).

*   This function should only be called on the main thread.

```
setOnSessionStartedCallback(Function1<String, Unit> callback)
```

Sets a callback function that's invoked whenever a new Clarity session starts or an existing session is resumed at app startup.

`callback` Function1<String, Unit>

The callback to be invoked whenever a Clarity session starts. The callback receives the new or resumed session ID as a string parameter.

Boolean

`true` if the callback was set successfully; otherwise `false`.

*   If the callback is set after a session has already started, the callback is invoked right away with the current session ID.
*   The specified callback is guaranteed to run on the main thread.

```
consent(Boolean adsStorage, Boolean analyticsStorage)
```

Sets the user's consent status for ads and analytics data collection so the SDK can adjust behavior based on the user's selections.

`adsStorage` Boolean

Indicates whether the user consents to ads data collection.

`analyticsStorage` Boolean

Indicates whether the user consents to analytics data collection.

Boolean

`true` if the consent status was set successfully; otherwise `false`.

*   You're responsible for obtaining the user's consent through a banner or another in-app experience.
*   Call this function on the main thread after the user provides their preferences.
*   If either parameter is `null`, the function logs an error and returns `false` without changing the current consent state.

*   In case you'd like to associate a name with your fragment for filtering on the Clarity dashboard, assign a certain tag (`com.microsoft.clarity.R.id.clarity_fragment_tag`) to the topmost/root view within your fragment view tree:

`view.setTag(com.microsoft.clarity.R.id.clarity_fragment_tag, "SettingFragment")`

*   The invocation of View masking APIs should occur in the `onCreate()` of the activity that hosts the targeted view.

Important

Remember to update your terms & conditions (if any) for your app users after integrating Clarity with your mobile app.

For more answers, refer to [FAQ](https://learn.microsoft.com/en-us/clarity/faq#clarity-for-mobile-apps).
