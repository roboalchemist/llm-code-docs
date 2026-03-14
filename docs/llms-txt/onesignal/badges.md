# Source: https://documentation.onesignal.com/docs/en/badges.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Badges

> Learn how to manage and customize app icon badge counts for push notifications on iOS and Android, including disabling auto-clearing, using the OneSignal API, implementing native badge logic, and testing setup.

Badges are the little numbered dots that appear on your mobile app icon. They help capture user attention and can influence engagement behavior. On iOS in particular, badges require additional setup and offer flexible control, as outlined below.

<Note>
  For Android Web Push notifications, the badge refers to the small icon shown on notifications—not the app icon—and can be customized. See [Web Push Badges](./push#badges).
</Note>

***

## Android badges

Android app icon badge behavior can be managed through [Android notification categories](./android-notification-categories). You can control whether a category (channel) displays a badge and set badge behavior on a per-category basis.

***

## Huawei badges

On Huawei devices, a badge can be displayed as a number or a dot on the app icon, depending on the user's device settings. Badges help indicate unread messages or pending actions, encouraging users to open the app. OneSignal lets you control Huawei badge counts directly through the dashboard or API.

### How Huawei badges work

* The badge displays on your app icon as either a **numeric count** or a **dot**, depending on the user's device-level badge display setting (controlled in the device's **Settings > Notifications > App icon badges**). Your API call controls the underlying count; the device decides the visual style.
* `huawei_badge_class` is **required** for any badge operation. This is the fully qualified class name of your app's entry Activity in the format `<package_name>.<ActivityName>` (e.g., `com.example.myapp.MainActivity`). It tells the Huawei system which app icon to apply the badge to.
* If you set both `huawei_badge_set_num` and `huawei_badge_add_num` in the same request, `huawei_badge_set_num` takes priority.
* If neither `huawei_badge_set_num` nor `huawei_badge_add_num` is provided (but `huawei_badge_class` is set), **the badge count increments by 1 by default**.
* `huawei_badge_set_num` accepts values from **0 to 99**. Setting it to `0` clears the badge.
* `huawei_badge_add_num` accepts values from **1 to 99**. For example, if the app currently shows a badge of 5 and you send `huawei_badge_add_num: 3`, the badge becomes 8.

### Send Huawei push with badges

<Tabs>
  <Tab title="Dashboard">
    1. Go to **Messages > Push** or **Templates**
    2. Under **Platform Settings > Send to Huawei Android > Badge**
    3. Choose either:
       * **Don't set** — badge is not affected by this notification
       * **Set to** — sets the badge to a specific number (0–99)
       * **Increase by** — increments the existing badge count (1–99)
  </Tab>

  <Tab title="API">
    Use the following parameters in the [Create message](/reference/create-message) API:

    * `huawei_badge_class` — *(string, required for badge)* The fully qualified class name of the app's launcher activity (e.g., `"com.example.myapp.MainActivity"`)
    * `huawei_badge_set_num` — *(integer, 0–99)* Sets the badge count to this exact number. Set to `0` to clear the badge.
    * `huawei_badge_add_num` — *(integer, 1–99)* Increments the existing badge count by this number. If omitted along with `huawei_badge_set_num`, defaults to incrementing by 1.

    **Set badge to a specific number:**

    ```json  theme={null}
    {
      "huawei_badge_class": "com.example.myapp.MainActivity",
      "huawei_badge_set_num": 5
    }
    ```

    **Increment badge by a specific amount:**

    ```json  theme={null}
    {
      "huawei_badge_class": "com.example.myapp.MainActivity",
      "huawei_badge_add_num": 1
    }
    ```

    **Clear the badge:**

    ```json  theme={null}
    {
      "huawei_badge_class": "com.example.myapp.MainActivity",
      "huawei_badge_set_num": 0
    }
    ```
  </Tab>
</Tabs>

### Clearing badges

Huawei does **not** automatically clear the badge when a user opens the app or taps a notification. To clear the badge, you have two options:

