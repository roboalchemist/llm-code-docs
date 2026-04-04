# Source: https://firebase.google.com/docs/ios/supporting-ios-14.md.txt

With iOS 14.5, Apple requires developers to receive the user's permission
through the App Tracking Transparency framework to track them or access their
device's advertising identifier (IDFA). See
[Apple's User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
and
[Apple's App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)
documentation for more details.

> [!WARNING]
> **Warning:** User acceptance of the App Tracking Transparency system prompt does not constitute consent under Google's EU user consent policy for serving personalized advertisements. See the [User Consent Policy Help page](https://www.google.com/about/company/user-consent-policy-help/) for more details. Consult [Apple's User Privacy and Data Use policy](https://developer.apple.com/app-store/user-privacy-and-data-use/) on whether your app's behaviors require user acceptance of an App Tracking Transparency prompt.

## Affected Firebase products

Firebase SDKs do not access IDFA, though some have integrations with
Google Analytics that may involve IDFA access.

The table below lists Firebase products that are available on Apple platforms
and describes how the functionality of each product is impacted if IDFA is not
accessible.

| Product | Impact if IDFA is not accessible |
|---|---|
| A/B Testing | Some targeting data (like demographics) in the A/B Testing integration with Google Analytics is derived from the IDFA. In apps without access to the IDFA, this targeting is unavailable. |
| Firebase AI Logic ^1^ | No impact |
| App Check | No impact |
| App Distribution | No impact |
| Authentication | No impact across Authentication and first-party Authentication providers, such as Google Sign-In and Phone Authentication. |
| Cloud Firestore | No impact |
| Cloud Functions | No impact |
| Cloud Messaging | When used with Google Analytics, Google Analytics will automatically log some FCM-related conversion events. Attribution for these events requires IDFA access. |
| Cloud Storage | No impact |
| Crashlytics | No impact. The Crashlytics integration with Google Analytics that provides real-time crash data and breadcrumbs is not dependent on the IDFA. |
| Dynamic Links | No impact for link-opening functionality. When used with Google Analytics, attribution for link conversion events is unavailable. |
| In-App Messaging | No impact |
| Firebase installations | No impact |
| InstanceID | No impact |
| Firebase ML | No impact |
| Performance Monitoring | No impact |
| Realtime Database | No impact |
| Remote Config | When used with Google Analytics, Remote Config does not allow automatically-created user properties for targeting without IDFA access. |

^**1** *Firebase AI Logic was formerly called
"Vertex AI in Firebase".*^

## Affected Firebase integrations

The table below lists Firebase-integrated products that are affected if IDFA is
not accessible.

| Product | Impact if IDFA is not accessible |
|---|---|
| Google Analytics | Analytics event logging, event reporting, and conversion measurement are unaffected, but attribution is impacted if IDFA is not accessible. To learn more about Google's response to iOS 14, see our [blog post](https://blog.google/products/ads-commerce/preparing-developers-and-advertisers-for-policy-updates/). |

## Requesting App Tracking Permission on iOS 14

If you would like your Apple application to be able to access IDFA, you can add
Apple's App Tracking Transparency framework to your app and request permission
to track or access your users' IDFA.

Many applications choose to present a warm-up, or explainer, screen prior to
asking for permission. The explainer screen allows you to give users more
context on how your app uses IDFA prior to requesting access.

If you are an AdMob or Ad Manager app publisher, consider using
[Funding Choices](https://support.google.com/fundingchoices/answer/9180084),
which handles obtaining consent for serving personalized advertisements as well
as consent for tracking the user according to Apple's guidelines automatically.
See the
[AdMob Consent with User Messaging page](https://developers.google.com/admob/ump/ios/quick-start)
for more details.

The following guide provides a solution using
[Firebase In-App Messaging](https://firebase.google.com/products/in-app-messaging) for creating and
displaying an explainer screen prior to requesting tracking access via
App Tracking Transparency.

> [!WARNING]
> **Warning:** Consult [Apple's User Privacy and Data Use policy](https://developer.apple.com/app-store/user-privacy-and-data-use/) on whether your app's behaviors require user acceptance of an App Tracking Transparency prompt. Also, take note of Apple's description of what constitutes an acceptable explainer screen.

### Add In-App Messaging to your app

Follow the instructions to
[add In-App Messaging to your Apple application](https://firebase.google.com/docs/in-app-messaging/get-started?platform=ios).

### Handle in-app message dismissal

First, avoid displaying the explainer screen on devices that cannot present the
consent dialog, such as devices running iOS 13. Make sure this code executes
immediately after `FirebaseApp.configure()`.

### Swift

    if NSClassFromString("ATTrackingManager") == nil {
      // Avoid showing the App Tracking Transparency explainer if the
      // framework is not linked.
      InAppMessaging.inAppMessaging().messageDisplaySuppressed = true
    }

Implement the
`https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Protocols/InAppMessagingDisplayDelegate`
protocol to handle events when the user dismisses the explainer screen. If the
user taps OK, display the system prompt via the App Tracking Transparency
framework.

### Swift

    // The InAppMessaging delegate must be assigned before events can be handled.
    InAppMessaging.inAppMessaging().delegate = self

    func messageClicked(_ inAppMessage: InAppMessagingDisplayMessage,
                        with action: InAppMessagingAction) {
      switch action.actionText {
      case "OK":
        ATTrackingManager.requestTrackingAuthorization { status in
          switch status {
          case .authorized:
            // Optionally, log an event when the user accepts.
            Analytics.logEvent("tracking_authorized", parameters: nil)
          case _:
            // Optionally, log an event here with the rejected value.
          }
        }
      case _:
        // do nothing
      }
    }

### Create an In-App Messaging campaign

Once the code is in place in your application, create an in-app message in the
Firebase console.

1. In the [Firebase console](https://console.firebase.google.com/u/0/project/_/inappmessaging), create a new In-App Messaging campaign.
2. Populate the in-app messages with your desired content and set the message to trigger on the `app_launch` event.
3. In the *Targeting* section, make sure the campaign targets only the most recent version of your app and above.

You can customize the appearance of the explainer screen by following the
instructions in the
[In-App Messaging documentation](https://firebase.google.com/docs/in-app-messaging/customize-messages?platform=ios).

## Optional: A/B Test different explainer screens

In-App Messaging has a built-in integration with
[Firebase A/B Testing](https://firebase.google.com/docs/ab-testing), which you can use to experiment
with different explainer screens.

Firebase A/B Testing automatically creates experiment groups and helps you
visualize how users interact with different variants of your application.

### Record app tracking permissions

If you didn't log a Google Analytics event when handling the app tracking
permissions response, you will need to in order to measure changes in the
response rate when running an A/B experiment.

### Swift

    ATTrackingManager.requestTrackingAuthorization { status in
      switch status {
      case .authorized:
        // Optionally, log an event when the user accepts.
        Analytics.logEvent("tracking_authorized", parameters: nil)
      case _:
        // Optionally, log an event here with the rejected value.
      }
    }

### Create a new conversion event

In the
[*Analytics* section](https://console.firebase.google.com//u/0/project/_/analytics)
of the Firebase console, navigate to the *Conversions* menu, then add a new
conversion event with the same name as the event logged with the sample code
above.

### Create a new experiment

In the console's
[In-App Messaging menu](https://console.firebase.google.com/u/0/project/_/inappmessaging),
click **New Experiment**, then follow the instructions on the resulting
screens.

- In the *Targeting* section, make sure the campaign targets only the most recent version of your app and above.
- In the *Goals* section, select the conversion event you created with the sample code above as well as any other metrics you would like to track.

Once you've published your experiment, it will need to collect data for some
time before it can produce conclusive results.

Read the
[Firebase A/B Testing documentation](https://firebase.google.com/docs/ab-testing/abtest-inappmessaging)
for information on how to monitor an experiment and roll out a successful
variant.