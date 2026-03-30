# Source: https://documentation.onesignal.com/docs/en/notification-icons.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Notification icons

> Learn how push notification icons work across Web Push, Android, and iOS, including current platform requirements, sizes, and best practices.

Push notification icons are small images that appear alongside your notifications. They help users quickly recognize your brand, understand context, and distinguish your messages from others. Each platform handles icons differently, so following platform-specific standards is critical to ensure your notifications display correctly.

This guide covers push notification icons. If you are looking for large images, see [Images & Rich Media](./rich-media).

<Frame caption="Example of an Android Chrome Web Push notification with small badge icon, large icon, and image.">
  <img src="https://mintcdn.com/onesignal/kfwVh0swYuB4jUMn/images/push/push-with-icons.png?fit=max&auto=format&n=kfwVh0swYuB4jUMn&q=85&s=6f75da9802f07db975405542bcf2125e" alt="Push notification icons" width="658" height="570" data-path="images/push/push-with-icons.png" />
</Frame>

***

## Best practices for push notification icons

* Use **PNG images with transparency** whenever possible.
* Keep icons **simple and recognizable** at very small sizes.
* Avoid text or fine details that may become illegible.
* Follow **platform-specific rules** for size, color, and transparency.
* Test notifications on real devices across platforms and OS versions.

***

## Web notification icons

Web push notifications display an icon provided at send time or defined as a default in your site settings. If no icon is provided, a default bell icon is used.

* Supported formats: PNG, JPG, GIF (non-animated)
* Icon must be square. Recommended size is `256x256` pixels.

<Info>
  Different browsers (Chrome, Edge, Safari, Firefox) may crop or scale icons differently depending on device and OS. A square `256x256` icon is recommended to ensure consistent display across all browsers.
</Info>

Set the default icon in your [Dashboard Settings > Push & In-App > Web Settings](./web-push-setup).

