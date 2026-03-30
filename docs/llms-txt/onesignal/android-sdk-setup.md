# Source: https://documentation.onesignal.com/docs/en/android-sdk-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Android SDK setup

> Add push notifications and in-app messages to your Android app using OneSignal's Android SDK.

export const SdkReleasesIframe = ({sdkFilter = undefined, viewMode = undefined, height, ...frameProps}) => {
  const baseUrl = 'https://onesignal.github.io/sdk-releases';
  const buildUrl = (theme, sdkFilter, viewMode) => {
    const url = new URL(baseUrl);
    const params = new URLSearchParams();
    if (theme) {
      params.set('theme', theme);
    }
    if (sdkFilter) {
      params.set('sdk', sdkFilter);
    }
    if (viewMode) {
      params.set('viewMode', viewMode);
    }
    if (params.toString()) {
      url.search = params.toString();
    }
    return url.toString();
  };
  const detectTheme = () => {
    if (document.documentElement.classList.contains('dark')) {
      return 'dark';
    }
    return 'light';
  };
  const [theme, setTheme] = useState('light');
  const [iframeSrc, setIframeSrc] = useState(() => {
    const initialTheme = detectTheme();
    return buildUrl(initialTheme, sdkFilter, viewMode);
  });
  useEffect(() => {
    const currentTheme = detectTheme();
    setTheme(currentTheme);
    setIframeSrc(buildUrl(currentTheme, sdkFilter, viewMode));
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const handleThemeChange = () => {
      const newTheme = detectTheme();
      setTheme(newTheme);
      setIframeSrc(buildUrl(newTheme, sdkFilter, viewMode));
    };
    if (mediaQuery.addEventListener) {
      mediaQuery.addEventListener('change', handleThemeChange);
    } else {
      mediaQuery.addListener(handleThemeChange);
    }
    window.addEventListener('storage', handleThemeChange);
    const observer = new MutationObserver(handleThemeChange);
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class', 'data-theme']
    });
    return () => {
      if (mediaQuery.removeEventListener) {
        mediaQuery.removeEventListener('change', handleThemeChange);
      } else {
        mediaQuery.removeListener(handleThemeChange);
      }
      window.removeEventListener('storage', handleThemeChange);
      observer.disconnect();
    };
  }, [sdkFilter, viewMode]);
  const getIframeHeight = () => {
    if (viewMode === 'table') {
      return '450';
    }
    if (viewMode === 'mini') {
      return '170';
    }
    return '800';
  };
  const iframeHeight = height || getIframeHeight();
  return <Frame {...frameProps}>
      <iframe src={iframeSrc} width="100%" height={iframeHeight} frameBorder="0" style={{
    border: "none"
  }} title="SDK Releases" key={iframeSrc} />
    </Frame>;
};

<SdkReleasesIframe sdkFilter="android" viewMode="mini" />

This guide walks you through adding OneSignal to your Android app using Android Studio. You'll install our SDK, setup push and in-app messages, and send test messages to confirm everything is working.

If this is your first time using OneSignal, follow the steps in order. If you're experienced, feel free to jump to the sections you need.

<Info>
  **Using an AI coding assistant?**
  For AI-driven installation, use this prompt:

  ```
  Integrate the OneSignal Android SDK into this codebase.

  Follow the instructions at:
  https://raw.githubusercontent.com/OneSignal/sdk-ai-prompts/main/docs/android/ai-prompt.md
  ```

</Info>

## Step 0. Configure FCM in OneSignal (required to deliver push)

You can install and initialize the OneSignal Android SDK without completing this step. However, **push notifications will not deliver** until Firebase Cloud Messaging (FCM) credentials are configured in your OneSignal app.