* **Via the API or dashboard**: Send a notification with `huawei_badge_set_num` set to `0` (or use **Set to > 0** in the dashboard). This can be a [data/background notification](./data-notifications) if you don't want a visible notification to appear.
* **Via client-side code**: Your app can clear the badge locally using the Huawei badge API. This requires the `com.huawei.android.launcher.permission.CHANGE_BADGE` permission in your `AndroidManifest.xml`. See [Huawei's badge development guide](https://developer.huawei.com/consumer/en/doc/hmscore-guides/android-badging-0000001050042083) for implementation details.

<Note>
  The `huawei_badge_set_num` parameter requires EMUI 10.0.0 or later and Push SDK 10.1.0 or later. On older devices, only `huawei_badge_add_num` is supported.
</Note>

***

## iOS badges

To ensure badge counts increment correctly on iOS, you must configure:

* The `OneSignalNotificationServiceExtension`
* App Groups

See [Mobile SDK setup](./mobile-sdk-setup) for full instructions.

By default, the OneSignal SDK will:

1. Clear the app icon badge when the app is opened.
2. Remove notifications from the Notification Center.

If you want to retain notifications and manage badge logic manually (e.g., using your own counter or syncing state across devices), you can disable this automatic behavior.

**Common use cases for manual badge control**

* Reset badge when the app launches or resumes
* Increment badge when a notification is received in the foreground
* Decrement when a message is read or dismissed
* Sync badge state across devices or app extensions via App Groups or your backend

### Disable automatic notification and badge clearing

In your app's `info.plist`, add the Key: `OneSignal_disable_badge_clearing` with Boolean type to Value `YES`

<Frame caption="Example info.plist with ` OneSignal_disable_badge_clearing` turned off (set to `YES `).">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/ea4fbad85bfcb4909ce88668e3882fc8749624c781a66d7c78c440b7e267999c-Screenshot_2025-04-01_at_4.37.05_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=e2aafae9e93e16b63e263f34770f262a" width="2284" height="1484" data-path="images/docs/ea4fbad85bfcb4909ce88668e3882fc8749624c781a66d7c78c440b7e267999c-Screenshot_2025-04-01_at_4.37.05_PM.png" />
</Frame>

```xml  theme={null}
<key>OneSignal_disable_badge_clearing</key>
<true/>
```

This prevents the SDK from automatically removing notifications or resetting the badge when the app opens.

#### iOS native badge management

If you disable OneSignal's automatic badge clearing, you can use Apple's native APIs to control badge behavior.

<Warning>
  Apple deprecated `UIApplication.shared.applicationIconBadgeNumber` in iOS 17. You should now use the following methods from the [UserNotifications framework](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter/setBadgeCount\(_:withCompletionHandler:\)):
</Warning>

**Set badge count**

To set the badge on the app icon to a specific value:

```swift Swift theme={null}
import UserNotifications
import UIKit

if #available(iOS 17.0, *) {
  UNUserNotificationCenter.current().setBadgeCount(5) { error in
    if let error = error {
      print("Failed to set badge count: \(error.localizedDescription)")
    } else {
      print("Badge count updated successfully.")
    }
  }
} else {
  UIApplication.shared.applicationIconBadgeNumber = 5
}
```

**Get current badge count**

iOS does not provide a method to retrieve the current badge count from the system. You must keep track of the badge count in your app's state (for example, using `UserDefaults`, your app's data model, or syncing with your backend).

```swift Swift theme={null}
// Example: Store and retrieve badge count using UserDefaults
let badgeCount = UserDefaults.standard.integer(forKey: "badgeCount")
// Update badge count as needed
UserDefaults.standard.set(badgeCount, forKey: "badgeCount")
```

**Increment or decrement badge**

You must manage badge logic manually, as relative changes (like +1 or -1) are not supported in payloads. Update your stored badge count and then set it:

```swift Swift theme={null}
// Example: Increment badge count and update system badge
let currentCount = UserDefaults.standard.integer(forKey: "badgeCount")
let updatedCount = max(0, currentCount + 1)
UserDefaults.standard.set(updatedCount, forKey: "badgeCount")

if #available(iOS 17.0, *) {
  UNUserNotificationCenter.current().setBadgeCount(updatedCount)
} else {
  UIApplication.shared.applicationIconBadgeNumber = updatedCount
}
```

**Clear badge**

To remove the badge entirely:

```swift Swift theme={null}

if #available(iOS 17.0, *) {
  UNUserNotificationCenter.current().setBadgeCount(0)
} else {
  UIApplication.shared.applicationIconBadgeNumber = 0
}
```

***

## Send iOS push with badges

You can set the badge count in the OneSignal dashboard or using the API.

<Tabs>
  <Tab title="Dashboard">
    1. Go to **Messages > Push** or **Templates**
    2. Under **Platform Settings > Send to Apple iOS > Badges**
    3. Choose either:
       * Set to a specific number
       * Increase by a relative amount

    <Frame caption="Set badges in the OneSignal dashboard message form.">
      <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a6f4a4c0d5869fd9ba5c83ded26752f83c1350c4f6f5213a985cf522fa4d0387-Screenshot_2025-04-01_at_4.42.50_PM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=8b428dfec1995ea5ec296d717bad9524" width="1528" height="558" data-path="images/docs/a6f4a4c0d5869fd9ba5c83ded26752f83c1350c4f6f5213a985cf522fa4d0387-Screenshot_2025-04-01_at_4.42.50_PM.png" />
    </Frame>
  </Tab>

  <Tab title="API">
    Use the following parameters in the [Create message](/reference/create-message) API:

    * `ios_badgeType` - Set to `SetTo` or `Increase`
    * `ios_badgeCount` - The number to set or increase by

    ```json  theme={null}
    {
      "ios_badgeType": "Increase",
      "ios_badgeCount": 1
    }
    ```
  </Tab>
</Tabs>

When sending iOS push notifications, the badge count will change based on these options.

If the app is open, the badge count will reset unless you followed the instructions above to [disable automatic badge clearing](#disable-automatic-notification-and-badge-clearing).

<Check>
  Badges tutorial complete!
  Next steps:

* [Android Notification Categories](./android-notification-categories)
* [Huawei authorization](./authorize-onesignal-to-send-huawei-push)
* [Push overview](./push)
</Check>

***

Built with [Mintlify](https://mintlify.com).
