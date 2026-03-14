# Source: https://documentation.onesignal.com/docs/en/ios-focus-modes-and-interruption-levels.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS: Focus modes and interruption levels

> Understanding device settings and how they interact with push

Focus modes help iOS users control when and how they receive notifications by allowing separate modes like Work, Sleep, and Personal. Each mode adjusts notification visibility and delivery behavior.

To support important use cases like emergency alerts or account security, Apple introduced **Interruption Levels** to control how and when notifications appear—even when Focus modes are active.

## Interruption levels

Interruption levels determine the urgency and delivery behavior of notifications. There are four levels:

<Columns cols={2}>
  <Card title="Active (default)" icon="play">
    Standard priority notifications. These include sound, vibration, and screen wake behavior. They do not bypass Focus modes.
  </Card>

  <Card title="Time Sensitive" icon="hourglass">
    Behaves like Active but includes a special banner. Time Sensitive notifications can break through Focus modes and scheduled delivery. Use only when urgent user attention is required.
  </Card>

  <Card title="Passive" icon="paper-plane">
    Low-priority notifications. No sound or vibration. They do not interrupt the user and do not break through Focus modes.
  </Card>

  <Card title="Critical" icon="triangle-exclamation">
    Highest priority notifications. Bypass all device controls and Focus modes. Used for emergencies like severe weather or health alerts. Requires prior approval from Apple to enable. See [Critical alerts setup](#critical-alerts-setup) for more details.
  </Card>
</Columns>

<Frame caption="Example. Image showing notifications that are time-sensitive.">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1f2c2a0-image_6.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=ac23ab6a90a3d0cd0be8dc58d9c502ee" width="1523" height="794" data-path="images/docs/1f2c2a0-image_6.png" />
</Frame>

***

## How to set interruption level in OneSignal

When sending a push from the OneSignal Dashboard, you'll find **Notification Interruption Level** under **Apple iOS Settings**. The default is **Active**.

If using the [Create notification API](/reference/create-message), use these parameters:

* `ios_interruption_level`: Set to `"active"`, `"time-sensitive"`, `"passive"`, or `"critical"`
* `ios_relevance_score`: Optional numeric value from 0 to 1 to indicate importance for delivery ordering.

***

## Critical alerts setup

**Critical Alerts:**

* Ignore Do Not Disturb and silent switch.
* Are reserved for high-priority cases (e.g., health, security).
* Require explicit approval from Apple, and users must opt in separately even if they’ve enabled normal push notifications.

### Request Apple entitlement for critical alerts

1. Review [Apple's documentation](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.usernotifications.critical-alerts/) and click **fill out the request form**.
2. Choose the Critical Alerts Entitlement request.
3. Fill out the form and submit the request.
4. Wait for Apple’s review and approval.

### Add the Critical Alerts entitlement to your app

Once Apple approves your request:

1. Open your `.entitlements` file in Xcode (or create one if you don't have it).
2. Add:

```xml  theme={null}
<key>com.apple.developer.usernotifications.critical-alerts</key>
<true/>
```

1. Ensure your provisioning profile includes this entitlement:

* Regenerate your provisioning profile in the Apple Developer portal if needed.
* Download and re-add it to Xcode.

### Request Critical Alert permission in your app code

Critical Alert permission is separate from standard push permission and must be requested like this (using Swift):

```swift  theme={null}
import UserNotifications

UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge, .criticalAlert]) { granted, error in
    if let error = error {
        print("Authorization error: \(error)")
    } else {
        print("Critical alert permission granted: \(granted)")
    }
}
```

<Warning>
  You should request this after getting standard push permission, ideally in your onboarding flow.
</Warning>

### Test Critical Alerts

1. Build and run your app.
2. Send a test push following the steps above in [How to set interruption level in OneSignal](#how-to-set-interruption-level-in-onesignal).

***

## Related docs

* [iOS: Relevance score](./ios-relevance-score)
* [Push overview](./push)

***

Built with [Mintlify](https://mintlify.com).