<Note>
  If your company already has a OneSignal account, [ask to be invited as an admin role](./manage-team-members) to configure the app. Otherwise, [sign up for a free account](https://onesignal.com) to get started.
</Note>

<Accordion title="Steps to configure your OneSignal app.">
  These steps connect your OneSignal app to Firebase Cloud Messaging (FCM). You only need to do this once per app.

  1. Login to [https://onesignal.com](https://onesignal.com) and create or select your App.
  2. Navigate to **Settings > Push & In-App**.
  3. Select **Google Android (FCM)** and **Continue** through the setup wizard.
  4. Input your [Firebase Server Key or Service Account](./android-firebase-credentials) details.
  5. Continue through the setup wizard to get your App ID. This will be used to initialize the SDK.

  <Info>For full setup instructions, see our [Mobile push setup](./mobile-push-setup) guide.</Info>
</Accordion>

***

## Setup contract & requirements

This section summarizes the tools, versions, and assumptions used throughout the guide.

* **SDK version:** `5.6.1+` (latest: check [releases](https://github.com/OneSignal/OneSignal-Android-SDK/releases))
* **AI setup instructions:** `https://raw.githubusercontent.com/OneSignal/sdk-ai-prompts/main/docs/android/ai-prompt.md`
* **SDK repo:** `https://github.com/OneSignal/OneSignal-Android-SDK`
* **Android Studio:** Meerkat+ (2024.2.1+)
* **Android API:** 23+ minimum (Android 6.0+), 31+ recommended (Android 12+)
* **Device/Emulator:** Android 7.0+ with Google Play Services installed
* **Required dependency:** `com.onesignal:OneSignal:[5.6.1, 5.9.99]`
* **Application class:** Required for proper SDK initialization
* **App ID format:** 36-character UUID (example: `12345678-1234-1234-1234-123456789012`) — find at OneSignal Dashboard > Settings > Keys & IDs
* **Initialize:** `OneSignal.initWithContext(this, "YOUR_APP_ID")`
* **Battery Optimization:** May affect background notifications
* **Recommended:** Assign External ID via `OneSignal.login("user_id")` to unify users across devices

***

## Android setup steps

By the end of the steps below, you will have:

* The OneSignal SDK installed and initialized in your Android app
* Push notification permissions prompting correctly on a real device
* A test push and in-app message successfully delivered

<Info>
  If you skipped **Step 0 (Configuring FCM in OneSignal)**, you can still complete the Android Studio setup below. Complete Step 0 before you test or send push notifications.
</Info>

### Step 1. Add the OneSignal SDK

1. In Android Studio, open your `build.gradle.kts (Module: app)` or `build.gradle (Module: app)` file
2. Add OneSignal to your `dependencies` section:

<CodeGroup>
  ```kotlin app/build.gradle.kts theme={null}
  implementation("com.onesignal:OneSignal:[5.6.1, 5.9.99]")
  ```

  ```groovy app/build.gradle theme={null}
  implementation 'com.onesignal:OneSignal:[5.6.1, 5.9.99]'
  ```

</CodeGroup>

<Frame caption="Example shows adding OneSignal to your App's build.gradle.kts file.">
  <img src="https://mintcdn.com/onesignal/dlRpLVMLP5Sd65F4/images/sdk/android-add-onesignal-to-build-gradle.png?fit=max&auto=format&n=dlRpLVMLP5Sd65F4&q=85&s=a1e031945c35197d41335c7c2956739e" width="3052" height="2030" data-path="images/sdk/android-add-onesignal-to-build-gradle.png" />
</Frame>

1. **Sync Gradle:** Click **Sync Now** in the banner that appears or go to **File > Sync Project with Gradle Files**

<Check>
  Verify that the gradle sync completes successfully without dependency conflicts.
</Check>

### Step 2. Create and configure Application class

It's best practice to initialize OneSignal in the `onCreate` method of your `Application` class to ensure proper SDK setup across all entry points.

**Create an Application class if you don't already have one:**

1. **File > New > Kotlin Class/File** (or Java Class)
2. Name: `ApplicationClass` (or your preferred name)

<Frame caption="Example shows creating a new Kotlin class named ApplicationClass.">
  <img src="https://mintcdn.com/onesignal/dlRpLVMLP5Sd65F4/images/sdk/android-create-application-class-kotlin.png?fit=max&auto=format&n=dlRpLVMLP5Sd65F4&q=85&s=7ce9f314acb72ff74311c2695368f5cf" width="2810" height="1798" data-path="images/sdk/android-create-application-class-kotlin.png" />
</Frame>

**Add the following OneSignal code to the Application class.**

Replace `YOUR_APP_ID` with your actual OneSignal App ID from the Dashboard > Settings > [Keys & IDs](./keys-and-ids).

<CodeGroup>
  ```kotlin ApplicationClass.kt theme={null}
  // FILE: ApplicationClass.kt
  // PURPOSE: Initialize OneSignal when your app launches
  // REQUIREMENT: Must be registered in AndroidManifest.xml

  package com.your.package.name // Replace with your actual package name

  import android.app.Application
  import kotlinx.coroutines.CoroutineScope
  import kotlinx.coroutines.Dispatchers
  import kotlinx.coroutines.launch

  import com.onesignal.OneSignal
  import com.onesignal.debug.LogLevel

  class ApplicationClass : Application() {
      override fun onCreate() {
          super.onCreate()

          // Enable verbose logging to debug issues (remove in production)
          OneSignal.Debug.logLevel = LogLevel.VERBOSE

          // Replace with your 36-character App ID from Dashboard > Settings > Keys & IDs
          OneSignal.initWithContext(this, "YOUR_APP_ID")

          // Prompt user for push notification permission
          // In production, consider using an in-app message instead for better opt-in rates
          CoroutineScope(Dispatchers.IO).launch {
              OneSignal.Notifications.requestPermission(false)
          }
      }
  }

  ```

  ```java ApplicationClass.java theme={null}
  // FILE: ApplicationClass.java
  // PURPOSE: Initialize OneSignal when your app launches
  // REQUIREMENT: Must be registered in AndroidManifest.xml

  package com.your.package.name; // Replace with your actual package name

  import android.app.Application;

  import com.onesignal.Continue;
  import com.onesignal.OneSignal;
  import com.onesignal.debug.LogLevel;

  public class ApplicationClass extends Application {
      @Override
      public void onCreate() {
          super.onCreate();
          
          // Enable verbose logging to debug issues (remove in production)
          OneSignal.getDebug().setLogLevel(LogLevel.VERBOSE);
          
          // Replace with your 36-character App ID from Dashboard > Settings > Keys & IDs
          OneSignal.initWithContext(this, "YOUR_APP_ID");
          
          // Prompt user for push notification permission
          // In production, consider using an in-app message instead for better opt-in rates
          OneSignal.getNotifications().requestPermission(false, Continue.none());
      }
  }
  ```

</CodeGroup>

<Frame caption="Example ApplicationClass.kt file.">
  <img src="https://mintcdn.com/onesignal/dlRpLVMLP5Sd65F4/images/sdk/android-application-class-kotlin.png?fit=max&auto=format&n=dlRpLVMLP5Sd65F4&q=85&s=e035c8995472b308f10e42ed82478a0a" width="3052" height="2030" data-path="images/sdk/android-application-class-kotlin.png" />
</Frame>

<Warning>
  Initializing in an `Activity` (like `MainActivity`) is not recommended because it may not be called on app cold-starts from deep links or notifications. Always initialize OneSignal in your `Application` class for reliability.
</Warning>

**Register the Application class:**

1. Open your app's `AndroidManifest.xml`
2. In your `<application>` tag add `android:name=".ApplicationClass"` (replace `.ApplicationClass` with your actual class name if set it to something different).

```xml AndroidManifest.xml theme={null}
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:name=".ApplicationClass"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        ...
      </application>

  </manifest>
```

<Frame caption="AndroidManifest.xml with the .ApplicationClass name.">
  <img src="https://mintcdn.com/onesignal/dlRpLVMLP5Sd65F4/images/sdk/android-androidmanifest-application-class.png?fit=max&auto=format&n=dlRpLVMLP5Sd65F4&q=85&s=289b016975723e22e23d1871457ae21f" width="3052" height="2030" data-path="images/sdk/android-androidmanifest-application-class.png" />
</Frame>

<Check>
  Verify that the app builds and runs without errors.
</Check>

### Step 3. Configure default notification icons (recommended)

Customize [notification icons](./notification-icons) to match your app's branding. This step is optional but recommended for a professional appearance.

### Step 4. Test the integration

**Verify Subscription creation:**

1. Launch app on device or emulator with Google Play Services
2. Check Dashboard > **Audience > Subscriptions** — status shows "Never Subscribed"
3. Accept the permission prompt when it appears
4. Refresh dashboard — status changes to "Subscribed"

<Frame caption="Example of the iOS and Android push permission prompts">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a90c2cc443f5fe9e7c80368c680a16cf1ca6203f7b28a0a6eec212add8510f80-Untitled_design_11.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=96dbf224b3ae93b3d814712cdc5416ba" alt="Example of the iOS and Android push permission prompts." width="1920" height="1080" data-path="images/docs/a90c2cc443f5fe9e7c80368c680a16cf1ca6203f7b28a0a6eec212add8510f80-Untitled_design_11.png" />
</Frame>

<Frame caption="Dashboard showing Subscription with 'Never Subscribed' status">
  <img src="https://mintcdn.com/onesignal/mJXnj6xKtiaVBd7y/images/dashboard/subscription-never-subscribed.png?fit=max&auto=format&n=mJXnj6xKtiaVBd7y&q=85&s=f6412faa44ca1c0dfbd07dc39e82fc08" alt="Dashboard showing Subscription with 'Never Subscribed' status." width="2472" height="1066" data-path="images/dashboard/subscription-never-subscribed.png" />
</Frame>

<Frame caption="After allowing push permissions, refresh the dashboard to see the Subscription status update to 'Subscribed'">
  <img src="https://mintcdn.com/onesignal/mJXnj6xKtiaVBd7y/images/dashboard/subscription-subscribed.png?fit=max&auto=format&n=mJXnj6xKtiaVBd7y&q=85&s=cef79235b64703bc1a1bbffab775366e" alt="After allowing push permissions, refresh the dashboard to see the Subscription status update to 'Subscribed'." width="2472" height="1066" data-path="images/dashboard/subscription-subscribed.png" />
</Frame>

<Check>
  You have successfully created a [mobile Subscription](./subscriptions).
  Mobile subscriptions are created when users first open your app on a device or if they uninstall and reinstall your app on the same device.
</Check>

#### Create test Subscription and segment

1. Click **⋮** next to the Subscription > **Add to Test Subscriptions** > name it
2. Go to **Audience > Segments > New Segment**
3. Name: `Test Users`, add filter **Test Users** > **Create Segment**

<Frame caption="Add a Test Subscription">
  <img src="https://mintcdn.com/onesignal/NCUI56Tiw7V-s0dT/images/dashboard/add-to-test-subscriptions.png?fit=max&auto=format&n=NCUI56Tiw7V-s0dT&q=85&s=2455d4cd74ea4ad686f76730cd95bbaa" alt="Add a Test Subscription." width="1188" height="742" data-path="images/dashboard/add-to-test-subscriptions.png" />
</Frame>

<Frame caption="Create a 'Test Users' segment with the Test Users filter">
  <img src="https://mintcdn.com/onesignal/NCUI56Tiw7V-s0dT/images/dashboard/create-test-users-segment.png?fit=max&auto=format&n=NCUI56Tiw7V-s0dT&q=85&s=91b8a021be6e83662854e68ec3e1da04" alt="Create a 'Test Users' segment with the Test Users filter." width="1188" height="742" data-path="images/dashboard/create-test-users-segment.png" />
</Frame>

<Check>
  You have successfully created a segment of test users.

  We can now test sending messages to this individual device and groups of test users.
</Check>

#### Send test push via API

1. Navigate to **Settings > [Keys & IDs](./keys-and-ids)**.
2. In the provided code, replace `YOUR_APP_API_KEY` and `YOUR_APP_ID` in the code below with your actual keys. This code uses the `Test Users` segment we created earlier.

```bash  theme={null}
curl -X POST 'https://api.onesignal.com/notifications' \
  -H 'Content-Type: application/json; charset=utf-8' \
  -H 'Authorization: Key YOUR_APP_API_KEY' \
  -d '{
    "app_id": "YOUR_APP_ID",
    "target_channel": "push",
    "name": "Testing basic setup",
    "headings": { "en": "👋" },
    "contents": {"en": "Hello world!"},
    "included_segments": ["Test Users"],
    "big_picture": "https://avatars.githubusercontent.com/u/11823027?s=200&v=4"
  }'
```

<Frame caption="Images will appear small in the collapsed notification view. Expand the notification to see the full image.">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e4e3e812eb6841ff11795a6ee0ea36eff483920ea9266733d6948ed34df3def3-Untitled_design_9.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=9bf6f4a73e38ec424b8cfec75a474a26" alt="Images in push notifications appear small in the collapsed notification view. Expand the notification to see the full image." width="1200" height="800" data-path="images/docs/e4e3e812eb6841ff11795a6ee0ea36eff483920ea9266733d6948ed34df3def3-Untitled_design_9.png" />
</Frame>

<Frame caption="Delivery stats showing confirmed delivery (unavailable on free plans)">
  <img src="https://mintcdn.com/onesignal/r7d-mmGxYBGknd0e/images/dashboard/delivery-stats-confirmed-delivery.png?fit=max&auto=format&n=r7d-mmGxYBGknd0e&q=85&s=9949b389aec0cc2e08fc338eaad941de" alt="Delivery stats showing confirmed delivery (unavailable on free plans)." width="2444" height="1462" data-path="images/dashboard/delivery-stats-confirmed-delivery.png" />
</Frame>

<Check>
  Verify the test device received a notification with:

* Your custom icon (if configured)
* Large image when expanded
* Dashboard > **Delivery > Sent Messages** shows "Confirmed" status (unavailable on free plans).
</Check>

<Warning>
  * No notification received? See [Mobile push not shown](./notifications-show-successful-but-are-not-being-shown).
  * No custom icon? Verify the icon name is `onesignal_small_icon_default` and in the correct drawable folders.
  * Having issues? Copy-paste the api request and a log from start to finish of app launch into a `.txt` file. Then share both with `support@onesignal.com`.
</Warning>

#### Test in-app messages

1. Close app for 30+ seconds
2. Dashboard > **Messages > In-App > New In-App** > select **Welcome** template
3. Audience: **Test Users** segment
4. Trigger: **On app open**
5. Schedule: **Every time trigger conditions are satisfied**
6. Click **Make Message Live**
7. Open app

<Frame caption="Targeting the 'Test Users' segment with an in-app message">
  <img src="https://mintcdn.com/onesignal/mJXnj6xKtiaVBd7y/images/dashboard/targeting-test-users-segment-with-in-app-message.png?fit=max&auto=format&n=mJXnj6xKtiaVBd7y&q=85&s=4f2e70263b932745cf929bad9030c819" alt="Targeting the 'Test Users' segment with an in-app message." width="2444" height="712" data-path="images/dashboard/targeting-test-users-segment-with-in-app-message.png" />
</Frame>

<Frame caption="Example customization of in-app Welcome message">
  <img src="https://mintcdn.com/onesignal/r7d-mmGxYBGknd0e/images/dashboard/example-customization-of-in-app-welcome-message.png?fit=max&auto=format&n=r7d-mmGxYBGknd0e&q=85&s=3decc127e575020980828a95eb7f96ce" alt="Example customization of in-app Welcome message." width="2440" height="1488" data-path="images/dashboard/example-customization-of-in-app-welcome-message.png" />
</Frame>

<Frame caption="In-app message scheduling options">
  <img src="https://mintcdn.com/onesignal/r7d-mmGxYBGknd0e/images/dashboard/in-app-message-scheduling-options.png?fit=max&auto=format&n=r7d-mmGxYBGknd0e&q=85&s=d7a46112e5ac3e12bc83b4f8e408159e" alt="In-app message scheduling options." width="2440" height="1074" data-path="images/dashboard/in-app-message-scheduling-options.png" />
</Frame>

<Frame caption="Welcome in-app message shown on devices">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a7ed4bb02be56900a65d2519e3d69f9c9b2c2a1c65fe740f07789e4ffe79cd67-Untitled_design_10.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=6f692b569706ca39df0b4cc2b70f3de2" alt="Welcome in-app message shown on devices." width="1920" height="1080" data-path="images/docs/a7ed4bb02be56900a65d2519e3d69f9c9b2c2a1c65fe740f07789e4ffe79cd67-Untitled_design_10.png" />
</Frame>

<Check>
  Verify the test device received an in-app message. See the [In-app messages setup](./in-app-messages-setup) guide for more details.
</Check>

<Warning>
  Not seeing the message?

* Start a new session
  * You must close or background the app for at least 30 seconds before reopening. This ensures a new session is started.
  * For more, see [how in-app messages are displayed](./in-app-messages-setup#how-are-iams-displayed%3F).
* Still in the `Test Users` segment?
  * If you reinstalled or switched devices, re-add the device to [Test Subscriptions](./find-set-test-subscriptions) and confirm it's part of the Test Users segment.
* Having issues?
  * Follow [Getting a Debug Log](./capturing-a-debug-log) while reproducing the steps above. This will generate additional logging that you can share with `support@onesignal.com` and we will help investigate what's going on.
</Warning>

<Check>
  You have successfully set up the OneSignal SDK and learned important concepts like:

* Gathering [Subscriptions](./subscriptions), setting [Test subscriptions](./find-set-test-subscriptions), and creating [Segments](./segmentation).
* Sending [Push](./push) with images using Segments and our [Create message](/reference/create-message) API.
* Sending [In-app messages](./in-app-messages-setup).

  Continue with this guide to identify users in your app and setup additional features.
</Check>

### Common Errors & Fixes

| Error / Symptom                             | Cause                                         | Fix                                                                 |
| ------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------- |
| `Cannot resolve symbol 'OneSignal'`         | SDK dependency not added or gradle not synced | Add dependency to build.gradle and sync project                     |
| `Application class not found`               | Application class not registered in manifest  | Add `android:name=".ApplicationClass"` to `<application>` tag       |
| `Google Play Services not available`        | Emulator/device missing Play Services         | Use device with Play Store or emulator with Google APIs             |
| Push received but default Android icon      | Custom icon not configured or wrong name      | Create notification icon asset named `onesignal_small_icon_default` |
| No push notifications received              | FCM not configured in OneSignal               | Complete Step 0: Configure FCM credentials in OneSignal dashboard   |
| In-app messages not showing                 | Session not started or network issues         | Close app 30+ seconds, reopen, check internet connection            |
| `Manifest merger failed`                    | Conflicting manifest attributes               | Check for duplicate application names or permissions conflicts      |
| Battery optimization blocking notifications | Device power management                       | Guide users to disable battery optimization for your app            |
| Can't diagnose issue                        | Not enough log info                           | Add verbose logging and check logcat output for errors              |

***

## User management

Previously, we demonstrated how to create mobile [Subscriptions](./subscriptions). Now we'll expand to identifying [Users](./users) across all their Subscriptions (including push, email, and SMS) using the OneSignal SDK.

### Assign External ID (recommended)

Use an External ID to identify users consistently across devices, email addresses, and phone numbers using your backend's user identifier. This ensures your messaging stays unified across channels and 3rd party systems. See our [Mobile SDK reference](./mobile-sdk-reference) for more details and Java code examples.

```kotlin Kotlin theme={null}
// Call when user logs in or is identified, safe to call multiple times
// Typically used in a login completion handler, or on app launch if already authenticated
fun onUserAuthenticated(userId: String) {
    OneSignal.login(userId)
}

// If you want to remove the External ID from the Subscription, setting it to an anonymous user
fun onUserLoggedOut() {
    OneSignal.logout()
}
```

<Note>
  OneSignal generates unique read-only IDs for Subscriptions (Subscription ID) and Users (OneSignal ID).

  Setting the External ID via our SDK is highly recommended to identify users across all their subscriptions, regardless of how they are created.

  Learn more about the [`login` method](./mobile-sdk-reference#login-external-id) in the SDK reference guide.
</Note>

### Add Tags & Custom Events

Tags and Custom Events are both ways to add data to your users. Tags are `key-value` strings and are generally associated with user properties (like `username`, `role`, or `status`) while Custom Events have a JSON format and are usually associated with actions (like `new_purchase`, `abandoned_cart`, and associated properties). Both can be used to power advanced [Message Personalization](./message-personalization) and Journeys. See our [Mobile SDK reference](./mobile-sdk-reference) for more details and Java code examples.

```kotlin Kotlin theme={null}
// Add a tag when the user's name is set
OneSignal.User.addTag("username", "john_doe")

// Create a custom event when user abandoned a cart
val properties = mapOf(
    "product_id" to "123456",
    "product_name" to "Product Name",
    "product_price" to 100,
    "product_quantity" to 1
)
OneSignal.User.trackEvent("abandoned_cart", properties)
```

<Note>
  More details on how to use Tags and Custom Events in the [Tags](./add-user-data-tags) and [Custom Events](./custom-events) guides.
</Note>

### Add email and/or SMS subscriptions

You can reach users through email and SMS channels in addition to push notifications. If the email address and/or phone number already exist in the OneSignal app, the SDK will add it to the existing user — it will not create duplicates. See our [Mobile SDK reference](./mobile-sdk-reference) for more details and Java code examples.

```kotlin Kotlin theme={null}
// Add email subscription
// Call when user provides their email (e.g., account creation, settings update) after calling OneSignal.login("user_id")
OneSignal.User.addEmail("user@example.com")

// Add SMS subscription
// Use E.164 format: + country code + number
// Call when user provides their phone number (e.g., account creation, settings update) after calling OneSignal.login("user_id")
OneSignal.User.addSms("+15551234567")
```

<Frame caption="A user profile with push, email, and SMS subscriptions unified by External ID">
  <img src="https://mintcdn.com/onesignal/mJXnj6xKtiaVBd7y/images/dashboard/user-profile-with-push-email-and-sms-subscriptions-unified-by-external-id.png?fit=max&auto=format&n=mJXnj6xKtiaVBd7y&q=85&s=3e7d5ed8763acb24e0afa5c4ff8f0d81" alt="A user profile with push, email, and SMS subscriptions unified by External ID." width="2440" height="1392" data-path="images/dashboard/user-profile-with-push-email-and-sms-subscriptions-unified-by-external-id.png" />
</Frame>

<Note>
  Best practices for multi-channel communication

* Obtain explicit consent before adding email or SMS subscriptions.
* Explain the benefits of each communication channel to users.
* Provide channel preferences so users can select which channels they prefer.
</Note>

***

### Privacy & user consent

To control when OneSignal collects user data, use the SDK's consent gating methods. See our [Mobile SDK reference](./mobile-sdk-reference) for more details and Java code examples.

```kotlin Kotlin theme={null}
// In ApplicationClass onCreate(), BEFORE OneSignal.initWithContext()
// Use this if your app requires GDPR or other privacy consent before data collection
OneSignal.consentRequired = true

// Later, after user grants consent (e.g., taps "I Agree" on your consent screen)
OneSignal.consentGiven = true
```

<Note>
  See our Privacy & security docs for more on:

* [Data collected by the SDK](./data-collected-by-the-onesignal-sdk)
* [Handling personal data](./handling-personal-data)
</Note>

***

## Prompt for push permissions

Instead of calling `requestPermission()` immediately on app open, take a more strategic approach. Use an in-app message to explain the value of push notifications before requesting permission.

For best practices and implementation details, see our [Prompt for push permissions](./prompt-for-push-permissions) guide.

***

## Listen to push, user, and in-app events

Use SDK listeners to react to user actions and state changes. Add these in your Application class after `OneSignal.initWithContext()`.

### Push notification events

```kotlin Kotlin theme={null}
// Add click listener to handle when users tap notifications
val clickListener = object : INotificationClickListener {
  override fun onClick(event: INotificationClickEvent) {
    Log.d("OneSignal", "Notification clicked: ${event.notification.title}")
  }
}
OneSignal.Notifications.addClickListener(clickListener)
```

### User state changes

Example shows how to use push subscription observer. Other user state events like the user state observer and notification permission observer are available in the [Mobile SDK Reference](./mobile-sdk-reference).

```kotlin Kotlin theme={null}
// Add subscription observer to track push subscription changes
class MyObserver : IPushSubscriptionObserver {
  init {
    OneSignal.User.pushSubscription.addObserver(this)
  }

  override fun onPushSubscriptionChange(state: PushSubscriptionChangedState) {
    if (state.current.optedIn) {
      println("User is now opted-in with push token: ${state.current.token}")
    }
  }
}
```

### In-app message events

Additional in-app message methods are available in the [Mobile SDK Reference](./mobile-sdk-reference).

```kotlin Kotlin theme={null}
// Add click listener for in-app message interactions
val clickListener = object : IInAppMessageClickListener {
  override fun onClick(event: IInAppMessageClickEvent) {
    print(event.result.actionId)
  }
}
OneSignal.InAppMessages.addClickListener(clickListener)
```

***

## Advanced setup & capabilities

### Android-specific features

* **[Notification Channels](./mobile-sdk-reference#notification-channels)** — Organize notifications into categories (Android 8.0+)
* **[Service Extensions](./service-extensions)** — Advanced notification customization
* **[Huawei/HMS Support](./huawei-sdk-setup)** — Alternative to Google Play Services

### Universal features

* [Deep Linking](./deep-linking) — Navigate users to specific screens from notifications
* [Action Buttons](./action-buttons) — Add interactive buttons to notifications
* [Identity Verification](./identity-verification) — Secure user identification
* [Location Tracking](./mobile-sdk-reference#location) — Location-based targeting
* [Integrations](./integrations) — Connect with analytics and data platforms
* [Multi-language Messaging](./multi-language-messaging) — Localized notifications

For full SDK method documentation, visit the [Mobile SDK Reference](./mobile-sdk-reference).

***

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
