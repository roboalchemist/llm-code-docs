# Source: https://documentation.onesignal.com/docs/en/migrating-to-onesignal.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating to OneSignal

> Best practices and technical steps for migrating to OneSignal from providers like Firebase, including SDK integration, phased rollout, user import, and testing guidance.

Welcome to OneSignal! This guide will help you migrate from your current messaging platform to OneSignal with minimal disruption.

It’s designed for:

* **Developers** implementing the OneSignal SDK
* **Marketers** managing campaigns and analytics

***

## Prerequisites

Before you begin:

* Setup an account at [OneSignal](https://onesignal.com)
* [Invite your team](./manage-team-members)

***

## Migration steps

### 1. Audit your current messaging setup

Before migration, take inventory of your current implementation:

**For developers:**

* The platforms you support: iOS, Android, Web, email, SMS, etc.
* The code handling push and in-app message events:
  * Foreground displaying and click handling
  * Deep link usage for push, email, etc.
  * Push token and payload handling
* How you are collecting email addresses, phone numbers, push tokens, etc.
* Email domains and DNS ownership
* SMS senders and opt-in mechanisms

**For marketers:**

* The types of messages you send: (transactional, marketing, etc.)
  * Templates for those messages
* How you are segmenting and targeting users.
* The analytics or conversion metrics you track.

### 2. Core OneSignal concepts

Some core concepts about OneSignal to understand before you begin:

* [Users](./users) - Identified via the External ID. Users are composed of properties (tags, session data, etc.) and subscriptions (push, email, SMS).
* [Subscriptions](./subscriptions) - Refers to how a user can receive messages. There are 4 types of subscriptions:
  * **Mobile**: Can receive push notifications, in-app messages, and Live Activities.
  * **Web push**: Can receive web push notifications.
  * **Email**: Can receive email notifications.
  * **SMS**: Can receive SMS notifications.
* [Segments](./segmentation) - A group of users that share common properties.
* [Tags](./add-user-data-tags) - A custom user property.
* [Custom Events](./custom-events) - An action a user takes.

### 3. Add the OneSignal SDK (developers)

Set up the OneSignal SDK in your mobile app and/or web site:

<Columns cols={2}>
  <Card title="Mobile SDK setup" href="./mobile-sdk-setup" arrow={true}>
    Our mobile SDKs are highly recommended for push and required for in-app messages.
  </Card>

  <Card title="Web SDK setup" href="./web-sdk-setup" arrow={true}>
    Our web SDK is required for web push notifications.
  </Card>
</Columns>

#### Identify users with External ID

The External ID is a unique identifier for a user that you can use to identify them across devices and messaging channels.

Call our SDK's `login` method to set the External ID for a user when they use your app or website.

* [Mobile SDK](./mobile-sdk-reference#login-external-id)
* [Web SDK](./web-sdk-reference#login-external-id)

#### Collect new emails and phone numbers

Email addresses and phone numbers can be added to your OneSignal app in several ways as discussed later in this guide.

If you collect email addresses and/or phone numbers in your mobile app or website directly, you can use our SDK to create these subscriptions:

* Email subscriptions: use the `addEmail` method in our [Mobile SDK](./mobile-sdk-reference#addemail-%2C-removeemail) and [Web SDK](./web-sdk-reference#addemail-%2C-removeemail)
* SMS subscriptions: use the `addSms` method in our [Mobile SDK](./mobile-sdk-reference#addsms-%2C-removesms) and [Web SDK](./web-sdk-reference#addsms-%2C-removesms)

### 4. Remove your legacy implementation

We recommend you remove any native or 3rd party methods and APIs for collecting push tokens, email addresses, and phone numbers. Especially for collecting push tokens, these can create conflicts with the OneSignal SDK.

#### Push token conflicts & format

Remove all legacy code generating push tokens. Only allow OneSignal to generate the push token which happens automatically when the SDK is initialized.

If needed, use our SDK to get the token and send it to your other provider or backend. Methods for doing so:

* Get device's push token identifier using our [Frontend Mobile SDK](./mobile-sdk-reference#user-pushsubscription-token)
* Get device's identifier using our [View user](/reference/view-user) API

OneSignal's push token format:

* **iOS Push APNS token format**: 64 characters, hexadecimal characters only (0-9,a-f). `deviceToken.map {String(format: "%02x", $0)}.joined()`
* **Android Push FCM token format**: Typically 163 characters, alphanumeric characters, may contain hyphens, colons and underscore.

#### Push payload handling

If using OneSignal and another push provider in parallel, you'll need to prevent your other SDK from processing OneSignal notifications to avoid duplicates.

OneSignal's push payload contains a specific `"custom"` key within the `rawPayload` of the [OSNotification object](./osnotification-payload) which our SDK uses to determine whether to handle the notification or not.

You will need to update your [Android NotificationCompat](https://developer.android.com/reference/androidx/core/app/NotificationCompat) to listen for an object on the [OSNotification payload](./osnotification-payload) that is different from your other provider's payload to prevent it from handling notifications sent from us.

#### Phased migration (mobile apps only)

If you must keep both SDKs for a limited time:

* **Do not let multiple SDKs generate push tokens.** Let OneSignal handle it, and share the token with your old system if needed.
  * Use [Frontend SDK](./mobile-sdk-reference#user-pushsubscription-token) or [View user API](/reference/view-user)
* **Update payload filters** so your legacy SDK doesn't process OneSignal pushes.
  * OneSignal uses a `"custom"` key in its `rawPayload` ([docs](./osnotification-payload)).
  * Check this key in `NotificationCompat` (Android).
* Decide which provider handles what types of notifications.
* Set a clear cutoff date and build a phase-out plan for legacy systems.
  * Create a [notification template](./templates) for each type of notification you send.
  * Set up your old provider to send messages to users on the older version of your app and OneSignal to send messages to users on the newer version of your app.
  * Create [segments](./segmentation) to target specific user groups.

### 5. Web push migration

If you're using the same HTTPS site [origin](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), subscribers will be silently added to OneSignal on their next visit. No prompt will be shown, and they can receive push from OneSignal immediately after. They should also stop getting push from the previous provider.

* You cannot import web push subscriptions due to browser security limits. OneSignal will register users when they return.
* You must unregister your old push service workers before OneSignal can take over.

**Steps:**

1. Remove the legacy SDK: Code on website and Service Worker files.
2. Add this code to make sure the Service Worker is unregistered.
3. Replace `sw.js` with the name of the 3rd party Service Worker file.

```js javascript theme={null}
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then(function(registrations) {
    for (let registration of registrations) {
      if (registration.active.scriptURL.includes("sw.js")) {
        registration.unregister();
      }
    }
  });
}
```

#### Migrating between OneSignal apps

If you are moving subscribers from one OneSignal app (App A) to another (App B):

* Web push subscriptions cannot be transferred directly between apps. Each subscription is tied to both your site’s domain (origin) and the OneSignal App ID.

* To migrate, update your site’s OneSignal initialization code to use App B’s appId:

```js  theme={null}
OneSignal.init({
  appId: "YOUR_APP_B_ID",
});
```

* When a user revisits your site, the browser’s existing push permission will allow OneSignal to silently register them in App B.

* No new permission prompt will appear, but users must visit your site at least once for the subscription to be created in App B.

* Subscribers will continue to appear in App A until they become inactive.

<Info> <strong>Best practice:</strong> Stop sending from App A once you confirm enough users have migrated. Monitor subscriber counts in both apps to validate migration progress. </Info>

### 6. Email and SMS setup

If you are sending emails and/or SMS with OneSignal, you will need to follow our [Email setup](./email-setup) and [SMS setup](./sms-setup) guides.

Migrating your current email sending domain to OneSignal simply requires updating the DNS records. You can setup multiple email senders in OneSignal if needed.

Migrating SMS senders may take time. Our team should be in touch with you to help with this process, but if not, you can reach out to `support@onesignal.com` anytime for assistance.

#### Is email warm up required?

If your sending domain has an established sending reputation then warm-up is not required unless you have a dedicated IP address.

#### Can I get a dedicated IP address?

Yes, depending on your plan type and needs, we can provide dedicated IP addresses. Contact your account manager for more details.

### 7. Import existing users (optional)

Importing subscribed users that have been active in your app within the past 270 days will help minimize disruption during migration.

We recommend you start by importing known test users, then import the remaining users before app launch.

#### Platform considerations

* Email addresses must be from active and valid users. Do not import email addresses that have never clicked or opened emails before.
* Phone numbers must be in a specific format and users must have consented to receive SMS.
* iOS subscriptions can start receiving push notifications immediately after import. Features like notification click tracking and confirmed deliveries require our SDK to be active on the device.
* Android/Huawei/Amazon subscriptions must have our SDK active on the device to receive notifications, either through an auto-update or manual update.
* Web subscriptions cannot be imported. If you follow the above in [Web push migration](#5-web-push-migration), the web push subscription will be created and push token fetched via our SDK when the user returns to the site.

#### Import steps

1. Review [Users](./users) and [Subscriptions](./subscriptions) docs for understanding.
2. Export test user data from old system.
3. Format data for OneSignal's [Create user](/reference/create-user) API.
4. Import test users and upon successful testing, keep the process to repeat in pre-release checklist.

**Required fields:**

* `token` - The push token or email address or phone number
* `type` - The type of subscription: `iOSPush`, `AndroidPush`, `WebPush`, `Email`, `SMS`
* `external_id` - A unique identifier for the user. This is recommended to be used for tracking and analytics.

**Example API request:**

```json POST https://api.onesignal.com/users theme={null}
  {
    "identity": {
      "external_id": "user_12345"
    },
    "subscriptions": [
      {
        "type": "iOSPush",
        "token": "7abcd49d0affb7426a8f1202420e8f4e2fc4df58e49501adc383f3bd66df8636"
      },
      {
        "type": "AndroidPush",
        "token": "dQGm89TZQXiTvLsRIj_GBo:APA91bpgqFgqkP2qYvV1uW2kdK5Z3TjgCXB_1jkL6VJrgH3hoYn16MvFY19tzDE4OuSgKjYC7itbFpSJYHBfKLWt-xZYBpgCVhYn9K5neV_9-Zj7s9mOSjRUJ2IwEwVSYhR-j5ICF9WB"
      },
      {
        "type": "Email",
        "email": "test@example.com"
      },
      {
        "type": "SMS",
        "phone_number": "+1234567890"
      }
    ]
  }
```

### 7. Test the migration

Thorough testing is crucial for a smooth transition.

1. Enable [Debug Logging](./capturing-a-debug-log) in the OneSignal SDK.
2. Test on real devices for all platforms (Android, iOS, Web, etc.).
3. Verify both foreground and background notification handling.

**Test scenarios for developers and marketers teams:**

* Send test notifications from OneSignal to imported users **before adding the OneSignal SDK**.
  * You should receive the push on iOS but will not get confirmed delivery or click analytics.
  * You may receive the push on Android if you have another push SDK and did not implement the [Payload handling](#push-payload-handling) requirements yet. The notification is likely missing data and doesn't work as expected when clicked.

* Send test notifications from OneSignal to imported users **after adding the OneSignal SDK**.
  * You should receive the push on both Android and iOS along with confirmed delivery and click analytics.

* Test notification behavior with app in different states.

* Verify deep links and custom actions work correctly.

**If using multiple providers:**

* Send from both your current provider and OneSignal.
* Check for duplicate notifications
* Verify each provider's notifications display correctly
* Test user login/logout scenarios

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

## Pre-release check list

**For marketers:**

* Build a messaging plan to prompt app updates
* Consider using push and in-app messages from your old system to gently remind users to update.

**For developers:**

* Verify that push and in-app message analytics are working as expected.
  * Click events and confirmed delivery are tracked across Android and iOS.
* Verify click events and foreground received events are handled correctly for messages sent from both providers.
* If importing users, export Android and iOS user that have been active in your app within the past 270 days to prevent importing expired tokens. See [FCM Expired Token FAQ](./fcm-expired-token-faq) for details.

***

## Release your app/site

* Most users will have their app's automatically update to the latest version.
* When users open your updated app, they will not be prompted to subscribe to push notifications if permissions were already granted—either through the required permission prompts or the app’s notification settings.

**If you did not import users:**

* Users will be created automatically in OneSignal when they open the updated version of the app. They will not be prompted for push if previously subscribed.
* You will need to wait for them to open the updated app before you can send them messages.
* Continue sending notifications and in-app message from the previous push provider for a couple days until enough users show up in OneSignal. Send additional alerts asking them to update the app to the latest version.

***

## Monitor results

**For developers:**

* Monitor error rates and crashes after deployment.
* Watch for unexpected token invalidations.
* Check SDK integration analytics.

**For marketers:**

* Mark the date of app release.

* Communicate with your developers on:
  * Which migration path was taken (**Clean** or **Phased** migration).
  * Were users imported?

* If following a **Clean** migration:
  * In the previous platform, create a segment or cohort of users that continue to be active. Check their session times, message received, and click events.
  * Only users that have not updated the app should continue to be active and contained in this group.
  * Continue sending push and in-app messages from your previous provider to these users, gently nudging them to update.
  * Stop sending from the previous provider until you are ready to move completely to OneSignal.

* If following a **Phased** migration:
  * In the previous platform, create a segment or cohort of users that have the the older app version before OneSignal.
  * Continue sending push and in-app messages from your previous provider to these older-app users, gently nudging them to update.
  * Stop sending from the previous provider until you are ready to move completely to OneSignal.
  * Remove the previous push provider's code on the next app release.

***

<Check>
  You have successfully migrated to OneSignal!

  For strategy questions about migration planning, our customer success team can provide personalized guidance.
</Check>

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
