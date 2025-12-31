# Source: https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers.md.txt

<br />

| TheFirebase App DistributionAndroid SDK is a**beta release**. This means that the functionality might change in backward-incompatible ways. A beta release is not subject to any SLA or deprecation policy and may receive limited or no support.

This guide describes how to enable in-app feedback using the optionalFirebase App DistributionAndroid SDK, so that your testers can submit feedback (including screenshots) directly in the app.

## Before you begin

If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
| **Note:** If you have multiple apps in your Firebase project, make sure the app you want to distribute withApp Distributionhas its own`google-services.json`config file. For more information, see[Support multiple environments](https://firebase.google.com/docs/projects/multiprojects#support_multiple_environments_in_your_android_application).

## Step 1: Enable theApp DistributionTester API

1. Open the[Google Cloudconsole](https://console.cloud.google.com/apis/library/firebaseapptesters.googleapis.com)and select your Firebase project.

2. Under the Firebase App Testers API, click**Enable**.

## Step 2: AddApp Distributionto your app

TheApp DistributionAndroid SDK consists of two libraries:

- `firebase-appdistribution-api`: The API-only library, which you can include in all[build variants](https://developer.android.com/studio/build/build-variants).
- `firebase-appdistribution`: The full SDK implementation (optional).

| **Caution:** To support features like[notifying testers about new builds](https://firebase.google.com/docs/app-distribution/set-up-alerts), the fullApp DistributionAndroid SDK implementation contains self-update functionality that may be considered a violation of[Google Play policy](https://support.google.com/googleplay/android-developer/answer/9888379), even if that code is not executed at runtime. Submitting your app to Google Play without removing the full SDK implementation may result in your app being removed from Google Play.

The API-only library lets your code make calls to the SDK. The calls have no effect if the full SDK implementation is not present.

1. Declare the dependency for theApp DistributionAndroid SDK in your**module (app-level)** Gradle file (usually`<project>/<app-module>/build.gradle.kts`or`<project>/<app-module>/build.gradle`).

2. To avoid including the full SDK implementation's self-update functionality in your Google Play builds, identify the build variants, including[build types](https://developer.android.com/studio/build/build-variants#build-types)or[product flavors](https://developer.android.com/studio/build/build-variants#product-flavors)that you will distribute throughApp Distribution.

3. Declare the dependency for theApp DistributionAndroid SDK in your**module (app-level) Gradle file** (usually`app/build.gradle`). Only add the full SDK implementation to variants that are intended exclusively for pre-release testing:

   ### Kotlin

   ```kotlin
   dependencies {
       // ADD the API-only library to all variants
       implementation("com.google.firebase:firebase-appdistribution-api-ktx:16.0.0-beta15")

       // ADD the full SDK implementation to the "beta" variant only (example)
       betaImplementation("com.google.firebase:firebase-appdistribution:16.0.0-beta17")
   }
   ```

   ### Java

   ```java
   dependencies {
       // ADD the API-only library to all variants
       implementation("com.google.firebase:firebase-appdistribution-api:16.0.0-beta17")

       // ADD the full SDK implementation to the "beta" variant only (example)
       betaImplementation("com.google.firebase:firebase-appdistribution:16.0.0-beta17")
   }
   ```

## Step 3: Configure in-app feedback

To collect feedback from your testers, use one of the following triggers to enable testers to initiate feedback:

- [Built-in notification trigger](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#notification-trigger): TheApp DistributionAndroid SDK can display an ongoing notification that the tester can tap from anywhere in the app. Use this trigger if you want to get started more quickly and you don't need to customize how your testers provide feedback.

- [Custom trigger](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#custom-trigger): You can provide your own trigger mechanism, like tapping a button or menu item in your app or shaking the device.

When you use either of these triggers and the tester submits feedback, the Android SDK performs the following actions:

1. Captures a screenshot of the app's current activity.

2. Runs checks to ensure the tester enabled the SDK's testing features. If the testing features are not enabled, the Android SDK prompts the tester to sign in toApp Distributionwith their Google account.

   | **Note:** Enabling testing features is a one-time process on the test device and persists across updates of your app. Testing features remain enabled on the test device until the tester uninstalls the app or until the app calls the`signOutTester`method.
3. Starts a full-screen activity that lets the tester write and submit their feedback.

### Option 1: Notification trigger

Use`showFeedbackNotification()`to display a persistent or[ongoing](https://developer.android.com/reference/android/app/Notification.Builder#setOngoing(boolean))notification on the tester's device that they can tap to initiate feedback. When you configure the notification, you need to provide some text that will be displayed to the tester before they submit feedback, and a level of interruption for the notification (corresponding to the notification channel's[importance](https://developer.android.com/develop/ui/views/notifications/channels#importance)). If you want to provide notice to your testers about the collection and processing of their feedback data, you can use the text to provide such a notice.

When you use`showFeedbackNotification()`and when the app goes to the background, the notification is hidden. If you want to explicitly hide the notification, use`cancelFeedbackNotification()`. We recommend that you put`showFeedbackNotification()`in your main activity's`onCreate()`.  

### Kotlin

    class MainActivity : AppCompatActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            Firebase.appDistribution.showFeedbackNotification(
                // Text providing notice to your testers about collection and
                // processing of their feedback data
                R.string.additionalFormText,
                // The level of interruption for the notification
                InterruptionLevel.HIGH)
        }
    }

### Java

    public class MainActivity extends AppCompatActivity {
        FirebaseAppDistribution firebaseAppDistribution =
            FirebaseAppDistribution.getInstance();
        @Override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            firebaseAppDistribution.showFeedbackNotification(
                // Text providing notice to your testers about collection and
                // processing of their feedback data
                R.string.additionalFormText,
                // The level of interruption for the notification
                InterruptionLevel.HIGH);
        }
    }

| **Note:** On Android 13 and higher, this method requires the[runtime permission for sending notifications](https://developer.android.com/develop/ui/views/notifications/notification-permission):`POST_NOTIFICATIONS`. If your app targets Android 13 (API level 33) or higher, you need to[declare the permission](https://developer.android.com/develop/ui/views/notifications/notification-permission#declare)and then[request it at runtime](https://developer.android.com/training/permissions/requesting).

### Option 2: Custom trigger

Use the`startFeedback()`method to initiate feedback using a mechanism of your choice. For example, to trigger feedback you might want to add a "Send feedback" menu item to your app's action menu, or let your testers[shake their device](https://github.com/firebase/firebase-android-sdk/blob/master/firebase-appdistribution/test-app/src/main/kotlin/com/googletest/firebase/appdistribution/testapp/ShakeDetectionFeedbackTrigger.kt)or[take a screenshot](https://github.com/firebase/firebase-android-sdk/blob/master/firebase-appdistribution/test-app/src/main/kotlin/com/googletest/firebase/appdistribution/testapp/ScreenshotDetectionFeedbackTrigger.kt). When you trigger feedback, provide some text that will be shown to the tester before they submit feedback. If you want to provide a notice to your testers about collection and processing of their feedback data, you can use this text to provide such a notice.  

### Kotlin

    Firebase.appDistribution.startFeedback(R.string.feedbackMessage)

### Java

    FirebaseAppDistribution.getInstance().startFeedback(R.string.feedbackMessage);

## Step 4: Build and test your implementation

### Local testing

To test your implementation without having to distribute the app first, follow these steps:

1. Enable dev mode on your local device:

   ```text
   adb shell setprop debug.firebase.appdistro.devmode true
   ```
2. Build your app as a pre-release variant that includes the fullApp Distributionlibraries, and test that you can trigger feedback using the mechanism implemented in[Step 3: Configure in-app feedback](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#configure-in-app-feedback). Feedback is not submitted when in dev mode.

3. After testing, you can disable dev mode on your device:

   ```text
   adb shell setprop debug.firebase.appdistro.devmode false
   ```

### End-to-end testing

| **Note:** By default, new feedback triggers email and in-console alerts to all Firebase project Owners and Editors.

To test that your app can send feedback, build your app as a pre-release variant that includes the fullApp Distributionlibraries, and test your implementation following these steps:

1. Upload a new app release toApp Distribution.

2. Distribute the app release to an account you have permission to access.

3. Download the app throughApp Distribution's web or Android tester app.

4. Trigger feedback using the mechanism implemented in[Step 3: Configure in-app feedback](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#configure-in-app-feedback).

5. Ensure you're signed in with the same account to which you distributed the app release, and submit feedback.

6. View your feedback in the new release's card in the[Firebaseconsole](https://console.firebase.google.com/project/_/appdistribution).

| **Caution:** Before releasing your app to the Google Play Store, be sure to test your app to verify that you are including only the API-only library dependency, and that your feedback mechanism is not included in your release variant. For more information, see[Step 2: AddApp Distributionto your app](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#add-app-distribution-to-your-app).

To learn how to resolve common issues, like testers unable to start feedback in the app, see[Enabling testing features with the SDK](https://firebase.google.com/docs/app-distribution/troubleshooting?platform=android#enable-android-alerts).

## Step 5: Manage tester feedback

After you enable your testers to send feedback, you can use the following tools to review and act on that feedback:

- [Firebaseconsole](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#view-feedback-firebase-console)

- [Email alerts for new feedback](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#receive-email-alerts-new-feedback)

- [Third-party tools](https://firebase.google.com/docs/app-distribution/collect-feedback-from-testers#send-new-feedback-third-party-tools)

### View and delete feedback in theFirebaseconsole

You can review and delete user feedback, including screenshots, by opening the**Tester feedback** tab under a specific release in theFirebaseconsole. User feedback is organized by release so you can confirm the version to which the feedback applies.

After reviewing user feedback, you can delete that feedback by clicking the**Delete feedback**button. The deleted feedback is removed from your release.

### Receive email alerts for new feedback

To proactively learn about new tester feedback, you can receive email alerts when a tester submits feedback. The email alert includes the written feedback your tester provided and a link to any screenshots they submitted.

To receiveApp Distributionemail alerts via this default mechanism, you must have the`firebase.projects.update`permission. The following roles include this required permission by default:[Firebase Admin](https://firebase.google.com/docs/projects/iam/roles-predefined-all-products)or project[Owner or Editor](https://firebase.google.com/docs/projects/iam/roles-basic).

By default, every project member who has the required permissions to receive email alerts will receive an email when a new feedback report is submitted. Project members can individually opt out of these alerts.

To disable email alerts, see[Receive Firebase alerts](https://support.google.com/firebase/answer/7276542).

### Send new feedback to third-party tools

You can also sendApp Distributionalerts to your team's preferred notification channel usingCloud Functions for Firebase. For example, you can write a function that captures an alert event for new in-app feedback and posts the alert information to a third-party service like Discord, Slack, or Jira.
| **Note:** To use advanced alerting capabilities, your Firebase project must use the[Blaze pricing plan](https://firebase.google.com/pricing).

To set up advanced alerting capabilities usingCloud Functions for Firebase, follow these steps:

1. [Set upCloud Functions for Firebase](https://firebase.google.com/docs/functions/beta/get-started), which includes the following tasks:

   1. Download Node.js and npm.

   2. Install and sign into theFirebaseCLI.

   3. InitializeCloud Functions for Firebaseusing theFirebaseCLI.

2. [Write and deploy a function](https://firebase.google.com/docs/functions/beta/alert-events)that captures an in-app feedback alert event fromApp Distributionand handles the event payload (for example, posts the alert information in a message on Discord).

To see an example function that shows you how to send new feedback to Jira, refer to[this sample](https://github.com/firebase/functions-samples/blob/main/Node/app-distribution-feedback-to-jira).

To learn about all of the alert events that you can capture, see the reference documentation for[App Distributionalerts](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution).