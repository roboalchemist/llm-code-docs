# Source: https://documentation.onesignal.com/docs/en/macos-app-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# macOS app setup

> Learn how to integrate OneSignal into your macOS app, whether using Mac Catalyst or direct API access. Step-by-step guidance for configuring platforms and sending push notifications.

## Configure your OneSignal app and platform

To send push notifications on macOS, your OneSignal app must be configured with Apple (APNs).

<Note>
  If your team already has a OneSignal account, [ask to be invited as an admin role](./manage-team-members) so you can configure the app. Otherwise, [sign up for a free account](https://onesignal.com) to get started.
</Note>

### 1. Create or select your app

* Select your app and go to **Settings > Push & In-App**.
* Or create a new app by clicking **New App/Website**.

<Frame caption="Example shows creating a new app.">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/13e619dc5fd638b4d9adf5505ddd645de431dc963dbeeac923462060c030ce7c-Screenshot_2025-04-07_at_3.48.57_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=77c331bb0aea78c3f5d96ed065e14d1f" width="2344" height="1544" data-path="images/docs/13e619dc5fd638b4d9adf5505ddd645de431dc963dbeeac923462060c030ce7c-Screenshot_2025-04-07_at_3.48.57_PM.png" />
</Frame>

### 2. Set up and activate macOS platform

* Choose a recognizable app and organization name.
* Select (More Options) macOS as the platform to activate.
* Click **Next: Configure Your Platform**.

<Frame caption="Example setting up your first OneSignal app, org, and channel.">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/macOS-setup.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=25be1bfb506afd630785c68e6df28066" width="2232" height="1658" data-path="images/dashboard/macOS-setup.png" />
</Frame>

### 3. Configure credentials

Follow the prompts to add either:

* [p8 Auth Key (Recommended)](./ios-p8-token-based-connection-to-apns)
* Or [p12 Certificate](./ios-p12-generate-certificates)

<Frame caption="Example showing the p8 Auth Key configuration page.">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/macOS-configuration.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=2f0dd6fb8f8956df4d8fd3172813e5ed" width="2232" height="1658" data-path="images/dashboard/macOS-configuration.png" />
</Frame>

Click **Save & Continue** after entering your credentials.

### 4. Save your App ID

You’ll be shown your OneSignal App ID — make sure to save it, as you’ll need it during setup.

<Frame caption="Save your App ID for setup.">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/macOS-appid.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=abc964a5bdbee6f40b36d0d181b3fc63" width="2154" height="1304" data-path="images/dashboard/macOS-appid.png" />
</Frame>

***

## Setup

If your macOS app was built with Mac Catalyst, you can integrate our iOS SDK directly. Otherwise, you can leverage our APIs to manage users and notifications.

<Tabs>
  <Tab title="Mac Catalyst">
    If you built your app with Mac Catalyst, you can integrate our [iOS SDK](./ios-sdk-setup) directly.
  </Tab>

  <Tab title="API-only integration">
    If you're not using Mac Catalyst, or need full control, you can integrate via the OneSignal REST API.

    <Steps>
      <Step title="Obtain a macOS push token">
        Follow [Apple's documentation](https://developer.apple.com/notifications/) to implement native push support and retrieve the APNs token from your macOS app.
      </Step>

      <Step title="Register a macOS Subscription with OneSignal">
        Call our [Create user API](/reference/create-user) to set the `subscription` object:

        * `type` of `macOSPush`
        * `token` of the APNs token
        * Include all other user data, especially `external_id` to track the user in OneSignal.
      </Step>

      <Step title="Updating users">
        Use the [Create user](/reference/create-user) or [Update user](/reference/update-user) APIs with the `external_id` to update user and subscription data.
      </Step>
    </Steps>
  </Tab>
</Tabs>

***

<Check>
  macOS setup complete!
  Recommended next steps:

* Understand [Users](./users) and [Subscriptions](./subscriptions)
* [Create message API](/reference/create-message) to send notifications
</Check>

***

Built with [Mintlify](https://mintlify.com).
