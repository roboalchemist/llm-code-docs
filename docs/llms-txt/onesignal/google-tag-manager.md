# Source: https://documentation.onesignal.com/docs/en/google-tag-manager.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Tag Manager setup

> Add OneSignal Web Push to your website using Google Tag Manager (GTM), including service worker setup, initialization, and sending user tags safely.

This guide shows you how to load and initialize the OneSignal Web SDK using Google Tag Manager (GTM), then optionally set an External ID and send OneSignal Tags after initialization.

## Prerequisites

* A site that supports HTTPS.
* You can publish changes in GTM for the site's container.
* You've completed the OneSignal [Web SDK setup](./web-sdk-setup) flow until **Add Code to Site**. This gives you:
  * A OneSignal Web Push app and App ID.
  * The [OneSignal Service Worker](./onesignal-service-worker) setup.

## Setup

### 1. Set up your OneSignal web app

Follow [Web SDK setup](./web-sdk-setup) until you reach **Add Code to Site**. This is where you will get the OneSignal App ID.

<Frame caption="Once you reach this step, you will need to make some adjustments to the code to work with Google Tag Manager.">
  <img src="https://mintcdn.com/onesignal/Y9PryqrHCRmPv_BC/images/web-push/add-code-to-site.png?fit=max&auto=format&n=Y9PryqrHCRmPv_BC&q=85&s=445d73fafe6bd92c5a6dcfbac563c1ee" alt="Add Code to Site step in OneSignal Web SDK setup dashboard" width="2588" height="1638" data-path="images/web-push/add-code-to-site.png" />
</Frame>

<Warning>
  You must upload the OneSignal Service Worker file to your server directly. See [OneSignal Service Worker](./onesignal-service-worker).
</Warning>

### 2. Create GTM variables

Create GTM variables for values you reference across tags. This avoids hardcoding and makes your setup easier to maintain.

**Create a `ONESIGNAL_APP_ID` variable**

1. In GTM, go to **Variables > New**.
2. Choose **Constant**.
3. Name it `ONESIGNAL_APP_ID`
4. Set the value to your OneSignal App ID.
5. Save

<Frame caption="Creating a OneSignal App ID variable">
  <img src="https://mintcdn.com/onesignal/wJS3gHTEqDzyW0IP/images/web-push/gtm-app-id-variable.png?fit=max&auto=format&n=wJS3gHTEqDzyW0IP&q=85&s=8a7752f1d4095d4c8e6b8119a9de2bfc" alt="Creating a OneSignal App ID variable in Google Tag Manager" width="2378" height="1656" data-path="images/web-push/gtm-app-id-variable.png" />
</Frame>

<Check>
  You can now reference your App ID anywhere in GTM using `{{ ONESIGNAL_APP_ID }}`.
</Check>

**Create an `ONESIGNAL_EXTERNAL_ID` variable (Recommended)**

Use this if you associate users with an external identifier (for example, a user ID from your database or auth system).

Choose a variable type based on where the value lives on your site. Common options:

* Data Layer Variable (recommended)
* First-Party Cookie
* DOM Variable (advanced)

### 3. Create the OneSignal init tag

1. In GTM, go to **Tags > New**
2. Name the tag: `OneSignal - Init`
3. Tag Type: **Custom HTML**
4. Paste the below code.
5. Under **Advanced Settings > Tag firing options**, set **Once per page**.
6. Under **Triggering**, select **Initialization - All Pages**.

