# Source: https://documentation.onesignal.com/docs/en/android-notification-categories.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Android notification categories

> Set up Android notification categories (channels) in OneSignal to improve user control and customization of push notifications.

Android notification categories (aka notification channels) were introduced in Android 8.0 (Oreo) to give users greater control over how they receive notifications from your app. This allows you to categorize your notifications and define different experiences such as display behavior, sound, vibration, badges, and lock screen visibility.

For example, if you have breaking news notifications, you can create a category for them and set "Urgent" importance and a custom sound to ensure they are displayed prominently verses less important notifications that may be muted or have a default sound.

OneSignal makes it easy to create and manage these categories directly within the dashboard. Alternatively, you can define categories programmatically in your app. See [Android’s guide to creating notification channels](https://developer.android.com/develop/ui/views/notifications/channels).

<Note>
  OneSignal's Android notification categories work for Google Android, Huawei Android, and Amazon FireOS.
</Note>

<Frame caption="Example of an app's notification categories on the device">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/abd709d-Screenshot_20220201-154501_Settings.jpg?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=97f84df6db5d90943808f25fccf182a5" width="500" height="1111" data-path="images/docs/abd709d-Screenshot_20220201-154501_Settings.jpg" />
</Frame>

***

## Default notification categories

OneSignal automatically creates two default categories:

### Miscellaneous

Used when you do not set a category.

* **Importance:** High
* **Sound:** Default
* **Vibration:** Default
* **Badges:** Enabled
* **Lockscreen:** Private

### Restored

Used when your app is force-quit and reopened. If your app has push notifications in the Notification Center when the app is force-quit, they will be removed from the device. Re-opening the app recreates (restores) those notifications. Our SDK will automatically set the category as "Restored" with the following settings to prevent unwanted behavior and potential customer frustration by getting multiple notifications from your app with sounds and pop-ups.

* **Importance:** Low
* **Sound:** Off
* **Vibration:** Off
* **Badges:** Disabled
* **Lockscreen:** Private

<Note>
  If you always send push notifications with a custom category, the "Miscellaneous" channel won’t appear on user devices. The "Restored" channel will always appear to handle restored notifications after force-quitting the app.
</Note>

#### Huawei-specific behavior

On Huawei devices, OneSignal does **not** set a default category. If you don't include one, Huawei will apply **High** importance by default.

For badge control on Huawei devices, you can also use dedicated Huawei badge parameters (`huawei_badge_class`, `huawei_badge_set_num`, `huawei_badge_add_num`) in the [Create message](/reference/create-message) API. See [Badges](./badges#huawei-badges) for details.

***

## Create Android notification categories in OneSignal

1. Go to **Settings > Push & In-App > Android Notification Channels** in the OneSignal Dashboard.
2. Click **Add Group** to organize your categories (e.g., “News Updates”, “Social Activity”).
3. Click **Add Channel** within the group to create a new category.

<Frame caption="Where to add Android categories in OneSignal">
  <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/android-notifications-categories-create-android-onesignal.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=e3ca711dd7ad860a97de9aa3f3d7109b" width="2616" height="1264" data-path="images/push/android-notifications-categories-create-android-onesignal.jpg" />
</Frame>

You’ll be asked to define the following:

### Name

*User-visible.* Keep it clear and descriptive.

### Description

*User-visible.* Briefly explain the type of notifications this category will handle.

### Importance

Controls how visible and interruptive the notification is:

* **Low:** Silent, no alerts
* **Medium:** No sound/vibration, minimal visual interruption
* **High:** Plays sound or vibrates, no screen pop-up
* **Urgent:** Plays sound and appears as a heads-up or banner-style notification.

### Sound

* **Off:** No sound
* **Default:** Device’s default notification tone
* **Custom:** Upload and reference a custom sound (no file extension).
  Example: `alert_beep` (not `alert_beep.wav`)
  See [Notification Sounds](./notification-sounds) for setup instructions.

### Vibration

* **Off:** No vibration
* **Default:** Uses device’s vibration pattern
* **Custom:** Define your own using a pattern (in ms).
  Example: `0, 300, 500, 300` → Wait 0ms, vibrate 300ms, pause 500ms, vibrate 300ms.

### LED Color

Some Android devices support LED indicators:

* **Off:** No LED
* **Default:** Device default
* **Custom:** ARGB hex value (e.g., `FF0000FF` for blue)

### Badges

Shows badge count on app icon:

* **Enabled:** Badge is shown
* **Disabled:** No badge displayed

### Lockscreen visibility

* **Public:** Full content shown
* **Private:** Only app name, hides content
* **Secret:** No notification visible on lock screen

<Check>
  Once your category is created, you can use it in your notifications.
</Check>

***

## Updating categories

After a device receives a notification with a category, Android locks that category’s behavior. **Changes to importance, sound, vibration, or other settings will not apply retroactively**. For example, if you send a push notification with a category using "High" importance and sound,then change the importance to "Urgent" and use a different sound file, the next push notification to that same device with that same category will not have "Urgent" importance or the new sound.

**Options**:

* **To update behavior:** Create a new category.
* **To test changes:** Clear app data or uninstall and reinstall the app.

You can update:

* Channel name
* Channel group name

These will update in Android's notification settings when the next notification is received using that updated channel.

***

## Deleting categories

To remove a deleted category from the user’s device:

1. Delete the category from the OneSignal dashboard.
2. Ensure all notifications are cleared from the Notification Center.
3. Have the user:
   * Put the app in the background for 60+ seconds
   * Open it again (triggers SDK sync)

The SDK will re-sync and remove the deleted category from Android settings.

***

## Adding categories to notifications

Depending on how you created the Android Category and how you are sending the message, these are the ways you can reference the category in your push notifications.

### Sending from the OneSignal Dashboard

1. Within your Template or Push Message Composer, navigate to the Android settings.
2. Under **Category**, select your category if created within the OneSignal dashboard or select **(Created in App)** if created programmatically in your app.
   * If created programmatically, also set the **Existing Channel** field to the name defined in your code.

<Frame caption="Where to select the Android category in the message composer">
  <img src="https://mintcdn.com/onesignal/qlRVasrK03Npyvy1/images/dashboard/category-selection.png?fit=max&auto=format&n=qlRVasrK03Npyvy1&q=85&s=612958a4fbcf7150a3e6e54aba917ed8" width="2036" height="1234" data-path="images/dashboard/category-selection.png" />
</Frame>

### Sending with the REST API

If you created the category in the OneSignal dashboard, use the `android_channel_id` in the [Create message](/reference/push-notification) API request. You can find the Channel ID in the Android Category setup screen.

<Frame caption="Find the Channel ID in the Android Category setup screen">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/711520e6676b87a1007fb262c97fa2608003322fada1fa4601dab8d4d154afa8-Screenshot_2024-11-12_at_9.31.05_AM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=85d8ab273f8828e666ac7f79740ceda4" width="878" height="1038" data-path="images/docs/711520e6676b87a1007fb262c97fa2608003322fada1fa4601dab8d4d154afa8-Screenshot_2024-11-12_at_9.31.05_AM.png" />
</Frame>

If using your own programmatically created Android channels, use the `existing_android_channel_id` parameterin the [Create message](/reference/push-notification) API request and set the name as defined in your code.

***

## FAQ & troubleshooting

### Can categories play sounds in Do Not Disturb (DND) mode?

No. OneSignal does not set `setBypassDnd` on categories. To override DND, create your own channel programmatically and enable this setting. See [setBypassDnd](https://developer.android.com/reference/android/app/NotificationChannel#setBypassDnd\(boolean\)).

### Can I localize category names or descriptions?

No. OneSignal does not support multiple languages for categories. To support localization, define your own Android channels and reference them via `existing_android_channel_id` in your push API requests.

### Why is my Android category not working?

There are several reasons why your Android category may not be working as expected. To troubleshoot, check the following:

* **What is not working?**
  * Is the sound file not playing?
  * Is it not displaying on the device?
  * Do you not see the category in the Android Notification Settings?
* **How was the category created?**
  * If created in the OneSignal dashboard, make sure the settings are defined as you expect.
  * If created programmatically in your app, review your code. See [Android’s guide to creating notification channels](https://developer.android.com/develop/ui/views/notifications/channels).
* **Review the category settings:**
  * Make sure the settings are defined as you expect.
  * Is the sound file being referenced correctly? See the [Sound](#sound) section above.
  * Is the category name or ID being referenced correctly when sending the message?
* **Did you update the settings after sending a notification?**
  * If you updated the settings after sending a notification, Android will not apply those updates to your device. See [Updating categories](#updating-categories) above.
* **Check OneSignal SDK initialization:**
  * Make sure OneSignal is initialized in the `Application` class, not an `Activity`. See [Android SDK Setup](./android-sdk-setup).

<Info>
  Still need help? We're here to assist! Email `support@onesignal.com` with the above information including:

* The Android category code if created programmatically in your app
* The URL to the message in your OneSignal dashboard with the issue

  We'll assist you as soon as possible!
</Info>

***

Built with [Mintlify](https://mintlify.com).
