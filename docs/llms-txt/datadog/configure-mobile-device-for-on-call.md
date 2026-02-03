# Source: https://docs.datadoghq.com/incident_response/on-call/guides/configure-mobile-device-for-on-call.md

# Source: https://docs.datadoghq.com/mobile/guide/configure-mobile-device-for-on-call.md

---
title: Set Up Your Mobile Device for Datadog On-Call
description: >-
  Configure your mobile device for reliable on-call notifications with critical
  alerts, Do Not Disturb bypass, and telephony contact setup.
breadcrumbs: >-
  Docs > Datadog Mobile App > Mobile App Guides > Set Up Your Mobile Device for
  Datadog On-Call
---

# Set Up Your Mobile Device for Datadog On-Call

Being on-call requires reliable and timely notifications to ensure you can respond to incidents effectively. This guide walks you through the steps to configure your mobile device for optimal performance with [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/).

1. Install the [Datadog mobile app](https://docs.datadoghq.com/service_management/mobile/?tab=ios).
1. Set up push notifications: Enable your device to receive notifications from the Datadog mobile app.
1. Circumvent mute and Do Not Disturb mode: Receive push notifications, voice calls, and SMS while your device is in Do Not Disturb mode.

## Set up push notifications{% #set-up-push-notifications %}

{% alert level="info" %}
When you log into the Datadog mobile app for the first time, an onboarding flow takes care of notification settings and permissions.
{% /alert %}

However, by default, the mobile app is not allowed to send you notifications. To receive push notifications:

{% tab title="iOS" %}

1. In the Datadog mobile app, navigate to **Settings** > **Notifications**.

   {% image
      source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_settings_may_2025.562c150592be3de420b831a0dbfbdd52.png?auto=format"
      alt="Find the notification settings in the iOS version of Datadog's mobile app." /%}

1. Enable the **Allow Notifications** toggle. If this is your first time enabling notifications, this opens up a permissions prompt. Grant permission, then touch **Enable Notifications** again to go to the iOS system settings.

   {% image
      source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_notification_may_2025.fb4f6bf0c9f84eb9222e606349709f54.png?auto=format"
      alt="Configure the system notification settings of your iOS device." /%}

1. Within the iOS system settings, make sure you enable the **Allow Notifications** toggle. Datadog highly recommends you also enable the **Sound** and **Badges** toggles.

Make sure you grant the mobile app the necessary permissions.
{% /tab %}

{% tab title="Android" %}

1. In the Datadog mobile app, navigate to **Settings** > **Notifications**.

   {% image
      source="https://datadog-docs.imgix.net/images/service_management/mobile/android_settings_may_2025.ad769189393557921169357fa6723d63.png?auto=format"
      alt="Find the notification settings in the Android version of Datadog's mobile app." /%}

1. Enable the **Allow notifications** toggle. Datadog highly recommends you also enable **Sound and vibration** and **Show content on Lock screen**.

   {% image
      source="https://datadog-docs.imgix.net/images/service_management/mobile/android_notification_may_2025.6580382f86e33dbfb9b3d843cf72a931.png?auto=format"
      alt="Configure the system notification settings of your Android device." /%}

{% /tab %}

### Custom sounds{% #custom-sounds %}

On both iOS and Android, you have the option to override the default system notification sounds. The Datadog app comes preloaded with a selection of custom sounds.

## Circumvent mute and Do Not Disturb mode for On-Call{% #circumvent-mute-and-do-not-disturb-mode-for-on-call %}

You can override your device's system volume and Do Not Disturb mode for both push notifications (from the Datadog mobile app) and telephony notifications (such as voice call and SMS).

### Critical push notifications{% #critical-push-notifications %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_critical_may_2025.027c678d284284780d7262ce880c672b.png?auto=format"
   alt="Override your iOS device's system volume and do-not-disturb mode." /%}

1. In the Datadog mobile app, navigate to **Settings** > **On-Call**.

1. Enable the **Critical Alerts** toggle. Critical alerts ignore the mute switch and Do Not Disturb. If you enable critical alerts, the system plays a critical alert's sound regardless of the device's mute or Do Not Disturb settings.

1. Within the iOS system settings, make sure you enable the **Critical Alerts** toggle. Make sure you grant the mobile app the necessary permissions.

1. Select your device for **High Urgency Notifications** and/or **Low Urgency Notifications** under the Notification Preferences section.

1. Test the setup of your critical push notification by tapping **Test push notifications**.

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_critical_may_2025.52f225b6c1c89d4ac0db154807c74d42.png?auto=format"
   alt="Override your Android device's system volume and Do Not Disturb mode." /%}

1. In the Datadog mobile app, navigate to **Settings** > **On-Call**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_allow_notification_may_2025.9cd9539b07da21e3130998b5a17889f3.png?auto=format"
   alt="Override your Android device's system volume and Do Not Disturb mode." /%}
If notification permissiongs are missing, tap **Bypass Do Not Disturb** and enable **Allow notifications** in System Settings.
{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_override_system_may_2025.209e33b7b41ebaf085d51f18e6491622.png?auto=format"
   alt="Override your Android device's system volume and Do Not Disturb mode." /%}

Then tap **Bypass Do Not Disturb** and enable **Override Do Not Disturb** in System Settings for High Urgency On-Call.

**On Samsung devices**: Go to **Settings** > **Notifications** > **Do Not Disturb** > **App notifications**. Select Datadog and allow it to bypass Do Not Disturb.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_override_system_volume_may_2025.591dd939d999fefc56f85977bf61fdec.png?auto=format"
   alt="Override your Android device's system volume and Do Not Disturb mode." /%}

