# Source: https://docs.datadoghq.com/mobile/guide/setup_mobile_device.md

---
title: Set Up Your Mobile Device for the First Time
description: >-
  Complete guide to setting up the Datadog mobile app including installation,
  push notifications, home screen customization, and widgets.
breadcrumbs: >-
  Docs > Datadog Mobile App > Mobile App Guides > Set Up Your Mobile Device for
  the First Time
---

# Set Up Your Mobile Device for the First Time

## Overview{% #overview %}

The Datadog mobile app helps you maintain continuous visibility into the health and performance of your system and take action on issues quickly, from anywhere. This guide walks you through the steps to configure your mobile device for optimal performance.

1. Install the mobile app
1. Set up your home screen
1. Enable push notifications
1. Set up widgets

## Installing{% #installing %}

Download the app from the [Apple App Store](https://apps.apple.com/us/app/datadog/id1391380318) for your iOS device, or from the [Google Play Store](https://play.google.com/store/apps/details?id=com.datadog.app&pli=1) for your Android device.

### SAML login{% #saml-login %}

[SAML login](https://docs.datadoghq.com/account_management/saml/#using-saml) requires you to set up and authenticate your SAML provider with Datadog using your default iOS/Android browser. See [this documentation for information on SAML IdP-initiated login](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login). To authenticate SAML:

1. Open the Datadog mobile app on your device.
1. Select your data center region (for example, US1) in the upper right corner of the landing page.
1. Press the **Log In** button.
1. Click the **Using Single Sign-On (SAML)?** link.
1. Enter your company email and tap **Send email**.
1. Open the email from Datadog on your mobile device and tap the link.
1. Enter your org's SAML credentials to be rerouted to an authenticated session of the Datadog mobile app.

### Login with a QR code{% #login-with-a-qr-code %}

1. In a desktop browser, open Datadog and navigate to [**Personal Settings > Organizations**](https://app.datadoghq.com/personal-settings/organizations).
1. Click **Log in to Mobile App** for your organization. This displays a QR code.
1. Use your default phone camera app to scan the QR code and then tap the suggested link to open the Datadog App. You will be automatically logged in.

### Switch organizations{% #switch-organizations %}

If you have multiple organizations in Datadog, you can navigate to the **Organizations page** under **Personal Settings** to switch between organizations to log in to.

## Set up your home screen{% #set-up-your-home-screen %}

Customize the order and modules of the mobile app home page.

{% tab title="Android" %}

1. Select the edit icon at the top right of the screen.
1. Toggle the modules that you would like displayed on the home page.
1. To reorder the modules, hold and drag the modules from the left hand side.
1. Make edits to Teams, Starred Items, or Monitors Saved Views by tapping the edit icon next to the respective module.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_edit_home.f3b29a85c5c515a5b1cf858559290887.png?auto=format"
   alt="Android home screen on the mobile app." /%}

{% /tab %}

{% tab title="iOS" %}

1. Select **Edit** at the bottom of the page.
1. Check the modules that you would like to display on the home page.
1. To reorder the modules, hold and drag the modules from the right hand side.
1. Make edits to Teams, Starred Items, or Monitor Saved Views by tapping "Edit" next to the respective module.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_edit_home.6432f9e95ffc644ba4646c05782985ef.png?auto=format"
   alt="iOS home screen on the mobile app" /%}

{% /tab %}

### Add starred items{% #add-starred-items %}

Add your most frequented dashboards, notebooks, and services for quick reference.

1. Select **Edit** next to **Starred Items**
1. Add and arrange up to 5 starred items
1. Tap **Done** when you are finished

### Add monitors saved views{% #add-monitors-saved-views %}

Quickly reference monitor saved views for your most important monitors. For more information, see [manage monitors](https://docs.datadoghq.com/monitors/manage/).

1. Select **Edit** next to Monitors Saved Views
1. Add and arrange up to 5 monitor saved views
1. Tap **Done** when you are finished

## Enable push notifications{% #enable-push-notifications %}

Enable push notifications to ensure timely response to alerts from On-Call, incidents, or workflows. To receive push notifications:

{% tab title="Android" %}

1. In the Datadog mobile app, navigate to **Settings > Notifications**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_settings.ad769189393557921169357fa6723d63.png?auto=format"
   alt="Android notifications settings" /%}
Enable the **Allow notifications** toggle. Datadog highly recommends you also enable **Sound and vibration** and **Show content on Lock screen**.
{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_notification.6580382f86e33dbfb9b3d843cf72a931.png?auto=format"
   alt="Android notifications settings" /%}

{% /tab %}

{% tab title="iOS" %}
Make sure you grant the mobile app the necessary permissions.

1. In the Datadog mobile app, navigate to **Settings > Notifications**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_settings.562c150592be3de420b831a0dbfbdd52.png?auto=format"
   alt="iOS notifications settings" /%}
