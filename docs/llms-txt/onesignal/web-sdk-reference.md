# Source: https://documentation.onesignal.com/docs/en/web-sdk-reference.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web SDK reference

> Complete API reference for OneSignal Web SDK v16 with initialization, user management, push notifications, slidedown prompts, and debugging methods. Learn how to implement web push notifications, manage user subscriptions, and integrate email/SMS features.

## Setup & debugging

You may notice the need to wrap your OneSignal calls with `OneSignalDeferred.push(async function() { ... })`

You can add as many methods into the `function()` as desired.

The OneSignal SDK is loaded with the `defer` attribute on your page. For example:

`<script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>`

This means the OneSignal code will execute after the HTML document has been fully parsed, preventing any blocking of the site by the OneSignal SDK. However, this presents a problem for page scripts that depend on the `OneSignalDeferred` variable existing. To resolve this, when you add OneSignal to your site, it should begin with:

`window.OneSignalDeferred = window.OneSignalDeferred || [];`

This creates a `OneSignalDeferred` variable, and if OneSignal is already loaded, it's then assigned to the loaded instance. Otherwise, the OneSignal variable equals an empty array - `[]`.

All arrays have a [`.push() function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push), so at this point, the `OneSignalDeferred` variable is simply an array of functions we're pushing on to it. When the SDK finally loads, the SDK [processes all the functions pushed so far and redefines .push()](https://github.com/OneSignal/OneSignal-Website-SDK/blob/03cd16cacb79ff6d37156878d4f59ebf31ad8044/src/OneSignal.js#L2050).

### `init()`

Initializes the OneSignal SDK. This should be called in the `<head>` tag once on each page of your site. The `ONESIGNAL_APP_ID` can be found in [Keys & IDs](./keys-and-ids).

<Note>
  If you want to delay initialization of the OneSignal SDK, we recommend using our [Privacy methods](#privacy).
</Note>

<CodeGroup>
  ```javascript JavaScript theme={null}
  window.OneSignalDeferred = window.OneSignalDeferred || [];
  OneSignalDeferred.push(async function(OneSignal) {
    await OneSignal.init({
      appId: "ONESIGNAL_APP_ID",
    });
  });
  ```
</CodeGroup>

<Warning>
  Init options only work with [Custom Code Setup](./web-push-custom-code-setup). Otherwise, these are configured in the OneSignal dashboard.
</Warning>

|             Parameter            |   Type  | Description                                                                                                                                                   |
| :------------------------------: | :-----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              `appId`             |  String | **Required:** Your OneSignal App ID found in [Keys & IDs](./keys-and-ids).                                                                                    |
|   `requiresUserPrivacyConsent`   | Boolean | Delays SDK initialization until the user provides privacy consent. Must call [`setConsentGiven()`](#setconsentgiven) to complete setup.                       |
|          `safari_web_id`         |  String | The Safari Web ID for your uploaded Safari `.p12` certificate. [Web Quickstart](./web-push-setup).                                                            |
|          `promptOptions`         |  Object | Customize the permission prompts. [Details below](#promptoptions-parameters).                                                                                 |
|          `notifyButton`          |  Object | Enable and configure the Subscription Bell. [Details below](#notifybutton-parameters).                                                                        |
|       `welcomeNotification`      |  Object | Customize or disable the welcome notification. [Details below](#welcomenotification-parameters).                                                              |
|       `persistNotification`      | Boolean | Chrome (desktop only) - `true`: notification persists until clicked, `false`: disappears after a short time. Firefox/Safari ignore this setting.              |
|            `webhooks`            |  Object | Configure event callbacks. [See Webhooks](./webhooks).                                                                                                        |
|         `autoResubscribe`        | Boolean | **Recommended:** Auto-resubscribes users who clear browser cache or migrate to OneSignal. Overrides dashboard setting if used in code.                        |
|  `notificationClickHandlerMatch` |  String | `"exact"` (default): focuses tab with an exact URL match. `"origin"`: focuses any tab with the same domain.                                                   |
| `notificationClickHandlerAction` |  String | `"navigate"` (default): navigates to `launchURL`. `"focus"`: focuses existing tab (only used with `"origin"` match).                                          |
|       `serviceWorkerParam`       |  Object | Set the `scope` of the service worker. Must be different from other service worker's scope if applicable. Example:<br />`{ scope: "/myPath/myCustomScope/" }` |
|        `serviceWorkerPath`       |  String | Set the location of the OneSignal service worker file. Example:<br />`"myPath/OneSignalSDKWorker.js"`                                                         |

***

#### `promptOptions` parameters

Use `promptOptions` to localize or customize the user permission prompts. All fields are optional.

|   Parameter  |       Type       | Description                                                                                                                                                                                                                                                                                                          |
| :----------: | :--------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  `slidedown` |      Object      | Contains an array of `prompts` with configuration options.                                                                                                                                                                                                                                                           |
|   `prompts`  | Array of Objects | An array of prompt configurations. Example:<br />`"slidedown": { "prompts": [{...}, {...}] }`                                                                                                                                                                                                                        |
|    `type`    |      String      | Prompt types:<br /><ul><li>`push` – Slide Prompt (no categories)</li><li>`category` – Slide Prompt with up to 10 categories</li><li>`email` – Collect email only</li><li>`sms` – Collect phone number only</li><li>`smsAndEmail` – Collect both</li></ul>See [Web Permission Prompts](./permission-requests).        |
| `autoPrompt` |      Boolean     | <ul><li>`true`: show based on `delay`.</li><li>`false`: prompt only shown manually via Slidedown API.</li></ul>                                                                                                                                                                                                      |
|    `delay`   |      Object      | Controls when auto-prompt is shown:<br />`{ pageViews: 3, timeDelay: 20 }` = Show after 3rd pageview and 20s wait.                                                                                                                                                                                                   |
|    `text`    |      Object      | Custom text options:<br /><ul><li>`actionMessage` (max 90 chars)</li><li>`acceptButton` (max 15)</li><li>`cancelButton` (max 15)</li><li>`emailLabel`, `smsLabel`, `confirmMessage`</li><li>`updateMessage`, `positiveUpdateButton`, `negativeUpdateButton` (used for updating categories or contact info)</li></ul> |
| `categories` | Array of Objects | Only for `type: category`. Each object includes:<br />`tag`: internal key<br />`label`: user-visible name<br />Example: `[ {tag: "local_news", label: "Local News"} ]`. See [Data Tags](./add-user-data-tags).                                                                                                       |

***

#### `notifyButton` parameters

Configure the Subscription Bell (notify button) shown on the page.

|      Parameter     |   Type   | Description                                                                                                   |
| :----------------: | :------: | ------------------------------------------------------------------------------------------------------------- |
|      `enable`      |  Boolean | Enables the Subscription Bell. Disabled by default.                                                           |
| `displayPredicate` | Function | Custom function (or Promise) that returns `true` or `false` to show/hide the Bell. Evaluated once when shown. |
|       `size`       |  String  | `'small'`, `'medium'`, or `'large'`. Shrinks to `'small'` after subscription.                                 |
|     `position`     |  String  | `'bottom-left'` or `'bottom-right'`.                                                                          |
|      `offset`      |  Object  | CSS pixel offsets: `{ bottom: '50px', left: '10px' }`                                                         |
|     `prenotify`    |  Boolean | If `true`, shows a "1 unread" icon and custom hover text.                                                     |
|    `showCredit`    |  Boolean | Set to `false` to hide "Powered by OneSignal" in the popup.                                                   |
|       `text`       |  Object  | Custom text for the bell UI.                                                                                  |

***

#### `welcomeNotification` parameters

Customize the welcome notification sent after first-time subscription.

| Parameter |   Type  | Description                                                                                |
| :-------: | :-----: | ------------------------------------------------------------------------------------------ |
| `disable` | Boolean | Disable welcome notification.                                                              |
| `message` |  String | **Required:** Notification message. Defaults to `'Thanks for subscribing!'` if blank.      |
|  `title`  |  String | Notification title. Defaults to site title. Use `' '` (space) to remove (not recommended). |
|   `url`   |   URL   | Optional URL to open when the user clicks the notification. Typically not needed.          |

***

**Example**:

<CodeGroup>
  ```javascript Example init for Custom Code Setup theme={null}
  <script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>
  <script>
  window.OneSignalDeferred = window.OneSignalDeferred || [];
  OneSignalDeferred.push(async function(OneSignal) {
    await OneSignal.init({
      appId: "YOUR_APP_ID",
      safari_web_id: "YOUR_SAFARI_WEB_ID",
      notifyButton: {
        enable: true,
      },
      promptOptions: {
        slidedown: {
          prompts: [{
              type: "smsAndEmail",
              autoPrompt: false,
              text: {
                emailLabel: "Insert Email Address",
                smsLabel: "Insert Phone Number",
                acceptButton: "Submit",
                cancelButton: "No Thanks",
                actionMessage: "Receive the latest news, updates and offers as they happen.",
                updateMessage: "Update your push notification subscription preferences.",
                confirmMessage: "Thank You!",
                positiveUpdateButton: "Save Preferences",
                negativeUpdateButton: "Cancel",
              },
              delay: {
                pageViews: 1,
                timeDelay: 20
              },
            },
            {
              type: "category",
              autoPrompt: true,
              text: {
                actionMessage: "We'd like to show you notifications for the latest news and updates.",
                acceptButton: "Allow",
                cancelButton: "Cancel",

                /* CATEGORY SLIDEDOWN SPECIFIC TEXT */
                negativeUpdateButton: "Cancel",
                positiveUpdateButton: "Save Preferences",
                updateMessage: "Update your push notification subscription preferences.",
              },
              delay: {
                pageViews: 3,
                timeDelay: 20
              },
              categories: [{
                  tag: "politics",
                  label: "Politics"
                },
                {
                  tag: "local_news",
                  label: "Local News"
                },
                {
                  tag: "world_news",
                  label: "World News",
                },
                {
                  tag: "culture",
                  label: "Culture"
                },
              ]
            }
          ]
        }
      }
    });
  });
  </script>

  ```
</CodeGroup>

### `setLogLevel()`

Set the logging to print additional logs to the console. See [Debugging with Browser DevTools](./troubleshooting-web-push#debugging-using-browser-developer-tools) for more details.

```javascript JavaScript theme={null}
  OneSignal.Debug.setLogLevel('trace');
```

**Log levels**:

* `'trace'`
* `'debug'`
* `'info'`
* `'warn'`
* `'error'`

***

## User identity & properties

When users subscribe to push notifications on your website, OneSignal automatically creates a OneSignal ID (user-level ID) and a Subscription ID (device-level ID). You can associate multiple Subscriptions (e.g., devices, emails, phone numbers) with a single user by calling `login()` with your unique user identifier.

<Note>
  See [Users](./users) and [Subscriptions](./subscriptions) for more details.
</Note>

### `login(external_id)`

Sets the current user context to the provided `external_id`. This links the current device (web push Subscription) to a known user and unifies all future data under a single `onesignal_id`. Use this method only for **identified users** (for example, after login or account restore). For anonymous users, do not call `login`. Instead, track them using their automatically assigned `onesignal_id` (see [OneSignal.User.onesignalId](#onesignal-user-onesignalid)).

**What happens when you call `login(external_id)`**

The SDK behaves differently depending on whether the `external_id` already exists within the OneSignal app.

**If the `external_id` already exists:**

* The SDK switches to that existing user.
  * You may see a `409 Conflict` error. This is an expected, innocuous error indicating that the External ID already exists within the OneSignal app and can be ignored.
* The current `onesignal_id` is discarded and the existing `onesignal_id` for that user is loaded.
* The current device (web push Subscription) is linked to the existing user.
* Anonymous data collected before login is not merged and is discarded. This includes tags, session data, email/SMS Subscriptions, and other local user properties.

**If the `external_id` does not exist:**

* A new user is created using the current `onesignal_id`.
* All data collected while the user was anonymous is retained.
* The device (web push Subscription) becomes linked to this new user.

**Retry behavior:**

* The SDK automatically retries the login request on network failures or server errors.
* You do not need to implement your own retry logic.

**Best practices:**

* Call `login(external_id)` **every page load** once you know the user's ID (for example, after sign-in or session restore).
* Call it again whenever the signed-in user changes (account switch).
* Do not call `login` before you have a stable, known user identifier.

```javascript JavaScript theme={null}
OneSignalDeferred.push(async function(OneSignal) {
  await OneSignal.login("external_id");
});
```

### `logout()`

Unlinks the current user from the web push Subscription.

* Removes the `external_id` from the current web push Subscription. Does not remove the `external_id` from other Subscriptions.
* Resets the `onesignal_id` to a new anonymous user.
* Any new data (e.g tags, Subscriptions, session data, etc.) will now be set on the new anonymous user until they are identified with the `login` method.

<Note>Use this when a user signs out of your site and you do not want to send targeted transactional messages to the browser anymore.</Note>

```javascript JavaScript theme={null}
OneSignalDeferred.push(async function(OneSignal) {
  await OneSignal.logout();
});
```

### `OneSignal.User.onesignalId`

Retrieves the current user's `onesignal_id` stored locally on the browser. This value represents the active user context (OneSignal's User ID) and can change over time — for example, when you call `login(external_id)` or when the SDK initializes. If called too early, this method may return `null`.

This value is not the Subscription ID which is used to identify the browser aka web push Subscription (see [User.PushSubscription.id](#user-pushsubscription-id)).

**When `onesignal_id` is available:**

* After the OneSignal SDK finishes initializing
* After a user is identified with `login(external_id)`
* After switching users or restoring a session

If you need to reliably react to changes or get this ID, use [User State `addObserver()`](#addeventlistener-user-state) instead of polling.

**Common use cases:**
In most cases, you will want to use your own External ID set via the `login` method. However, there are some cases where you may want to use the `onesignal_id` directly.

* Tracking anonymous users before an External ID is set
* Storing the OneSignal ID in your backend for support or debugging
* Correlating OneSignal users with internal logs
* Displaying the ID for troubleshooting or QA

<Warning> Do not persist the OneSignal ID as a permanent user identifier. It can change when users log in, log out, or switch accounts. </Warning>

```javascript JavaScript theme={null}
const onesignalId = OneSignal.User.onesignalId;
```

### `OneSignal.User.externalId`

Retrieve the current user's External ID saved locally on the browser. May be `null` if not set via the `login` method or called before user state is initialized. Instead, use [User State `addObserver()`](#addeventlistener-user-state) to listen for user state changes.

```javascript JavaScript theme={null}
  const externalId = OneSignal.User.externalId;
```

### `addEventListener()` *User State*

Listen for changes in the user context (e.g., login, logout, ID assignment).

```javascript JavaScript theme={null}
  OneSignalDeferred.push(function() {
    OneSignal.User.addEventListener('change', function (event) {
      console.log('change', { event });
    });
  });
```

### `addAlias()`, `addAliases()`, `removeAlias()`, `removeAliases()`

Aliases are alternative identifiers (like usernames or CRM IDs).

* Set `external_id` with `login()` before adding aliases. Aliases added to subscriptions without `external_id` will not sync across multiple subscriptions.
* See [Aliases](./aliases) for details.

```javascript JavaScript theme={null}
  // Add a single alias
  OneSignal.User.addAlias("ALIAS_LABEL", "ALIAS_ID");

  // Add multiple aliases
  OneSignal.User.addAliases({
    ALIAS_LABEL_01: "ALIAS_ID_01",
    ALIAS_LABEL_02: "ALIAS_ID_02",
    ALIAS_LABEL_03: "ALIAS_ID_03",
  });

  // Remove a single alias
  OneSignal.User.removeAlias("ALIAS_LABEL");

  // Remove multiple aliases
  OneSignal.User.removeAliases(["ALIAS_LABEL_01", "ALIAS_LABEL_02", "ALIAS_LABEL_03"]);
```

### `getLanguage()`, `setLanguage()`

Get and/or override the auto-detected language of the user. See [Multi-language messaging](./multi-language-messaging) for a list of available language codes.

```javascript JavaScript theme={null}
  // Get the language of the currently logged-in user
  OneSignal.User.getLanguage()

  // Set the language of the currently logged-in user
  OneSignal.User.setLanguage('en')
```

***

## Custom events

[Trigger Journeys](./journeys-settings#custom-events) and [Wait Until step activation](./journeys-actions#wait-until) via a [custom event](./custom-events).

<Note>
  Custom events require Web SDK `160500`+

  A user should be logged in for custom events to be tracked.
</Note>

Track and send a custom event performed by the current user.

* `name` - **Required.** The name of the event as a string.
* `properties` - **Optional.** Key-value pairs to add to the event. The properties dictionary or map must be serializable into a valid JSON Object. Supports nested values.

The SDK automatically includes app-specific data into the properties payload under the reserved key `os_sdk` that will be available to consume. For example, to target events by subscription type, you would access `os_sdk.type`.

```json json theme={null}
{ 
  "os_sdk": {
    "device_os": "138",
    "type": "ChromePush",
    "device_model": "MacIntel",
    "sdk": "160500"
  }
}
```

### `trackEvent()`

```javascript JavaScript theme={null}
const properties = {
  "promo_code": "NEW50",
  "membership_details": {
     "vip": true,
     "products_viewed_count": 15,
  }
}
window.OneSignal.User.trackEvent('started_free_trial', properties);

// You can also track an event by name without additional properties associated
window.OneSignal.User.trackEvent('my_event_name');
```

***

## Data tags

Tags are custom `key : value` pairs of string data you set on users based on events or user properties. See [Data Tags](./add-user-data-tags) for more details.

### `addTag()`, `addTags()`

Set a single or multiple tags on the current user.

* Values will be replaced if the key already exists.
* Exceeding your plan's tag limit will cause the operations to fail silently.

```javascript JavaScript theme={null}
  // Add a single tag
  OneSignal.User.addTag('tag_key', 'tag_value');

  // Add multiple tags
  OneSignal.User.addTags({
   KEY_01: "VALUE_01",
   KEY_02: "VALUE_02",
   KEY_03: "VALUE_03"
  });
```

### `removeTag()`, `removeTags()`

Delete a single or multiple tags from the current user.

```javascript JavaScript theme={null}
  // Delete a single tag
  OneSignal.User.removeTag("KEY");

  OneSignal.User.removeTags(['KEY_01', 'KEY_02', 'KEY_03']);
```

### `getTags()`

Returns the local copy of the user's tags. Tags are updated from the server during `login()` or new app sessions.

```javascript JavaScript theme={null}
  const tags = OneSignal.User.getTags()
```

***

## Privacy

### `setConsentRequired()`

Enforces user consent before data collection begins. Must be called **before initializing the SDK**.

This method is the same as adding the `requiresUserPrivacyConsent: true` to the `init` method.

```javascript JavaScript theme={null}
  OneSignal.setConsentRequired(true);
```

### `setConsentGiven()`

Grants or revokes user consent for data collection. Without consent, no data is sent to OneSignal and no subscription is created.

* If [`setConsentRequired()`](#setconsentrequired) or `requiresUserPrivacyConsent` is set to `true`, our SDK will not be fully enabled until `setConsentGiven` is called with `true`.
* If `setConsentGiven` is set to `true` and a Subscription is created, then later it is set to `false`, that Subscription will no longer receive updates. The current data for that Subscription remains unchanged until `setConsentGiven` is set to `true` again.
* If you want to delete the User and/or Subscription data, use our [Delete user](/reference/delete-user) or [Delete subscription](/reference/delete-subscription) APIs.

```javascript JavaScript theme={null}
  OneSignal.setConsentGiven(true);
```

***

## Subscriptions

A Subscription represents a single messaging channel instance (for example, a browser) and has a unique Subscription ID (OneSignal's device-level ID). A user can have multiple Subscriptions across devices and platforms.

See [Subscriptions](./subscriptions) for more details.

### `User.PushSubscription.id`

Retrieves the web push Subscription ID for the current browser, stored locally by the SDK.

This ID uniquely identifies this specific browser’s push channel, not the user. It is commonly used when associating devices or browsers with your backend or debugging delivery issues.

If called before the Subscription is created or restored, this value may be `null`.

<Note> To reliably detect when the web push Subscription ID becomes available or changes, use the [push Subscription listener](#addeventlistener-push-subscription-changes). </Note>

```javascript JavaScript theme={null}
  const subscription_id = OneSignal.User.PushSubscription.id;
```

### `User.PushSubscription.token`

Returns the current push subscription token. May return `null` if called too early. Its recommended to get this data within the [subscription observer](#addeventlistener-push-subscription-changes) to react to changes.

```javascript JavaScript theme={null}
  OneSignal.User.PushSubscription.token;
```

### `addEventListener()` *Push Subscription Changes*

Use this method to respond to push subscription changes like:

* The device receives a new push token from Google (FCM) or Apple (APNs)
* OneSignal assigns a subscription ID
* The `optedIn` value changes (e.g. called `optIn()` or `optOut()`)
* The user toggles push permission in system settings, then opens the app

When this happens, the SDK triggers the `onPushSubscriptionChange` event. Your listener receives a state object with the `previous` and `current` values so you can detect exactly what changed.

To stop listening for updates, call the associated `removeObserver()` or `removeEventListener()` method.

```javascript JavaScript theme={null}
  function pushSubscriptionChangeListener(event) {
    console.log("event.previous.id", event.previous.id);
    console.log("event.current.id", event.current.id);
    console.log("event.previous.token", event.previous.token);
    console.log("event.current.token", event.current.token);
    console.log("event.previous.optedIn", event.previous.optedIn);
    console.log("event.current.optedIn", event.current.optedIn);
  }

  OneSignalDeferred.push(function(OneSignal) {
    OneSignal.User.PushSubscription.addEventListener("change", pushSubscriptionChangeListener);
  });
```

### `optOut()`, `optIn()`, `optedIn`

Control the subscription status (`subscribed` or `unsubscribed`) of the current push Subscription. Use these methods to control the push subscription status on your site. Common use cases: 1) Prevent push from being sent to users that log out. 2) Implement a notification preference center within your site.

* `optOut()`: Sets the current push subscription status to unsubscribed (even if the user has a valid push token).
* `optIn()`: Does one of three actions:
  1. If the Subscription has a valid push token, it sets the current push subscription status to `subscribed`.
  2. If the Subscription does not have a valid push token, it attempts to display the push permission prompt.
* `optedIn`: Returns `true` if the current push subscription status is subscribed, otherwise `false`. If the push token is valid but `optOut()` was called, this will return `false`.

```javascript JavaScript theme={null}
  OneSignal.User.PushSubscription.optOut();

  OneSignal.User.PushSubscription.optIn();

  var optedIn = OneSignal.User.PushSubscription.optedIn;
```

### `addEmail()`, `removeEmail()`

Adds or removes an email Subscription (email address) for the current user.

These methods are compatible with [Identity Verification](./identity-verification).

**When you call `addEmail(email)`:**

* The email address becomes an email Subscription for the current user.
* The email may be created or reassigned.
* The same email address cannot exist multiple times in the same OneSignal app. If you see duplicate email addresses, check your REST API requests and contact support if needed.

The SDK returns the following HTTP status codes:

| Status code      | Meaning                                                                              |
| ---------------- | ------------------------------------------------------------------------------------ |
| **200 OK**       | The email Subscription already belongs to the current user. No changes were made.    |
| **201 Created**  | A new email Subscription was created and linked to the user.                         |
| **202 Accepted** | The email Subscription already existed in the app and was moved to the current user. |

**When you call `removeEmail(email)`:**

* The email Subscription is removed from the current user.
* The current External ID is removed from the email Subscription.
* A new OneSignal ID is assigned to the email Subscription.
* Other Subscriptions (push, SMS, other emails) remain unaffected.

**Best practices:**

* Call `login()` first, then call `addEmail()`. Otherwise, the email may be attached to an anonymous user.
* Use a stable, verified email address.
* Follow [Email reputation best practices](./email-reputation-best-practices).

```javascript JavaScript theme={null}
  OneSignal.User.addEmail("example@email.com");

  OneSignal.User.removeEmail("example@email.com");
```

### `addSms()`, `removeSms()`

Adds or removes an SMS Subscription (phone number) for the current user. Phone numbers must be provided in [E.164 format](https://www.twilio.com/docs/glossary/what-e164) (for example, `+15551234567`).

These methods are compatible with [Identity Verification](./identity-verification).

**When you call `addSms(phoneNumber)`:**

* The phone number becomes an SMS Subscription for the current user.
* The number may be created or reassigned.
* The same phone number cannot exist multiple times in the same OneSignal app. If you see duplicate phone numbers, check your REST API requests and contact support if needed.

The SDK returns the following HTTP status codes:

| Status code      | Meaning                                                                            |
| ---------------- | ---------------------------------------------------------------------------------- |
| **200 OK**       | The SMS Subscription already belongs to the current user. No changes were made.    |
| **201 Created**  | A new SMS Subscription was created and linked to the user.                         |
| **202 Accepted** | The SMS Subscription already existed in the app and was moved to the current user. |

**When you call `removeSms(phoneNumber)`:**

* The SMS Subscription is removed from the current user.
* The current External ID is removed from the SMS Subscription.
* A new OneSignal ID is assigned to the SMS Subscription.
* Other Subscriptions (push, email, other SMS) remain unaffected.

**Best practices:**

* Call `login()` first, then call `addSms()`. Otherwise, the SMS Subscription may be attached to an anonymous user.
* Always validate and normalize phone numbers to [E.164 format](https://www.twilio.com/docs/glossary/what-e164) before sending.
* Follow [SMS Registration Requirements](./sms-registration-requirements).

```javascript JavaScript theme={null}
  OneSignal.User.addSms("+15558675309");

  OneSignal.User.removeSms("+15558675309");
```

***

## Slidedown prompts

Display the various slidedown prompts on your sites. See [Web permission prompts](./permission-requests) for more details.

* If dismissed, future calls will be ignored for at least three days. Further declines will lengthen the time required to elapse before prompting the user again.
* To override back-off behavior, pass `{force: true}` to the method. However, to provide a good user experience, bind the action to a UI-initiated event like a button click.

<Warning>
  This does not replace the Native Browser Prompt required for subscription. You must obtain permissions using the native browser prompt.
</Warning>

### `promptPush()`

Displays the regular slidedown prompt for push notifications.

* If using categories, call [`promptPushCategories()`](#promptpushcategories) instead.
* Subject to backoff logic set by the OneSignal. See [Web permission prompts](./permission-requests#auto-prompt-%26-display-settings) for more details.

```javascript JavaScript theme={null}
  OneSignal.Slidedown.promptPush();
  // To bypass backoff logic while testing, pass {force: true}
  //OneSignal.Slidedown.promptPush({force: true});
```

### `promptPushCategories()`

Displays the category slidedown prompt, allowing users to update their tags. Also triggers the native notification permission prompt if the user has not already granted permission.

* If not using categories, call [`promptPush()`](#promptpush) instead.
* Subject to backoff logic set by the OneSignal. See [Web permission prompts](./permission-requests#auto-prompt-%26-display-settings) for more details.

```javascript JavaScript theme={null}
  OneSignal.Slidedown.promptPushCategories();
  // To bypass backoff logic while testing, pass {force: true}
  //OneSignal.Slidedown.promptPushCategories({force: true});
```

### `promptSms()`

Displays the SMS subscription prompt.

* Subject to backoff logic set by the OneSignal. See [Web permission prompts](./permission-requests#auto-prompt-%26-display-settings) for more details.

```javascript JavaScript theme={null}
  OneSignal.Slidedown.promptSms();
  // To bypass backoff logic while testing, pass {force: true}
  //OneSignal.Slidedown.promptSms({force: true});
```

### `promptEmail()`

Displays the email subscription prompt.

* Subject to backoff logic set by the OneSignal. See [Web permission prompts](./permission-requests#auto-prompt-%26-display-settings) for more details.

```javascript JavaScript theme={null}
  OneSignal.Slidedown.promptEmail();
  // To bypass backoff logic while testing, pass {force: true}
  //OneSignal.Slidedown.promptEmail({force: true});
```

### `promptSmsAndEmail()`

Displays the SMS and email subscription prompts simultaneously.

* Subject to backoff logic set by the OneSignal. See [Web permission prompts](./permission-requests#auto-prompt-%26-display-settings) for more details.

```javascript JavaScript theme={null}
  OneSignal.Slidedown.promptSmsAndEmail();
  // To bypass backoff logic while testing, pass {force: true}
  //OneSignal.Slidedown.promptSmsAndEmail({force: true});
```

### `addEventListener()` *Slidedown*

Add a callback to detect the Slidedown prompt shown event.

```javascript JavaScript theme={null}
  OneSignalDeferred.push(function(OneSignal) {

    OneSignal.Slidedown.addEventListener('slidedownShown', function (event) {
      console.log('slidedownShown', { event });
    });

  });
```

***

## Push notifications

### `requestPermission()`

Requests push notifications permission via the native browser prompt. Subject to backoff logic set by the browser. See [Web permission prompts](./permission-requests#native-permission-prompt) for more details.

```javascript JavaScript theme={null}
  OneSignal.Notifications.requestPermission();
```

### `isPushSupported()`

Returns `true` if the current browser supports web push.

```javascript JavaScript theme={null}
  const isSupported = OneSignal.Notifications.isPushSupported();
```

### `OneSignal.Notifications.permission`

Returns a boolean indicating the site's current permission to display notifications.

* `true`: The user has granted permission to display notifications.
* `false`: The user has either denied or not yet granted permission to display notifications.

This is just the sites's permission, does not factor in OneSignal's `optOut` status or the existence of the Subscription ID and Push Token, see `OneSignal.User.PushSubscription` for these.

To listen for changes in permission, use the [`permissionChange`](#permissionchange) event.

```javascript JavaScript theme={null}
  let permission = OneSignal.Notifications.permission;
```

### `addEventListener()` *Notifications*

You can hook into the notification life-cycle by attaching your event handlers to a notification event. Calling `addEventListener` lets you add an arbitrary number of event handlers for notification events.

To stop listening for events, call the associated `removeEventListener()` method.

```javascript JavaScript theme={null}
  function eventListener(event) {
    console.log(`${event}`);
  }

  OneSignal.Notifications.addEventListener("event", eventListener);

  OneSignal.Notifications.removeEventListener("event", eventListener);
```

#### `permissionChange`

This event occurs when the user clicks Allow or Block or dismisses the browser's native permission request.

```javascript JavaScript theme={null}
  function permissionChangeListener(permission) {
    if (permission) {
      console.log(`permission accepted!`);
    }
  }

  OneSignal.Notifications.addEventListener("permissionChange", permissionChangeListener);
```

#### `permissionPromptDisplay`

This event occurs when the browser's native permission request has just been shown.

```javascript JavaScript theme={null}
  function promptListener() {
    console.log(`permission prompt dispslayed event: ${event}`);
  }

  OneSignal.Notifications.addEventListener("permissionPromptDisplay", promptListener);
```

#### `click`

This event will fire when the notification's body/title or action buttons are clicked.

```javascript JavaScript theme={null}
  function clickEventListener(event) {
    console.log(`click event: ${event}`);
  }

  OneSignal.Notifications.addEventListener("click", clickEventListener);
```

#### `foregroundWillDisplay`

This event occurs before a notification is displayed. This event is fired on your page. If multiple browser tabs are open on your site, this event will be fired on *all* pages on which OneSignal is active.

```javascript JavaScript theme={null}
  function foregroundWillDisplayListener(event) {
    console.log(`notification will display: ${notification}`);
  }

  OneSignal.Notifications.addEventListener("foregroundWillDisplay", foregroundWillDisplayListener);
```

#### `dismiss`

This event occurs when:

* A user purposely dismisses the notification without clicking the notification body or action buttons
* On Chrome on Android, a user dismisses all web push notifications (this event will be fired for each web push notification we show)
* A notification expires on its own and disappears

<Info>
  This event *does not occur* if a user clicks on the notification body or one of the action buttons. That is considered a notification `click` event.
</Info>

```javascript JavaScript theme={null}
  function notificationDismissedListener(event) {
    console.log(`dismiss event: ${event}`);
  }

  OneSignal.Notifications.addEventListener("dismiss", notificationDismissedListener);
```

### `setDefaultUrl()`

Sets the default URL for notifications.

If you haven't set a default URL, your notification will open to the root of your site by default.

```javascript JavaScript theme={null}
  OneSignal.Notifications.setDefaultUrl("https://onesignal.com");
```

To set the default URL for notifications, provide a valid URL that you want to be launched when the notification is clicked. This default URL will be used if no other URL is specified when creating a notification. If you do specify a URL when creating a notification, the default URL will be overridden.

In the case of Safari, the default notification icon URL will be set to the Site URL that you have specified in your Safari settings, as this function is not available.

### `setDefaultTitle()`

Sets the default title to display on notifications.

```javascript JavaScript theme={null}
  OneSignal.Notifications.setDefaultTitle("Powered by OneSignal!");
```

If a notification is created with a title, the specified title always overrides this default title.

A notification's title defaults to the title of the page the user last visited. If your page titles vary between pages, this inconsistency can be undesirable. Call this to standardize page titles across notifications, as long as a notification title isn't specified.

***

## Outcomes

### `sendOutcome()`

Triggers an outcome which can be viewed in the OneSignal dashboard. Accepts an outcome name (`string`, required) and a value (`number`, optional). Each time `sendOutcome` method is invoked with the same outcome name passed, the outcome count will increase, and the outcome value will be increased by the amount passed in (if included). See [Custom Outcomes](./custom-outcomes) for more details.

```javascript JavaScript theme={null}
  OneSignal.Session.sendOutcome('outcome name', 19.84);
```

### `sendUniqueOutcome()`

Triggers an outcome which can be viewed in the OneSignal dashboard. Accepts only the outcome name (`string`, required). `sendUniqueOutcome` will increase the count for that outcome only once per user. See [Custom Outcomes](./custom-outcomes) for more details.

```javascript JavaScript theme={null}
  OneSignal.Session.sendUniqueOutcome('outcome name');
```

***

Built with [Mintlify](https://mintlify.com).
