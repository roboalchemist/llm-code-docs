# Source: https://docs.datadoghq.com/mobile/push_notification.md

---
title: Set Up Push Notifications on Mobile App
description: >-
  Configure push notifications on iOS and Android for on-call alerts, incidents,
  and workflow updates with critical alert settings.
breadcrumbs: Docs > Datadog Mobile App > Set Up Push Notifications on Mobile App
---

# Set Up Push Notifications on Mobile App



{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Only Incident Management push notifications are supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site) ().
{% /alert %}


{% /callout %}
Receive mobile push notifications for on-call alerts, incidents, and workflow automation updates, so you can stay informed in real time from the Datadog mobile app.


## Set up push notifications{% #set-up-push-notifications %}

By default, the mobile app is not allowed to send you notifications. To receive push notifications:

{% tab title="iOS" %}

1. In the Datadog mobile app, navigate to **Settings** > **Notifications**.

   {% image
      source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_settings_may_2025.562c150592be3de420b831a0dbfbdd52.png?auto=format"
      alt="Find the notification settings in the iOS version of Datadog's mobile app." /%}

1. Enable the **Allow Notifications** toggle. If this is your first time enabling notifications, this opens up a permissions prompt. Grant permission, then touch **Enable Notifications** again to go to the iOS system settings.

   {% image
      source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_notification_may_2025.fb4f6bf0c9f84eb9222e606349709f54.png?auto=format"
      alt="Configure the system notification settings of your iOS device." /%}

1. Within the iOS system settings, make sure you enable the **Allow Notifications** toggle. Datadog recommends you also enable the **Sound** and **Badges** toggles.

Make sure you grant the mobile app the necessary permissions.

### Custom sounds{% #custom-sounds %}

You can override the default system notification sounds with custom sounds preloaded in the Datadog mobile app.

To customize notification sounds:

1. In the Datadog mobile app, navigate to **Settings** > **Notifications** > **Notification categories**.
1. Select the notification category you want to customize.
1. Select a sound from the available options.

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

### Custom sounds{% #custom-sounds %}

You can override the default system notification sounds with custom sounds preloaded in the Datadog mobile app.

To customize notification sounds:

1. Go to **Device Settings** > **Notifications** > **Advanced Settings**.
1. Select **Manage notification categories for each app** and make sure Datadog is selected.
1. In the Datadog mobile app, navigate to **Settings** > **Notifications** > **Notification categories**.
1. Select the notification category you want to customize.
1. Select a sound from the available options.

**Note**: The volume for push notifications is dictated by your device's system volume settings.
{% /tab %}

## Circumvent mute and Do Not Disturb mode for On-Call{% #circumvent-mute-and-do-not-disturb-mode-for-on-call %}

You can override your device's system volume and Do Not Disturb mode for both push notifications (from the Datadog mobile app) and telephony notifications (such as voice call and SMS).

For more information, see the [guide on setting up your mobile device for On-Call][4].

### Critical push notifications{% #critical-push-notifications %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
On-Call is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site) ().
{% /alert %}


{% /callout %}

{% alert level="info" %}
Critical push notifications are only available for On-Call. If you are setting up On-Call on the Datadog mobile app for the first time, an onboarding flow takes care of notification settings and permissions.
{% /alert %}

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
If notification permissions are missing, tap **Bypass Do Not Disturb** and enable **Allow notifications** in System Settings.
{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_override_system_may_2025.209e33b7b41ebaf085d51f18e6491622.png?auto=format"
   alt="Override your Android device's system volume and Do Not Disturb mode." /%}

Then tap **Bypass Do Not Disturb** and enable **Override Do Not Disturb** in System Settings for High Urgency On-Call.

**On Samsung devices**: Go to **Settings** > **Notifications** > **Do Not Disturb** > **App notifications**. Select Datadog and allow it to bypass Do Not Disturb.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_override_system_volume_may_2025.591dd939d999fefc56f85977bf61fdec.png?auto=format"
   alt="Override your Android device's system volume and Do Not Disturb mode." /%}

In order to override system volume, tap the **Override system volume** and allow **Mode access** in System Settings to toggle on **Override system volume**.

Select your device for **High Urgency Notifications** and/or **Low Urgency Notifications** under the Notification Preferences section.

