# Source: https://documentation.onesignal.com/docs/en/troubleshooting-web-push.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web SDK troubleshooting

> Troubleshoot OneSignal Web Push issues on Chrome, Firefox, Safari, and Android. Fix common service worker, origin, MIME type, and mobile push errors with step-by-step debugging guidance.

## Overview

This guide walks you through troubleshooting your OneSignal Web SDK setup. Before continuing, review the [Web SDK Setup](./web-sdk-setup) to ensure you've completed all steps.

The most common reasons web push appears to not be working are actually related to your browser and device's notification settings:

### Browser compatibility

Users may see [web permission prompts](/docs/en/permission-requests) but cannot subscribe to push notifications in incognito, private, or guest browser modes.

<Accordion title="Browser compatibility by operating system">
  | Browser                                                                          | Windows | macOS | Android | iOS |
  | -------------------------------------------------------------------------------- | ------- | ----- | ------- | --- |
  | [Chrome](https://en.wikipedia.org/wiki/Google_Chrome)                            | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Firefox](https://en.wikipedia.org/wiki/Firefox)                                 | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Safari 10+](https://en.wikipedia.org/wiki/Safari_\(web_browser\))               | ❌       | ✅     | ❌       | ✅ ¹ |
  | [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge)                   | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Opera](https://en.wikipedia.org/wiki/Opera_\(web_browser\)) ²                   | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Samsung Internet](https://en.wikipedia.org/wiki/Samsung_Internet_for_Android) ² | ❌       | ❌     | ✅       | ✅ ¹ |
  | [Yandex](https://en.wikipedia.org/wiki/Yandex_Browser) ²                         | ✅       | ✅     | ✅       | ✅ ¹ |
  | [UC Browser](https://en.wikipedia.org/wiki/UC_Browser) ²                         | ✅       | ❌     | ✅       | ✅ ¹ |
  | [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer)             | ❌       | ❌     | ❌       | ❌   |
  | [DuckDuckGo](https://en.wikipedia.org/wiki/DuckDuckGo)                           | ❌       | ❌     | ❌       | ❌   |

  <Info>
    ¹ iOS requires web app installation (see [iOS web push setup](/docs/en/web-push-for-ios))

    ² Chromium-based browsers appear as "Chrome" in OneSignal analytics
  </Info>
</Accordion>

### Device notification settings

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

### Prompt display issues

The following are common reasons why the web push notification prompt may not display as expected.

<Steps>
  <Step title="Confirm a prompt is configured">
    Review your [Web permission prompt](/docs/en/permission-requests) setup to ensure you have configured a prompt and understand the different browser behaviors.

    For instance, some browsers like Safari require a user gesture (clicking a button) before the native prompt can appear. Details for each browser can be found in our [Web permission prompt > Native permission prompt](/docs/en/permission-requests#native-permission-prompt) section.
  </Step>

  <Step title="Check browser compatability, incognito, private browser, or guest browser modes.">
    Browsers do not allow users to subscribe to notifications in these modes. This is why the Slide Prompt may show but the native Permission Prompt will not display.

    Make sure you are [using a browser and device that supports web push](/docs/en/troubleshooting-web-push#browser-compatibility).
  </Step>

  <Step title="Check your browser's Notification Settings">
    Navigate to your browser's settings and check the "Notifications" permission setting. Chrome example: `chrome://settings/content/notifications`

    <Frame caption="Chrome Notifications settings">
      <img src="https://mintcdn.com/onesignal/GxkD7lQqPiL4KVpn/images/push/chrome-notifications-settings.png?fit=max&auto=format&n=GxkD7lQqPiL4KVpn&q=85&s=8edb5d3cdbe4b785086053fdfc82bd1c" width="2268" height="2012" data-path="images/push/chrome-notifications-settings.png" />
    </Frame>

    In this example:

    * The user has selected "Don't allow sites to send notifications" which will prevent the native permission prompt from showing. This must show "Sites can ask to send notifications" to allow the native permission prompt to show.
    * The user has added `https://yoursite.com` to the "Not allowed to send notifications" list, which will prevent the native permission prompt from showing. This must be removed from the list to allow the native permission prompt to show.

    **Browser specific documentation:**

    * [Chrome](https://support.google.com/chrome/answer/3220216) - This page explains how to manage notifications in Chrome by going to Settings > Privacy and security > Site Settings > Notifications, where you can control default behavior and manage permissions for individual websites.
    * [Firefox](https://support.mozilla.org/en-US/kb/push-notifications-firefox) - This guide covers Firefox's Web Push notifications, explaining how to manage notification permissions through Settings > Privacy & Security > Notifications, and how to control permissions for specific sites through the address bar's site information icon.
    * [Safari](https://support.apple.com/guide/safari/customize-website-notifications-sfri40734/mac) - This Apple guide explains how to customize Safari notifications on Mac through Safari > Preferences > Websites > Notifications, where you can manage which sites can send notifications and control notification behavior through System Preferences.
    * [Edge](https://support.microsoft.com/en-us/microsoft-edge/manage-website-notifications-in-microsoft-edge-0c555609-5bf2-479d-a59d-fb30a0b80b2b) - This article details how to manage Edge notifications by navigating to Settings > Privacy, search, and services > Site permissions > Notifications, or by clicking the site information icon in the address bar.
  </Step>

  <Step title="iOS/iPadOS requirements are not met.">
    For iOS, there are some additional requirements to prompt users for their subscription. More information can be seen in the [Mobile Web Push for iOS/iPadOS](/docs/en/web-push-for-ios) guide.
  </Step>
</Steps>

***

## Troubleshooting steps

After checking the above, follow these steps to troubleshoot your OneSignal Web SDK setup.

<Steps>
  <Step title="Open the browser developer tools console">
    The browser's developer tools can be used to interact with our web SDK on your webpage and enable logging to check for errors.

    <Tabs>
      <Tab title="Desktop">
        * **Chrome**: Right click on the page, click *Inspect*, and click the *Console* tab of the popup window that opens up.
        * **Firefox**: Right click on the page, click *Inspect element*, and click the *Console* tab of the popup window that opens up.
        * **Safari**: Go to **Safari → Preferences → Advanced** and make sure *Show Develop menu in menu bar* is checked. Then, on your webpage, right click, click *Inspect element*, and click the *Console* tab of the popup window that opens up.

        <Frame caption="Desktop Developer Tools Console">
          <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/M6r7mvTPT7W1USDDy5Wz_console.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=452fc53b810bd258234dc5cc46f0b45e" width="1510" height="598" data-path="images/docs/M6r7mvTPT7W1USDDy5Wz_console.png" />
        </Frame>
      </Tab>

      <Tab title="Android">
        * **Chrome on Android**: [Enable USB Debugging](https://developer.chrome.com/docs/devtools/remote-debugging/), connect your device into your computer and access the Dev Tools with `chrome://inspect#devices` in your Desktop Chrome browser.
        * **Firefox on Android**: [Enable USB Debugging](https://developer.mozilla.org/en-US/docs/Tools/about:debugging), connect your device into your computer and access the Dev Tools with `about:debugging` in your Desktop Firefox browser.
      </Tab>

      <Tab title="iOS">
        1. [Enable the web inspector on iOS](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/GettingStarted/GettingStarted.html).
        2. Open the Safari browser on your mac and select **Develop > your device > your site**.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Enable web SDK logging">
    You can now run commands in the developer tools Console. Execute the following code:

    ```javascript JavaScript theme={null}
      OneSignal.Debug.setLogLevel('trace');
    ```

    * You should see `undefined` as the result.
    * Close the tab and open a new one to the same page. Refreshing alone won't trigger all SDK initialization events.
    * You will start to see OneSignal SDK logs in the Console.

    <Frame caption="Console with verbose SDK logs">
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/PTU11ly5R0quyNQDYeb8_consoleLog1.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=388624dc46350f2c2c38e834297f2f59" width="2880" height="1214" data-path="images/docs/PTU11ly5R0quyNQDYeb8_consoleLog1.png" />
    </Frame>
  </Step>
</Steps>

### Configuration errors

You may encounter the following errors after OneSignal initializes:

<Danger>
  Error: SDK already initialized
</Danger>

<Frame caption="Duplicate SDK initialization error">
  <img src="https://mintcdn.com/onesignal/6sTkY-dQpGTrB0vT/images/sdk/sdk-already-initialized-error.png?fit=max&auto=format&n=6sTkY-dQpGTrB0vT&q=85&s=09e589bc31483e0cd9c052944376bb1e" width="1798" height="388" data-path="images/sdk/sdk-already-initialized-error.png" />
</Frame>

**What this means:** The OneSignal Web SDK `init` code is being called more than once, often caused by combining WordPress plugin setup with manual code or accidentally adding the OneSignal `init` code multiple times.

**How to fix:** Remove any duplicate `init` calls. If using the WordPress plugin, remove any manual OneSignal code from your theme files.

<Danger>
  Error: Can only be used on: (URL Set in OneSignal Dashboard)
</Danger>

<Frame caption="Example shows the URL set in OneSignal dashboard `http://127.0.0.1:5501` is not the current site origin you are visiting.">
  <img src="https://mintcdn.com/onesignal/6sTkY-dQpGTrB0vT/images/sdk/site-origin-mismatch-error.png?fit=max&auto=format&n=6sTkY-dQpGTrB0vT&q=85&s=6d6c788f674e4b65f0b20be4a70d1090" width="1798" height="564" data-path="images/sdk/site-origin-mismatch-error.png" />
</Frame>

**What this means:** The domain you are currently visiting doesn't match the site URL configured in your OneSignal dashboard.

**How to fix:** Copy the site URL in your browser and paste it into your OneSignal dashboard **Settings > Push & In-app > Web > Site URL** configuration. Make sure it is the site origin using the following format:

* **Protocol:** Must be `https://` (for local testing, see [Localhost configuration](./web-sdk-setup#local-testing))
* **Domain:** `example.com` vs `www.example.com`
* **Subdomain:** `app.example.com` vs `example.com`

All three components must match between your actual site URL and your dashboard configuration.

<Danger>
  Error: OneSignalSDK: The "My site is not fully HTTPS" option is no longer supported starting with version 16 (User Model) of the OneSignal SDK.
</Danger>

<Frame caption="Example of the HTTP site not supported error">
  <img src="https://mintcdn.com/onesignal/u7GEHl8RqZEg_hFd/images/sdk/http-site-not-supported-error.png?fit=max&auto=format&n=u7GEHl8RqZEg_hFd&q=85&s=5009ca5985c1ddcc0b1904146504f1db" width="526" height="141" data-path="images/sdk/http-site-not-supported-error.png" />
</Frame>

**What this means:** Your OneSignal dashboard is configured to use an HTTP site and you likely updated to use HTTPS.

Your users that subscribed to your site while using HTTP or the "My site is not fully HTTPS" option are actually subscribed to a subdomain we provided you in the format `https://your-label.os.tc` and not your actual site origin. This is because web push isn't supported on HTTP sites or websites that cannot host service workers.

**How to fix:** You have 2 options, but both require your users to resubscribe because they are actually subscribed to the `os.tc`subdomain.

1. Create a new OneSignal App and set the new App ID in your OneSignal init code. The benefit of this is you can continue sending push from the old/original OneSignal App. Send as many notifications as you want letting your users know the site has been updated and they should come back and subscribe again to keep getting updates. Offering a discount or incentive to resubscribe goes a long way. Set the "Launch URL" to a landing page and provide them a button to easily resubscribe like our Bell prompt, Custom Link prompt, or Category Slide prompt. See [Permission prompts](./permission-requests) for more details.

2. If you want to keep the same App ID, you would need to use our [Update an App](/reference/update-an-app) API to update the `chrome_web_origin` and `safari_site_origin` to your HTTPS site origin. Because these users subscribed to the `os.tc` subdomain, they do not have push permissions allowed in the browser for your site. The browser doesn't "know" they are subscribed to your site, so they will get prompted again. If they subscribe again, they will have 2 web push Subscriptions to your site on the same browser and will get duplicate notifications. For this reason, we recommend [deleting all your current web push subscribers](./delete-users) to prevent them from getting duplicate notifications. Before deleting, send a few notifications letting them know the site has been updated and they should subscribe again to keep getting updates. Offering a discount or incentive to resubscribe works really well. Set the "Launch URL" to a landing page and provide them a button to easily resubscribe like our Bell prompt, Custom Link prompt, or Category Slide prompt. See [Permission prompts](./permission-requests) for more details.

### Service worker installation errors

If you are presented with the [Native permission prompt](./permission-requests) and click "Allow", you may encounter the following service worker installation errors:

<Danger>
  Y: Registration of a Service Worker failed.
</Danger>

<Danger>
  \[Service Worker Installation] Installing service worker failed TypeError: Failed to register a ServiceWorker for scope ('`https://your-site.com/`') with script ('`https://your-site.com/...`'): A bad HTTP response code (404) was received when fetching the script.
</Danger>

<Danger>
  \[Service Worker Installation] Installing service worker failed TypeError: Failed to register a ServiceWorker for scope ('`https://www.yoursite.com/`') with script ('`https://www.yoursite.com/...`'): A bad HTTP response code (403) was received when fetching the script.
</Danger>

<Frame caption="Example of a service worker installation error">
  <img src="https://mintcdn.com/onesignal/6sTkY-dQpGTrB0vT/images/sdk/service-worker-installation-error.png?fit=max&auto=format&n=6sTkY-dQpGTrB0vT&q=85&s=a3471311e9e42d914e220e28525dbb8d" width="1798" height="816" data-path="images/sdk/service-worker-installation-error.png" />
</Frame>

<Danger>
  The script has an unsupported MIME type ('current MIME type').
  \[Service Worker Installation] Installing service worker failed SecurityError: Failed to register a ServiceWorker for scope ('[https://your-site.com/](https://your-site.com/)') with script ('[https://your-site.com/](https://your-site.com/)...'): The script has an unsupported MIME type ('current MIME type').
</Danger>

<Frame caption="MIME type error in service worker">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f4215e3-Screen_Shot_2020-02-18_at_5.00.49_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=70bb68c3eb6f26e2c42c5462ec8ea138" width="2594" height="136" data-path="images/docs/f4215e3-Screen_Shot_2020-02-18_at_5.00.49_PM.png" />
</Frame>

<Danger>
  \[Service Worker Installation] Installing service worker failed SecurityError: Failed to register a ServiceWorker for scope ('[https://your-site.com/](https://your-site.com/)') with script ('[https://your-site.com/](https://your-site.com/)...'): The script resource is behind a redirect, which is disallowed.
</Danger>

<Frame caption="Redirect error in console">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1ed3985-Screen_Shot_2020-02-19_at_7.12.05_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=d7b09ca6815ca516b553505fd46d37cd" width="1643" height="74" data-path="images/docs/1ed3985-Screen_Shot_2020-02-19_at_7.12.05_PM.png" />
</Frame>

**What this means:** Your service worker file is configured incorrectly.

**How to fix:**

<Steps>
  <Step title="Find your service worker path">
    Our SDK looks for the `OneSignalSDKWorker.js` service worker file in the root directory of your site unless you specify a custom filename or location as described in the [Service Worker Setup Guide](./onesignal-service-worker).

    Make sure you have configured the correct filename, location, and scope for our SDK to find the service worker file.
  </Step>

  <Step title="Visit the service worker file directly in your browser">
    Based on your configuration, open the file directly in your browser.

    * If you did not configure a custom location, then you should see the JavaScript code for the service worker file in your site's root: `https://yoursite.com/OneSignalSDKWorker.js`
    * If using WordPress, you should see it here: `https://yoursite.com/wp-content/plugins/onesignal-free-web-push-notifications/sdk_files/OneSignalSDKWorker.js`
    * If using a custom location, you should see it here: `https://yoursite.com/your-custom-location/OneSignalSDKWorker.js`

    <Warning>
      File names are case-sensitive. Make sure you use `OneSignalSDKWorker.js` or the filename you configured.

      Some servers will automatically lowercase the filename. Take this into consideration if you cannot find the file.
    </Warning>
  </Step>

  <Step title="Verify the file loads">
    * You should see the following JavaScript code:
      ```javascript JavaScript theme={null}
      importScripts("https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js");
      ```
    * This file must be served with a `content-type` of `application/javascript`.
    * There can be no redirects to this file. Files must be hosted on the same domain as your site (no CDN or proxy domains)
  </Step>
</Steps>

<Check>
  Review the [Service Worker Setup Guide](./onesignal-service-worker) for more detailed setup instructions.
</Check>

### Notifications not shown

This section assumes:

1. You have reviewed the [Notifications Not Shown: Web Push](./notifications-not-shown-web-push) guide for common reasons why notifications may not be showing up in your device.
2. You were shown the [Native permission prompt](./permission-requests) and clicked "Allow". See [Prompt Display Issues](#prompt-display-issues) above if you did not subscribe via the Native permission prompt.

If the above are true, follow these steps to check your Subscription ID and send yourself a push notification:

<Steps>
  <Step title="Get your Subscription ID">
    Run the following code in the browser developer tools console:

    ```javascript JavaScript theme={null}
      function getUserInfo() {
       console.log('getUserInfo()');
       Promise.all([
          OneSignal.Notifications.isPushSupported(),
        OneSignal.Notifications.permission,
          OneSignal.User.PushSubscription.optedIn,
          OneSignal.User.PushSubscription.id
       ]).then(([
          isPushSupported,
          isSubscribed,
          isOptedIn,
          subscriptionId
        ]) => {
          console.log('The current URL of this page: ', location.href);
          console.log('Push is supported on this browser: ', isPushSupported);
          console.log('You are subscribed to notifications in the browser: ', isSubscribed);
          console.log('You are opted-in with OneSignal: ' , isOptedIn);
          console.log('Your OneSignal Subscription ID: ', subscriptionId);
        }).catch(e => {
          console.error('Error getting user info:', e);
        });
      }
      getUserInfo();
    ```

    This will tell you:

    * The URL of the page you are on if there is any confusion.
    * If the current browser you are using supports push notifications.
      * `true` means the browser supports push notifications.
      * `false` means the browser does not support push notifications.
    * If you are subscribed to notifications in the browser.
      * `true` means you allowed push permissions for this URL.
      * `false` means you did not allow or denied push permissions for this URL.
    * If you are opted-in with OneSignal.
      * `true` means your Subscription is subscribed to push notifications in OneSignal.
      * `false` means your Subscription is not subscribed to push notifications in OneSignal. Check for the [`optOut()` method](./web-sdk-reference) is being called on your site.
    * Your OneSignal Subscription ID.

      * Save this for the next step. This is the ID you will use to send yourself a push notification.

      <Frame caption="Example of user info">
        <img src="https://mintcdn.com/onesignal/6sTkY-dQpGTrB0vT/images/sdk/user-info-example.png?fit=max&auto=format&n=6sTkY-dQpGTrB0vT&q=85&s=eb88becd62fc4da42bb26b2b6b6d61b6" width="1798" height="1054" data-path="images/sdk/user-info-example.png" />
      </Frame>

      <Warning>
        Save this console data to a text file and share with our Support team if you need further assistance.
      </Warning>
  </Step>

  <Step title="Send yourself a notification">
    If you are subscribed to notifications, opted-in with OneSignal, and have a Subscription ID, you can send yourself a notification.

    Follow the steps in the [Find & Set Test Subscriptions](./find-set-test-subscriptions) to set yourself as a tester and send yourself a notification.
  </Step>

  <Step title="Test with Chrome">
    If you are not getting notifications in Chrome, use these Chrome-specific diagnostic tools to identify the issue.

    1. In a new tab, open `chrome://gcm-internals`.
    2. Click the "Start Recording" button on the top left. Making sure you see "Connection State: CONNECTED".
    3. Leave this open and send yourself another push notification to your Chrome web push Subscription.
    4. You should see something in the "Receive Message Log" if you got it.

    <Frame caption="GCM internals logging">
      <img src="https://mintcdn.com/onesignal/6sTkY-dQpGTrB0vT/images/sdk/chrome-gcm-internals-logging.png?fit=max&auto=format&n=6sTkY-dQpGTrB0vT&q=85&s=1cb6d1d8b43673e34e3c8d4989e4e36b" width="2556" height="2228" data-path="images/sdk/chrome-gcm-internals-logging.png" />
    </Frame>

    * If you don't see a "Data msg received", then your Chrome browser is not receiving the notification at all. Please let us know on support about this.
    * If you see "Data msg received" but you still didn't receive a notification, continue to the next step.

    5. Open a new tab to `chrome://serviceworker-internals`
    6. Search for `Scope: https://your-site.com` (replace `your-site.com` with your actual site domain).
    7. Click **Inspect**, or **Start -> Inspect**. A Chrome Developer Tools popup will appear.

    <Frame caption="Inspecting the service worker">
      <img src="https://mintcdn.com/onesignal/6sTkY-dQpGTrB0vT/images/sdk/chrome-serviceworker-internals-inspect.png?fit=max&auto=format&n=6sTkY-dQpGTrB0vT&q=85&s=bb162542bf608c5c85d74aa510eb2593" width="2288" height="1270" data-path="images/sdk/chrome-serviceworker-internals-inspect.png" />
    </Frame>

    8. On the Chrome Developer Tools popup to our service worker, click the **Console** tab, and run `OneSignalWorker.log.trace();`. It should return `undefined`. Any messages from our service worker should now appear in this popup.
  </Step>
</Steps>

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