```html HTML theme={null}
<!--
  OneSignal – Web SDK initialization using Google Tag Manager

  This snippet:
  - Loads the OneSignal Web SDK
  - Initializes OneSignal with your App ID
  - Enables the Subscription Bell (notifyButton)

  Works for most sites out of the box.
-->

<!-- 1. Load the OneSignal Web SDK (v16) -->
<!-- This script must load on every page where you want OneSignal available -->
<script
  src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js"
  defer>
</script>

<script>
  // Ensure the GTM dataLayer exists
  // Used here only to optionally push a "OneSignalInitialized" event
  window.dataLayer = window.dataLayer || [];

  // OneSignalDeferred is a queue that runs once the SDK is fully loaded
  window.OneSignalDeferred = window.OneSignalDeferred || [];

  // 2. Initialize OneSignal once the SDK is ready
  window.OneSignalDeferred.push(function (OneSignal) {

    OneSignal.init({
      /*
        REQUIRED
        It is recommended to set the OneSignal App ID as a GTM variable.
        You can find this in your OneSignal Dashboard under:
        Settings > Keys & IDs
      */
      appId: "{{ONESIGNAL_APP_ID}}",

      /*
        OPTIONAL – ONLY NEEDED IF YOUR SERVICE WORKER IS NOT AT THE ROOT

        If your service worker is hosted at:
          /OneSignalSDKWorker.js

        …then you should NOT set serviceWorkerPath or serviceWorkerParam.

        Uncomment and update the options below ONLY if your service worker
        is hosted in a subdirectory (for example: /push/onesignal/).
      */

      //serviceWorkerPath: "push/onesignal/OneSignalSDKWorker.js",
      //serviceWorkerParam: { scope: "/push/onesignal/" },

      /*
        OPTIONAL
        Enable the OneSignal Subscription Bell (notifyButton),
        which allows users to subscribe or unsubscribe from notifications.
        For more prompt options, see: https://documentation.onesignal.com/docs/en/permission-requests
      */
      notifyButton: {
        enable: true
      }
    })
    .then(function () {
      // OneSignal initialized successfully
      console.log("[OneSignal] init success");

      // Recommended: push an event to GTM for triggering other tags
      window.dataLayer.push({
        event: "OneSignalInitialized"
      });
    })
    .catch(function (e) {
      // Initialization failed (invalid App ID, missing service worker, etc.)
      console.log("[OneSignal] init failed", e);
    });
  });
</script>
```

<Frame caption="Configuring the OneSignal - Init tag">
  <img src="https://mintcdn.com/onesignal/Y9PryqrHCRmPv_BC/images/web-push/gtm-init-tag.png?fit=max&auto=format&n=Y9PryqrHCRmPv_BC&q=85&s=6cec423472cb84777bddd893a59c83ff" alt="Configuring the OneSignal - Init tag in Google Tag Manager" width="2442" height="2296" data-path="images/web-push/gtm-init-tag.png" />
</Frame>