You can also override the icon per notification using the dashboard or REST API. See [Send notifications with non-default icons](#send-notifications-with-non-default-icons) for details.

### Android web push badge icon

On Android devices, Web Push notifications may display a smaller **badge icon** defined by the Web App Manifest `badge` property. The badge icon is used in limited UI contexts (such as the Android status bar) and may not appear on all Android devices. If no badge icon is provided, the default is the browser icon.

While badge icons are not subject to the same strict alpha-only rules as Android app small notification icons, they are still rendered in system-controlled UI.

**Best practices:**

* Use a **square PNG** with a **transparent background**
* Keep the design **simple and high-contrast**
* Avoid text or fine detail
* Use monochrome or minimal color for best consistency

A minimum size of `72×72 pixels` is recommended. Larger images are acceptable and will be downscaled as needed.

Example small badge icon: `https://i.imgur.com/9QFB20F.png`

<Frame caption="Example of how the badge icon is displayed in the Android status bar using the example badge icon.">
  <img src="https://mintcdn.com/onesignal/kfwVh0swYuB4jUMn/images/push/badge-icon-android-status-bar.png?fit=max&auto=format&n=kfwVh0swYuB4jUMn&q=85&s=5864715448d5c0a3053c03e42e49a49e" alt="Example of how the badge icon is displayed in the Android status bar using the example badge icon." width="744" height="162" data-path="images/push/badge-icon-android-status-bar.png" />
</Frame>

<Note>
  Unlike Android app small notification icons, Web Push badge icons may preserve color on some devices. However, full-color or complex icons may render inconsistently depending on Android version, browser, and device manufacturer.
</Note>

See [Send notifications with non-default icons](#send-notifications-with-non-default-icons) for details.

***

## iOS notification icons

iOS notifications always use your **app icon**.

* The notification icon is automatically derived from your app's icon asset
* You cannot change the notification icon per message
* Changing the icon requires updating your app icon and shipping a new app version

<Note>
  There is no APNs payload field that allows you to specify a custom notification icon on iOS.

  This behavior is enforced by iOS and applies to standard push notifications, Critical Alerts, and Live Activities.
</Note>

### Communication Notifications

On iOS 15 and newer, Apple supports [Communication Notifications](https://developer.apple.com/documentation/usernotifications/implementing-communication-notifications).

When properly implemented, communication-style notifications (such as messaging or calling apps) may display a **contact or sender image** instead of the app icon in supported system views.

<Note>
  Communication Notifications are limited to specific use cases and require explicit adoption of Apple’s communication notification APIs. They are not available for general-purpose notifications.
</Note>

***

## Android notification icons

Android (including Amazon and Huawei devices) supports **Small** and **Large** notification icons.

Android also supports [Conversation Notifications](https://developer.android.com/develop/ui/views/notifications/conversations) that allow you to change the icon to the user's profile image.

<Note>
  On Android 8.0+ (API 26+), notification appearance is heavily influenced by system UI, [notification channels](./android-notification-categories), and device manufacturer customizations.
</Note>

<Frame>
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/cbb4e86-android-notification-icons.jpg?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=a366f3629206f59331f76502bcb485b5" alt="Android notification icon placement" width="1888" height="1274" data-path="images/docs/cbb4e86-android-notification-icons.jpg" />
</Frame>

### Small notification icons

The small notification icon appears in the status bar and the top-left of the notification. If no custom small icon is provided, OneSignal displays a default bell icon.

Android renders small notification icons using the **icon's alpha channel**, not its color data. The system applies its own tint (or your configured accent color) when displaying the icon.

**Requirements and best practices:**

* Use a **monochrome silhouette icon** on a **transparent background**
* Design the icon so the **shape is defined by transparency**, not color
* Avoid gradients, shadows, or multi-color artwork
* Keep the design simple and recognizable at very small sizes

A common and recommended approach is to design the icon as **white artwork on a transparent background**, but technically Android uses the **alpha mask**, not the white color itself.

<Warning>
  Icons with solid backgrounds or full-color artwork may render incorrectly — often appearing as a white square, clipped shape, or unexpected silhouette — depending on the device manufacturer and Android version.

  Android often ignores color information in small notification icons and derives the final appearance from the alpha channel and system or app-defined tinting.
</Warning>

#### Small icon accent color

You can change the color shown around the small icon of the notification.

<Frame>
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4fce1c6db18b7ff1019763684781993a3d921b538e93918e33fc3fb0d78a79b6-Screenshot_20240927_151014_One_UI_Home.jpg?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=84872fd066f015557904a412a17fdcd0" width="1080" height="1058" data-path="images/docs/4fce1c6db18b7ff1019763684781993a3d921b538e93918e33fc3fb0d78a79b6-Screenshot_20240927_151014_One_UI_Home.jpg" />
</Frame>

To set a default color, add the following line to your `res/values/strings.xml` file in your project.

If you want a different color for dark mode, add the key to your `res/values-night/strings.xml` as well.

Use the HEX value. Use [Android Asset Studio](https://romannurik.github.io/AndroidAssetStudio/icons-generic.html#source.type=clipart\&source.clipart=ac_unit\&source.space.trim=1\&source.space.pad=0\&size=32\&padding=8\&color=rgb\(139%2C%20195%2C%2074\)\&name=ic_ac_unit) Color scheme for assistance.

<CodeGroup>
  ```xml xml theme={null}
  <resources>
      <string name="onesignal_notification_accent_color">FF00FF00</string>
  </resources>
  ```
</CodeGroup>

To set the color on per notification bases, set `android_accent_color` on our [Create notification](/reference/create-message) API call or enter a value in the Accent color field under Messages > New Push > Platform Settings > Google Android Options.

<Warning>
  If you've very recently added an icon resource to your app, you may want to wait a few days before sending notifications using the icon. This is because it can take many days or even weeks for the majority of your users to update their apps to the latest version which contain your new icons.
</Warning>

#### Custom non-alpha channel small icon images

Some device manufactures display the image as-is (ignoring the alpha channel rule). You can setup a [custom notification layout based on Android's documentation](https://developer.android.com/training/notify-user/custom-notification) if you wish to use non-alpha channel images across all devices.

We highly recommend following the alpha rule as the icons may not look consistent on all devices. Google designed it this way — the icon is too small to see any meaningful detail, so enforcing a single color helps enforce an easier to recognize icon at a glance.

### Large notification icons

The large icon appears on the right side of the Android notification.

* Recommended size: **256×256 pixels**
* Format: PNG or JPG
* If not set, Android may reuse the small icon

***

## How to add Android default icons

We strongly recommend configuring default notification icons for every Android-based app (Google Play, Amazon, Huawei). Missing or incorrectly configured icons are the most common cause of broken notification rendering.

Android supports two default icons:

* **Small notification icon** (required)
* **Large notification icon** (optional but recommended)

<Steps>
  <Step title="Generate the small notification icon">
    The small notification icon appears in the status bar and notification header.

    **Requirements:**

    * Monochrome silhouette icon
    * Transparent background (alpha channel required)
    * No colors, gradients, or shadows

    A common and recommended approach is a **white icon on a transparent background**, but Android uses the **alpha channel**, not the white color itself.

    <Note>
      The fastest and safest way to generate compliant small icons is using [Android Asset Studio – Notification Icons](http://romannurik.github.io/AndroidAssetStudio/icons-notification.html#source.space.trim=1\&source.space.pad=0\&name=ic_stat_onesignal_default).
    </Note>

    **Name the icon:** `ic_stat_onesignal_default`
  </Step>

  <Step title="Create required small icon sizes">
    **Required**: You must include **all density variants** for the small icon. Missing any size can cause Android to fall back to a system default icon.

    | Icon name                   | Density (dp) | Size (px) |
    | --------------------------- | ------------ | --------- |
    | `ic_stat_onesignal_default` | MDPI         | 24x24     |
    | `ic_stat_onesignal_default` | HDPI         | 36x36     |
    | `ic_stat_onesignal_default` | XHDPI        | 48x48     |
    | `ic_stat_onesignal_default` | XXHDPI       | 72x72     |
    | `ic_stat_onesignal_default` | XXXHDPI      | 96x96     |
  </Step>

  <Step title="Generate the large notification icon (optional)">
    **Best practices:**

    * Square image
    * PNG or JPG
    * Transparent background recommended
    * Recommended size: **256×256 px**

    Unlike small icons:

    * Color is allowed
    * Alpha-only is **not required**
    * Only one size is needed

    **Required file name:** `ic_onesignal_large_icon_default.png`
  </Step>

  <Step title="Place icons in the correct project paths">
    Each icon must be placed in the correct resource directory for your framework. Make sure the following paths exist; create any folders you are missing.

    **Required**: Each image must be present in the following paths:

    <Tabs>
      <Tab title="Android Native">
        * `res/drawable-mdpi/` (24x24)
        * `res/drawable-hdpi/` (36x36)
        * `res/drawable-xhdpi/` (48x48)
        * `res/drawable-xxhdpi/` (72x72)
        * `res/drawable-xxxhdpi/` (96x96)
        * `res/drawable-xxxhdpi/` (256x256) (Large Icon)
      </Tab>

      <Tab title="Unity">
        * `Assets/Plugins/Android/OneSignalConfig.androidlib/src/main/res/drawable-mdpi/` (24x24)
        * `Assets/Plugins/Android/OneSignalConfig.androidlib/src/main/res/drawable-hdpi/` (36x36)
        * `Assets/Plugins/Android/OneSignalConfig.androidlib/src/main/res/drawable-xhdpi/` (48x48)
        * `Assets/Plugins/Android/OneSignalConfig.androidlib/src/main/res/drawable-xxhdpi/` (72x72)
        * `Assets/Plugins/Android/OneSignalConfig.androidlib/src/main/res/drawable-xxxhdpi/` (96x96)
        * `Assets/Plugins/Android/OneSignalConfig.androidlib/src/main/res/drawable-xxxhdpi/` (256x256) (Large Icon)
      </Tab>

      <Tab title="Cordova/Ionic">
        * `<project-root>/platforms/android/app/src/main/res/drawable-mdpi/` (24x24)
        * `<project-root>/platforms/android/app/src/main/res/drawable-hdpi/` (36x36)
        * `<project-root>/platforms/android/app/src/main/res/drawable-xhdpi/` (48x48)
        * `<project-root>/platforms/android/app/src/main/res/drawable-xxhdpi/` (72x72)
        * `<project-root>/platforms/android/app/src/main/res/drawable-xxxhdpi/` (96x96)
        * `<project-root>/platforms/android/app/src/main/res/drawable-xxxhdpi/` (256x256) (Large Icon)

        <Warning>
          With versions of Cordova before 7.0, you will need to use `<project-root>/platforms/android/res/drawable-{size}/` instead of the path shown above when adding the icon resource to `config.xml`
        </Warning>
      </Tab>

      <Tab title="React Native">
        * `android/app/src/main/res/drawable-mdpi/` (24x24)
        * `android/app/src/main/res/drawable-hdpi/` (36x36)
        * `android/app/src/main/res/drawable-xhdpi/` (48x48)
        * `android/app/src/main/res/drawable-xxhdpi/` (72x72)
        * `android/app/src/main/res/drawable-xxxhdpi/` (96x96)
        * `android/app/src/main/res/drawable-xxxhdpi/` (256x256) (Large Icon)
      </Tab>

      <Tab title=".NET Maui">
        * `Resources/Images/drawable-mdpi/` (24x24)
        * `Resources/Images/drawable-hdpi/` (36x36)
        * `Resources/Images/drawable-xhdpi/` (48x48)
        * `Resources/Images/drawable-xxhdpi/` (72x72)
        * `Resources/Images/drawable-xxxhdpi/` (96x96)
        * `Resources/Images/drawable-xxxhdpi/` (256x256) (Large Icon)
      </Tab>

      <Tab title="Flutter">
        * `android/app/src/main/res/drawable-mdpi/` (24x24)
        * `android/app/src/main/res/drawable-hdpi/` (36x36)
        * `android/app/src/main/res/drawable-xhdpi/` (48x48)
        * `android/app/src/main/res/drawable-xxhdpi/` (72x72)
        * `android/app/src/main/res/drawable-xxxhdpi/` (96x96)
        * `android/app/src/main/res/drawable-xxxhdpi/` (256x256) (Large Icon)
      </Tab>
    </Tabs>
  </Step>
</Steps>

Your project should look similar to this (depending on your SDK):

<Frame title="Android Native">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/42f16ed-Screen_Shot_2021-12-10_at_10.36.53_AM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=4b0c4810b478b4b84e3ec15984c35e19" width="982" height="1404" data-path="images/docs/42f16ed-Screen_Shot_2021-12-10_at_10.36.53_AM.png" />
</Frame>

<Warning>
  If you see a **solid square** instead of your icon, the image does not have proper transparency.
</Warning>

<Warning>
  If you see the **OneSignal bell icon**, one or more required small icon sizes are missing or placed in the wrong directory.
</Warning>

<Check>
  Your Android app is now correctly configured with default notification icons.
</Check>

***

## Send notifications with non-default icons

When sending push notifications from the OneSignal dashboard or REST API, you can override the default icons with custom icons for Android, Amazon, Huawei, and Web Push notifications. You cannot override the icon for iOS notifications.

### REST API parameters

**Android, Amazon, and Huawei REST API parameters:**

<ParamField path="small_icon" type="string">
  Amazon: `adm_small_icon` Huawei: `huawei_small_icon`

  For the small icon, the image must exist within the same project path as the default small icon. It cannot use a remote URL. See [How to add Android default icons](#how-to-add-android-default-icons) for details on where to add your custom icons.

  Set the icon name **without** the file extension in the REST API parameters.

  Example: `"small_icon": "my_custom_icon_name_without_extension"`
</ParamField>

<ParamField path="large_icon" type="string">
  Amazon: `adm_large_icon` Huawei: `huawei_large_icon`

  For the large icon, the image can exist within the same project path as the default large icon or as a remote URL. See [How to add Android default icons](#how-to-add-android-default-icons) for details on where to add your custom icons.

  Set the icon name **without** the file extension in the REST API parameters.

  Example: `"large_icon": "my_custom_icon_name_without_extension"`
</ParamField>

**Web Push REST API parameter:**

<ParamField path="chrome_web_icon" type="string">
  Firefox: `firefox_icon`

  The URL to the image resource. Must be the direct URL to the image resource.

  Example: `"chrome_web_icon": "https://example.com/my_custom_icon.png"`
</ParamField>

<ParamField path="chrome_web_badge" type="string">
  The URL to the image resource. Must be the direct URL to the image resource.

  Example: `"chrome_web_badge": "https://i.imgur.com/9QFB20F.png"`
</ParamField>

### Dashboard

In the OneSignal dashboard, using the **Messages > Push > New Push** form or **Templates**, navigate to the platform-specific options.

For Android, Amazon, and Huawei, if the file exists within the same project path as the default icon, set the icon names **without** the file extension. With Large Notification Icons, you can also supply a direct URL where the icon will be displayed from.

<Frame caption="OneSignal dashboard, where to override the default icons.">
  <img src="https://mintcdn.com/onesignal/-HTs3_mQDpKtLbvU/images/push/android-icon-override.png?fit=max&auto=format&n=-HTs3_mQDpKtLbvU&q=85&s=f5ad49e6b26dfa3245d82d07049f0997" width="1052" height="396" data-path="images/push/android-icon-override.png" />
</Frame>

***

Built with [Mintlify](https://mintlify.com).