In order to override system volume, tap the **Override system volume** and allow **Mode access** in System Settings to toggle on **Override system volume**.

On web, set up notification preferences for **High Urgency Notifications** and/or **Low Urgency Notifications**.

Test the setup of your critical push notification by tapping **Test push notifications**.

{% alert level="warning" %}
On Android, the Datadog mobile app cannot bypass system volume or Do Not Disturb settings when used within a Work Profile. As a workaround, install the Datadog mobile app on your personal profile.
{% /alert %}

{% /tab %}

### Custom sounds and volume for critical push{% #custom-sounds-and-volume-for-critical-push %}

For high-urgency notifications, Datadog strongly recommends customizing your system sounds and volume settings. This ensures that alerts are not only more distinct and recognizable, but also more effective in capturing attention. Test your notification preferences to confirm that they behave as expected.

### Telephony channels (voice calls and SMS){% #telephony-channels-voice-calls-and-sms %}

For reliability, Datadog uses a rotating set of phone numbers to contact you. To help your phone recognize calls and messages from Datadog On-Call, you can create a digital contact card. This card automatically updates with Datadog's latest phone numbers. You can assign special permissions to this contact in your system settings for enhanced functionality, such as circumventing Do Not Disturb mode.

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_sync_card_may_2025.0517fc8f14ec2780920de099d8c99bac.png?auto=format"
   alt="Override your iOS device's Do Not Disturb mode for SMS and voice calls" /%}

1. In the Datadog mobile app, navigate to **Account** > **Settings** > **Notifications**.

1. Toggle on **Enable Automatic Contact Card Sync**. This creates a contact named "Datadog On-Call", which updates regularly with Datadog's latest phone numbers.

1. After this contact is created, open your iOS system settings and navigate to **Focus** > **Do Not Disturb**.

1. Under **People**, allow notifications from the Datadog On-Call contact. If you enabled critical alerts for Datadog push applications, then the Datadog mobile app also appears under **Apps**.

1. To bypass silent mode, navigate to the Datadog On-Call contact Â» tap **Ringstone** Â» activate **Emergency Bypass**.

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_sync_card_may_2025.10418c13eb4ea1325e9b3d999f0b0631.png?auto=format"
   alt="Override your Android device's do-not-disturb mode for SMS and voice calls" /%}

1. In the Datadog mobile app, navigate to **Settings** > **On-Call**.

1. Under **Phone & SMS**, enable **Automatic Contact Card Sync**. This creates a contact named "Datadog On-Call", which updates regularly with Datadog's latest phone numbers.

1. After this contact is created, mark it as a favorite.

1. Open your Android system settings and navigate to **Sound & vibration** > **Do Not Disturb**. Create an exception for the Datadog On-Call contact.

{% /tab %}

{% alert level="info" %}
[Download the current version of the Datadog On-Call contact card](https://datadog-on-call.s3.amazonaws.com/datadog-on-call.vcf). **Note**: The contact card is subject to change at any time.
{% /alert %}

## On-Call mobile widgets{% #on-call-mobile-widgets %}

Add On-Call home screen and lock screen widgets to access your pages and shifts.

### On-Call home screen widget{% #on-call-home-screen-widget %}

View your On-Call shifts and On-Call pages on your mobile home screen with Datadog widgets.

You can customize your On-Call shift widgets by filtering on:

- Organization
- Period of time

You can customize your On-Call page widgets by filtering on:

- Organization
- Team
- Order

**Note**: You can add additional filters for the On-Call pages widget.

#### Edit an On-Call shift widget{% #edit-an-on-call-shift-widget %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_shifts_widget_may_2025.c3a277e8b8b26f9a9d8c91ccfcfa0b12.png?auto=format"
   alt="Configured home screen on-call shift widgets displayed on iOS screens" /%}

1. Long press on the widget to configure.
1. Tap **Edit Widget** to bring up the configuration screen.
1. Select the **Organization** and **Period** you would like to see your On-Call shifts for.
1. Tap out of the widget to validate your selection and exit the configuration screen.

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_shifts_widget_may_2025.f6f0a3d1f92fb2db6f18a921a32d4eeb.png?auto=format"
   alt="Configured home screen On-Call shift widgets displayed on Android screens" /%}

1. Tap on the widget to configure.
1. Select the **Organization** and **Time Period** you would like to see your On-Call shifts for.
1. Tap **â** to save the configuration.
1. Long press and resize the widget to fit your preference.

{% /tab %}

### On-Call lock screen widget{% #on-call-lock-screen-widget %}

The On-Call lock screen widget displays your On-Call status. Lock screen widgets are only available on iOS.

1. Long press on your lock screen.
1. Tap **Customize**, then **Lock Screen**.
1. Tap on the lock screen widget space to pull up the **Add Widgets** card.
1. Scroll to and tap on the **Datadog** app.
1. Tap the On-Call lock screen widget.
1. Tap the widget on the lock screen to pull up the configuration panel.
1. Select the organization you would like to display your On-Call status for.

**Note**: You must have an empty space on your lock screen to add a new widget. You can delete lock screen widgets by tapping the **-** button on the top left of the widget you would like to delete.

## Troubleshooting{% #troubleshooting %}

For help with troubleshooting, [contact Datadog support](https://docs.datadoghq.com/help/). You can also send a message in the [Datadog public Slack](https://chat.datadoghq.com/) [\#mobile-app](https://datadoghq.slack.com/archives/C0114D5EHNG) channel.