Test the setup of your critical push notification by tapping **Test push notifications**.

{% alert level="warning" %}
On Android, the Datadog mobile app cannot bypass system volume or Do Not Disturb settings when used within a Work Profile. As a workaround, install the Datadog mobile app on your personal profile.
{% /alert %}

{% /tab %}

### Custom sounds and volume for critical push{% #custom-sounds-and-volume-for-critical-push %}

{% alert level="info" %}
Volume and sound controls are available only for On-Call notifications. Incident and workflow notifications use your device's default system settings.
{% /alert %}

For high-urgency notifications, Datadog strongly recommends customizing your system sounds and volume settings. This ensures that alerts are not only more distinct and recognizable, but also more effective in capturing attention. Test your critical push notification preferences to confirm that they behave as expected.

## Incident notifications{% #incident-notifications %}

Receive status updates on your active incidents by setting up [Notification Rules for incidents on the Web][2].

1. In Incidents, navigate to **Settings** > [**Notification Rules**](https://app.datadoghq.com/incidents/settings?_gl=1*334tvl*_gcl_aw*R0NMLjE3NDUwMDYwODQuQ2p3S0NBand0ZGlfQmhBQ0Vpd0E5N3k4QkxnWmU4cTdmazJtUlJoQ3o1OTZXcTNmRWJIQTk1Rzg4dnAtUmZtUHBQUGx0OVNVSjRlSk9Sb0Nwek1RQXZEX0J3RQ..*_gcl_au*MTAxODMyNDk1My4xNzQwNDk1NzA3LjExNzUxOTU1MTUuMTc0NjQ5NTU3OS4xNzQ2NDk1NTc5*_ga*MjExMzI1MjUyOS4xNzQ1ODU2NjMx*_ga_KN80RDFSQK*czE3NDY0OTQzMzYkbzU4JGcxJHQxNzQ2NDk5MzA0JGowJGwwJGg5NTQ2NTk0Ng..*_fplc*Q2V5WVJmNnRSV2R0RmljTDZyWmg3ZEVZMFZPeDNlTFhLZkxnenFCOXBvTUslMkZTWWk0a3JzVEw1cDU5YlZzTW55TE5YazY5bjdhJTJGOXpySzJ0TFMxTEozZms0WTVlOWVibEN5ZFBNNm1XYmJJQll0R0d4YnlralJ2eU1CS1NoUSUzRCUzRA..#Rules).
1. Click the **+ New Rule** button on the top right.
1. Enter your desired condition fields for **When an incident isâ¦** and **And meets the following conditionsâ¦**. By default, these filters are empty, and a notification rule triggers for any incident.
1. Under **Notifyâ¦** select your notification recipient.If you want to notify a recipient's mobile device, select the option for their name that includes **(Mobile Push Notification)**. The recipient must have enabled notifications in the Datadog mobile app for this option to appear.
1. **With Template:** Select the desired message template you want the notification rule to use.
1. **Renotify on updates to:** Select the incident properties that trigger notifications. A new notification is sent whenever one or more of the selected properties change.
1. Click **Save**.

By default if you have push notifications enabled and are assigned as a commander to an incident, you automatically receive push notification for the incident.

## Workflow automation notifications{% #workflow-automation-notifications %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Workflow automation is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site) ().
{% /alert %}


{% /callout %}

Create [workflow automations][3] that send mobile push notifications.

1. On the workflow canvas, click the **+icon**.
1. Search for **Send mobile push notification**.
1. Under **To** select your notification recipient. The recipient must have enabled notifications in the Datadog mobile app for this option to appear.
1. Enter the message **Body**.

### Further Reading{% #further-reading %}

- [On-Call Documentation](https://docs.datadoghq.com/incident_response/on-call/)
- [Incident Notification Rules Documentation](https://docs.datadoghq.com/incident_response/incident_management/notification/)
- [Workflow Automation Documentation](https://docs.datadoghq.com/getting_started/workflow_automation/)

[2] /incident_response/incident_management/incident_settings/notification_rules/ [3]:https://docs.datadoghq.com/getting_started/workflow_automation/ [4]: /incident_response/on-call/guides/configure-mobile-device-for-on-call
