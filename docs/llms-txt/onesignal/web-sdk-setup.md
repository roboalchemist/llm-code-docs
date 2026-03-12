# Source: https://documentation.onesignal.com/docs/en/web-sdk-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web SDK setup

> Add OneSignal web push notifications to your website with the JavaScript SDK, service worker setup, and dashboard configuration.

export const SdkReleasesIframe = ({sdkFilter = undefined, viewMode = undefined, height, ...frameProps}) => {
  const baseUrl = 'https://onesignal.github.io/sdk-releases';
  const buildUrl = (theme, sdkFilter, viewMode) => {
    const url = new URL(baseUrl);
    const params = new URLSearchParams();
    if (theme) {
      params.set('theme', theme);
    }
    if (sdkFilter) {
      params.set('sdk', sdkFilter);
    }
    if (viewMode) {
      params.set('viewMode', viewMode);
    }
    if (params.toString()) {
      url.search = params.toString();
    }
    return url.toString();
  };
  const detectTheme = () => {
    if (document.documentElement.classList.contains('dark')) {
      return 'dark';
    }
    return 'light';
  };
  const [theme, setTheme] = useState('light');
  const [iframeSrc, setIframeSrc] = useState(() => {
    const initialTheme = detectTheme();
    return buildUrl(initialTheme, sdkFilter, viewMode);
  });
  useEffect(() => {
    const currentTheme = detectTheme();
    setTheme(currentTheme);
    setIframeSrc(buildUrl(currentTheme, sdkFilter, viewMode));
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const handleThemeChange = () => {
      const newTheme = detectTheme();
      setTheme(newTheme);
      setIframeSrc(buildUrl(newTheme, sdkFilter, viewMode));
    };
    if (mediaQuery.addEventListener) {
      mediaQuery.addEventListener('change', handleThemeChange);
    } else {
      mediaQuery.addListener(handleThemeChange);
    }
    window.addEventListener('storage', handleThemeChange);
    const observer = new MutationObserver(handleThemeChange);
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class', 'data-theme']
    });
    return () => {
      if (mediaQuery.removeEventListener) {
        mediaQuery.removeEventListener('change', handleThemeChange);
      } else {
        mediaQuery.removeListener(handleThemeChange);
      }
      window.removeEventListener('storage', handleThemeChange);
      observer.disconnect();
    };
  }, [sdkFilter, viewMode]);
  const getIframeHeight = () => {
    if (viewMode === 'table') {
      return '450';
    }
    if (viewMode === 'mini') {
      return '170';
    }
    return '800';
  };
  const iframeHeight = height || getIframeHeight();
  return <Frame {...frameProps}>
      <iframe src={iframeSrc} width="100%" height={iframeHeight} frameBorder="0" style={{
    border: "none"
  }} title="SDK Releases" key={iframeSrc} />
    </Frame>;
};

<SdkReleasesIframe sdkFilter="react,vue,vue3,angular,wordpress" viewMode="table" height="380" />

## Overview

This guide walks you through adding OneSignal web push notifications to your site — from dashboard configuration to SDK installation. OneSignal supports Chrome, Firefox, Edge, Safari, and [other major browsers](./web-push-setup-faq).

***

## Requirements

* HTTPS website: Web push does not work on HTTP or in incognito/private modes.
* Server access: You’ll need to upload a service worker file to your site.
* Single origin: Web push follows the [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy). If you have multiple origins (domains/subdomains), you will need multiple OneSignal apps (one per origin). To comply with this browser limitation, you can either:
  * Redirect traffic to a single origin for subscriptions.
  * Create multiple OneSignal apps—one per origin.

