# Source: https://documentation.onesignal.com/docs/en/notifications-not-shown-web-push.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web push: Notifications not shown

> Troubleshoot web push notifications that show as Delivered in OneSignal but don't appear on a subscriber's device.

When a notification shows as "Delivered" in OneSignal, it means we have successfully sent the notification to the FCM (Google) / APNs (Apple) / WNS (Microsoft) servers which then distribute the notifications to your subscribers. The following are reasons why notifications may show as "Delivered", but are not visible on your device.

## Device settings

Device Notification Settings are the **most common cause** of web push not appearing on a device. Check the following settings including Focus modes (Do Not Disturb, Low Battery, etc.) before looking elsewhere.

<Warning>
  Select the correct operating system from the tabs below. You should see Windows, macOS, Android, and iOS.
</Warning>

<Tabs>
  <Tab title="Windows">
    <Accordion title="Windows 10 Notification Settings">
      1. Select **Start > Settings > Notifications & Actions > Get notifications from apps and other senders**

      2. **Make sure your site and browser are also enabled.**

      <Frame caption="Windows 10 Notification Settings">
        <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/cb85585-f0eb72bb-313f-b80e-480c-46321fdb5ebd.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=21acf8bf7acb457822fe6f442a0f2fad" width="558" height="317" data-path="images/docs/cb85585-f0eb72bb-313f-b80e-480c-46321fdb5ebd.png" />
      </Frame>
    </Accordion>

    **Windows 11 Notification Settings:**

    1. Select **Start > Settings > System > Notifications**

    <Frame caption="Windows 11 Notification Settings">
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9e6b656-Screenshot_2023-07-13_at_4.03.13_PM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=8e4d1b4617fc098bd0d0060defb23851" width="2046" height="1598" data-path="images/docs/9e6b656-Screenshot_2023-07-13_at_4.03.13_PM.png" />
    </Frame>

    2. Turn On **Notifications**

    3. Turn Off **Do not disturb** (while testing, push will show when this is disabled)

    4. Scroll down to **Notifications from apps and other senders**

    <Frame caption="Windows 11 Notifications from apps and other senders">
      <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/ed955fa-Screenshot_2023-07-13_at_4.04.16_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=e6943675129e73eabe9286c976163091" alt="Windows 11 Settings showing the Notifications from apps and other senders list" width="2046" height="1598" data-path="images/docs/ed955fa-Screenshot_2023-07-13_at_4.04.16_PM.png" />
    </Frame>

    5. Make sure your browsers are turned **On**.

    <Frame caption="Windows 11 Notification Settings Browser List">
      <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/258c7ee-Screenshot_2023-07-13_at_4.11.32_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=48f5b6b47512f24ef6589a404d6fb413" width="2046" height="1598" data-path="images/docs/258c7ee-Screenshot_2023-07-13_at_4.11.32_PM.png" />
    </Frame>
  </Tab>

  <Tab title="macOS">
    1. Navigate to **System Settings > Notifications**
    2. Make sure **Notifications** is enabled in Notification Center.

    <Info>
      You may need to select **Allow notifications when mirroring or sharing the display**.
    </Info>

    <Frame caption="macOS Notification Center Settings">
      <img src="https://mintcdn.com/onesignal/iYHHyW9S1IVpDgxC/images/push/macos-notification-center-settings.png?fit=max&auto=format&n=iYHHyW9S1IVpDgxC&q=85&s=3978f6da8fd11a30efae0da02a5c8a5a" width="1670" height="1938" data-path="images/push/macos-notification-center-settings.png" />
    </Frame>

    3. Scroll down to **Application Notifications** list and make sure your browser is turned on.

    <Warning>
      Some browsers like Chrome and Edge show 2 different application entries.

      1. Standard web push notifications
      2. Internal alerts e.g Google calendar

      Make sure both are enabled.
    </Warning>

    <Frame caption="macOS Application Notifications List. Example shows Chrome and Edge have 2 entries and both need to be enabled.">
      <img src="https://mintcdn.com/onesignal/iYHHyW9S1IVpDgxC/images/push/macos-application-notifications-list.png?fit=max&auto=format&n=iYHHyW9S1IVpDgxC&q=85&s=adebcf8e4a20d72fccf92459dc94bda1" width="1670" height="1938" data-path="images/push/macos-application-notifications-list.png" />
    </Frame>

    4. Select the Application and toggle on the settings. Select how you want notifications to be displayed.

    <Frame caption="macOS Application Notifications Settings">
      <img src="https://mintcdn.com/onesignal/iYHHyW9S1IVpDgxC/images/push/macos-application-notifications-settings.png?fit=max&auto=format&n=iYHHyW9S1IVpDgxC&q=85&s=45cc68b248d15f60c6b344eca3114447" width="1670" height="1938" data-path="images/push/macos-application-notifications-settings.png" />
    </Frame>

    <Warning>
      Some older versions of Safari may show the website in your Application Notifications list. Make sure to check the website is turned on in this case.
    </Warning>

    5. Navigate to **System Settings > Focus** and make sure no Focus modes are active while testing.

    <Frame caption="macOS Focus Mode Settings">
      <img src="https://mintcdn.com/onesignal/iYHHyW9S1IVpDgxC/images/push/macos-focus-mode-settings.png?fit=max&auto=format&n=iYHHyW9S1IVpDgxC&q=85&s=7924eb3a1907400fee662fcf249081ef" width="1670" height="1392" data-path="images/push/macos-focus-mode-settings.png" />
    </Frame>
  </Tab>

  <Tab title="Android">
    1. Navigate to **Settings > Notifications > your browser of choice**.
    2. Make sure **"Show notifications"** and your website are checked.

    <Frame caption="Android Notification Settings">
      <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b75b427-Screenshot_20210816-174706_Settings.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=f2de2e15cdf5b36f423b707903ba82ae" width="800" height="873" data-path="images/docs/b75b427-Screenshot_20210816-174706_Settings.png" />
    </Frame>

    <Note>
      Android uses per-app notification channels. If your browser's notification channel is set to silent or turned off, push notifications won't appear even if the top-level toggle is on. In Settings, tap the browser entry and check that each notification channel is enabled and set to a visible alert style.
    </Note>
  </Tab>

  <Tab title="iOS">
    <Warning>
      iOS requires you to add your site to the Home Screen before subscribers can receive push notifications on iPhones and iPads. Complete the [iOS web push setup](/docs/en/web-push-for-ios) before troubleshooting.
    </Warning>

    1. Click the browser's **Share** button and select **Add to Home Screen**.
    2. Open your site from the Home Screen and allow notifications when the permission prompt appears.
    3. Go to device's **Settings > Notifications > your site** and make sure **Allow Notifications** is toggled on.
  </Tab>