Enable the **Allow Notifications** toggle. If this is your first time enabling notifications, this opens up a permissions prompt. Grant permission, then touch **Enable Notifications** again to go to the iOS system settings.
{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_notification.fb4f6bf0c9f84eb9222e606349709f54.png?auto=format"
   alt="iOS notifications settings" /%}
Within the iOS system settings, make sure you enable the **Allow Notifications** toggle. Datadog highly recommends you also enable the **Sound** and **Badges** toggles.
{% /tab %}

**Note**: If you are using the mobile app for Datadog On-Call, follow this guide to [set up your mobile device for Datadog On-Call](https://docs.datadoghq.com/service_management/on-call/guides/configure-mobile-device-for-on-call/?tab=ios).

## Set up home or lock screen widgets{% #set-up-home-or-lock-screen-widgets %}

For fast access to important data, add Datadog widgets to your mobile device's home or lock screen. You can set up incident, SLO, monitor, dashboard, and on-call widgets. For more information, see [mobile device widgets](https://docs.datadoghq.com/mobile/widgets?tab=android).

### Home screen widgets{% #home-screen-widgets %}

Set up home screen widgets to quickly access dashboards.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_dashboard_widget.797c4c5dd173b60dfefc98d88184f0ef.png?auto=format"
   alt="iOS home screen dashboard widgets" /%}

{% tab title="Android" %}

1. Long press on your home screen.
1. Tap the **Widgets** button on your home screen editor. If you have app shortcuts, the **Widgets** button might appear as only an icon on the top right corner of the bubble.
1. Search for "Datadog" widgets.
1. Tap your desired widget and tap **Add**.
1. Resize the widget to fit your preference.
1. Tap the widget to configure the widget fields. When you access the mobile app from the widget, these are the fields that are queried in the app.

{% /tab %}

{% tab title="iOS" %}

1. Long press on your home screen.
1. Tap **Edit**, then tap the **Add Widget** button on the top left corner of the screen.
1. Search for "Datadog" widgets.
1. Tap your desired widget and your preferred size (small, medium, or large).
1. Tap **Add Widget** and configure the widget fields. When you access the mobile app from the widget, these are the fields that are queried in the app.
1. Drag, minimize, or expand the widget to customize the location and size of the widget on your home screen.

{% /tab %}

### Lock screen widgets{% #lock-screen-widgets %}

Lock screen widgets for monitors, SLOs, incidents, and dashboards are supported on iOS.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/lock_screen_widget.673850869ea1cdf1bde090dd2cdc8116.png?auto=format"
   alt="iOS home screen dashboard widgets" /%}

1. Long press on your lock screen.
1. Tap **Customize**, then select **Lock Screen**.
1. Tap on the lock screen widget space to pull up the Add Widgets card.
1. Scroll to and tap on the Datadog app.
1. Tap the lock screen widget you would like to add.
1. Tap the widget on the lock screen to pull up the configuration panel.
1. Configure the widget according to the fields specified for the selected widget.
1. Drag, minimize, or expand the widget to customize the location and size of the widget on your lock screen.

## Further Reading{% #further-reading %}

- [Getting started with the Datadog mobile app](https://www.datadoghq.com/blog/mobile-app-getting-started/)
- [Shortcut Configurations](https://docs.datadoghq.com/mobile/shortcut_configurations/)
- [Improve your on-call experience with Datadog mobile dashboard widgets](https://www.datadoghq.com/blog/datadog-mobile-widgets/)