<Note>
  If your team already created an account with OneSignal, [ask to be invited as an admin role](./manage-team-members) so you can set up the app. Otherwise, sign up for a free account at [onesignal.com](https://onesignal.com) to get started.
</Note>

***

## Configure your OneSignal app and platform

In the OneSignal dashboard:

* Go to **Settings > Push & In-App > Web**.

<Frame caption="Activate the web platform in your OneSignal settings">
  <img src="https://mintcdn.com/onesignal/KPVdijCt4_xCbkO8/images/dashboard/web-push-platform-activation.png?fit=max&auto=format&n=KPVdijCt4_xCbkO8&q=85&s=beba7df5d3a4ad5545311951da0f03d2" alt="OneSignal dashboard Settings page showing Web platform activation" width="1188" height="597" data-path="images/dashboard/web-push-platform-activation.png" />
</Frame>

Select integration type:

<Columns cols={3}>
  <Card title="Typical Site (recommended)">
    Manage prompts and settings directly through the OneSignal dashboard without additional coding.
  </Card>

  <Card title="WordPress" href="./wordpress" arrow={true}>
    Required if using WordPress with our official plugin.
  </Card>

  <Card title="Custom Code" href="./web-push-custom-code-setup" arrow={true}>
    For developers who need full control over prompts and SDK configuration.
  </Card>
</Columns>

### Site setup

Add the site details:

* **Site Name**: The name of your site and default notification title.
* **Site URL**: The URL of your site. See [Site URL](#site-url) for more details.
* **Auto Resubscribe**: Enable this to automatically resubscribe users who clear their browser data when they return to your site (no new permission prompt required).
* **Default Icon URL**: Upload a square 256x256px PNG or JPG image that appears in notifications and prompts. If not set, a bell icon is used as the default.

<Frame caption="Web settings in the OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1c14649d87698eba5cb74297a64064c9754ccb64e6335466e5a160edf9f4c009-Screenshot_2024-10-25_at_1.35.23_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=b34a1a59e462eba01c13fbf24327b4da" alt="OneSignal web push configuration showing site name, URL, and icon settings" width="2072" height="712" data-path="images/docs/1c14649d87698eba5cb74297a64064c9754ccb64e6335466e5a160edf9f4c009-Screenshot_2024-10-25_at_1.35.23_PM.png" />
</Frame>

#### Site URL

Enter the exact [origin](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) of your site, e.g., `https://yourdomain.com`. Avoid using `www.` if your site isn’t configured that way.

If you have multiple origins:

* Redirect to a single origin.
* Or set up one OneSignal app per origin.

#### Local testing

The web SDK can be tested on localhost environments. If you are testing on localhost, use a separate OneSignal app from your production app.

<Accordion title="Localhost configuration" icon="circle-chevron-down">
  Set the **SITE URL** to exactly match your localhost environment URL. The URL must match one of these common localhost formats:

* `http://localhost`
* `https://localhost:3000`
* `http://127.0.0.1`
* `https://127.0.0.1:5000`

  <Note>
    If your localhost is using HTTP, select **Treat HTTP localhost as HTTPS for testing**.

    Google Chrome treats `http://localhost` and `http://127.0.0.1` as secure origins, allowing HTTPS integrations even on HTTP. This is why you cannot test other non-standard origins on HTTPS localhost.
  </Note>

  <Frame caption="Local testing in the OneSignal dashboard">
    <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b7f98cead1dcfb39b8887e66f61bb58649891b3cbfb5a051897391e5d324dc56-Screenshot_2024-10-25_at_1.53.11_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=c46d81db4be53243526d961eba527b9c" alt="OneSignal localhost configuration with Treat HTTP localhost as HTTPS option" width="2072" height="712" data-path="images/docs/b7f98cead1dcfb39b8887e66f61bb58649891b3cbfb5a051897391e5d324dc56-Screenshot_2024-10-25_at_1.53.11_PM.png" />
  </Frame>

#### Add `allowLocalhostAsSecureOrigin` to your OneSignal `init` options

  When initializing OneSignal on your localhost site, add `allowLocalhostAsSecureOrigin: true,` to your OneSignal `init` options.

  Additionally, if you're testing localhost on HTTPS with a self-signed certificate, you may have to ask Chrome to ignore invalid certificates for testing with: `--allow-insecure-localhost`. Firefox and Safari provide built-in mechanisms to add exceptions for security certificates.

  ```html  theme={null}
    <script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>
    <script>
      window.OneSignalDeferred = window.OneSignalDeferred || [];
      OneSignalDeferred.push(function(OneSignal) {
        OneSignal.init({
          appId: "YOUR_OS_APP_ID",
          allowLocalhostAsSecureOrigin: true,
        });
      });
    </script>
  ```

</Accordion>

### Permissions prompt

Typical site setup allows you or your team members to add, remove, and update permission prompts through the OneSignal dashboard anytime.

<Card title="Web permission prompts" icon="bell" href="./permission-requests" arrow={true}>
  Configure when and how the browser permission dialog appears to your users.
</Card>

### Welcome notification (optional)

You can also set a welcome notification to be sent to users when they subscribe to push notifications.

### Advanced settings

The following features are configurable in the OneSignal dashboard.

#### Webhooks

The web SDK can `POST` certain web push events to a URL of your choosing.

Web Push Webhooks are a separate implementation from [Event Webhooks](./event-streams) and cannot be used interchangeably.

<Card title="Web push webhooks" icon="webhook" href="./webhooks">
  Send web push events to your server via POST requests.
</Card>

#### Service workers

On the next page of web push configuration, you will be provided the `OneSignalSDKWorker.js` service worker file.

The web SDK looks for this file in the root of your site by default. You can change the file location, name, and scope in the settings below.

* **Path to service worker files** is the path to the directory where you will host the service worker file.
* **Main and Updater service worker filenames** defaults to `OneSignalSDKWorker.js`. You can rename this file, but it must use a `.js` extension.
* **Service worker registration scope** controls which pages the service worker can operate on. For push notifications this has no effect. Set it to the same path as your service worker file location.

<Frame caption="Service worker configuration">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/862419b594a5a0f7f77b8ed4199cae82d6db5d4d421024f6b553ca5b30e3ea00-Screenshot_2024-10-25_at_2.44.04_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=13f219cd99022bdea5ecbdd2fb6a8f1c" alt="Service worker path, filename, and scope configuration fields" width="1214" height="566" data-path="images/docs/862419b594a5a0f7f77b8ed4199cae82d6db5d4d421024f6b553ca5b30e3ea00-Screenshot_2024-10-25_at_2.44.04_PM.png" />
</Frame>

With this example, you should see the file's code publicly accessible at `https://yourdomain.com/push/onesignal/OneSignalSDKWorker.js`

<Card title="OneSignal service worker" icon="gear" href="./onesignal-service-worker">
  Advanced service worker configuration, custom integration, and migration from other providers.
</Card>

#### Click behavior

Control how users navigate to the [URL](./links) you set when they click the notification.

If the user does not have your site open in any tab, the browser opens a new tab and navigates to the notification URL. If the user already has your site open, the behavior depends on the setting you choose:

| Setting                      | Matches on                             | Action                                                |
| ---------------------------- | -------------------------------------- | ----------------------------------------------------- |
| **Exact Navigate** (default) | Exact URL (e.g. `example.com/product`) | Navigates to the notification URL in the matching tab |
| **Origin Navigate**          | Origin (e.g. `example.com`)            | Navigates to the notification URL in the matching tab |
| **Exact Focus**              | Exact URL                              | Focuses the matching tab without refreshing           |
| **Origin Focus**             | Origin                                 | Focuses the matching tab without refreshing           |

#### Persistence

By default, web push notifications appear on the device for roughly 5 seconds before moving to the Notification Center, where they remain for about 1 week before the operating system removes them.

Some devices and versions of Chrome and Edge allow you to persist notifications on screen until the user interacts with them. **This can annoy users and is not recommended.** Enabling persistence may also reduce character count and affect how images and buttons display.

Changes to persistence settings only take effect for subscribers who visit your site after the update. If you do not see the change, wait for subscribers to revisit your site or ask them to clear their browser data.

#### Safari certificate (Optional)

OneSignal automatically provides the necessary certificates to work with Safari browsers at no additional cost. If you already have your own Safari Web Push Certificates, toggle on this option to upload your `Safari Web .p12 Push Certificate` and password.

<Frame caption="Safari certificate configuration">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a515412b69ecdd249c610e4e833cf3f1169b70b7a25075f5311c27bcc9b8ed10-Screenshot_2024-10-25_at_2.59.27_PM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=2dc2354ec6ec21a71f090cd63e5a149d" alt="Safari Web Push certificate upload toggle and fields" width="1208" height="406" data-path="images/docs/a515412b69ecdd249c610e4e833cf3f1169b70b7a25075f5311c27bcc9b8ed10-Screenshot_2024-10-25_at_2.59.27_PM.png" />
</Frame>

***

## Upload service worker file

Add the `OneSignalSDKWorker.js` service worker file to your site.

Download it from the OneSignal dashboard or [from GitHub](https://github.com/OneSignal/OneSignal-Website-SDK/files/11480764/OneSignalSDK-v16-ServiceWorker.zip).

<Frame caption="Upload service worker file step">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/30d6d942cb4f6be59443b121ea226f50196995e56cb9e16586031475de66d15f-Screenshot_2024-10-25_at_3.54.04_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=f94e408fb2ecbfd3ecefda65e9839dd3" alt="OneSignal service worker file download and setup step" width="1742" height="416" data-path="images/docs/30d6d942cb4f6be59443b121ea226f50196995e56cb9e16586031475de66d15f-Screenshot_2024-10-25_at_3.54.04_PM.png" />
</Frame>

Either put this file in your site's root directory or in a subdirectory. If you put it in a subdirectory, you will need to set the **Path to service worker files** in the [Advanced settings > Service workers](#service-workers) section.

Once the file is on your server, check the following to make sure it works:

<Steps>
  <Step title="Verify the location">
    Make sure the file is located in the same **Path to service worker files** as set in [Advanced settings > Service workers](#service-workers). If you did not update these settings, then you should have put the file in your root. For example:

    * `https://yourdomain.com/OneSignalSDKWorker.js`
    * `https://yourdomain.com/some-subdirectory/OneSignalSDKWorker.js`
  </Step>

  <Step title="It must be publicly accessible on your origin">
    The `OneSignalSDKWorker.js` file must be publicly accessible and available on your origin. It cannot be hosted via a CDN or placed on a different origin with redirect.

    When you visit the URL to the file, you should see the code.
  </Step>

  <Step title="It must be served with a content-type: application/javascript">
    This is a JavaScript file and must be served as such. It cannot have a content-type of text/html.
  </Step>
</Steps>

<Card title="OneSignal service worker" icon="gear" href="./onesignal-service-worker" arrow={true}>
  Advanced configuration and migration from other web push providers.
</Card>

## Add code to your site

The JavaScript SDK code below works on any site. If your site is built with [Angular](./angular-setup), [React JS](./react-js-setup), or [Vue JS](./vue-js-setup) then follow these links.

To initialize OneSignal on your site with our JavaScript SDK, copy/paste the provided code into your website's `<head>` tags. The OneSignal dashboard provides this same snippet pre-filled with your [app ID](./keys-and-ids).

```javascript  theme={null}
  <script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>
  <script>
    window.OneSignalDeferred = window.OneSignalDeferred || [];
    OneSignalDeferred.push(async function(OneSignal) {
      await OneSignal.init({
        appId: "YOUR_ONESIGNAL_APP_ID",
      });
    });
  </script>
```

### iOS web push support

Apple started supporting web push notifications on iPhones and iPads running iOS 16.4+. Unlike Android devices where web push just "works" as long as visited on a supported browser, Apple added a few more requirements such as a `manifest.json` file and a user action to add your site to their home screen.

<Card title="iOS web push setup" icon="apple" href="./web-push-for-ios">
  Add the required `manifest.json` file and guide users to add your site to their home screen.
</Card>

***

## Testing the OneSignal SDK integration

This guide helps you verify that your OneSignal SDK integration is working correctly by testing push notifications and subscription registration.

### Check web push subscriptions

<Steps>
  <Step title="Launch your site on a test device.">
    * Use Chrome, Firefox, Edge, or Safari while testing.
    * **Do not use Incognito or private browsing mode.** Users cannot subscribe to push notifications in these modes.
    * The prompts should appear based on your [permission prompts](/docs/en/permission-requests) configuration.
    * Click **Allow** on the native prompt to subscribe to push notifications.

    <Frame caption="Web push native permission prompt">
      <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/push/web-push-native-permission-prompt.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=91c15dd6677de6a0ba37da20449ccca1" alt="Browser native permission prompt asking the user to allow or block notifications" width="1724" height="974" data-path="images/push/web-push-native-permission-prompt.png" />
    </Frame>
  </Step>

  <Step title="Check your OneSignal dashboard">
    * Go to **Audience > Subscriptions**.
    * You should see a new entry with the status **Subscribed**.

    <Frame caption="Dashboard showing subscription with 'Subscribed' status">
      <img src="https://mintcdn.com/onesignal/KPVdijCt4_xCbkO8/images/dashboard/web-push-subscription-status.png?fit=max&auto=format&n=KPVdijCt4_xCbkO8&q=85&s=786e9c5e4131f01fef20d11bebd1a3d0" alt="OneSignal dashboard Subscriptions page showing a web push subscription with Subscribed status" width="1188" height="742" data-path="images/dashboard/web-push-subscription-status.png" />
    </Frame>

    <Check>You have successfully created a [web push subscription](/docs/en/subscriptions).
    Web push subscriptions are created when users first subscribe to push notifications on your site.</Check>
  </Step>
</Steps>

### Set up test subscriptions

Test subscriptions are helpful for testing a push notification before sending a message.

<Steps>
  <Step title="Add to Test Subscriptions.">
    In the dashboard, next to the subscription, click the **Options (three dots)** button and select **Add to Test Subscriptions**.

    <Frame caption="Adding a device to Test Subscriptions">
      <img src="https://mintcdn.com/onesignal/NCUI56Tiw7V-s0dT/images/dashboard/add-to-test-subscriptions.png?fit=max&auto=format&n=NCUI56Tiw7V-s0dT&q=85&s=2455d4cd74ea4ad686f76730cd95bbaa" alt="Options menu on a subscription showing the Add to Test Subscriptions option" width="1188" height="742" data-path="images/dashboard/add-to-test-subscriptions.png" />
    </Frame>
  </Step>

  <Step title="Name your subscription.">
    Name the subscription so you can easily identify your device later in the **Test Subscriptions tab**.
  </Step>

  <Step title="Create a test users segment.">
    Go to **Audience > Segments > New Segment**.
  </Step>

  <Step title="Name the segment.">
    Name the segment `Test Users` (the name is important because it will be used later).
  </Step>

  <Step title="Add the Test Users filter and click Create Segment.">
    <Frame caption="Creating a 'Test Users' segment with the Test Users filter">
      <img src="https://mintcdn.com/onesignal/NCUI56Tiw7V-s0dT/images/dashboard/create-test-users-segment.png?fit=max&auto=format&n=NCUI56Tiw7V-s0dT&q=85&s=91b8a021be6e83662854e68ec3e1da04" alt="Segment editor with Test Users filter selected and the segment named Test Users" width="1188" height="742" data-path="images/dashboard/create-test-users-segment.png" />
    </Frame>

    <Check>You have successfully created a segment of test users.
    You can now test sending messages to this individual device and groups of test users.</Check>
  </Step>
</Steps>

### Send test push via API

<Steps>
  <Step title="Get your App API Key and App ID.">
    In your OneSignal dashboard, go to **Settings > [Keys & IDs](/docs/en/keys-and-ids)**.
  </Step>

  <Step title="Update the provided code.">
    Replace `YOUR_APP_API_KEY` and `YOUR_APP_ID` in the code below with your actual keys. This code uses the `Test Users` segment created earlier.

    ```curl  theme={null}
    curl -X POST --url 'https://api.onesignal.com/notifications' \
      --header 'content-type: application/json; charset=utf-8' \
      --header 'authorization: Key YOUR_APP_API_KEY' \
      --data '{
        "app_id": "YOUR_APP_ID",
        "target_channel": "push",
        "name": "Testing basic setup",
        "headings": {
          "en": "👋"
        },
        "contents": {
          "en": "Hello world!"
        },
        "included_segments": [
          "Test Users"
        ],
        "chrome_web_image": "https://avatars.githubusercontent.com/u/11823027?s=200&v=4"
      }'
    ```
  </Step>

  <Step title="Run the code.">
    Run the code in your terminal.
  </Step>

  <Step title="Check images and confirmed delivery.">
    If all setup steps were completed successfully, the test subscriptions should receive a notification.

    <Warning>Only Chrome supports images. Images will appear small in the collapsed notification view. Expand the notification to see the full image.</Warning>

    <Frame caption="Expanded push notification with image on Chrome macOS">
      <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/push/web-push-image.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=8dd90279daff9e24d3fd281e73aa1e74" alt="Expanded Chrome push notification on macOS displaying a custom image" width="740" height="896" data-path="images/push/web-push-image.png" />
    </Frame>
  </Step>

  <Step title="Check for confirmed delivery.">
    In your dashboard, go to **Delivery > Sent Messages**, then click the message to view stats. You should see the **confirmed** stat, meaning the device received the push.

    <Note>Safari does not support Confirmed Delivery.</Note>

    <Card title="Push notification message reports" icon="chart-bar" href="/docs/en/push-notification-message-reports">
      View delivery, click, and conversion stats for your push notifications.
    </Card>
  </Step>
</Steps>

<Check>You have successfully sent a notification via the API to a segment.</Check>

If notifications are not arriving, contact `support@onesignal.com` with the following:

* The API request and response (copy-paste into a `.txt` file)
* Your Subscription ID
* Your website URL with the OneSignal code

***

## User identification

The previous section covered creating web push [Subscriptions](/docs/en/subscriptions). This section expands to identifying [Users](/docs/en/users) across all their subscriptions (including push, email, and SMS) using the OneSignal SDK. It covers External IDs, tags, multi-channel subscriptions, privacy, and event tracking to help you unify and engage users across platforms.

### Assign External ID

Use an External ID to identify users consistently across devices, email addresses, and phone numbers using your backend's user identifier. This ensures your messaging stays unified across channels and 3rd party systems (especially important for [Integrations](/docs/en/integrations)).

Set the External ID with the SDK's [`login` method](/docs/en/web-sdk-reference#login-external-id) each time a user is identified by your app.

<Note>
  OneSignal generates unique read-only IDs for subscriptions (Subscription ID) and users (OneSignal ID).

  As users download your app on different devices, subscribe to your website, and/or provide you email addresses and phone numbers outside of your app, new subscriptions will be created.

  Setting the External ID via the SDK is highly recommended to identify users across all their subscriptions, regardless of how they are created.
</Note>

### Add data tags

[Tags](/docs/en/add-user-data-tags) are key-value pairs of string data you can use to store user properties (like `username`, `role`, or preferences) and events (like `purchase_date`, `game_level`, or user interactions). Tags power advanced [Message Personalization](/docs/en/message-personalization) and [Segmentation](/docs/en/segmentation) allowing for more advanced use cases.

Set tags with the SDK's [`addTag` and `addTags` methods](/docs/en/web-sdk-reference#addtag-%2C-addtags) as events occur in your app.

In this example, the user reached level 6 identifiable by the tag called `current_level` set to a value of `6`.

<Frame caption="A user profile in OneSignal with a tag called &#x22;current_level&#x22; set to &#x22;6&#x22;">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d4674261847231079fecc176ba88065409c90943e3854b9df200457325a0aed4-Screenshot_2025-03-18_at_14.47.25.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=91083bf83a4c03ea40d485b23f072259" alt="OneSignal user profile showing a data tag named current_level with value 6" width="1380" height="941" data-path="images/docs/d4674261847231079fecc176ba88065409c90943e3854b9df200457325a0aed4-Screenshot_2025-03-18_at_14.47.25.png" />
</Frame>

You can create a segment of users with a level between 5 and 10, then use that segment to send targeted and personalized messages:

<Frame caption="Segment editor showing a segment targeting users with a current_level value of greater than 4 and less than 10">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/300d36b632a6f6d7017780457bbe2610b71767fd0db093c7611e59714dcbda5b-Screenshot_2025-03-18_at_14.49.56.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=b84ab0d2c6eedbd6d4e7a2bf15afe103" alt="Segment editor filtering users where current_level is greater than 4 and less than 10" width="1380" height="941" data-path="images/docs/300d36b632a6f6d7017780457bbe2610b71767fd0db093c7611e59714dcbda5b-Screenshot_2025-03-18_at_14.49.56.png" />
</Frame>

<Frame caption="Push notification targeting the Level 5-10 segment with a personalized message">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/97e09b42d25c6d3f4c7cb0a6fff4dfb8893cbb4b283f7ff1f77977c33113319c-Screenshot_2025-03-18_at_14.55.47.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=c7839b12057d65a12a4eaddce6e2c11f" alt="Push notification composer targeting the Level 5-10 segment with a personalized message" width="2764" height="2286" data-path="images/docs/97e09b42d25c6d3f4c7cb0a6fff4dfb8893cbb4b283f7ff1f77977c33113319c-Screenshot_2025-03-18_at_14.55.47.png" />
</Frame>

### Add email and/or SMS subscriptions

The OneSignal SDK creates web push subscriptions automatically when users opt in. You can also reach users through email and SMS channels by creating the corresponding subscriptions.

* Use the [`addEmail` method](/docs/en/web-sdk-reference#addemail-%2C-removeemail) to create email subscriptions.
* Use the [`addSms` method](/docs/en/web-sdk-reference#addsms-%2C-removesms) to create SMS subscriptions.

If the email address or phone number already exists in the OneSignal app, the SDK adds it to the existing user. It does not create duplicates.

You can view unified users via **Audience > Users** in the dashboard or with the [View user API](/reference/view-user).

<Frame caption="A user profile with push, email, and SMS subscriptions unified by External ID">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b1cf9999d41da6e4ce333e1126612529b85eac47447bb0b434418d082f595acd-Screenshot_2025-03-18_at_14.43.46.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=7c3885b66e44e097fa0ed7c47f27c911" alt="OneSignal user profile showing push, email, and SMS subscriptions linked by External ID" width="1506" height="848" data-path="images/docs/b1cf9999d41da6e4ce333e1126612529b85eac47447bb0b434418d082f595acd-Screenshot_2025-03-18_at_14.43.46.png" />
</Frame>

<Note>
  Best practices for multi-channel communication

* Obtain explicit consent before adding email or SMS subscriptions.
* Explain the benefits of each communication channel to users.
* Provide channel preferences so users can select which channels they prefer.
</Note>

***

### Privacy & user consent

To control when OneSignal collects user data, use the SDK's consent gating methods:

* [`setConsentRequired(true)`](/docs/en/web-sdk-reference#setconsentrequired): Prevents data collection until consent is given.
* [`setConsentGiven(true)`](/docs/en/web-sdk-reference#setconsentgiven): Enables data collection once consent is granted.

For more on privacy and security:

<Columns cols={2}>
  <Card title="Data collected by the SDK" icon="database" href="/docs/en/data-collected-by-the-onesignal-sdk">
    Review what data the OneSignal SDK collects from users.
  </Card>

  <Card title="Handling personal data" icon="shield-halved" href="/docs/en/handling-personal-data">
    Manage and protect user data in compliance with privacy regulations.
  </Card>
</Columns>

***

## Listen to push, user, and in-app events

Use SDK listeners to react to user actions and state changes.

The SDK provides several event listeners you can hook into. See the [SDK reference guide](/docs/en/web-sdk-reference) for more details.

### Push notification events

* [Click event listener](/docs/en/web-sdk-reference#click): Detect when a notification is tapped.
* [Foreground lifecycle listener](/docs/en/web-sdk-reference#foregroundwilldisplay): Control how notifications behave in foreground.

### User state changes

* [User state change event listener](/docs/en/web-sdk-reference#addeventlistener-user-state): Detect when the External ID is set.
* [Permission observer](/docs/en/web-sdk-reference#permissionchange): Track the user's specific interaction with the native push permission prompt.
* [Push subscription change observer](/docs/en/web-sdk-reference#addeventlistener-push-subscription-changes): Track when the push subscription status changes.

***

## Advanced setup & capabilities

Explore more capabilities to enhance your integration:

<Columns cols={3}>
  <Card title="Migrating to OneSignal" icon="rotate" href="/docs/en/migrating-to-onesignal">
    Move from another push provider to OneSignal.
  </Card>

  <Card title="Integrations" icon="plug" href="/docs/en/integrations">
    Connect OneSignal with third-party tools and platforms.
  </Card>

  <Card title="Action buttons" icon="bell" href="/docs/en/action-buttons">
    Add interactive buttons to push notifications.
  </Card>

  <Card title="Multi-language messaging" icon="globe" href="/docs/en/multi-language-messaging">
    Send localized messages to users in their preferred language.
  </Card>

  <Card title="Identity Verification" icon="shield-check" href="/docs/en/identity-verification">
    Secure your SDK integration with server-side identity verification.
  </Card>

  <Card title="Custom Outcomes" icon="chart-line" href="/docs/en/custom-outcomes">
    Track custom conversion events tied to your messages.
  </Card>
</Columns>

### Web SDK setup & reference

<Columns cols={2}>
  <Card title="Web push setup" icon="gear" href="/docs/en/web-push-setup">
    Enable all key web push features for your integration.
  </Card>

  <Card title="Web SDK reference" icon="code" href="/docs/en/web-sdk-reference">
    Full details on available methods and configuration options.
  </Card>
</Columns>

<Check>Congratulations! You've successfully completed the Web SDK setup guide.</Check>

***

***

## FAQ

### Does web push work on HTTP sites?

No. Web push requires HTTPS. Browsers enforce this as a security requirement. The only exception is `localhost` and `127.0.0.1`, which browsers treat as secure origins for development purposes.

### Why do I need a service worker file?

The service worker runs in the background and handles incoming push notifications even when the user does not have your site open. Without it, the browser cannot display notifications. The `OneSignalSDKWorker.js` file must be publicly accessible on your origin.

### Can I use web push on iOS (iPhone/iPad)?

Yes, starting with iOS 16.4+. However, Apple requires a `manifest.json` file and the user must add your site to their home screen first. See [iOS web push setup](./web-push-for-ios) for the full requirements.

### Why are my notifications not showing?

Common causes include an incorrectly placed service worker file, a mismatched Site URL in the dashboard, or the user having notifications blocked in their browser settings. See [Notifications not shown or delayed](./notifications-show-successful-but-are-not-being-shown) for a full troubleshooting checklist.

***

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