</Tabs>

### Network issues - no internet

Devices must be online to receive push notifications. If the device is turned off, in airplane mode, has unstable or no internet connection, the push will not show until a proper connection is made. You can set the timeframe FCM and APNs will wait for a connection with the Time To Live (TTL) Parameter (the default is 3 days).

If the device is on a WiFi network with a firewall or VPN, that network may be blocking the connection to Apple or Google servers. Test by switching to cellular data.

If you are managing network traffic through a firewall, configure it to allow the following:

* **FCM (Chrome, Android):** outbound TCP ports 5228, 5229, and 5230. See [FCM documentation](https://firebase.google.com/docs/cloud-messaging/concept-options) for full requirements.
* **APNS (Safari, iOS):** outbound TCP port 5223 and TCP port 443 or 2197. See [Apple's documentation](https://support.apple.com/en-us/HT203609) for full requirements.

***

## Browser settings

Your browser has its own notification permission settings separate from your OS settings. A site can be blocked at the browser level even if OS notifications are enabled for the browser.

* **Chrome**: Go to `chrome://settings/content/notifications` and confirm your site is listed under "Allowed to send notifications", not "Not allowed to send notifications".
* **Firefox**: Go to `about:preferences#privacy`, scroll to **Permissions > Notifications**, and click **Settings** to check your site's status.
* **Edge**: Go to `edge://settings/content/notifications` and verify your site is allowed.
* **Safari**: Go to **Safari > Settings > Websites > Notifications** and check that your site is set to **Allow**.

### Browser is closed

Browsers won't show push notifications unless they are running. If you open the browser before the [Time To Live (TTL)](./push#time-to-live) expires on a sent notification, it will pop up.

### Unsupported browser

Users must subscribe to notifications on their desktop or mobile device to receive notifications and it must be a browser that supports push notifications. Please see [Web Push FAQ](./web-push-setup-faq) for Supported Web Platforms.

### Mobile browser app data full

If your mobile browser app has reached its data limit or its data is full, you will need to clear the data on the app.

If your mobile browser app has many unread push notifications and/or many tabs open, this can cause notifications to not show.

***

## User subscription

Make sure your device is still subscribed and targeted for push notifications.

### Subscription eligibility

Check the message audience to verify that your web push Subscription is included:

* **[Segments](./segmentation)**: Verify your Subscription meets all audience filter conditions.
* **Direct send**: Confirm the ID you are targeting is correct:
  * The Subscription is still subscribed to push.
  * It has a recent last session date — you may be sending to an old or inactive Subscription.

Use the [troubleshooting steps](#troubleshooting-web-push-notifications) below to look up your Subscription ID and confirm it is subscribed and active.

***

## Website codebase

### Unregistering service worker or adding pwa

Check your site's codebase for the `.unregister()` method. Calling this method will delete Service Workers. See [this guide](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/unregister) for details on this method.

If you have another service worker like for your PWA you will need to follow our [Service Worker guide on integrating multiple service workers](./onesignal-service-worker).

***

## Troubleshooting web push notifications

Follow these steps to get a clean web push Subscription and confirm web push is working end-to-end.

<Steps>
  <Step title="Open your site in browser">
    These steps use Chrome but Edge, Firefox, and others follow the same pattern. Do not use Incognito or Guest Browser mode, and close any other tabs open to your site.

    <Accordion title="Mobile device debugging">
      **Android**

      Plug your Android device into your desktop with a USB cable.

      * **Chrome**: Open `chrome://inspect/#devices` on desktop, then follow the steps below on your mobile device.
      * **Firefox**: See [about:debugging](https://developer.mozilla.org/en-US/docs/Tools/about:debugging).

      **iOS** (Mac only)

      iOS web push is only supported in Safari via a site added to the Home Screen. To inspect it:

      1. On your iPhone or iPad, go to **Settings > Safari > Advanced** and enable **Web Inspector**.
      2. Connect your device to your Mac with a USB cable.
      3. Open Safari on your Mac, then go to **Develop > \[your device name] > \[your site's page]**.
      4. Follow the steps below using your mobile device.
    </Accordion>
  </Step>

  <Step title="Reset browser permissions and clear site data">
    This resets the site to simulate a first-time visitor state.

    1. Click the **site information icon** next to your URL.
    2. If you see **Notifications**, select **Reset permission** (you want to see "Can ask to send notifications").
    3. Click **Cookies and site data**.

    <Frame caption="Chrome site settings panel showing Notifications reset permission and Cookies options">
      <img src="https://mintcdn.com/onesignal/dzd4t2XokDP_R8GG/images/web-push/chrome-site-settings-panel-notifications-reset-permission-and-cookies-options.png?fit=max&auto=format&n=dzd4t2XokDP_R8GG&q=85&s=1705ca95848068edbea491ddf21dcd90" alt="Chrome site settings panel showing Notifications reset permission and Cookies options" width="2064" height="1508" data-path="images/web-push/chrome-site-settings-panel-notifications-reset-permission-and-cookies-options.png" />
    </Frame>

    4. Click **Manage on-device site data**.

    <Frame caption="Chrome Cookies and site data panel with Manage cookies and site data button">
      <img src="https://mintcdn.com/onesignal/dzd4t2XokDP_R8GG/images/web-push/chrome-cookies-and-site-data-panel-with-manage-cookies-and-site-data-button.png?fit=max&auto=format&n=dzd4t2XokDP_R8GG&q=85&s=d62e11591cc0ff5a755af151032f1a3b" alt="Chrome Cookies and site data panel with Manage cookies and site data button" width="2064" height="1508" data-path="images/web-push/chrome-cookies-and-site-data-panel-with-manage-cookies-and-site-data-button.png" />
    </Frame>

    5. Click the **Trash Icon** next to:

    * Your site URL
    * `onesignal.com`

    Then click **Done**.

    <Frame caption="Chrome cookies list with trash icon to remove site data">
      <img src="https://mintcdn.com/onesignal/dzd4t2XokDP_R8GG/images/web-push/chrome-cookies-list-with-trash-icon-to-remove-site-data.png?fit=max&auto=format&n=dzd4t2XokDP_R8GG&q=85&s=10749177b3db6b1f9b33ebe813cba4a9" alt="Chrome cookies list with trash icon to remove site data" width="2064" height="1508" data-path="images/web-push/chrome-cookies-list-with-trash-icon-to-remove-site-data.png" />
    </Frame>

    6. Close the tab and open your site again in a new tab.
  </Step>

  <Step title="Open the Console and subscribe to push notifications">
    1. When you return to your site in a new tab, right click the page and select **Inspect** to open the Console.
    2. Follow the steps you set up to trigger the native browser permission prompt and allow notifications. See [Web permission prompts](./permission-requests) for more details.

    <Frame caption="Browser notification permission prompt asking to allow or block notifications">
      <img src="https://mintcdn.com/onesignal/dzd4t2XokDP_R8GG/images/web-push/browser-notification-permission-prompt-asking-to-allow-or-block-notifications.png?fit=max&auto=format&n=dzd4t2XokDP_R8GG&q=85&s=9fb78665792856e16dfc8a9e44cb8529" alt="Browser notification permission prompt asking to allow or block notifications" width="2064" height="1508" data-path="images/web-push/browser-notification-permission-prompt-asking-to-allow-or-block-notifications.png" />
    </Frame>

    3. Click **Allow** to subscribe to push notifications.
    4. Check the **Console** for any errors. If you see anything in red related to OneSignal, see our [Web SDK troubleshooting](./troubleshooting-web-push) docs.
  </Step>

  <Step title="Get your Subscription ID and set as a test Subscription">
    1. In the **Console**, run the following code to get your Subscription ID:

    ```javascript JavaScript theme={null}
    OneSignal.User.PushSubscription.id
    ```

    <Frame caption="JavaScript Console showing OneSignal.User.PushSubscription.id returning a subscription ID">
      <img src="https://mintcdn.com/onesignal/dzd4t2XokDP_R8GG/images/web-push/javascript-console-showing-onesignal-user-pushsubscription-id-returning-a-subscription-id.png?fit=max&auto=format&n=dzd4t2XokDP_R8GG&q=85&s=cd132e56f4f00f3161233766eecc4a85" alt="JavaScript Console showing OneSignal.User.PushSubscription.id returning a subscription ID" width="2064" height="1508" data-path="images/web-push/javascript-console-showing-onesignal-user-pushsubscription-id-returning-a-subscription-id.png" />
    </Frame>

    2. Copy the ID without quotes.

    3. In the OneSignal dashboard, navigate to **Audience > Subscriptions**, paste the Subscription ID (without quotes) in the search bar, click the **Options** button, and select **Add as test Subscription**.

    <Frame caption="OneSignal dashboard showing Subscriptions search bar with Subscription ID pasted">
      <img src="https://mintcdn.com/onesignal/dzd4t2XokDP_R8GG/images/web-push/onesignal-dashboard-showing-subscriptions-search-bar-with-subscription-id-pasted.png?fit=max&auto=format&n=dzd4t2XokDP_R8GG&q=85&s=dfa40b9702699d39b660e1cd2fc9abe5" alt="OneSignal dashboard showing Subscriptions search bar with Subscription ID pasted" width="2064" height="1508" data-path="images/web-push/onesignal-dashboard-showing-subscriptions-search-bar-with-subscription-id-pasted.png" />
    </Frame>
  </Step>

  <Step title="Send a test message to yourself">
    1. Navigate to **Messages > New Push** and write a message in the **Message** field.
    2. Under **Test & Preview**, select your test Subscription and send the push to yourself.

    <Frame caption="OneSignal dashboard showing New Push message form with test Subscription selected">
      <img src="https://mintcdn.com/onesignal/dzd4t2XokDP_R8GG/images/web-push/onesignal-dashboard-showing-new-push-message-form-with-test-subscription-selected.png?fit=max&auto=format&n=dzd4t2XokDP_R8GG&q=85&s=993d667a2f90cd0a77e40a09359b670e" alt="OneSignal dashboard showing New Push message form with test Subscription selected" width="2064" height="1508" data-path="images/web-push/onesignal-dashboard-showing-new-push-message-form-with-test-subscription-selected.png" />
    </Frame>

    <Check>
      Success! You should receive the push you tested.

      If you did not receive the push, review this entire guide one more time and try again.
    </Check>
  </Step>
</Steps>

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Your OneSignal App ID
* The Subscription ID or External ID
* The URL to the message you tested in the OneSignal Dashboard
* The URL to your site with the OneSignal web SDK code

  We're happy to help!
</Info>

Built with [Mintlify](https://mintlify.com).
