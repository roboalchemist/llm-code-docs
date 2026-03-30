# Source: https://documentation.onesignal.com/docs/en/vue-js-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Vue JS Web SDK setup

> Integrate OneSignal Web Push Notifications into your Vue.js application using either the onesignal-vue or @onesignal/onesignal-vue3 plugin. Learn how to install, configure, and customize service workers for seamless push delivery.

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

<SdkReleasesIframe sdkFilter="vue" viewMode="mini" />

## Overview

This guide explains how to integrate OneSignal push notifications into a Vue.js application. It covers both Vue 2 and Vue 3 using the official OneSignal Vue plugins, along with key setup considerations including service worker configuration and TypeScript support.

***

## Requirements

* Configured OneSignal app and platform. See [Web Push Setup](./web-push-setup) to get started.

### Vue Compatibility

Make sure you install a plugin version compatible with your Vue environment.

| Vue | OneSignal Plugin                                              |
| --- | ------------------------------------------------------------- |
| 2   | [onesignal-vue](https://github.com/OneSignal/onesignal-vue)   |
| 3   | [onesignal-vue3](https://github.com/OneSignal/onesignal-vue3) |

***

## Installation

Install via your preferred package manager:

<CodeGroup>
  ```bash yarn theme={null}
  yarn add onesignal-vue
  # or yarn add @onesignal/onesignal-vue3
  ```

  ```bash npm theme={null}
  npm install --save onesignal-vue
  # or npm install --save @onesignal/onesignal-vue3
  ```

</CodeGroup>

***

## Initialization

Import the OneSignal service and initialize it in your root component. The `init` function returns a promise that resolves when OneSignal is loaded.

Replace `YOUR_APP_ID` with your OneSignal app ID found in [Keys & IDs](./keys-and-ids).

<CodeGroup>
  ```javascript Vue2 theme={null}
  import Vue from 'vue'
  import OneSignalVue from 'onesignal-vue'

  Vue.use(OneSignalVue);

  new Vue({
    render: h => h(App),
    beforeMount() {
      this.$OneSignal.init({ appId: 'YOUR_APP_ID' });
    }
  }).$mount('#app')
  //Example 1
  await this.$OneSignal.init({ appId: 'YOUR_APP_ID' });
  // do other stuff

  //Example 2
  this.$OneSignal.init({ appId: 'YOUR_APP_ID' }).then(() => {
    // do other stuff
  });

  ```

  ```javascript Vue3 theme={null}
  /*
  In Vue 3, you can pass in the OneSignal initialization options directly as an argument to the `use` function. You can still initialize separately if you prefer editor benefits like code completion.
  */
  import { createApp } from 'vue'
  import OneSignalVuePlugin from '@onesignal/onesignal-vue3'

  createApp(App).use(OneSignalVuePlugin, {
    appId: 'YOUR_APP_ID',
  }).mount('#app');

  // OR

  import { createApp } from 'vue'
  import OneSignalVuePlugin from '@onesignal/onesignal-vue3'

  createApp(App).use(OneSignalVuePlugin).mount('#app');

  // component
  this.$OneSignal.init({
    appId: "YOUR_APP_ID"
  });
  ```

</CodeGroup>

The OneSignal plugin automatically exposes a `$OneSignal` global property accessible inside the application.

### Composition API

You can also leverage Vue's [Composition API](https://vuejs.org/guide/extras/composition-api-faq.html) via the `useOneSignal()` hook that can be called from within [`setup`](https://vuejs.org/api/composition-api-setup.html#basic-usage).

### Customizing init options

You can customize your initialization with additional [`init` parameters](./web-sdk-reference#init).

### Service Worker Settings

If you haven't done so already, you will need to [download the OneSignal Service Worker file](https://github.com/OneSignal/OneSignal-Website-SDK/files/11480764/OneSignalSDK-v16-ServiceWorker.zip) to add to your site.

The `OneSignalSDKWorker.js` file must be publicly accessible. You can put it in your `public` directory, top-level root, or a subdirectory. However, if you are placing the file in a subdirectory and/or have another service worker for your site, then make sure to specify the path. See [OneSignal Service Worker](./onesignal-service-worker) for details.

| Option               | Description                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `serviceWorkerParam` | Scope controlled by the OneSignal worker. **Recommendation:** Use a custom sub-path (e.g., `"/onesignal/"`).                |
| `serviceWorkerPath`  | Path to your hosted OneSignal service worker file (e.g., `"onesignal/OneSignalSDKWorker.js"`). Must be publicly accessible. |

**Example:**

```javascript  theme={null}
this.$OneSignal.init({
  appId: 'YOUR-ONESIGNAL-APP-ID',
  serviceWorkerParam: {
    scope: '/onesignal/'
  },
  serviceWorkerPath: 'onesignal/OneSignalSDKWorker.js'
});
```

#### Hosting the worker

* Public root (default): `/OneSignalSDKWorker.js`
* Custom folder (recommended): e.g., `/onesignal/OneSignalSDKWorker.js` as set in the previous step.

#### Verify service worker hosting

Visit the path in your browser to confirm it's accessible.

If you used root:

```
https://your-site.com/OneSignalSDKWorker.js
```

If using the example path:

```
https://your-site.com/onesignal/OneSignalSDKWorker.js
```

It should return valid JavaScript.

### Important notes

* Avoid Duplicate Initialization in Development
  * When testing in a development environment, you might see the OneSignal SDK initialize twice, which can cause console errors.
  * This happens due to `<React.StrictMode>` causing effects to run twice in development. To resolve it, remove `<React.StrictMode>` from your root component during development.

<Warning>
  Strict mode only affects development—it does not impact production builds.
</Warning>

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

Built with [Mintlify](https://mintlify.com).