<Warning>
  If you use a consent banner / CMP, see [Consent Mode and privacy considerations](#consent-mode-and-privacy-considerations) options below.
</Warning>

### 4. Set External ID & tags

Setting the [External ID](./users#external-id) is optional but recommended because it allows you to identify users across devices and syncs with your backend.

**Push `ONESIGNAL_EXTERNAL_ID` into the dataLayer**

This example shows how you might push a user ID into the dataLayer so GTM can read it via the `ONESIGNAL_EXTERNAL_ID` variable (created in step 2).

```html HTML theme={null}
<script>
  window.dataLayer = window.dataLayer || [];

  // Get your user ID from your database or auth system.
  // Ensure this is a string value.
  var userId = "your_user_id_here";

  dataLayer.push({
    ONESIGNAL_EXTERNAL_ID: String(userId),
  });
</script>
```

**Create a GTM Tag to set the External ID**
Tag configuration:

* Tag name: `OneSignal – Set External ID`
* Tag type: **Custom HTML**
* Tag firing options: **Once per page**
* Trigger:
  * Create a custom event trigger for `OneSignalInitialized` (set in the above **OneSignal - Init** tag) and
  * Optionally if you know the user ID is available on the page load.

<Warning>
  The required method to set the External ID is `OneSignal.login(externalId)` where `externalId` is a string.

  If `{{ONESIGNAL_EXTERNAL_ID}}` is empty (or GTM substitutes "undefined" / "null"), the login call will be skipped and the External ID will not be set. This is a common GTM timing issue.
</Warning>

<CodeGroup>
  ```html Basic Example to set the External ID theme={null}
  <script>
    // OneSignalDeferred ensures this runs after the OneSignal SDK is ready
    window.OneSignalDeferred = window.OneSignalDeferred || [];

    window.OneSignalDeferred.push(function (OneSignal) {
      /*
        Read the External ID from Google Tag Manager.
        This should be a GTM variable (Data Layer Variable or Custom JS Variable).
      */
      var externalId = "{{ONESIGNAL_EXTERNAL_ID}}";

      console.log("[OneSignal] raw external ID from GTM:", externalId);

      /*
        Basic validation:
        - GTM may substitute undefined/null as strings
        - OneSignal.login requires a string
      */
      if (!externalId || externalId === "undefined" || externalId === "null") {
        console.log("[OneSignal] External ID missing, skipping login");
        return;
      }

      // Ensure the External ID is a clean string
      externalId = String(externalId).trim();

      console.log("[OneSignal] Calling OneSignal.login with External ID:", externalId);

      /*
        Log the user into OneSignal using the External ID.
        This links the current browser/device to this user.
      */
      OneSignal.login(externalId)
        .then(function () {
          console.log("[OneSignal] External ID set successfully:", externalId);
        })
        .catch(function (e) {
          console.log("[OneSignal] Failed to set External ID", e);
        });
    });
  </script>
  ```

  ```html Advanced Example to try if External ID is not being set theme={null}
  <script>
    window.dataLayer = window.dataLayer || [];
    window.OneSignalDeferred = window.OneSignalDeferred || [];

    OneSignalDeferred.push(function (OneSignal) {
      var rawExternalId = "{{ONESIGNAL_EXTERNAL_ID}}";

      // ---- Helpers ----
      function log() {
        console.log.apply(console, ["[OneSignal External ID]"].concat([].slice.call(arguments)));
      }

      function normalizeExternalId(v) {
        // GTM commonly substitutes these as strings
        if (
          v === undefined ||
          v === null ||
          v === "undefined" ||
          v === "null"
        ) return null;

        var s = String(v).trim();
        if (!s.length) return null;

        return s;
      }

      function pushDL(eventName, extra) {
        try {
          var payload = Object.assign({ event: eventName }, extra || {});
          window.dataLayer.push(payload);
        } catch (e) {
          // no-op
        }
      }

      function readStateSnapshot() {
        var snapshot = {
          onesignalId: null,
          externalId: null,
          pushSubscriptionId: null
        };

        try {
          snapshot.onesignalId = OneSignal.User && OneSignal.User.onesignalId;
          snapshot.externalId = OneSignal.User && OneSignal.User.externalId;
          snapshot.pushSubscriptionId =
            OneSignal.User &&
            OneSignal.User.PushSubscription &&
            OneSignal.User.PushSubscription.id;
        } catch (e) {
          log("Error reading OneSignal.User state", e);
        }

        return snapshot;
      }

      function isExternalIdApplied(targetExternalId) {
        var current = normalizeExternalId(OneSignal.User && OneSignal.User.externalId);
        return current === targetExternalId;
      }

      // ---- Initial logging ----
      log("Tag fired. rawExternalId:", rawExternalId, "type:", typeof rawExternalId);

      var externalId = normalizeExternalId(rawExternalId);
      log("Normalized externalId:", externalId, "type:", typeof externalId);

      if (!externalId) {
        log("Not calling login(): externalId missing/invalid");
        pushDL("OneSignalExternalIdMissing", { reason: "invalid_or_missing_external_id" });
        return;
      }

      // Optional: enable verbose OneSignal logs during testing
      if (OneSignal.Debug && OneSignal.Debug.setLogLevel) {
        OneSignal.Debug.setLogLevel("trace");
        log("Enabled OneSignal Debug log level: trace");
      }

      // ---- Attach User State observer ----
      var changeFired = false;

      OneSignal.User.addEventListener("change", function (event) {
        changeFired = true;

        log("User change event fired:", event);

        var snapshot = readStateSnapshot();
        log("User state snapshot:", snapshot);

        // Helpful: push snapshot-ish DL event (optional)
        pushDL("OneSignalUserStateChanged", {
          onesignal_id: snapshot.onesignalId || "",
          external_id: normalizeExternalId(snapshot.externalId) || "",
          push_subscription_id: snapshot.pushSubscriptionId || ""
        });
      });

      // ---- Login + confirm + retry ----
      var attempt = 0;
      var MAX_RETRIES = 3;
      var CONFIRM_WINDOW_MS = 1500;
      var BASE_BACKOFF_MS = 500;

      function doLogin() {
        attempt += 1;
        changeFired = false;

        log("Calling OneSignal.login()", { externalId: externalId, attempt: attempt });

        OneSignal.login(externalId)
          .then(function () {
            log("OneSignal.login() promise resolved");
            waitForConfirmation();
          })
          .catch(function (e) {
            log("OneSignal.login() promise rejected", e);
            retry("promise_rejected");
          });
      }

      function waitForConfirmation() {
        var start = Date.now();

        (function check() {
          if (isExternalIdApplied(externalId)) {
            log("Confirmed externalId applied via state check:", externalId);

            var snapshot = readStateSnapshot();
            log("Final state snapshot:", snapshot);

            pushDL("OneSignalExternalIdSet", {
              external_id: externalId,
              attempt: attempt,
              push_subscription_id: snapshot.pushSubscriptionId || ""
            });

            return;
          }

          if (changeFired) {
            log("Change event observed but externalId not yet reflected; waiting...");
          }

          if (Date.now() - start >= CONFIRM_WINDOW_MS) {
            log("No confirmation within window", {
              attempt: attempt,
              changeFired: changeFired,
              currentExternalId: normalizeExternalId(OneSignal.User && OneSignal.User.externalId)
            });

            retry("no_confirmation");
            return;
          }

          setTimeout(check, 100);
        })();
      }

      function retry(reason) {
        if (attempt >= MAX_RETRIES) {
          log("Giving up after max retries", { attempts: attempt, reason: reason });

          var snapshot = readStateSnapshot();
          log("State at give-up:", snapshot);

          pushDL("OneSignalExternalIdSetFailed", {
            external_id: externalId,
            reason: reason,
            attempts: attempt,
            push_subscription_id: snapshot.pushSubscriptionId || ""
          });

          return;
        }

        var delay = BASE_BACKOFF_MS * Math.pow(2, attempt - 1);
        log("Retrying login after delay", { delayMs: delay, reason: reason, nextAttempt: attempt + 1 });

        setTimeout(doLogin, delay);
      }

      // If already applied, don't spam login()
      if (isExternalIdApplied(externalId)) {
        log("ExternalId already applied; skipping login.", externalId);

        var snapshot = readStateSnapshot();
        log("Current state snapshot:", snapshot);

        pushDL("OneSignalExternalIdAlreadySet", {
          external_id: externalId,
          push_subscription_id: snapshot.pushSubscriptionId || ""
        });

        return;
      }

      // Kick it off
      doLogin();
    });
  </script>
  ```

</CodeGroup>

#### Set Data Tags

This sends [OneSignal User Tags](./add-user-data-tags) using our Web SDK.

Tag configuration:

* Name: `OneSignal - Add Tags`
* Tag Type: **Custom HTML**
* Tag firing options: **Once per page**
* Trigger:
  * `OneSignalInitialized`, and
  * Your condition for when tag data is available (for example: after login, on a profile page, after purchase).

Paste this code and replace the example tag TAG and VALUE.

```html HTML theme={null}
<script>
  window.OneSignalDeferred = window.OneSignalDeferred || [];
  window.OneSignalDeferred.push(function (OneSignal) {
    OneSignal.User.addTags({
      TAG_1: "VALUE_1",
      TAG_2: "VALUE_2",
    });
  });
</script>
```

<Note> Only send tags when you actually have the user data available (for example: after login, after a profile loads, or after a known conversion event). </Note>

### Consent Mode and privacy considerations

If your site uses Consent Mode / a CMP, decide whether OneSignal should load:

* Only after consent (common for EU/UK), or
* Immediately (common where "functional" storage is allowed by default).

GTM supports a Consent Initialization trigger and tag-level consent controls to manage tag behavior based on user consent. However, OneSignal also provides privacy consent methods to control when the SDK loads.

* [Handling personal data](./handling-personal-data)
* [Web SDK Privacy Methods](./web-sdk-reference#privacy)

***

## Testing

1. In GTM, open Preview mode.
2. Load your site and confirm:
   * `OneSignal - Init` fires once.
   * `OneSignalInitialized` appears in the GTM event timeline (if you kept the event push).
3. Subscribe to your website. See [Web permission prompts](./permission-requests) for prompting details.
4. In the OneSignal dashboard, go to **Audience > Subscriptions** and confirm:
   * A Subscription appears after you opt in.
   * An External ID is visible if you set one.
5. Send a test push from **Messages > New Push**.

<Check> If initialization is working, you’ll see subscriptions appearing in OneSignal after opt-in. </Check>

### Troubleshooting

* Init tag fires, but SDK never loads
  * Check for Content Security Policy (CSP) blocking `https://cdn.onesignal.com`.
  * Check for ad blockers/script blockers.

* `dataLayer` errors
  * Ensure `window.dataLayer = window.dataLayer || []` is set before any `dataLayer.push()` calls.

* Duplicate prompts / duplicate SDK load
  * Make sure you are not also loading OneSignal via site code, a CMS plugin, or another GTM tag.

* Add Tags runs but doesn’t appear in OneSignal
  * Confirm the Trigger Group waits for `OneSignalInitialized`.
  * Confirm your user action trigger actually fires.
  * Confirm tags are valid key/value pairs and within [Plan limits](https://onesignal.com/pricing).

<Warning>
  If you still need help, see [Web SDK troubleshooting](./troubleshooting-web-push) for common fixes.
</Warning>

## Next steps

* [Web permission prompts](./permission-requests)
* [User Data Tags](./add-user-data-tags)
* [Web SDK reference](./web-sdk-reference)

***

Built with [Mintlify](https://mintlify.com).
